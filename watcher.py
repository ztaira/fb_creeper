"""
Note: Spaghetti code follows!
Tested on Python 3.5.1
"""

import json
import time
import configparser
import requests
import facebook

class Watcher():
    def __init__(self):
        print("Getting User Info...")
        self.get_user_info()
        self.lat_dict = {}

    def get_user_info(self):
        """Get the user's information from a config file"""
        config_parser = configparser.ConfigParser()
        config_parser.read('config.txt')
        self.config = config_parser['SECRETS']

    def make_fb_request(self, seq_number):
        """Make the request using the url, params, and headers"""
        response_obj = requests.get(self.url, params=self.params, headers=self.headers)
        return response_obj.text[10:]

    def stream_times(self):
        """Set up log files, maintain a connection, and log stuff"""
        # Set up url, params, headers
        self.url = "https://5-edge-chat.facebook.com/pull"
        self.set_default_params()
        self.set_default_headers()
        # make initial request
        initial_response = json.loads(self.make_fb_request(self.params['seq']))
        seq_number = initial_response['seq']
        initial_response = initial_response['ms']
        # set up the text file logs
        self.setup(initial_response, 0)
        # write data to the text file logs
        self.write_data(initial_response)
        print('\n')
        # maintain the connection and keep logging stuff
        while True:
            if int(time.time()) % 15 == 0:
                print("Trying to connect another time...")
                self.update_params('seq', seq_number)
                next_response = json.loads(self.make_fb_request(seq_number))
                try:
                    seq_number = next_response['seq']
                except:
                    print("Error:", next_response)
                print("Seq:", seq_number)
                try:
                    self.write_data(next_response['ms'])
                except KeyError:
                    print("KeyError, no ms", next_response)
                print("\n")


    def set_default_params(self):
        """Set the default parameters"""
        self.params = {
            # get these from your request
        }

    def set_default_headers(self):
        """Set the default headers"""
        self.headers = {
            # get these from your request
        }

    def update_params(self, field, value):
        """Update the paramaters"""
        self.params[field] = value

    def write_data(self, response):
        """Write data depending on the structure of the response"""
        for data in response:
            # when it passes the entire friends list and last active times
            if 'buddyList' in data:
                for user in data['buddyList']:
                    file_name = 'data/' + user + '.txt'
                    if user not in self.lat_dict or self.lat_dict[user] != str(data['buddyList'][user]['lat']):
                        with open(file_name, 'a') as workfile:
                            workfile.write(str(data['buddyList'][user]['lat']))
                            workfile.write("\n")
                            self.lat_dict[user] = str(data['buddyList'][user]['lat'])
                    print(user, data['buddyList'][user]['lat'], len(self.lat_dict))
            # when it's just updating last active times
            elif 'overlay' in data:
                for user in data['overlay']:
                    file_name = 'data/' + user + '.txt'
                    if self.lat_dict[user] != str(data['overlay'][user]['la']):
                        with open(file_name, 'a') as workfile:
                            workfile.write(str(data['overlay'][user]['la']))
                            workfile.write("\n")
                            self.lat_dict[user] = str(data['overlay'][user]['la'])
                    print(user, data['overlay'][user]['la'], len(self.lat_dict))
            # when you're chatting with someone
            elif 'delta' in data:
                if 'messageMetadata' in data['delta']:
                    user = data['delta']['messageMetadata']['threadKey']['otherUserFbId']
                    user2 = data['delta']['messageMetadata']['actorFbId']
                    timestamp = data['delta']['messageMetadata']['timestamp']
                    message = data['delta']['body']
                    file_name = 'data/' + user + '.txt'
                    with open(file_name, 'a') as workfile:
                        message = timestamp + ' ' + message
                        workfile.write(message)
                        if user != user2:
                            workfile.write(' (me)')
                        workfile.write('\n')
                    print(user, message)
                    print(data)
            # other data
            else:
                print("Else:", data)

    def setup(self, initial_response, get_names):
        """Set up files, or use existing files and erase all previously logged data"""
        graph = facebook.GraphAPI(self.config['access_token'])
        # write completely new files using names from the fb api
        if get_names == 1:
            for data in initial_response:
                if 'buddyList' in data:
                    for user in data['buddyList']:
                        file_name = 'data/' + user + '.txt'
                        with open(file_name, 'w') as workfile:
                            try:
                                profile = graph.get_object(user)
                                workfile.write(profile['name'])
                                workfile.write('\n')
                                print(profile['name'])
                            except:
                                pass
        # use existing files, but clear all previously logged data
        else:
            for data in initial_response:
                if 'buddyList' in data:
                    for user in data['buddyList']:
                        try:
                            file_name = 'data/' + user + '.txt'
                            with open(file_name, 'r') as readfile:
                                name = readfile.readline()
                            with open(file_name, 'w') as workfile:
                                workfile.write(name)
                            print(name)
                        except:
                            pass

if __name__ == '__main__':
    # create a watcher instance
    watcher = Watcher()
    # start streaming data
    watcher.stream_times()

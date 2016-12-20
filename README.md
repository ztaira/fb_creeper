# fb_creeper
Hack-A-Week 13: Python script to programmatically watch fb chat for you. Info
obtained includes when the person last accessed facebook (little green dot in
the chat bar) and all messages.

I'm not exactly sure which settings will allow you to hide from this script.
Turning off messenger/appearing offline would probably do it, so I've included
instructions to do so at the bottom of this README under "How to Turn Off Chat."

Regardless, I hope this repository serves as a very good reminder to be wary
of what you put out on social media. You never know who could be watching.

Note: This is just a proof-of-concept script, so there's lots of spaghetti code
lying around. You've been warned.

### Usage:
- Fill the config.txt file with your personal information
- Put default headers and params into the watcher.py file
- Run the watcher.py file

### Features:
- Can view all of your incoming and outgoing fb messages in real time
- Can view last-active-time information of everyone in your friends list

### What it does:
- Sets up and maintains a connection to fb's chat url
- Logs each friend's "last active time" info and any messages sent/recieved to
a text file titled with their user ID
- Includes friend's name in plaintext as the first line of the text file

### Included Files:
```
- README.md..................This readme file
- data/......................Example data directory containing example log file
- watcher.py.................Python script to connect to fb's chat url and log stuff
- config.txt.................Config file to hold sensitive information
```

### Example Output:
See data directory for example. The two formats of log messages are:
```
[last active time in seconds]
[message timestamp in milliseconds] message text (me if sent by me)
```

Transcript:

```
Friend Name
1480027098
1480035622293 hey friend I wanna test my creepy script (me)
1480035679083 respond plz (me)
1480035681
1480035684082 Hi
1480035740571 this is actually terrifying (me)
1480035702
1480036895
1480043698
1480043716
1480043806
1480044838
1480044868
1480054500
1480054566
1480054921
1480054944
1480055584
1480055681588 g'night
```

### How to Turn Off Chat for Facebook.com, Messenger.com, and Messenger for Android:
### Facebook's site, in the chat bar options:

![alt text][outputimage]
[outputimage]: https://github.com/ztaira14/fb_creeper/blob/master/data/fb_site.png "Facebook's site, in the chat bar"

### Messenger.com, in the "Active Contacts" menu:

![alt text][outputimage2]
[outputimage2]: https://github.com/ztaira14/fb_creeper/blob/master/data/messenger_site.png "Messenger.com, in the Active Contacts menu"

![alt text][outputimage3]
[outputimage3]: https://github.com/ztaira14/fb_creeper/blob/master/data/messenger_site2.png "Messenger.com, in the Active Contacts menu"

### Messenger for Android, in the third tab:

![alt text][outputimage4]
[outputimage4]: https://github.com/ztaira14/fb_creeper/blob/master/data/messenger_on_android.png "Messenger for Android, in the third tab"


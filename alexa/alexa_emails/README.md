# Alexa skills : Send proper emails to your employees

Thanks to this skill, you'll be able to send emails to your employees using Alexa. Sending emails was never as easy as it is now !

### Database

You have to have a database that matches :

**1.** The names of your employees with their email addresses

**2.** The subject of the email with the content you want to sender

For the sake of simplicity, we just used [python dictionaries](./db.py)

### Emailing

In order to send emails via python we used the library [smtplib](https://docs.python.org/3/library/smtplib.html) with Google's Gmail service. To do so you have to configure the sender email to allow your code to interact with it.

Go to Gmail's [Less Secure App setting](https://myaccount.google.com/lesssecureapps) and allow third party apps by switching to ON, as shown in the following figure.

<img src="./images/LessSecureAppAccess.PNG" alt="Less secure app access">

The login and password are in another [file](./config.py). Keep in mind this is for learning purposes, we do not recommend managing authentication this way in production.

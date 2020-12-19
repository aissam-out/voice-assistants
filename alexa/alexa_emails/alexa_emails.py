import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from db import employees, content


def get_email(name):
    '''get the email of a given employee'''
    name = name.lower()
    try:
        email = employees[name]
        return True, email
    except:
        error = "No {} in the database".format(name)
        return False, error

def get_content(subject):
    subject = subject.lower()
    try:
        body = content[subject]
        return True, body
    except:
        error = "No {} in the database".format(subject)
        return False, error

def send_email(name, to, subject, content):

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = config.sender_email
    message['To'] = to
    message['Subject'] = subject

    #The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))

    try:
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(config.sender_email, config.sender_password) #login with mail_id and password
        text = message.as_string()
        session.sendmail(config.sender_email, to, text)
        session.quit()
        answer = "your {} email was successfully sent to {}".format(subject, name)
        #print('Mail Sent')
        #return True, answer
    except:
        answer = "Email failed to send."
        #print("Email failed to send.")
        #return False, answer
    return answer

def alexa_mail(name, subject):
    bool_mail, email_msg = get_email(name)
    bool_content, content = get_content(subject)

    if (bool_mail & bool_content):
        answer = send_email(name, email_msg, subject, content)

    elif ((not bool_mail) & bool_content):
        answer = email_msg

    elif (bool_mail & (not bool_content)):
        answer = content

    else:
        answer = "Neither {} nor {} are in the database".format(name, subject)

    return answer

if __name__ == '__main__':
    # for test
    subject = 'assistance'
    alexa_mail("aissam", subject)

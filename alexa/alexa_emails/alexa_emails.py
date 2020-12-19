import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from db import employees, content


def get_email(name):
    '''get the email of a given employee from the database'''
    name = name.lower()
    try:
        email = employees[name]
        return True, email
    except:
        error = "No {} in the database".format(name)
        return False, error

def get_content(subject):
    '''get the content of the email from the database given its subject'''
    subject = subject.lower()
    try:
        body = content[subject]
        return True, body
    except:
        error = "No {} in the database".format(subject)
        return False, error

def send_email(name, to, subject, content):
    '''send email give name, destination, subject and content'''
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

    except:
        answer = "Email failed to send."

    return answer

def alexa_mail(name, subject):
    '''extract email and content and send email given name and subject'''
    # get email adress
    bool_mail, email_msg = get_email(name)
    # get email content
    bool_content, content = get_content(subject)

    # if email and content exist in the database, send email
    if (bool_mail & bool_content):
        answer = send_email(name, email_msg, subject, content)

    # if email adress doesn't exist in the db, send an appropriate message
    elif ((not bool_mail) & bool_content):
        answer = email_msg

    # if email content doesn't exist in the db, send an appropriate message
    elif (bool_mail & (not bool_content)):
        answer = content

    # if both don't exist
    else:
        answer = "Neither {} nor {} are in the database".format(name, subject)

    return answer

if __name__ == '__main__':
    # for test
    subject = 'assistance'
    alexa_mail("aissam", subject)

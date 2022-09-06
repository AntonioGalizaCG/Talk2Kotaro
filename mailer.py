#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

## @package mailer
## Contains all the necessary methods and variables for sending emails.

## your e-mail address; str.
gmail_user = "your_email_user@.your_domain.com"
## your e-mail password; str.
gmail_password = "your_password"
## sender of the email, in this case, yourself; str.
sent_from = gmail_user
## list of addresses to which the email will be sente; in this case, only you;
## list of str.
to = [gmail_user]


## Function responsible for creating aN email containing a request for deleting
## a minor's profile, including images in the email's body.
## @param id the ID of the profile to be deleted; str.
## @param image picture from which face recognition will be performed for
## deleting the profile of a minor whe the guardians do not know the profile's
## ID; np.array.
## @oaram reasons resons for which the guardians are requesting the deletion of
## the given profile.
def Mail(id="",image = None, Reasons=""):
    ## email subject; str.
    subject = 'Deletion Request from'
    ## contents of the email; str.
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    Delete profile with ID:%s

    Stated Reasons for Deletion: %s

    Image: %s
    """ % (sent_from, ", ".join(to), subject, id, Reasons,str(image))

    try:
        ## email server; smtplib.SMTP_SSL.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

    except:
        pass


## Function responsible for creating aN email containing a request for deleting
## a minor's profile with the possibility of attaching files.
## @param id the ID of the profile to be deleted; str.
## @param image picture from which face recognition will be performed for
## deleting the profile of a minor whe the guardians do not know the profile's
## ID; np.array.
## @oaram Reasons resons for which the guardians are requesting the deletion of
## the given profile.
def Mail2(id="",image = None, Reasons="", email=""):
    ## email contents; email.mime.multipart.MIMEMultipart.
    message = MIMEMultipart()
    message['From'] = 'talk.with.kotaro@gmail.com'
    message['To'] = 'talk.with.kotaro@gmail.com'
    message['Subject'] = 'Deletion Request Form'
    mail_content= """From: %s
    To: talk.with.kotaro@gmail.com
    Subject: Deletion Request Form

    Delete profile with ID: %s

    Stated Reasons for Deletion: %s

    """ % (email, id, Reasons)
    message.attach(MIMEText(mail_content, 'plain'))
    if image is not None:
        attach_file_name = image.filename
        attach_file = image
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload(image.read())
        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)
    ## email server.
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.ehlo()
    session.starttls() #enable security
    session.login(gmail_user, gmail_password) #login with mail_id and password
    ## contents of the email to be sent; str.
    text = message.as_string()
    session.sendmail(gmail_user, gmail_user, text)
    session.quit()

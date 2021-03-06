import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

gmail_user = 'talk.with.kotaro@gmail.com'
gmail_password = "qazxcvfr4321"
sent_from = gmail_user
to = [gmail_user]

def Mail(id="",image = None, Reasons=""):
    subject = 'Deletion Request from'
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    Delete profile with ID:%s

    Stated Reasons for Deletion: %s

    Image: %s
    """ % (sent_from, ", ".join(to), subject, id, Reasons,str(image))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

    except:


def Mail2(id="",image = None, Reasons="", email=""):
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
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.ehlo()
    session.starttls() #enable security
    session.login(gmail_user, gmail_password) #login with mail_id and password
    text = message.as_string()
    session.sendmail(gmail_user, gmail_user, text)
    session.quit()

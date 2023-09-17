import smtplib
import email
from email import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header

class Sender:
    server = None
    email = None
    password = None
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.email, self.password)

    # This method sends an email using an HTML template
    def send_template(self, to, subject, template_path, is_html=True):
        with open(template_path, "r") as f:
            template = f.read()
        
        self.send(to, subject, template, is_html)

    def send(self, to, subject, body, is_html=False):
        if not isinstance(self.server, smtplib.SMTP):
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()
            self.server.login(self.email, self.password)

        if not isinstance(body, str):
            body = str(body)
        
        try:
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = to
            msg["Subject"] = subject
            if not is_html:
                msg.attach(MIMEText(body, "plain"))
            else:
                msg.attach(MIMEText(body, "html"))
            text = msg.as_string()
            self.server.sendmail(self.email, to, text)
        except Exception as e:
            print(e)
    def close(self):
        self.server.quit()
        server = None
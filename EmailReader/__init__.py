import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header
from bs4 import BeautifulSoup

class Reader:
    email_address = ""
    password = ""
    imap = None
    def __init__(self, email, password):
        self.email_address = email
        self.password = password
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.imap.login(self.email_address, self.password)
        self.imap.select("INBOX")

    def get_latest_email(self):
        status, messages = self.imap.search(None, "ALL")
        try:
            latest = messages[0].split()[-1]
            status, data = self.imap.fetch(latest, "(RFC822)")
            raw_email = data[0][1]
            return raw_email
        except Exception as e:
            print("No emails found.\n(Full exception below)\n")
            print(e)
    
    def get_email(self, id):
        status, data = self.imap.fetch(id, "(RFC822)")
        raw_email = data[0][1]
        return raw_email
    
    def get_email_subject(self, emailSent):
        msg = email.message_from_bytes(emailSent)
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding)
        return subject
    
    def get_email_sender(self, emailSent):
        msg = email.message_from_bytes(emailSent)
        sender = msg.get("From")
        try:
            from_ = sender.split("<")[1].split(">")[0]
        except Exception as e:
            # assume it's already formatted correctly
            from_ = sender
        return from_
    
    def get_email_body(self, emailSent):
        msg = email.message_from_bytes(emailSent)
        body = ""
        # Extract the content
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                try:
                    body = part.get_payload(decode=True)
                except Exception as e:
                    print(f"Error: {e}")   
                    pass
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True)
        else:
            content_type = msg.get_content_type()
            body = msg.get_payload(decode=True).decode()
            if content_type == "text/plain":
                body = msg.get_payload(decode=True).decode()

        # Parse the HTML
        soup = BeautifulSoup(body, "html.parser")
        body = soup.get_text()
        return body
    
    def close(self):
        self.imap.close()
        self.imap.logout()
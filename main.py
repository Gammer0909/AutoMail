from EmailReader import Reader
from EmailSender import Sender
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import yaml
import sys

EMAIL = None
PASSWORD = None
TEMPLATE_PATH = None

# Get the email and password from the config file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    EMAIL = config["email"]
    PASSWORD = config["password"]
    if config["path-to-template"] is not None:
        TEMPLATE_PATH = config["path-to-template"]


def main():
    if len(sys.argv) < 2:
        print("Example usage: python3 main.py --save-latest-email --use-template")
        print("If not using a template, replace --use-template with what you wish to send, eg: python3 main.py --save-latest-email Hello World!")
        print("Note: templates should be .html files, and in the same directory as main.py")
        return
    args = sys.argv
    reader = None
    sender = None
    # Make sure the email and password are not None
    if EMAIL is None or PASSWORD is None:
        print("Please enter your email and password in config.yaml")
        return
    # Double checking cause dynamic typing sucks
    if EMAIL is not None and PASSWORD is not None:
        reader = Reader(EMAIL, PASSWORD)
        sender = Sender(EMAIL, PASSWORD)

    use_template = False
    # Check if the template path is not None
    if TEMPLATE_PATH is not None:
        use_template = True
    
    # Get the latest email
    if reader is not None:
        latest_email = reader.get_latest_email()
        email_sender = reader.get_email_sender(latest_email)
        email_subject = reader.get_email_subject(latest_email)
        if args[1] == "--save-latest-email":
            # Make a new file in the /Emails directory
            with open("Emails/latest_email.html", "w") as f:
                f.write(str(latest_email))
        # Send the email
        if use_template:
            with open(TEMPLATE_PATH, "r") as f:
                try:
                    # Hopefully they read the documentation and know to leave the sender and reciever to us
                    sender.send_template(email_sender, f"Re: {email_subject}", TEMPLATE_PATH)
                except Exception as e:
                    print("An error occurred:")
                    print(e)


if __name__ == "__main__":
    main()

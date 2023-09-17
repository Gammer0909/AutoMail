# AutoMail

AutoMail is an automatic mailserver that automatically responds to emails by by sending a pre-defined message to the sender.
This is a very simple implementation, using only imaplib and smtplib (with the built-in email module).
Sadly, I think it only works with gmail, however if you wanted you could **try** it with other email providers, however if it doesn't work that's not on me.

I made this because I am often at school, and if someone emails me I want them to know that I care, so I wrote this program to automatically respond.

## Installation

This project requires Python 3.11.4 or above, and pip 23.2.1 or higher.

First, clone the repository:

```bash
git clone https://github.com/Gammer0909/AutoMail.git
```

Then, install the requirements:

```bash
pip install -r requirements.txt
```

Finally, create a file called `config.py` in the root directory of the project, and add the following code:

```yaml
# EXAMPLE CONFIG FILE
# -------------------
# Configuration file for AutoMail
# Replace the values below with your own

email: your email address # replace with your email address
password: your email app password # replace with your email app password 
path-to-template: template.html # replace with the path to your template file
```

Don't know how to get an email app password? [Click here](https://support.google.com/accounts/answer/185833?hl=en) to find out how. (Your normal email password won't work!)

If you want to use a template file, create a file called `template.html` in the root directory of the project, and add the following code:

```html
<!DOCTYPE html>
<html>
    <head>
        Example Template
    </head>
    <body>
        <h1>Example Template</h1>
        <p>This is an example template</p>
    </body>
</html>
```

## Usage

To run the program, simply run the following command:

```bash
python main.py --save-latest-email
```

(The --save-latest-email parameter is optional, and will save the latest email to a file called `latest-email.html` in the /Emails directory)

### Want to Automate it?

To Automate this (On a Linux machine) you can use cron jobs.

To do this, run the following command:

```bash
crontab -e
```

Then, add the following line to the bottom of the file:

```
* * * * * python main.py --save-latest-email
```

This example runs the script every minute, if you want to change this, you can use [crontab.guru](https://crontab.guru/) to help you.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This is licensed under the [MIT](https://choosealicense.com/licenses/mit/)
license.

## Support

If you need any help, feel free to open an issue!
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    mail = None
    me = "<your_email>"
    retries = 0

    def __init__(self):
        with open('template.txt') as f:
            self.text = f.read()
        with open('template.html') as f:
            self.html = f.read()

    def connect(self):
        self.mail = smtplib.SMTP('smtp.gmail.com', 587)
        self.mail.ehlo()
        self.mail.starttls()
        self.mail.login('<your_email>', '<your_password>')

    def send(self, to):
        print(f"Sending to {to}")
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Podziękowania"
            msg['From'] = self.me
            msg['To'] = to
            part1 = MIMEText(self.text, 'plain')
            part2 = MIMEText(self.html, 'html')
            msg.attach(part1)
            msg.attach(part2)
            self.mail.sendmail(self.me, to, msg.as_string())
        except Exception as e:
            print(f"Failed to send to {to}, error: {str(e)}")
            if self.retries < 3:
                print("Retrying...")
                self.retries += 1
                self.connect()
                self.send(to)
            else:
                print("Max retries reached. Finishing...")
                raise

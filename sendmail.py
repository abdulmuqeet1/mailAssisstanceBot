import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import config

# paste the file/resume to be send in the same directory as script file
# path = os.getcwd()
# filename = "Resume.pdf"
# filepath = path+"\\" + filename


class Email:
    def __init__(self, mail_to):
        self.mail_to = mail_to

    def send(self):

        # tuple unpacking
        sub, body = self.textpart()

        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = config.EMAIL_ADDRESS
        msg['To'] = self.mail_to
        msg.attach(MIMEText(body))

        # for pdf file
        # enter the file names in the list below to send with email
        files = ["Resume.pdf"]
        for f in files:
            pdffile = MIMEApplication(open(f, "rb").read())
            pdffile.add_header('Content-Disposition',
                               'attachment', filename="Resume.pdf")
            msg.attach(pdffile)

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            # .sendmail(from, to, message)
            server.sendmail(config.EMAIL_ADDRESS,
                            self.mail_to, msg.as_string())
            server.quit()
            print("mail send to: ", self.mail_to)
        except Exception as e:
            print("email sent fail! \nerror: ", e)

    def textpart(self):
        subject = "abc text"
        body = "abkasdjasdaklsjladsk {}. \njasdkasdladj".format(subject)
        return (subject, body)

    # # def htmlpart(self):
    # #     pass


# def sendmail():
#     filename = "emailist.txt"
#     emaillist = open(filename).read()
#     for emailid in emaillist.split(" "):
#         email(emailid)

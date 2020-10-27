import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import config
import logging

# paste the file/resume to be send in the same directory as script file
# path = os.getcwd()
# filename = "Resume.pdf"
# filepath = path+"\\" + filename


class Email:
    # def __init__(self):
    #     pass

    def send(self, mail_to, subject="Sofware Engineer Job"):
        filename = "record.txt"

        if mail_to:
            # tuple unpacking
            sub, body = self.textpart(subject)

            msg = MIMEMultipart()
            msg['Subject'] = sub
            msg['From'] = config.EMAIL_ADDRESS
            msg['To'] = mail_to
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
                                mail_to, msg.as_string())
                server.quit()
                msg = subject + "  " + mail_to + "  success \n\n"
                with open(filename, "a") as f:
                    f.write(msg)

                return True

            except Exception as e:
                msg = subject + "  " + mail_to + \
                    "  failed \n error: " + str(e) + "\n\n"
                with open(filename, "a") as f:
                    f.write(msg)

                return False

    def textpart(self, subject):
        body = "Hi, I am abdul muqeet mehmood CS graduate from pakistan applying for {}. \nroles. Resume is attached with the mail. \nRegards".format(
            subject)
        return (subject, body)

    # # def htmlpart(self):
    # #     pass


from configparser import ConfigParser
import smtplib

def main():
    file = 'config.ini'
    config = ConfigParser()
    config.read(file)

    From_mail = config['mail']['me']
    password = config['mail']['password']

    to = config['mail']['to']
    cc = [config['mail']['cc']]
    bcc = [config['mail']['bcc']]
    subject = config['mail']['subject']
    body = config['mail']['body']

    email = f'To: {to} \rCc: {", ".join(cc)} \rBcc :{", ".join(bcc)}\nSubject: {subject}\n\n{body}'
    #\r carriage return

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()       #puts the connection to the SMTP server into TLS mode.
    print("trying to login")
    server.login(From_mail, password)
    print("login in successful")
    server.sendmail(From_mail,[to]+cc+bcc, email)
    server.close()
    print("mail sent")

if __name__ == '__main__':
    main()
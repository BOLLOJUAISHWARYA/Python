import smtplib

From_mail = 'aishwarya.bolloju@gmail.com'
password = "ymfmdgotbmhnottr"

to = "vibha.rawan@neosoftmail.com"
cc = ["sai.uddaraju@neosoftmail.com", "anushka.mhatre@neosoftmail.com"]
bcc = ["arun.nadar@neosoftmail.com", "rohan.dhere@neosoftmail.com", "aishwarya.bolloju@gmail.com"]
subject = 'Email sending Assignment'
body = "Hi ! this mail is generated using python code--Aishwarya Bolloju"

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

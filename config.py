#!/usr/bin/python3
import smtplib

# required
#----------------------------------
x = "sender_mail@gmail.com" 
y = "recipient_mail@gmail.com" 
z = "sender_mail@gmail.com"
c = "sender_password"
#----------------------------------
# example:
# x = "generatorexit999999@gmail.com"
# y = "generatorexit999999@gmail.com"
# z = "generatorexit999999@gmail.com"
# c = "Passw0rd!"



# never delete
#-----------------------------------------------
sender = x
recipient = y
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.login(z,c)
#-----------------------------------------------
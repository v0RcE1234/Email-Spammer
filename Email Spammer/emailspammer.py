import smtplib
import json

json_file = open("config.json", "r")
config = json.load(json_file)
json_file.close()

sender = config["Sender"]
senderPassword = config["Sender Password"]
recipent = config["Recipent"]
message = config["Message"]
howManyTimesToSend = config["How Many Times To Send Message"]


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, senderPassword)
for i in range (howManyTimesToSend):
    server.sendmail(sender,
                    recipent,
                    message
                    )
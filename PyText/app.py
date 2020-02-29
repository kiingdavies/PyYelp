# 1. After registering on twilio & getting a number
# 2. pipenv install twilio
# 3. in app.py import Client from twilio.rest
#  create an instance of the client() object paste-in an account_sid & auth_token gotten from the project account in twilo (which you should save in a var above)
# 4. use the messages method on client object, then the create() method on messages which takes in to=<a phone number>,from_=<your twilio number>, body=<content of text>. 
#       This will return a call object which you can print
#  5. take out the account sid & auth_token and save them in config.py which should be saved in .gitignore

from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
client.messages.create(
    to= config.tonum,
    from_= config.fromnum,
    body = "Testing Testing"
)


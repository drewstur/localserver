from twilio.rest import TwilioRestClient

account_sid = "AC6adea007cd9e3fbaf251f1598672639d" # Your Account SID from www.twilio.com/console
auth_token  = "319e40f1fcb7d7b3f7216c45a4e0cbab"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+12196807463",    # Replace with your phone number
    from_="+12194724158") # Replace with your Twilio number

print(message.sid)

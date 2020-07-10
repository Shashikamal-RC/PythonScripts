# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0a0f081fc70f492122a54dc2771ce222'
auth_token = '319f37d64f5dc49919eccba159df2d8b'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+917353679106',
                              to='+918277140058'
                          )

print(message.sid)

from twilio.rest import TwilioRestClient

account_sid = "AC0de490c562ce27397f3b5c4ac825d6fb" # Your Account SID from www.twilio.com/console
auth_token  = "24a7c0ead0cec28ba2d9adb812dffce4"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="ASU is getting destroyed",
    to="+19253608980",    # Replace with your phone number
    from_="+19252394701") # Replace with your Twilio number

print(message.sid)

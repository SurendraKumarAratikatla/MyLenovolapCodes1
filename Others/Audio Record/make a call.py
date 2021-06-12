from twilio.rest import Client


account_sid = 'AC01b96e6ad4777b98b21ee5cd82b37365'
auth_token = 'b82b160693c854b6ee542d23621e87c6'

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello',
    to='whatsapp:+918500906002'
)

print(message.sid)
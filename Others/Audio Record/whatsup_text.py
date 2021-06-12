from twilio.rest import Client

account_sid = 'AC01b96e6ad4777b98b21ee5cd82b37365'
auth_token = 'b82b160693c854b6ee542d23621e87c6'

client = Client(account_sid,auth_token)

from_wtsup_number = 'whatsapp:+14155238886'
to_wtsup_number = 'whatsapp:+918143920926'

client.messages.create(body='hello buddy', from_=from_wtsup_number, to=to_wtsup_number)

msgs = client.messages.list(limit=20)

for record in msgs:
    if record not in ['hi','Hi','Hello','hello','Hey','hey']:
        print(record.body)
        print(record.to)
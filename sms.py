#pip install vonage
import vonage

#Create a vonage account from here https://developer.vonage.com/

#Store key and secret in a different file and add to .gitignore
key = __import__('key').key
secret = __import__('key').secret


client = vonage.Client(key=key, secret=secret)

sms = vonage.Sms(client)

sms_to = input("Enter number here..: ")
sms_message = input("Enter message here..: ")

response_data = sms.send_message(
    {
        "from": "SMS TEST",
        "to": sms_to,
        "text": sms_message
    }
)

if response_data["messages"][0]["status"] == "0":
    print("Message sent successfully!")
    print(response_data)
else:
    print(f"Message failed with error:{response_data['messages'][0]['error-text']}")

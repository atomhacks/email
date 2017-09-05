import argparse
import boto3

from src import *

def send_email(client, config, email, member):
    """Sends an email to someone.

    Args:
        client: The boto3 client that will make the request to AWS.
        config: The current config file model.
        email: The model of the email that should be sent.
        member: The member that this email will be sent to.

    Returns:
        The JSON response of the request that was made to send the email.
    """

    source = "%s <%s>" % (config.email.sender_name, config.email.sender_email)

    destination = {
        "ToAddresses": [
            "%s <%s>" % (config.email.recipient_name, config.email.recipient_email)
        ],
        "BccAddresses": [
            "%s %s <%s>" % (member.first, member.last, member.email)
        ]
    }

    message = {
        "Subject": {
            "Data": email.subject
        },
        "Body": {
            "Html": {
                "Data": render_template(email, member)
            }
        }
    }

    return client.send_email(Source = source, Destination = destination, Message = message)

parser = argparse.ArgumentParser(description = "Send some emails. With style.")
parser.add_argument("email", type = str, help = "The name of the email file that you want to send out.")
args = parser.parse_args()

# Remove .email extension if it's here in case it was added mistakenly
email_name = args.email.replace(".email", "")

client = boto3.client(service_name = "ses", region_name = "us-east-1")
email = load_email(email_name)
config = load_config()

for member in request_members(config):
    result = send_email(client, config, email, member)

    status_code = result["ResponseMetadata"]["HTTPStatusCode"]

    if status_code == 200:
        print("Email to %s was sent successfully!" % member.email)
    else:
        print("Email to %s could not be sent." % member.email)
        print(result)

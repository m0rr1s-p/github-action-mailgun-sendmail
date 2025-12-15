import os
from mailgun.client import Client

def set_github_action_output(name, value):
    with open(os.path.abspath(os.environ['GITHUB_OUTPUT']), 'a') as f:
        f.write(f'{name}={value}\n')

def post_message(
        sender: str,
        recipient: str,
        subject: str,
        body: str,
        domain: str,
        client: Client) -> None:
    # Messages
    # POST /<domain>/messages
    data = {
        "from": sender,
        "to": recipient,
        "subject": subject,
        "html": body,
    }

    req = client.messages.create(data=data, domain=domain)
    if req.status_code == 200:
        print(req.json())
        set_github_action_output("result", req.json())
    else:
        print(req.text)
        set_github_action_output("result", req.text)

def main():
    input_key: str = os.environ["INPUT_API_KEY"]
    input_domain: str = os.environ["INPUT_DOMAIN"]
    input_sender: str = os.environ["INPUT_FROM"]
    input_recipient: str = os.environ["INPUT_TO"]
    input_subject: str = os.environ["INPUT_SUBJECT"]
    input_body: str = os.environ["INPUT_MESSAGE"]

    client: Client = Client(auth=("api", input_key),api_url="https://api.eu.mailgun.net/")

    post_message(input_sender, input_recipient, input_subject, input_body, input_domain, client)

if __name__ == "__main__":
    main()
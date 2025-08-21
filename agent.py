import sys

from utils.parser import parse_instruction
from providers.gmail import send_gmail_email
from providers.outlook import send_outlook_email


class EmailSendingAgent:
    def send_mail(self, provider, to, subject, body):
        if provider == 'gmail':
            send_gmail_email(to, subject, body)
        elif provider == 'outlook':
            send_outlook_email(to, subject, body)
        else:
            raise ValueError(f"{provider} is not supported")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python agent.py '<instruction>' <provider>")
        sys.exit(1)

    print(f"Your Input command:  {sys.argv}")
    instruction = sys.argv[1]
    provider = sys.argv[2].lower()

    # Parse the instruction
    parsed_instruction = parse_instruction(instruction)
    email_agent = EmailSendingAgent()
    email_agent.send_mail(
        provider, parsed_instruction['to'],
        parsed_instruction['subject'],
        parsed_instruction['body']
        )

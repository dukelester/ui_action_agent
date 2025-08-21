import re


def parse_instruction(instruction: str):
    """
    Mock LLM parser that extracts recipient, subject, and body from a
    natural language command.
    Example: "Send an email to james@example.com
    subject 'Meeting'
    body 'See you at 2pm'"
    """
    match = re.match(
        r"send email to (.+?) subject '(.+?)' body '(.+?)",
        instruction, re.IGNORECASE)
    if match:
        return {
            "to": match.group(1),
            "subject": match.group(2),
            "body": match.group(3)
        }
    raise ValueError("""Could not parse the instruction. Use format:
                    send email to <email>
                    subject '<sub>'
                    body '<msg>'
                    """)

# Cross-Platform Action Agent – Email Automation

This project implements **Case Study 2** from the Humaein AI Full Stack Developer screening challenge.  
It is a **prototype agent** that can perform the same user goal across different platforms with varying UIs.  

For this prototype, the chosen task is:  
**Send an email via Gmail Web and Outlook Web**  

---

## Features
    - Accepts **natural language instructions** such as:
    - Uses a **mock LLM parser** (regex-based) to extract intent:
    - recipient (`to`)
    - subject
    - body
    - Automates email sending with **Playwright**:
    - Clicks "Compose" (Gmail) or "New Mail" (Outlook)
    - Fills in recipient, subject, body
    - Sends the email
    - Logs each agent step (`"[Agent] Clicked Compose"`, etc.)
    - Supports **two providers** with different DOM structures (Gmail + Outlook)
    - Unified **agent interface** (`EmailAgent`) for extensibility

---

## Project Structure

```
ui_action_agent/
├── agent.py # Main CLI entrypoint
├── providers/
│ ├── gmail.py # Gmail automation logic
│ ├── outlook.py # Outlook automation logic
├── utils/
│ ├── parser.py # Instruction parsing (mock LLM)
│ ├── logger.py # Step logging
├── requirements.txt
└── README.md

```

---

## Setup & Installation
1. Clone repository:
   ```bash
   git clone https://github.com/dukelester/ui_action_agent.git
   cd ui_action_agent
   ```
## 2. Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# OR venv\Scripts\activate # Windows
```

## 3. Install dependencies:

`pip install -r requirements.txt`


## 4. Install Playwright browsers:

`playwright install`


## Usage

Gmail Example

`python agent.py "send email to alice@example.com subject 'Meeting' body 'See you at 2pm'" gmail`

Outlook Example
`python agent.py "send email to bob@example.com subject 'Report' body 'Please see attached'" outlook`

## Sample Execution (Gmail)
[Agent] Launching Gmail automation
[Agent] Login manually if required...
[Agent] Clicked Compose
[Agent] Filled recipient: alice@example.com
[Agent] Filled subject: Meeting
[Agent] Filled body
[Agent] Clicked Send


## Author

`Duke Nyamongo`
Humaein AI Full Stack Developer Screening – Case Study 2
from playwright.sync_api import sync_playwright

from utils.logger import log_step


def send_gmail_email(to, subject, body):
    ''' Send Gmail email'''
    log_step("Launching the Gmail Automation")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mail.google.com/")

        # Log in manually if required
        log_step("Log into your email account ...")

        # Wait until we actually see Mail UI
        page.wait_for_selector("button[aria-label='New mail']", timeout=120000)
        log_step("Mailbox loaded")

        # Click the Compose button
        page.click("div.T-I.T-I-KE.L3")
        log_step("Clicked the Compose button")

        # Fill in the fields for the email
        page.fill("textarea[name=to]", to)
        log_step(f"Filled the email recipient to : {to}")

        page.fill("input[name=subjectbox]", subject)
        log_step(f"Filled the email subject to : {subject}")

        page.fill("div[aria-label='Message Body']", body)
        log_step(f"Filled the email body to : {body}")

        # Send the email
        page.click("div[aria-label='Send']")
        log_step("Clicked on Send")

        browser.close()

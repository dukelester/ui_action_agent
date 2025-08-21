from playwright.sync_api import sync_playwright
from utils.logger import log_step


def send_outlook_email(to, subject, body):
    ''' Send outlook email'''
    log_step("Launching Outlook automation")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://outlook.office.com/mail/")

        log_step("Login manually if required...")

        # Wait until we actually see Mail UI
        page.wait_for_selector("button[aria-label='New mail']", timeout=120000)
        log_step("Mailbox loaded")

        # Click on New mail
        page.click("button[aria-label='New mail']")
        log_step("Clicked on the New Mail button")

        page.fill("input[aria-label='To']", to)
        log_step(f'Filled the recipient to : {to}')

        page.fill("input[aria-label='Subject']", subject)
        log_step(f"Filled the subject to : {subject}")

        page.fill("div[aria-label='Message body']", body)
        log_step("Filled body")

        # Send the Outlook mail
        page.click("button[aria-label='Send']")
        log_step("Clicked send ...")

        browser.close()

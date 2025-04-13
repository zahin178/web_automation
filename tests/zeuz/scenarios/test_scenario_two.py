from email import message
import time
from playwright.sync_api import Page, expect
from datetime import datetime, timedelta

def test_date_scenario(page:Page):
    url = "https://demo.zeuz.ai/web/level/two/actions/web_level_two_action_date"
    today = datetime.today().date()
    after_seven_days = today + timedelta(days=7)
    str_date = datetime.strftime(after_seven_days, "%d/%m/%Y")
    success_message = "You select correct date"

    page.goto(url)
    page.locator("#date-picker-example").focus()
    page.keyboard.type(str_date)
    page.keyboard.press("Enter")
    page.keyboard.press("Escape")
    expect(page.locator("#text_showing")).to_contain_text(success_message)
    time.sleep(3)


def test_scrolling(page:Page):
    url = "https://demo.zeuz.ai/web/level/two/actions/web_level_two_action_scroll_to_an_element"
    success_message = "successfully find the button"
    page.goto(url)
    page.locator("#element").scroll_into_view_if_needed()
    page.locator("#element").click()
    expect(page.locator("#text_showing")).to_contain_text(success_message)
    time.sleep(3)


def test_parent_element(page:Page):
    url = "https://demo.zeuz.ai/web/level/two/actions/web_level_two_action_click_by_parent"
    success_message = "clicked parent 2 button"
    page.goto(url)
    page.locator("#parent_two").locator("button").click()
    
    time.sleep(3)

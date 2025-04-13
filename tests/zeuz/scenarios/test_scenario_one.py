from playwright.sync_api import Page, expect

def test_login_scenario(page:Page):
    url = "https://demo.zeuz.ai/web/level/one/scenerios/login"
    username = "zeuzTest"
    password = "zeuzPass"
    success_message = "Login Successful"
    page.goto(url)
    page.locator("#username_id").fill(username)
    page.locator("#password_id").fill(password)
    page.locator("#signin_id").click()
    expect(page.locator("#text_showing")).to_contain_text(success_message)


def test_button_wait(page:Page):
    url = "https://demo.zeuz.ai/web/level/one/actions/wait_for_an_element_to_appear"
    page.goto(url)
    page.locator("#element_id").click()
    expect(page.locator("#countdown")).to_contain_text("0 seconds remaining")


def test_save_and_compare_variable(page:Page):
    url = "https://demo.zeuz.ai/web/level/one/actions/save_text"
    page.goto(url)
    random_text = page.locator("#randomText").inner_text()
    page.locator("#enter_text").fill(random_text)
    page.locator("#verify_id").click()    
    expect(page.locator("#text_showing")).to_contain_text("successfully verified the text")
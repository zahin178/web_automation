from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page:Page, username, password):
        self.page = page
        self.username = username
        self.password = password
        self.url = "https://demo.zeuz.ai/web/level/one/scenerios/login"
        self.username_field = page.locator("#username_id")
        self.password_field = page.locator("#password_id")
        self.signin_button = page.locator("#signin_id")
        self.error_message_field = page.locator("#error_id")
        self.error_message = "Wrong UserName or Password"
        self.success_message_field = page.locator("#text_showing")
        self.success_message = "Login Successful"
        

    def visit_page(self):
        self.page.goto(self.url)


    def enter_credentials(self):
        self.username_field.fill(self.username)
        self.password_field.fill(self.password)
        self.signin_button.click()

    def validate_error_message(self):
        expect(self.error_message_field).to_contain_text(self.error_message)

    def validate_success_message(self):
        expect(self.success_message_field).to_contain_text(self.success_message)
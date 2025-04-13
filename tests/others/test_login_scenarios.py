from pages.login_page import LoginPage 

def test_login_with_wrong_username(page):
    username = "test"
    password = "zeuzPass"
    p = LoginPage(page, username, password)
    p.visit_page()
    p.enter_credentials()
    p.validate_error_message()



def test_login_with_wrong_password(page):
    username = "zeuzTest"
    password = "password"
    p = LoginPage(page, username, password)
    p.visit_page()
    p.enter_credentials()
    p.validate_error_message()


def test_login_with_correct_creds(page):
    username = "zeuzTest"
    password = "zeuzPass"
    p = LoginPage(page, username, password)
    p.visit_page()
    p.enter_credentials()
    p.validate_success_message()
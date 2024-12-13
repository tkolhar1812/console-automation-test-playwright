from pages.login_page import LoginPage
import time

def test_login(page):
    # Replace these with valid credentials
    username = ""
    password = ""

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    # Example validation after login
    assert page.url != "https://login.beyondtrust.io/signin/"
    time.sleep(5)
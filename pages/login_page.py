from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "kendo-textbox[id='email'] input"
        self.password_input = "kendo-textbox[type='password'] input"
        self.login_button = "button[title='Login']"
        self.login_next = "button[title='Next']"

    def navigate(self):
        self.page.goto("https://login.beyondtrust.io/signin/")

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.click(self.login_next)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
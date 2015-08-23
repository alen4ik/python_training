__author__ = 'ASUS'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        txt_field_user = wd.find_element_by_name("user")
        txt_field_user.click()
        txt_field_user.clear()
        txt_field_user.send_keys(username)
        txt_field_password = wd.find_element_by_name("pass")
        txt_field_password.click()
        txt_field_password.clear()
        txt_field_password.send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
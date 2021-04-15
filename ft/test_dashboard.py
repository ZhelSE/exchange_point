from selenium.webdriver.common.keys import Keys

from ft.base import FunctionalTest


class DashboardTest(FunctionalTest):

    def test_can_start_dashboard_and_styling(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('Обменный пункт', self.browser.title)
        navbar = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertIn('Exchange', navbar)
        sidebar = self.browser.find_element_by_class_name('sidebar-sticky').text
        self.assertIn('Покупка', sidebar)


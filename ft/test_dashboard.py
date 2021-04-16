from selenium.webdriver.common.keys import Keys

from ft.base import FunctionalTest


class DashboardTest(FunctionalTest):

    def test_can_start_dashboard(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Обменный пункт', self.browser.title)


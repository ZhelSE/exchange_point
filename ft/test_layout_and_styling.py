from ft.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Открываем домашнюю страницу
        self.browser.get(self.live_server_url)
        # Устанавливаем ширину окна
        self.browser.set_window_size(1024, 768)
        # Панель навигации на месте
        self.assertIn('Exchange',
                      self.wait_for(
                          lambda: self.browser.find_element_by_id('navbar').text
                      ))
        # Левая панель на месте
        self.assertIn('Покупка',
                      self.wait_for(
                          lambda: self.browser.find_element_by_id('sidebar').text
                      ))
        # Приветствие примерно по центру
        greeting = self.wait_for(
                          lambda: self.browser.find_element_by_class_name('text-light')
                      )
        self.assertAlmostEqual(
            greeting.location['x'] + greeting.size['width'] / 2,
            512,
            delta=15
        )

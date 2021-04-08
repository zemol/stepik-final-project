class BasePage():
    """class for Base Page."""

    def __init__(self, browser, url):
        #super(BasePage, self).__init__()
        self.browser = browser
        self.url = url

        def open(self):
            self.browser.get(self.url)

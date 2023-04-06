import time

from selenium.common import WebDriverException
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class GoogleParser:
    def __init__(self):
        self.url = 'https://google.com.ua/'
        self.phrase = "Python Developer"
        self.delay = 5

        self.driver = self._init_driver()

    @staticmethod
    def _init_driver():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        return Chrome(options=options)

    def run(self):
        try:
            # visit site
            self.driver.get(self.url)

            # find search field and send keys
            search_field = self.driver.find_element(By.NAME, 'q')
            search_field.send_keys(self.phrase)
            search_field.send_keys(Keys.RETURN)

            self.driver.implicitly_wait(self.delay)

            # get elements (no ads, no accordion items)
            search_results = self.driver.find_elements(By.CLASS_NAME, 'yuRUbf')
            search_results = [result for result in search_results if
                              result.find_element(By.XPATH, "./..").get_attribute('class') != 'tF2Cxc']

            for result in search_results[:5]:
                title = result.find_element(By.TAG_NAME, 'h3').text
                url = result.find_element(By.TAG_NAME, 'a').get_attribute('href')

                print(
                    f"Title: {title}\n"
                    f"Url: {url}\n"
                )

        except WebDriverException as error:
            print(f" - Error: {error.msg}")
        finally:
            self.driver.quit()


if __name__ == '__main__':
    parser = GoogleParser()
    parser.run()

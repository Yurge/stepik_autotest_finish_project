import time, math, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

ufo_msg = []

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print('\n', ''.join(ufo_msg))

class TestUrl():
    @pytest.mark.parametrize('url', links)
    def test_url_for_string(self, browser, url):
        answer = str(math.log(int(time.time())))
        browser.implicitly_wait(7)
        browser.get(url)
        textarea = browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, "submit-submission").click()
        feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        if feedback != 'Correct!':
            ufo_msg.append(feedback)

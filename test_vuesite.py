import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import webDriverwait
from selenium.webdriver.common.by import By

class VerifySearchTestScenario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_tc_appointment(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8080/")
        self.assertIn("piechat", driver.title)
        elem = driver.find_element_by_id("login_btn")
        elem.click()
        time.sleep(2)
        print(driver.current_url)
        self.assertEqual(driver.current_url, "http://127.0.0.1:8080/login/")

        # try:
        #     element = webDriverwait(driver, 10).until(
        #         EC.presence_of_element_located((By.ID, ""))
        #     )
        # finally:
        #     driver.quit()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
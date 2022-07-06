from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from time import sleep

sleep(30)
print("updated")
driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        options=webdriver.FirefoxOptions())
try:
    driver.get("https://www.instagram.com/")
    driver.save_screenshot("image.png")
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    driver.save_screenshot("image.png")
    assert "No results found." not in driver.page_source
    assert "Estevao Direto" in driver.page_source
finally:
    print("finally rodado")
    driver.quit()
    driver.close()

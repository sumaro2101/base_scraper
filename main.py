from selenium.webdriver import Safari
from selenium.webdriver.common.by import By

browser = Safari()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, 'sale_button').click()

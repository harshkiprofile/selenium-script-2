from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
url = "https://www.uconnect.ae/"
driver.get(url)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="login"]/input[1]').send_keys('User_123')
driver.find_element_by_xpath('//*[@id="login"]/input[2]').send_keys('password')
driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/button').click()
time.sleep(8)
driver.find_element_by_link_text('My articles').click()
time.sleep(4)
driver.get('https://uconnect.ae/create-blog/')
driver.find_element_by_xpath('//*[@id="blog_title"]').send_keys('This is an awesome blog title')
driver.find_element_by_xpath('//*[@id="new-blog-desc"]').send_keys('This is an awesome blog description')
time.sleep(3)
driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Anish\\Downloads\\macbook_wallpaper.jpg")
time.sleep(4)
driver.find_element_by_id('blog_ifr').click()
actions = ActionChains(driver)
actions.send_keys("Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit Lorem Ipsuma asf dorem sit")
actions.perform()
select = Select(driver.find_element_by_id('blog_category'))
select.select_by_value('2')
driver.find_element_by_xpath('//*[@id="insert-blog"]/div[1]/div[6]/div/div/input').send_keys('#trending')
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[1]/div/a').click()
driver.find_element_by_xpath('//*[@id="insert-blog"]/div[3]/button').click()

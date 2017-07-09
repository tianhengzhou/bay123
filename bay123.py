import time
from selenium import webdriver
# from urlparse import urlparse
# from urlparse import parse_qs
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import Select
# import re
# from retrying import retry


class Modules:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def bay123_autopost(self):
        url = 'http://bay123.com/forum.php?mod=post&action=newthread&fid=40'
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element_by_id('typeid_ctrl').click()
        south_bay_xpath = "//div[@id='typeid_ctrl_menu']/ul/li[2]"
        self.driver.find_element_by_xpath(south_bay_xpath).click()
        self.driver.find_element_by_id('subject').send_keys('南湾 95123 客房出租 $1200  带家具包水电拎包入住')
        self.driver.find_element_by_id('e_textarea').send_keys('南湾 95123 出租一间客房 $1200 带家具包水电费 拎包入住。' +
                                                               '小区自带健身房，游泳池。步行距离至超市。2mile 到' +
                                                               'costco，walmart，whole food。交通便利，离85和101很近。' +
                                                               '\nhttp://bay123.com/thread-33029-1-1.html')
        self.driver.find_element_by_xpath("//div[@class='mtm']/span/span/input").send_keys('2017')
        self.driver.find_element_by_id('postsubmit').click()
        time.sleep(2)
        self.driver.quit()

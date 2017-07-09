#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Modules:
    def __init__(self):
        display = Display(visible=0, size=(1024, 768))
        display.start()
        self.driver = webdriver.Chrome()

    def bay123_autopost(self):
        url = 'http://bay123.com/forum.php?mod=post&action=newthread&fid=40'
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element_by_id('typeid_ctrl').click()
        south_bay_xpath = "//div[@id='typeid_ctrl_menu']/ul/li[2]"
        self.driver.find_element_by_xpath(south_bay_xpath).click()
        self.driver.find_element_by_id('subject').send_keys(u'Cupertino 2b1b apartment 主卧出租 $1400 不包水电')
        self.driver.find_element_by_id('e_textarea').send_keys(u'Cupertino 2b1b apartment 主卧出租 $1400 不包水电。' +
                                                               u'小区位置超好，3分钟到safeway， target，鲜芋仙，cupertino main stree ' + 
                                                               u'5分钟到大华99，附近超多中餐馆，离苹果和De Anza College几分钟，出门就能上280。' + 
                                                               u'面积825 sqft，超大主卧，和室友共用bathroom，要求男性，爱干净，好相处。\n' + 
                                                               u'联系方式： 5416027889（text only）')
        self.driver.find_element_by_xpath("//div[@class='mtm']/span/span/input").send_keys('2017')
        self.driver.find_element_by_id('postsubmit').click()
        time.sleep(2)
        self.driver.quit()

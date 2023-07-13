__author__ = "boss"
__date__ = '2023/7/18 3:49'
# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
learn_url = "http://www.tcm512.com/"
#打开 learn_url
browser = webdriver.Chrome()
browser.get(learn_url)

# 根据文字 查询
weixin_xpath = r"//*[@id='newHead']/div/div/div[9]/div[2]/div"

#找到 微信登录
time.sleep(15)
# 等待 直到 出现 微信登录

weixin = browser.find_element_by_xpath(weixin_xpath)
#点击 微信登录
weixin.click()

#点击 微信登录

time.sleep(15)
# course_xpath = r"//*[@id="tab"]/div[1]"
course_xpath = r"//*[@id='tab']/div[1]"
#找到 课程
course = browser.find_element_by_xpath(course_xpath)
#点击 课程
course.click()
#找到 class = new_neirong 的 div
course_divs = browser.find_element_by_class_name("new_neirong")
#遍历 course_divs
for course_div in course_divs:
    #找到 course_div class = studystate 的 span 标签
    studystate = course_div.find_elements_by_class_name("studystate")[0]
    #如果 studystate 的 text 是 未学
    if studystate.text == "未学":
        #找到 course_div 下 class = new_leixing new_leixing_border_black 的 span 标签
        new_leixing = course_div.find_elements_by_class_name("new_leixing new_leixing_border_black")[0]
        #点击 new_leixing
        new_leixing.click()
        # 鼠标 移动到坐标 0, 500
        browser.execute_script("window.scrollTo(0, 500)")
        time.sleep(random.randint(1, 15))






studystate_s = browser.find_elements_by_class()
studystate_s = browser.find_element_class()

#//*[@id="3731_label"]

time.sleep(500)



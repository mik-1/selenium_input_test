#coding: utf-8

import time
import random
from selenium import webdriver

# 
INPUT_RULE = ''
TERGET_URL = 'https://localhost/selenium_test.html'
TARGER_BROWSER = 'PC-CHROME'
PATH_TO_CHROMEDRIVER = './chromedriver'

def input_element(input_type, attribute, attribute_value, value):

    if attribute == 'name':
        es = browser.find_elements_by_name(attribute_value)
    elif attribute == 'id':
        es = browser.find_elements_by_id(attribute_value)
    elif attribute == 'class':
        es = browser.find_elements_by_class_name(attribute_value)
    elif attribute == 'xpath':
        es = browser.find_elements_by_xpath(attribute_value)
    elif attribute == 'selector':
        es = browser.find_elements_by_css_selector(attribute_value)
    else:
        return

    for e in es:
        if input_type == 'checkbox':
            pass
        elif input_type == 'radio':
            pass
        elif input_type in ['text', 'password', 'textarea']:
            e.send_keys(value)
        else:
            return

# ブラウザの準備
if TARGER_BROWSER == 'android':
    browser = webdriver.Remote(command_executor='http://localhost:8080/wd/hub',  desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
else:
    browser = webdriver.Chrome(PATH_TO_CHROMEDRIVER)

time.sleep(1)

# inputルールの取得, 一行目はヘッダーなので読み飛ばし
input_rule = open('rule.csv').readlines()[1:]

# 対象のURLを取得
browser.get(TERGET_URL)

# 入力
for r in input_rule:

    # ルールの取得
    rule_line = r[:-1].split(',')
    if len(rule_line) != 4 or rule_line[0] == 'submit':
        # submit
        break
        
    input_type, attribute, attribute_value, value_file = rule_line

    # 入力する値をランダムに取得
    value = random.sample(open(value_file).readlines(), 1)
    value = list(value[0])[:-1]

    # typeに合わせて値を設定
    input_element(input_type, attribute, attribute_value, value)

    time.sleep(0.5)

# browser.close()

    
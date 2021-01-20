from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time

global url
url = 'https://www.epicgames.com/fortnite/en-US/vbuckscard'
web = webdriver.Chrome(
    executable_path='C:\\Users\\Radioactive Panda\\PycharmProjects\\Python and Pygame\\chromedriver_win32\\chromedriver.exe')
web.get(url)
NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
ALP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']

CODE_MADE_VALID = False
global CODE_MADE_VALID
IF_SIGNED_IN = input('HAVE YOU SIgN IN:')
if IF_SIGNED_IN == str('YES'):
    url = web.current_url
    IF_SIGNED_IN_AND_WENT_TO_CODE_AREA = input('HAVE YOU GONE TO CODE AREA')
    if IF_SIGNED_IN_AND_WENT_TO_CODE_AREA == str('YES'):
        while True:
            VAR_1_C = random.choice([NUM, ALP])
            VAR_2_C = random.choice([NUM, ALP])
            VAR_3_C = random.choice([NUM, ALP])
            VAR_4_C = random.choice([NUM, ALP])
            VAR_5_C = random.choice([NUM, ALP])
            VAR_6_C = random.choice([NUM, ALP])
            VAR_7_C = random.choice([NUM, ALP])
            VAR_8_C = random.choice([NUM, ALP])
            VAR_9_C = random.choice([NUM, ALP])
            VAR_10_C = random.choice([NUM, ALP])
            VAR_11_C = random.choice([NUM, ALP])
            VAR_12_C = random.choice([NUM, ALP])
            VAR_13_C = random.choice([NUM, ALP])
            VAR_14_C = random.choice([NUM, ALP])
            VAR_15_C = random.choice([NUM, ALP])
            VAR_16_C = random.choice([NUM, ALP])
            VAR_1 = random.choice(VAR_1_C)
            VAR_2 = random.choice(VAR_2_C)
            VAR_3 = random.choice(VAR_3_C)
            VAR_4 = random.choice(VAR_4_C)
            VAR_5 = random.choice(VAR_5_C)
            VAR_6 = random.choice(VAR_6_C)
            VAR_7 = random.choice(VAR_7_C)
            VAR_8 = random.choice(VAR_8_C)
            VAR_9 = random.choice(VAR_9_C)
            VAR_10 = random.choice(VAR_10_C)
            VAR_11 = random.choice(VAR_11_C)
            VAR_12 = random.choice(VAR_12_C)
            VAR_13 = random.choice(VAR_13_C)
            VAR_14 = random.choice(VAR_14_C)
            VAR_15 = random.choice(VAR_15_C)
            VAR_16 = random.choice(VAR_16_C)
            code = VAR_1 + VAR_2 + VAR_3 + VAR_4 + VAR_5 + VAR_6 + VAR_7 + VAR_8 + VAR_9 + VAR_10 + VAR_11 + VAR_12 + VAR_13 + VAR_14 + VAR_15 + VAR_16
            time.sleep(1)
            ENTER_CODE = web.find_element_by_xpath('//*[@id="fortnite-posa-redemption"]/div[1]/div[2]/div/div[2]/input')
            ENTER_CODE.send_keys(code)
            time.sleep(0.5)
            CONFIRM_CODE_BUTTON = web.find_element_by_xpath(
                '//*[@id="fortnite-posa-redemption"]/div[1]/div[2]/div/button')
            CONFIRM_CODE_BUTTON.click()
            time.sleep(9)


            def CHECK_INVALID_VALID(xpath):

                try:
                    web.find_element_by_xpath(xpath)
                except NoSuchElementException:
                    global CODE_MADE_VALID
                    CODE_MADE_VALID = True
                pass


            if CODE_MADE_VALID:
                print('FOUND CODE AND REDEEMED PLEASE CHECK EMAIL')
                quit()
            if not CODE_MADE_VALID:
                ENTER_CODE.clear()
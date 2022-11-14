from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, init
from random import uniform, randint

import sys
import time
import numpy as np
import scipy.interpolate as si

init(autoreset=True)

MIN_RAND        = 0.64
MAX_RAND        = 1.27
LONG_MIN_RAND   = 4.78
LONG_MAX_RAND = 11.1

try:
    password_file = open('password.txt', 'r')
except FileNotFoundError:
    print(Fore.RED + 'password.txt nao encontrado')

try:    
    validade = open('validade.txt', 'r')
except FileNotFoundError:
    print(Fore.RED + 'validade.txt nao encontrado')
try:
    with open('email.txt') as email_file:
        email = list(email_file)
except FileNotFoundError:
    print(Fore.RED + 'email.txt nao encontrado')

try:
    with open('cc.txt') as cc_file:
        cc = list(cc_file)
except FileNotFoundError:
    print(Fore.RED + 'cc.txt nao encontrado')

try: 
    with open("cvv.txt") as cvv_file:
        cvv = list(cvv_file)
except:
    print(Fore.RED + 'cvv.txt nao encontrado')



intro = """
====================[/]====================

███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗    ██████╗  ██████╗ ████████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝     ██████╔╝██║   ██║   ██║
██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗     ██╔══██╗██║   ██║   ██║
██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗    ██████╔╝╚██████╔╝   ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝

====================[/]====================

     """


print (Fore.GREEN + intro)


looptimes = int(input("how many create:"))

password = password_file.readline()
validade = validade.readline()

def human_like_mouse_move(action, start_element):
    points = [[6, 2], [3, 2],[0, 0], [0, 2]];
    points = np.array(points)
    x = points[:,0]
    y = points[:,1]

    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)

    x_tup = si.splrep(t, x, k=1)
    y_tup = si.splrep(t, y, k=1)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = si.splev(ipl_t, x_list)
    y_i = si.splev(ipl_t, y_list)

    startElement = start_element

    action.move_to_element(startElement);
    action.perform();

    c = 5
    i = 0
    
    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x,mouse_y);
        action.perform();
        print("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
        i += 1
        if i == c:
            break;

def wait_between(a, b):
    rand = uniform(a, b)
    time.sleep(rand)

def do_captcha(driver):

    driver.switch_to.default_content()
    print("Switch to new frame")
    iframes = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])

    print("Wait for recaptcha-anchor")
    check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID ,"recaptcha-anchor")))

    print("Wait")
    wait_between(MIN_RAND, MAX_RAND)

    action =  ActionChains(driver);
    human_like_mouse_move(action, check_box)

    print("Click")
    check_box.click()

    print("Wait")
    wait_between(MIN_RAND, MAX_RAND)

    print("Mouse movements")
    action =  ActionChains(driver);
    human_like_mouse_move(action, check_box)

    print("Switch Frame")
    driver.switch_to.default_content()
    iframes = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(iframes[7])

    print("Wait")
    wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

    print("Find solver button")
    capt_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(By.ID, "solver-button"))

    print("Wait")
    wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

    print("Click")
    capt_btn.click()

    print("Wait")
    wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

    try:
        print("Alert exists")
        alert_handler = WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Wait before accept alert")
        wait_between(MIN_RAND, MAX_RAND)

        alert.accept()

        wait_between(MIN_RAND, MAX_RAND)
        print("Alert accepted, retry captcha solver")

        do_captcha(driver)
    except:
        print("No alert")
        
    print("Wait")
    driver.implicitly_wait(5)
    print("Switch")
    driver.switch_to.default_content()

def main():

    main
    
    options = webdriver.ChromeOptions()
    options.add_extension('C:/webdrivers/buster.crx')
    
    url = 'https://www.spotify.com/pt-en/purchase/offer/default-trial-1m?country=PT'
    driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe", options = options)
    driver.get(url)
            
    time.sleep(0.8)
            
    driver.find_element_by_id('sign-up-link').click()
    
    time.sleep(0.8)
    
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    
    time.sleep(0.8)
            
    emailpop = email.pop(0)

    driver.find_element_by_id('email').send_keys(emailpop)  # Email
            
    driver.find_element_by_id('confirm').send_keys(emailpop)  # Email Confirm
            
    driver.find_element_by_id('displayname').send_keys(password) # Password
            
            
    driver.find_element_by_id('day').send_keys('1')
    select = Select(driver.find_element_by_id('month'))
    select.select_by_value('01')
    
    driver.find_element_by_id('year').send_keys('2000')
    
    #driver.find_element_by_id('gender_option_male').click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='gender_option_male']"))))
            
    #driver.find_element_by_id('terms-conditions-checkbox').click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='terms-conditions-checkbox']"))))
            
    do_captcha(driver)
    
    time.sleep(2.0)

    driver.find_element_by_class('Button-sc-8cs45s-0 jgLyVk').click()
    time.sleep(0.8)

    driver.find_element_by_xpath("//*[@data-value='billing_adyen_cards']").click()
            
    driver.find_element_by_id('cardnumber').send_keys(cc.pop(0)) # CC
    driver.find_element_by_id('expiry-date').send_keys(validade) # Validade 
    driver.find_element_by_id('security-code').send_keys(cvv.pop(0)) # CVV
            
    driver.find_element_by_id('checkout_submit').click()
            
    try:
        driver.find_element_by_id('premium-message')
        print (Fore.GREEN + "Conta Criada")
        time.sleep(1)
        driver.quit()
    except NoSuchElementException:
        print(Fore.RED + "Erro ao Criar a Conta")
        time.sleep(1)
        driver.quit()
        sys.exit()

for i in range(looptimes):
    main()
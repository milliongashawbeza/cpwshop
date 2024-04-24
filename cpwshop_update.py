import asyncio
from playwright.async_api import async_playwright
import csv

from playwright.sync_api import sync_playwright
from twocaptcha import TwoCaptcha
import time
import requests
import threading
solver = TwoCaptcha('')
fields = ['file_name','url','date']
config = {
            'server':           '2captcha.com',
            'apiKey':           '',
            'softId':            123,
            'callback':         'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)
##Instances
def instance_one():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page_no = 0
        rows = []
        url = "removed for secturity reason "
        page.goto(url, timeout=706775)
        print(("Navigatin to.. " + url))
        # USER INPUTS
        #################
        token_key = ''
        CID = ''
        PASSWORD = ''
        #ANIMAL = 'Deer'
        ANIMAL_NUMBER = 1
        CODE = 'DE034P2R'
       # EDUCATION_NUMBER = '4444'
        #COUNTRY = 'United States'
       # STATE = 'Idaho'
        #################
        #################
        login_button_selector = '.customerloginmenu a'
        login_id_selector = '#ConsumerHFIdentifierLoginBean-243533984.criteria.selectedIdentifierType'
        sign_in_button_selector = '.tn-primary.action-default.btn.btn-default.first-underline'
        cid_selector = '[aria-label="The Identifier Number for Identifier Type CID # must contain at least 5 numbers and letters combined, and must only contain numbers, letters, embedded spaces or a dash. And the entry also must contain at least 1 characters,at most 9 characters, excluding spaces and dashes."]'
        password_selector = '.show-password-container input'
        sign_in_selector = '#submit'
        page.wait_for_selector(login_button_selector, timeout=789999)
        page.click(login_button_selector)
        # Bot detection selecton
        #  await page.wait_for_selector(login_id_selector,timeout=40000)
        page.wait_for_selector(cid_selector, timeout=78900)
        page.query_selector(cid_selector).fill(CID)
        page.query_selector(password_selector).fill(PASSWORD)
        page.click(sign_in_selector)
        page.wait_for_selector('#submit', timeout=67000)
        page.click('#submit')
        page.wait_for_selector('#mainnavbar')
        licensing = 'Go Hunting & Fishing'
        lice = page.get_by_text(licensing)
        lice.click()
        buy_licensing_selector = '#tile-text-wrap-container-rawtext1'
        page.wait_for_selector(buy_licensing_selector, timeout=35000)
        page.click(buy_licensing_selector)
        residenace_selector = '#selectResidency'
        print('Residency Choice ..*')
        page.wait_for_selector(residenace_selector, timeout=34000)
        if (page.query_selector(residenace_selector)):
            radios = page.query_selector_all('input[type="radio"]')
            print('Resedential choice')
            radios[1].click()
            page.click('#submit')
        # Choose an Animal
        page.wait_for_selector('#productList')
        animals = page.query_selector_all('.panel-heading.panel-heading-title-root a')
        animals[ANIMAL_NUMBER].click()
        purchase_element = '.panel-collapse.collapse.in a'
        page.wait_for_selector(purchase_element, timeout=40000)
        page.click(purchase_element)
        page.wait_for_selector('table')
        ##Enter a code.
        i1 = CODE[1]
        i2 = CODE[2] + CODE[3] + CODE[4]
        i3 = CODE[5] + CODE[6]
        i4 = CODE[7]
        table = page.query_selector_all('table')
        input1 = table[0].query_selector_all('td')
        input1[3].query_selector('input').fill(i1)
        input1[5].query_selector('input').fill(i2)
        input1[7].query_selector('input').fill(i3)
        input1[9].query_selector('input').fill(i4)
        # Solve Cptcha
        print('checking element.')
        captcha_id = 'iframe[title="reCAPTCHA"]'

        page.wait_for_selector(captcha_id, timeout=670900)
        iframe = page.query_selector(captcha_id)
        print('I have got an Iframe...')
        site_key = iframe.get_attribute('src')
        paramaters = site_key.split('&')
        s_k = paramaters[1]
        s_k_f = s_k[2:]
        page.wait_for_timeout(15670)
        captchaFrame = page.wait_for_selector("iframe[src*='recaptcha/api2']");
        captchaFrameContent = captchaFrame.content_frame();

        # await locator.click()
        try:
            result = solver.recaptcha(
                sitekey=s_k_f,
                url=url,
            )

        except Exception as e:
            print(e)

        else:
            print('solved: ' + str(result))
            # get a result
            captcha_id = result['captchaId']
            url_out = 'http://2captcha.com/res.php?key=' + token_key + '&action=get&id=' + captcha_id + ''
            # r = requests.get(url_out,headers={'Accept': 'application/json'})
            print(captcha_id)
            while True:
                ##url = f'<http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}>'
                resp = requests.get(url_out)
                print(resp.text)
                if 'CAPCHA_NOT_READY' in resp.text:
                    time.sleep(7)
                    print('solving captcha...')
                else:
                    captcha_response = resp.text.split('|')[1]
                    break

            print(captcha_response)
            page.eval_on_selector(
                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                expression="(el) => el.style.display = 'block'",#el.removeAttribute('style.display') #(el) => el.style.display = 'flex'
            )

            page.eval_on_selector(
                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                expression="(el) => el.style.float = 'left'",
                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex'
            )
            page.eval_on_selector(
                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                expression="(el) => el.style.width = '80px'",
                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex' #margin-bottom:120px;
            )
            page.eval_on_selector(
                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                expression="(el) => el.style.margin = '100px 100px'",
                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex' #margin-bottom:120px;
            )

            page.eval_on_selector(
                selector="#submit",  # Modify the selector to fit yours.
                expression="(el) => el.style.display = 'float'",
                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex'
            )

            page.query_selector('#g-recaptcha-response').fill(captcha_response[3:])
            #page.evaluate("___grecaptcha_cfg.clients['0']['U']['U']['callback']")
            page.evaluate("___grecaptcha_cfg.clients['0']['P']['P']['callback']")
            page.wait_for_timeout(3000)
            page.wait_for_selector('#submit')
            page_url = page.title()
            while(True):
                try:
                    if(page.locator('#submit').is_enabled()):
                        print('clicking submit')
                        page.click('#submit')
                        #change the below number for faster, it's in millisecond
                        page.wait_for_timeout(10)
                    elif(page.url==page_url and page.locator('#submit').is_enabled()):
                        print('clicking submit')
                        page.click('#submit')
                    elif(page.locator('#submit').is_disabled()):
                        #Solve captcha
                        captcha_id = 'iframe[title="reCAPTCHA"]'

                        page.wait_for_selector(captcha_id, timeout=670900)
                        iframe = page.query_selector(captcha_id)
                        print('I have got an Iframe...')
                        site_key = iframe.get_attribute('src')
                        paramaters = site_key.split('&')
                        s_k = paramaters[1]
                        s_k_f = s_k[2:]
                        page.wait_for_timeout(15670)
                        captchaFrame = page.wait_for_selector("iframe[src*='recaptcha/api2']");
                        captchaFrameContent = captchaFrame.content_frame();

                        # await locator.click()
                        try:
                            result = solver.recaptcha(
                                sitekey=s_k_f,
                                url=url,
                            )

                        except Exception as e:
                            print(e)

                        else:
                            print('solved: ' + str(result))
                            # get a result
                            captcha_id = result['captchaId']
                            url_out = 'http://2captcha.com/res.php?key=' + token_key + '&action=get&id=' + captcha_id + ''
                            # r = requests.get(url_out,headers={'Accept': 'application/json'})
                            print(captcha_id)
                            while True:
                                ##url = f'<http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}>'
                                resp = requests.get(url_out)
                                print(resp.text)
                                if 'CAPCHA_NOT_READY' in resp.text:
                                    time.sleep(7)
                                    print('solving captcha...')
                                else:
                                    captcha_response = resp.text.split('|')[1]
                                    break

                            print(captcha_response)

                            page.eval_on_selector(
                                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                                expression="(el) => el.style.display = 'block'",
                                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex'
                            )

                            page.eval_on_selector(
                                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                                expression="(el) => el.style.float = 'left'",
                                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex'
                            )
                            page.eval_on_selector(
                                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                                expression="(el) => el.style.width = '80px'",
                                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex' #margin-bottom:120px;
                            )
                            page.eval_on_selector(
                                selector="#g-recaptcha-response",  # Modify the selector to fit yours.
                                expression="(el) => el.style.margin = '100px 100px'",
                                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex' #margin-bottom:120px;
                            )

                            page.eval_on_selector(
                                selector="#submit",  # Modify the selector to fit yours.
                                expression="(el) => el.style.display = 'float'",
                                # el.removeAttribute('style.display') #(el) => el.style.display = 'flex'
                            )
                            page.query_selector('#g-recaptcha-response').fill(captcha_response[3:])
                            #page.evaluate("___grecaptcha_cfg.clients['0']['U']['U']['callback']")
                            page.evaluate("___grecaptcha_cfg.clients['0']['P']['P']['callback']")
                            page.wait_for_timeout(3000)
                            page.wait_for_selector('#submit')
                            page.wait_for_timeout(100)
                    else:
                        break
                except:
                    print('x')



           # page.wait_for_timeout(100)


        page.wait_for_timeout(100)


        page.wait_for_selector('#page-purchaseprivilege')
        page.query_selector('#submit').click()
        #page.wait_for_selector(
        #    '[aria-label="OK: The following product(s) will be added to your purchase as a result of regulations: Product Name SWA0-SWA Access "]')
        #page.query_selector(
        #    '[aria-label="OK: The following product(s) will be added to your purchase as a result of regulations: Product Name SWA0-SWA Access "]').click()
        #page.wait_for_timeout(1000)
        #input_elements = page.query_selector_all('input')
        #form_group = page.query_selector_all('select')
        #input_elements[0].fill(EDUCATION_NUMBER)
        #form_group[1].select_option(COUNTRY)
        #page.wait_for_timeout(1000)
        #form_group_2 = page.query_selector_all('select')
        #form_group_2[2].select_option(STATE)
        #page.query_selector('#bottom-button-addToCart').click()
        #page.wait_for_timeout(10000)
        print('********* SOLVED ' + page_no + '**************')
        print('done!')
        print(page.title())
        #page.close()

def instance_two():
    instance_one()
def instance_three():
    instance_one()
def instance_four():
    instance_one()
def instance_five():
  instance_one()
def instance_six():
    instance_one()
#def instance_seven():
#    instance_one()
#def instance_eight():
#    instance_one()
#def instance_nine():
#    instance_one()
#def instance_ten():
#    instance_one()


def main():
    #Declare thread
    t = threading.Thread(target=instance_one)
    t1 = threading.Thread(target=instance_two)
    t2 = threading.Thread(target=instance_three)
    t3 = threading.Thread(target=instance_four)
    t4 = threading.Thread(target=instance_five)
    t5 = threading.Thread(target=instance_six)
 #   t6 = threading.Thread(target=instance_seven)
#    t7 = threading.Thread(target=instance_eight)
 #   t8 = threading.Thread(target=instance_nine)
 #   t9 = threading.Thread(target=instance_ten)

    #Start thread.
    t.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
 #   t6.start()
 #   t7.start()
 #   t8.start()
 #   t9.start()

    ##Join Thread.
    t.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
 #   t6.join()
 #   t7.join()
 #   t8.join()
 #   t9.join()

#asyncio.run(main())
if __name__ == "__main__":
    main()

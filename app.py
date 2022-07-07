from selenium import webdriver
import time
import os
def getAIWriting(input):
    result = ""
    try:
        sleep = 5
        username = os.environ.get('username')
        password = os.environ.get('password')

        url = 'https://app.conversion.ai/templates'
        # options = Options()
        # options.add_argument(
        #     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36")
        # options.add_argument("--headless")
        # browser = webdriver.Chrome(options=options)
        #
        browser.get(url)
        time.sleep(2.5)
        # login
        email_text = browser.find_element_by_id('email')
        email_text.send_keys(username)

        pass_text = browser.find_element_by_id('password')
        pass_text.send_keys(password)
        submit_xpath: str = '//button[@type="submit"]'
        button_xpath: str = '//button[@type="button"]'

        login_btns = browser.find_elements_by_xpath(submit_xpath)

        for login_btn in login_btns:
            if (login_btn.text == "Sign in"):
                login_btn.click()

        time.sleep(2.5)

        # select template

        bio_url = 'https://app.conversion.ai/templates/view/2b38fa60-e113-4e82-9c85-0f9e179d80b3'

        TOV = 'Witty'
        POV = 'First Person'

        browser.get(bio_url)
        time.sleep(2.5)

        # input
        # clean input
        generate_btns = browser.find_elements_by_xpath(button_xpath)

        for clean_input_btn in generate_btns:
            if (clean_input_btn.text == "Clear inputs"):
                clean_input_btn.click()

        time.sleep(0.3)
        personalInformation = browser.find_element_by_id('personalInformation')
        personalInformation.send_keys(input)
        time.sleep(0.3)
        tone = browser.find_element_by_id('tone')
        tone.send_keys(TOV)
        time.sleep(0.3)
        pointOfView = browser.find_element_by_id('pointOfView')
        pointOfView.send_keys(POV)
        time.sleep(0.3)
        # generate
        generate_btns = browser.find_elements_by_xpath(submit_xpath)

        for generate_btn in generate_btns:
            if (generate_btn.text == "Generate"):
                generate_btn.click()
        time.sleep(sleep)
        time.sleep(4)
        # time.sleep(sleep)
        # output
        outputs = browser.find_elements_by_css_selector('pre')

        for output in outputs:
            print(output.text)
            result += output.text + '\n\n'

        browser.close()
    except Exception as e:
        browser.quit()
        print("Exception occurred:{}".format(e))

    return result
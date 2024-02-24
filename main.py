from config import envVars

# impors for selenium & chrome drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

import time
def scrap():
     
    chromedriver_autoinstaller.install()
    web = webdriver.Chrome()
    web.get('https://instagram.com')
    
    #acceptCookies = web.find_element_by_xpath().click()
    time.sleep(3)

    inputUser = web.find_element(by= By.XPATH , value='//*[@id="loginForm"]/div/div[1]/div/label/input')
    inputUser.send_keys(envVars.IG_USERNAME)

    inputPassword = web.find_element(by= By.XPATH , value='//*[@id="loginForm"]/div/div[2]/div/label/input')
    inputPassword.send_keys(envVars.IG_PASSWORD)

    loginButton = web.find_element(by= By.XPATH , value='//*[@id="loginForm"]/div/div[3]/button').click()

    time.sleep(5)

    web.get(envVars.PROFILE_FOLLOWERS_URL)
    time.sleep(5)
    pop_up_window = web.find_element(by= By.XPATH , value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
    time.sleep(4)

    timeout = time.time() + float(envVars.WAIT_TIME_IN_SECONDS)
    while True:
        if time.time() > timeout:
            break
        web.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
            pop_up_window
        )
        time.sleep(1)

    followers = []

    listFollowers = web.find_element(by= By.XPATH , value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]')

    for child in listFollowers.find_elements(by=By.CSS_SELECTOR, value='.notranslate'):
        followers.append(child.text)
    
    save_file(followers)
    return followers

def save_file(followers):
    filename = 'data' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    file = open(filename,'w')
    for follower in followers:
        file.write(follower+"\n")
    file.close()

def check_unfollows(file_name, new_followers):
    old_followers = []
    with open(file_name, 'r') as f:
        old_followers = [line.strip() for line in f]
    unfollowers = list(set(old_followers) - set(new_followers))
    return unfollowers
    

if __name__ == "__main__":
    try:
        new_followers = scrap()
        if envVars.OLD_FOLLOWERS_FILENAME:
            print('Checking unfollows...')
            unfollowers = check_unfollows(envVars.OLD_FOLLOWERS_FILENAME, new_followers)
            if len(unfollowers) > 0:
                print('Unfollowers:')
                print(unfollowers)
            else:
                print('You have 0 unfollowers')
        else: {
            print('If you want to check unfollows please specify OLD_FOLLOWERS_FILENAME enviroment variable.')
        }
        time.sleep(1)
        exit()
    except ValueError as e:
        print(f"Error: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path = '/Users/mac/Downloads/chromedriver_mac64/chromedriver'
service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service)
driver.get('https://www.linkedin.com')
time.sleep(2)

# Log in
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys('your_email@example.com')
password.send_keys('your_password')
time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()

driver.get('https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aautocomplete%3A1407932827&keywords=data%20scientist&origin=SWITCH_SEARCH_VERTICAL&position=3&searchId=e904e239-1ebc-4efd-82a6-ac7dacd8df3e&sid=ta0')
time.sleep(2);

all_buttons = driver.find_elements(By.TAG_NAME, 'button');
connect_buttons = [btn for btn in all_buttons if btn.text == 'Connect'];

note_text = "I hope this message finds you well. My name is [Your_Name], and I came across your profile while exploring professionals in the fields of AI, Data Science, and Data Analytics. \n" \
            "  I am truly impressed by your accomplishments and the impact you've made in the industry. I am also passionate about these fields and am eager to connect with like-minded professionals like yourself." \
            " As someone who is always looking to learn and grow, I believe that exchanging ideas and experiences can be mutually beneficial. By connecting, we can stay updated on the latest industry trends, share valuable insights, and even explore potential collaboration opportunities. " \
            "\n I would be honored to have you as a connection on LinkedIn, and I look forward to engaging in meaningful discussions and learning from your experiences. Please feel free to check my profile to learn more about my background and expertise. Thank you for considering my connection request," \
            " and I hope you have a great day! \n Best regards, Your_Name"

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn);
    time.sleep(2)

    add_note = driver.find_element(By.XPATH, "//button[contains(., 'Add a note')]");
    driver.execute_script("arguments[0].click();", add_note);
    time.sleep(1);

    note = driver.find_element(By.XPATH, "//textarea[@name='message']");
    note.send_keys(note_text)
    time.sleep(1);

    send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']");
    driver.execute_script("arguments[0].click();", send);
    time.sleep(2)

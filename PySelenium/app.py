# Browser Automation Testing with Python and Selenium
# Run pipenv install selenium
# Search for selenium on pypi.org to download a driver that matches your chrome/browser version. Selenium requires a driver to interface with the chosen browser 
# Extract the zipped file, copy it into a New file in C drive named ChromeDriver
# import webdriver from selenium in app.py
# To automate chrome, create an instance of the Chrome class in webdriver which returns a browser object
# Pass the chromedriver file path into the Chrome method like this webdriver.Chrome("C:/ChromeDriver/chromedriver") Save it in a browser var
# use the get method on browser and pass in the url as a parameter then run the program
# it would open a page of the website . inspect the signin
# if the class and ID on the element are not uniquely named, then use the .find_element_by_link_text() method on browser object to take in the element's text as param store it in a var "Signin_link"
# use the click method on signin_link run the program
# Next is to sign into the site from selenium 
# inspect the siginin input field, use the .find_element_by_id() method on browser. 
# Pass the element id "login_field" in the method above then store in a var "username_box"
# use the send_keys method on username_box pass in your username as a string
# Duplicate the find_element_by_id & send_keys lines below then edit the params to var=password_box & id=password instead of login_field
# Input your password in the send_keys method
# use submit method on password_box & run the code
# finally assert by running: assert "username" in browser.page_source OR
# to be more specific run: browser.find_element_by_class_name("user-profile-link") store in var profile_link
# use the .get_attribute method on profile_link pass "innerHTML" as the param & store in var link_label
# final assertion run: assert "username" in link_label 
# When you are done run: browser.quit()

from selenium import webdriver

browser = webdriver.Chrome("C:/ChromeDriver/chromedriver")
browser.get("https://github.com")

Signin_link = browser.find_element_by_link_text("Sign in")
Signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("kiingdavies")

password_box = browser.find_element_by_id("password")
password_box.send_keys("adedeji007.")

password_box.submit()

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "kiingdavies" in link_label

browser.quit()

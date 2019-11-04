from selenium import webdriver

driver = webdriver.Firefox()
# Go to your page url
driver.get('https://www.facebook.com/Daylon.Hester/allactivity?entry_point=profile_shortcut&privacy_source=activity_log&log_filter=cluster_11&category_key=statuscluster')
# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
button_element = driver.find_element_by_id('button id')
button_element.click()
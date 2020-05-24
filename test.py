from browsermobproxy import Server
from selenium import webdriver

server = Server('/usr/local/Cellar/browsermob-proxy/2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)
proxy.new_har("file_name", options={'captureHeaders': True, 'captureContent': True})
driver.get("https://www.google.co.jp")
proxy.wait_for_traffic_to_stop(1, 60)
for ent in proxy.har['log']['entries']:
    print(ent)

server.stop()
driver.quit()

from browsermobproxy import Server
server = Server("path/to/browsermob-proxy")
server.start()
proxy = server.create_proxy()

from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("google")
driver.get("http://www.google.co.uk")
proxy.har # returns a HAR JSON blob

server.stop()
driver.quit()

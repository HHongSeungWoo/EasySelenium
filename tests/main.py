import mitmproxy.http
import re
from EasySelenium import webdriver
from EasySelenium.proxy import Proxy
from EasySelenium.proxy.addon.base import HttpAddonBase, CommonAddonBase


class testAddon(HttpAddonBase, CommonAddonBase):

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        print(flow.request.url)

    def error(self, flow: mitmproxy.http.HTTPFlow):
        pass


if __name__ == '__main__':

    p = Proxy()
    p.add_addon(testAddon())
    p.start()

    desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
    desired_capabilities['proxy'] = {
        "httpProxy": 'localhost:8080',
        "ftpProxy": 'localhost:8080',
        "sslProxy": 'localhost:8080',
        "proxyType": "MANUAL",
    }

    # desired_capabilities['acceptSslCerts'] = True

    driver = webdriver.Ie(desired_capabilities=desired_capabilities)
    driver = webdriver.Chrome()
    driver.get("https://github.com")
    driver.quit()
    try:
        driver.get("https://google.com/")
    except Exception as e:
        print(e)

    import time

    time.sleep(50)

    driver.quit()
    p.stop()

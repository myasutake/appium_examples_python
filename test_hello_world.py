from time import sleep

from appium import webdriver

import config


# For ALL tests, launch Appium Server before running any test.


def test_android_emulator_chrome():
    # Launch an emulator before running this test.

    capabilities = {
        'browserName': 'Chrome',
        'platformName': 'Android',
        'udid': config.emulator_udid,
        'chromedriverExecutableDir': config.chromedriver_executable_dir
    }
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

    driver.get('https://amazon.com')
    sleep(3)

    driver.quit()
    return

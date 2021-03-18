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

    do_test(capabilities)
    return


def test_android_device_chrome():
    # Launch an emulator before running this test.

    capabilities = {
        'browserName': 'Chrome',
        'platformName': 'Android',
        'udid': config.physical_udid,
        'chromedriverExecutableDir': config.chromedriver_executable_dir,
    }

    do_test(capabilities)
    return


def test_ios_emulator_safari():
    # Launch an emulator before running this test.

    capabilities = {
        'automationName': 'XCUITest',
        'browserName': 'Safari',
        'platformName': 'iOS',
        'udid': config.ios_simulator_udid,
        'deviceName': 'asdf',
    }

    do_test(capabilities)
    return


def do_test(capabilities):
    # Connect the device before running this test. Obv.

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

    driver.get('https://amazon.com')
    sleep(3)

    driver.quit()
    return

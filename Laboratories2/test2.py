from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options as Fopt
import logging as logger
from time import sleep

for log in [logger.getLogger(name) for name in logger.root.manager.loggerDict]:
    log.setLevel(logger.WARNING)

logger.basicConfig(filename="test2.log", filemode="w", level=logger.DEBUG)
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
for driver in [webdriver.Edge(opt), webdriver.Firefox(options=Fopt())]:
    driver.get("https://www.amazon.pl/")
    sleep(2)
    logger.info("Test start")
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/span/form/div[3]/span[1]/span/input").click()
    sleep(2)
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[1]/div[3]/div/a[1]/div/span").click()
    sleep(1)
    # driver.find_element(by=By.CLASS_NAME, value="nav-action-signin-button").click()
    sleep(1)
    emailInput = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[1]/input[1]")
    emailInput.send_keys("wrongEmail")
    logger.info("wrong email test input")
    sleep(2)
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/form/div/div/div/div[2]/span/span/input").click()
    wrongEmail = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/ul/li/span")
    assert "Nie udało się znaleźć konta powiązanego z tym adresem e-mail." in wrongEmail.text
    logger.info("wrong email test pass - email not found")
    logger.info("All assertions passed")
logger.info("Tests passed for all browsers")
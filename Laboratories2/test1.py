from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options as Fopt
import logging as logger
from time import sleep

for log in [logger.getLogger(name) for name in logger.root.manager.loggerDict]:
    log.setLevel(logger.WARNING)
opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

logger.basicConfig(filename="test1.log", filemode="w", level=logger.DEBUG)
for driver in [webdriver.Edge(opt), webdriver.Firefox(options=Fopt())]:
    driver.get("https://ztm.gda.pl/bilety/bilety-jednorazowe,a,3019")

    logger.info("Test start")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[3]/button").click()

    oneRide = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]/p[1]")
    assert "na jeden przejazd" in oneRide.text
    logger.info("na jeden przejazd test pass - text was found ")

    fullPrice = driver.find_element(by = By.XPATH, value="/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div[4]/div/div[1]/div/table/tbody/tr[2]/td[2]/p[1]/strong")
    assert "4,80" in fullPrice.text
    logger.info("4,80 test pass - text found")

    reducedPrice = driver.find_element(by = By.XPATH, value="/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div[4]/div/div[1]/div/table/tbody/tr[2]/td[3]/p[1]/strong")
    assert "2,40" in reducedPrice.text
    logger.info("2,40 test pass - text found")

    time75Ride = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]/p[2]")
    assert "75 - minutowy" in time75Ride.text
    logger.info("75 - minutowy test pass - text was found ")

    fullPrice75 = driver.find_element(by = By.XPATH, value="/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div[4]/div/div[1]/div/table/tbody/tr[2]/td[2]/p[2]/strong")
    assert "6,00" in fullPrice75.text
    logger.info("6,00 test pass - text found")

    reducedPrice75 = driver.find_element(by = By.XPATH, value="/html/body/div[1]/main/div/div/div/div[2]/div/div[1]/div[4]/div/div[1]/div/table/tbody/tr[2]/td[3]/p[2]/strong")
    assert "3,00" in reducedPrice75.text
    logger.info("3,00 test pass - text found")

    logger.info("All assertions passed")
logger.info("Tests passed for all browsers")
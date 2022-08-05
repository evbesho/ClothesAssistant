from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def am_scrape(driver, search):
    link = "https://amazon.ca/s?k=" + search
    driver.get(link)
    dick = {}

    divs = driver.find_elements(By.CLASS_NAME, "sg-col-inner")
    for div in divs:
        try:
            brand = div.find_element(By.CLASS_NAME, "s-line-clamp-1").text
            whole = div.find_element(By.CLASS_NAME, "a-price-whole").text
            frac = div.find_element(By.CLASS_NAME, "a-price-fraction").text
            name = div.find_element(By.TAG_NAME, "h2").text
            link = div.find_element(By.TAG_NAME, "a").get_attribute("href")

            if brand == "" or whole == "" or frac == "" or name == "" or link =="" :
                continue

            one = brand + " - " + name
            two = "$" + whole + "." + frac
            dick[one + "\n" + two] = link
        except NoSuchElementException:
            continue

    return dick

def etsy_scrape(driver, search):
        link = "https://www.etsy.com/ca/search?q=" + search
        driver.get(link)
        dick = {}

        divs = driver.find_elements(By.CLASS_NAME, "wt-height-full")
        for div in divs:
            try:
                name = div.find_element(By.TAG_NAME, "h3").text
                currency = div.find_element(By.CLASS_NAME, "currency-symbol").text
                cost = div.find_element(By.CLASS_NAME, "currency-value").text
                link = div.find_element(By.TAG_NAME, "a").get_attribute("href")

                if name == "" or currency == "" or cost == "":
                    continue

                one = name
                two = currency + cost
                dick[one + "\n" + two] = link
            except NoSuchElementException:
                continue

        return dick

def asos_scrape(driver, search):
    link = "https://www.asos.com/us/search/?q=" + search
    driver.get(link)
    WebDriverWait(driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe.top')))

    divs = driver.find_elements(By.CLASS_NAME, "_2qG85dG")
    for div in divs:
        try:
            name = div.find_element(By.CLASS_NAME, "_3J74XsK").text
            cost = div.find_element(By.CLASS_NAME, "_16nzq18").text

            if name == "" or cost == "":
                continue

            print(name + " - " + cost + "\n")
        except NoSuchElementException:
            continue

def start(search):
    list = []
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    list.append(am_scrape(driver, search.replace(" ", "+")))
    list.append(etsy_scrape(driver, search.replace(" ", "%20")))
    # asos_scrape(driver, search.replace(" ", "+"))

    for dick in list:
        for ent in dick.keys():
            print(ent)
            print(dick[ent] + "\n")
    driver.quit()
    return list


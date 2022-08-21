from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = ""
brave_path = ""

driver = webdriver.ChromeOptions()
driver.binary_location = brave_path


outfile = open('outfile.txt', 'w', encoding="utf-8")


for i in range(11, 31):
    driver = webdriver.ChromeOptions()
    driver.binary_location = brave_path
    driver = webdriver.Chrome(
        executable_path=driver_path, chrome_options=driver)
    driver.get("https://games-stats.com/steam/?tag=side-scroller&page="+str(i))

    table_rows = driver.find_elements_by_tag_name("tr")
    counter = 1

    for row in table_rows:
        flag = False
        tags = ''
        print(str(counter))
        Title = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[2]/a[1]")
        elem = driver.find_elements_by_xpath(
            "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[3]/span/span[1]")
        if len(elem) > 0:
            Release = driver.find_element(
                By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[3]/span/span[1]")
        else:
            Release = ' '
            flag = True
        elem = driver.find_elements_by_xpath(
            "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[3]/span/span[2]")
        if len(elem) > 0:
            DueDate = driver.find_element(
                By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[3]/span/span[2]")
        else:
            DueDate = ' '
            flag = True
        Price = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[4]")
        driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[5]/div").click()
        time.sleep(1)
        All_Tags = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[5]/div")
        entries = All_Tags.find_elements_by_tag_name('span')
        for entry in entries:
            tags = tags + ',,'+entry.text
        Followers = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[6]")
        Reviews = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[7]")
        Score = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[8]")
        Revenue = driver.find_element(
            By.XPATH, "/html/body/section/div/div/div[2]/table/tbody/tr["+str(counter)+"]/td[9]/span")
        if(flag):
            outfile.writelines(str(counter) + "_" + Title.text + "_" + " " + "_" + " " + "_" + Price.text +
                               "_" + tags + "_" + Followers.text + "_" + Reviews.text + "_" + Score.text + "_" + Revenue.text + "\n")
        else:
            outfile.writelines(str(counter) + "_" + Title.text + "_" + Release.text + "_" + DueDate.text + "_" + Price.text +
                               "_" + tags + "_" + Followers.text + "_" + Reviews.text + "_" + Score.text + "_" + Revenue.text + "\n")
        counter = counter + 1
        if(counter == 31):
            break
    driver.close()
    time.sleep(10)


outfile.close()

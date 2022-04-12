from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://genshin.gg/teams')


html = driver.page_source


a = driver.find_elements(By.CLASS_NAME, 'teams-item')    
b = driver.find_elements(By.CLASS_NAME, 'tier-list-teams')    

alpha = []
beta = []


for el in a:
    alpha.append(el.get_attribute('innerHTML'))
    
for ele in b:
    beta.append(ele.get_attribute('innerHTML')) 


with open('indexx.html', 'w') as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Document</title>\n<link rel="stylesheet" href="style.css">\n</head>\n<body>\n')
    for item in beta:
        f.write(item + '\n')
    for items in alpha:
        f.write(items)
    f.write('</body></html>')
    f.close()   
     
driver.close()     

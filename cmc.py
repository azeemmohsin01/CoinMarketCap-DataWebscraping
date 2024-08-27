# Complete Program

# import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# create dictionaries that contains columns of the scraped data
data = {
    'coin_names' : [],
    'prices' : [],
    '1h%' : [],
    '24h%' : [],
    '7days%' : [],
    'Market_Cap' : [],
    'Volume' : [],
    'circulating_supplies' : []
}

# store url of cmc to the variable
url = 'https://coinmarketcap.com/'

# open separate chrome windows 
driver = webdriver.Chrome()

# navigate to the url on recently opened chrome windows
driver.get(url)

# waits 5 seconds before fetching details
time.sleep(5)

# navigate to each column data with the help of full x path
cnames = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[3]')
prices = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[4]')
h1s = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[5]')
h24s = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[6]')
d7s = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[7]')
mcs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[8]')
vol_24hs = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[9]')
cir_supplies = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr/td[10]')


# apply loop to run for fetching each columns data and accessing first 15 rows 
for i in range(len(h1s))[:15]:

    # append the first name of the coin into dictionary
    data['coin_names'].append(cnames[i].text.split('\n')[0].strip())
    
    # print the fetched data
    print(cnames[i].text)

    # append the price of the coin into dictionary and remove $ sign, commas and spaces
    data['prices'].append(prices[i].text.replace('$','').replace(',','').strip())

    # print the fetched data
    print(prices[i].text)
    
    # append the last 1 hour percentage change of the coin into dictionary and remove % sign and spaces
    data['1h%'].append(h1s[i].text.replace('%','').strip())
    
    # print the fetched data
    print(h1s[i].text)
    
    # append the last 24 hours percentage change of the coin into dictionary and remove % sign and spaces 
    data['24h%'].append(h24s[i].text.replace('%','').strip())

    # print the fetched data
    print(h24s[i].text)
    
    # append the last 7 days percentage change of the coin into dictionary and remove % sign and spaces 
    data['7days%'].append(d7s[i].text.replace('%','').strip())

    # print the fetched data
    print(d7s[i].text)
    
    # append the market cap into dictionary and removing commas, $ sign and spaces
    data['Market_Cap'].append(mcs[i].text.replace(',','').replace('$','').strip())
    
    # print the fetched data
    print(mcs[i].text)

    # append the volume into dictionary, and splittig values and selecting the first index value, removing commas, $ sign and spaces
    data['Volume'].append(vol_24hs[i].text.split('\n')[0].replace(',','').replace('$','').strip())
    
    # print the fetched data
    print(vol_24hs[i].text)

    # append circulating supply into dictionary, and splittig values and selecting the first index value, removing commas and spaces
    data['circulating_supplies'].append(cir_supplies[i].text.split()[0].replace(',','').strip())
    
    # print the fetched data
    print(cir_supplies[i].text)

# close the browser
driver.quit()

# convert dictionary data to pandas data frame
df = pd.DataFrame(data)

# exporting data to .csv format
df.to_csv('first15cmccoins.csv', index=None)

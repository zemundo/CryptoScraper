from selenium import webdriver
from bs4 import BeautifulSoup
import datetime


filename = "Crypto Data " + datetime.datetime.now().strftime("%Y-%m-%d")
filenameStr = str(filename)


driver = webdriver.PhantomJS(executable_path = r'C:\Users\YourPCNameHere\Desktop\CryptoPrices\phantomjs-2.1.1-windows\bin\phantomjs.exe')


driver.get('https://coinranking.com/')

html_doc = driver.page_source


soup = BeautifulSoup(html_doc, 'lxml')
driver.close()

coinName = [] 
coinPrice = []
coinMarketCap = []
coin24hChange = []
def findCryptoData():

	div = soup.find('div' ,class_ ='coin-list')
	for n in div.find_all('span' ,class_ ='coin-name'):
		coinName.append(n.text)
	for p in div.find_all('span' , class_ = 'coin-list__body__row__price__value'):
		coinPrice.append(p.text.replace(",",""))
	for mc in div.find_all('span' , class_ = 'coin-list__body__row__market-cap__value'):
		coinMarketCap.append('$'+mc.text.replace(",","."))
	for change in div.find_all('span' , class_ = 'coin-list__body__row__change'):
		coin24hChange.append(change.text.replace('\n', '' ))	





def writeToFile():
	filename = filenameStr +'.csv'
	f = open(filename, "w")
	headers = "Coin Name, Coin Price, Coin Market Cap, Coin Change 24h \n"
	f.write(headers)
	
	for i,o,p,q in zip(coinName,coinPrice,coinMarketCap,coin24hChange):
		f.write(i+ "," + o + "," + p + "," +q + "\n")
	
	f.close()



findCryptoData()
writeToFile()



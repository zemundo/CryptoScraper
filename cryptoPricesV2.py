from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

#now = datetime.datetime.now() Uzima danasnji datum i lokalno vreme
filename = "Crypto Data " + datetime.datetime.now().strftime("%Y-%m-%d")
filenameStr = str(filename)


driver = webdriver.PhantomJS(executable_path = r'C:\Users\PC\Desktop\CryptoPrices\phantomjs-2.1.1-windows\bin\phantomjs.exe')


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


'''def printNames():
	

	nl = '\n'
	for a,b,c,d in zip(coinName,coinPrice,coinMarketCap,coin24hChange):
		print('\n''Coin:' + " "+ str(a) + '\n''Price:' + " "+ str(b)+ '\n''Market Cap:' + " "+ str(c) + '\n''24h Change:' + " "+ str(d))
'''


#def dateAndTime(): //Ispis Datum Vreme
	#print(now)

def writeToFile():
	filename = filenameStr +'.csv'
	f = open(filename, "w")
	headers = "Coin Name, Coin Price, Coin Market Cap, Coin Change 24h \n"
	f.write(headers)
	'''
	cName = ("\n".join(coinName))
	cPrice = ("\n".join(coinPrice))

	f.write("\n".join(coinName) + "\n".join(coinPrice))
	'''
	for i,o,p,q in zip(coinName,coinPrice,coinMarketCap,coin24hChange):
		f.write(i+ "," + o + "," + p + "," +q + "\n")
	#f.write(coinName + "," + coinPrice+ "\n")
	f.close()



findCryptoData()
writeToFile()
#dateAndTime() //Ispis Datum Vreme

#printNames()
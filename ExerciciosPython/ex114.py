from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get('http://www.pudim.com.br/')
except:
    print('\n\033[1:31mNão foi possível acessar o site!\033[m')
else:
    print('\n\033[1:33mSite Pudim acessado com sucesso!\033[m')

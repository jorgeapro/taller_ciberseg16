from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unicodedata

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

'''
def crawling():
	continue_link = driver.find_element_by_link_text('Go STEP 2 for checking APK file before Download >>')
	continue_link.click()
	continue_link_sig = driver.find_element_by_link_text('Go STEP 3 for get APK Download Link >>')
	continue_link_sig.click()
	continue_link_sig_sig= driver.find_element_by_link_text('CLICK HERE to download APK file')
	print continue_link_sig_sig.get_attribute('href')
	#continue_link_sig_sig.click()
'''

driver = webdriver.Firefox()

#driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);

driver.get("https://www.linkedin.com/uas/login")
driver.implicitly_wait(30)
#element = WebDriverWait(driver, 20).until(EC.visibility_of((By.NAME, "q")))
#assert "Python" in driver.title
content = driver.find_elements_by_xpath('//li/div/input[@id="session_key-login"]')
content2 = driver.find_elements_by_xpath('//li/div/div/input[@id="session_password-login"]')

boton_click=driver.find_elements_by_xpath('//div/div/ul/li/div/input[@id="btn-primary"]')

content[0].send_keys("TU_EMAIL")
content2[0].send_keys("TU_PASSWORD")
boton_click[0].click()


menu_red = driver.find_element_by_link_text('Red')
act=ActionChains(driver).move_to_element(menu_red)

act.perform()

menu_contactos = driver.find_element_by_link_text('Contactos')
menu_contactos.click()

primer_contacto=driver.find_elements_by_xpath('//li[@class="first"]')
print primer_contacto[0].text

#Escribimos los datos del primer contacto en un fichero.
archivo=open('datos.txt','w')
archivo.close()

lista=primer_contacto[0].text.split('\n')

archivo=open('datos.txt','a')

archivo.write(elimina_tildes(lista[0]+'\n'))
archivo.write(elimina_tildes(lista[1]+'\n'))
archivo.write(elimina_tildes(lista[2]+'\n'))

archivo.close()

'''
for i in range(0,len(content)):
	content[i].click()
	crawling()
'''	


#elem = driver.find_element_by_name("keyword")
#elem.send_keys("mapfre")
#elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
#driver.close()

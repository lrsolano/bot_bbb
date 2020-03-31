from selenium import webdriver
import time
votos = 0
while 1:
    #Setamos onde está nosso chromedriver.
    chrome = 'chromedriver.exe'
    #Configuramos um profile no chrome para não precisar logar no whats toda vez que iniciar o bot.
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=\profile\wpp")
    #Iniciamos o driver.
    driver = webdriver.Chrome(chrome, chrome_options=options)
    driver.minimize_window()
    driver.get('https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml')
    
    achar_elemento =driver.find_elements_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[1]')[0]
    achar_elemento.click()
    time.sleep(3)
    while 1:
        try:
            imagem = driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[1]/div[2]/div/div/div[2]/div/div[2]/img')
            imagem.click()
            time.sleep(6)
        except:
            break
    votos += 1 
    print("Votos: {}".format(votos))
    driver.close()
    time.sleep(5)

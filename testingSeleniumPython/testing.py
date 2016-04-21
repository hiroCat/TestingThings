from selenium import webdriver
import time
import os 


#DISCLAIMER => FOR TESTING USES ONLY , DO NOT USE FOR DDOS ATACKS OR MASSIVE AUTOMATITZATION , ASK PERMISION FIRST !!
def searchIfNotesPublished(dniInput,bornDateInput,permitClassInput,examDateInput):
    os.environ["PATH"] = '$PATH:.' 
    url = 'https://sedeapl.dgt.gob.es/WEB_NOTP_CONSULTA/consultaNota.faces' 
    browser = webdriver.Firefox() 
    browser.get(url)
    time.sleep(2) #Wait for the page to load

    nif = browser.find_element_by_id("formularioBusquedaNotas:nifnie")
    nif.clear()
    nif.send_keys(dniInput)

    examDate = browser.find_element_by_id("formularioBusquedaNotas:fechaExamen")
    examDate.clear()
    examDate.send_keys(examDateInput)

    permitClass = browser.find_element_by_id("formularioBusquedaNotas:clasepermiso")
    for option in permitClass.find_elements_by_tag_name('option'):
        if option.text == permitClassInput:
            option.click()
            break

    bornDate = browser.find_element_by_id("formularioBusquedaNotas:fechaNacimiento")
    bornDate.clear()
    bornDate.send_keys(bornDateInput)

    browser.find_element_by_name("formularioBusquedaNotas:j_id51").click()
    
    browser.implicitly_wait(10) #Wait for the page to load with the response 
    
    html=browser.page_source
    try:
        errors = browser.find_element_by_id("formularioBusquedaNotas:messages")
        foundScore = True
        error =  errors.find_element_by_tag_name('ul')
        for msg in error.find_elements_by_tag_name('li'):
            if msg.text != "":
                print "Sorry you don't have the score yet"
    #            print msg.text
                foundScore = False
                break
        if(foundScore):
            YouMayHaveTheScore(browser)
    except:
        YouMayHaveTheScore(browser)


def YouMayHaveTheScore(browser):
    try:
        score = browser.find_element_by_id("formularioResultadoNotas:j_id37:0:j_id69")
        if (score.text != ""):
            print "Run for it you have the score !!!!"
            print "And you score is -> ", score.text
    except:
        print "Some problems in paradise" 
        
#searchIfNotesPublished("44444444X","01/01/2001","A2","01/01/2001")
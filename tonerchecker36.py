from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import socket

#check if connection is using kompak's LAN cable, otherwise die
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

useCable = True

while True:
    #ipadrr = socket.gethostbyname(socket.gethostname())
    #ipadrr2 = socket.getfqdn()
    ipadrr3 = get_ip()
    if ipadrr3.startswith('192.168.62.'):
        break
    else:
        #print "Your IP address is (gethostname) "+ipadrr
        #print "Your IP address is (fqpdn) "+ipadrr2
        print "Your IP address is (get_ip) "+ipadrr3
        print "You need to be connected via LAN cable"
        answer = raw_input('try again? (y/n)')
        if answer =='y':
            continue
        else:
            print "goodbye!"
            quit()

ptc = "chromedriver.exe"
driver = webdriver.Chrome(ptc)
    
#vars
awHeadIP = "http://192.168.62."
driver.set_page_load_timeout(22)

#printers list
printersBW = {
	'203':'536027#',
	'204':'579558#',
	'206':'596442#',
	'207':'419789#'
	}
printersColor = {
	'36':'520486#',
	'202':'520300#'
	}

#get toners condition in color printers
for key,value in printersColor.items():

    awCheckerB = False
    awCheckerC = False
    awCheckerM = False
    awCheckerY = False
    awCheckerW = False
    awCheckerDB = False
    awCheckerDC = False
    awCheckerDM = False
    awCheckerDY = False

    try:
        driver.get(awHeadIP+key+'/stsply.htm')

        print ""
        print "===================================="
        print ""
        print "Printer IP Address: 192.168.62."+key
        awChecker = False
        
        #BLACK
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "BLACK"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" toner"
                awCheckerB = True
            else:
                print "=> PREWARNING, no need to reorder yet."
                awCheckerB = False

        #CYAN
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[6]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "CYAN"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" toner"
                awCheckerC = True
            else:
                print "=> PREWARNING, no need to reorder yet."
                awCheckerC = False
            
        #MAGENTA
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[8]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "MAGENTA"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" toner"
                awCheckerM = True
            else:
                print "=> PREWARNING, no need to reorder yet."
                awCheckerM = False

        #YELLOW
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[10]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "YELLOW"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" toner"
                awCheckerY = True
            else:
                print "=> PREWARNING, no need to reorder yet."
                awCheckerY = False

        #WASTE
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[4]//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        trColor = "WASTE"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" toner"
                awCheckerW = True
        else:
                awCheckerW = False

        #BLACK DRUM
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[6]//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        trColor = "BLACK DRUM"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" cartridge"
                awCheckerDB = True
        else:
                awCheckerDB = False
        #CYAN DRUM
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[6]//table[@bgcolor='#E3E7F1']/tbody/tr[6]")))
        trColor = "CYAN DRUM"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" cartridge"
                awCheckerDC = True
        else:
                awCheckerDC = False
        #MAGENTA DRUM
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[6]//table[@bgcolor='#E3E7F1']/tbody/tr[8]")))
        trColor = "MAGENTA DRUM"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" cartridge"
                awCheckerDM = True
        else:
                awCheckerDM = False
        #YELLOW DRUM
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[6]//table[@bgcolor='#E3E7F1']/tbody/tr[10]")))
        trColor = "YELLOW DRUM"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" cartridge"
                awCheckerDY = True
        else:
                awCheckerDY = False


        if (awCheckerB == False and awCheckerC == False and awCheckerM == False and awCheckerY == False and awCheckerW == False and awCheckerDB == False and awCheckerDM == False and awCheckerDC == False and awCheckerDY == False):
                print "=> no action needed"
        else:
                print "-> Call: 1500345 -> 2 (for supply)"
                print "-> Machine Part Number: "+value
                #get total impression
                driver.get('http://192.168.62.'+key+'/prcnt.htm')
                impColPrint = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[5]/td[2]"))).text)
                impColCopy = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[8]/td[2]"))).text)
                impBWPrint = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[6]/td[2]"))).text)
                impBWCopy = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[9]/td[2]"))).text)
                impTot = impColPrint + impColCopy + impBWPrint + impBWCopy
                print "-> Total Impression: " + str(impTot)
                print "-> KOMPAK's phone number: 021 8067 5000"
			
    except TimeoutException:
        print ""
        print "===================================="
        print ""
        print awHeadIP+key
        print "=> Cannot be reached. Please check manually."

#for BW printers
for key,value in printersBW.items():

    try:
        driver.get('http://192.168.62.'+key+'/stsply.htm')

        print ""
        print "===================================="
        print ""
        print "Printer IP Address: 192.168.62."+key
        awCheckerB = False
        awCheckerW = False
        awCheckerF = False
        
        #BLACK
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        #check if toner level is below 25%
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "BLACK"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" toner"
                awCheckerB = True
            else:
                print "=> PREWARNING, no need to reorder yet."
                awCheckerB = False

        #DRUM
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[4]//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        trColor = "DRUM"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "=> WARNING, please reorder "+trColor+" cartridge"
                awCheckerW = True
        else:
                awCheckerW = False

        #FUSER ASSEMBLY (only in 203 or 207)
        if (key == "203" or key == "207"):            
            trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[6]/tbody/tr/td/table/tbody/tr/td/table[@bgcolor='#E3E7F1']/tbody/tr[4]/td[2]")))
            trColor = "FUSER ASSEMBLY"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                    print "=> WARNING, please reorder "+trColor+"."
                    awCheckerF = True
            else:
                    awCheckerF = False
        else:
            awCheckerF = False

        if (awCheckerB == False and awCheckerW == False and awCheckerF == False):
            print "=> no action needed"
        else:
            print "-> Call: 1500345 -> 2 (for supply)"
            print "-> Machine Part Number: "+value
            #get total impression
            driver.get('http://192.168.62.'+key+'/prcnt.htm')
            impBWPrint = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[4]/td[2]"))).text)
            impBWCopy = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[5]/td[2]"))).text)
            impTot = impBWPrint + impBWCopy
            print "-> Total Impression:" + str(impTot)

    except TimeoutException:
        print ""
        print "===================================="
        print ""
        print awHeadIP+key
        print "=> Cannot be reached. Please check manually."

#for COB printer
try:
    driver.get('http://192.168.62.215')
    print ""
    print "===================================="
    print ""
    print "Printer IP Address: 192.168.62.215"
    awCheckerB = False
    awCheckerC = False
    awCheckerM = False
    awCheckerY = False
    
    #BLACK
    trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/table/tbody/tr[2]/td[2]/div[5]/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[2]")))
    trBN = int(filter(unicode.isdecimal,trScr.text))
    trColor = "BLACK"
    if trBN <= 15:
        print trColor + " is low (" + str(trBN) + "%)"
        print "=> WARNING, please reorder "+trColor+" toner"
        awCheckerB = True
    else:
        awCheckerB = False

    #CYAN
    trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/table/tbody/tr[2]/td[2]/div[5]/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]")))
    trBN = int(filter(unicode.isdecimal,trScr.text))
    trColor = "CYAN"
    if trBN <= 15:
        print trColor + " is low (" + str(trBN) + "%)"
        print "=> WARNING, please reorder "+trColor+" toner"
        awCheckerC = True
    else:
        awCheckerC = False

    #MAGENTA
    trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/table/tbody/tr[2]/td[2]/div[5]/table/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[2]")))
    trBN = int(filter(unicode.isdecimal,trScr.text))
    trColor = "MAGENTA"
    if trBN <= 15:
        print trColor + " is low (" + str(trBN) + "%)"
        print "=> WARNING, please reorder "+trColor+" toner"
        awCheckerM = True
    else:
        awCheckerM = False

    #YELLOW
    trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/table/tbody/tr[2]/td[2]/div[5]/table/tbody/tr[1]/td[4]/table/tbody/tr[1]/td[2]")))
    trBN = int(filter(unicode.isdecimal,trScr.text))
    trColor = "YELLOW"
    if trBN <= 15:
        print trColor + " is low (" + str(trBN) + "%)"
        print "=> WARNING, please reorder "+trColor+" toner"
        awCheckerY = True
    else:
        awCheckerY = False

    if (awCheckerB == False and awCheckerM == False and awCheckerC == False and awCheckerY == False):
        print "=> no action needed"
    else:
        print "-> Please replace the indicated low toners."

except TimeoutException:
    print ""
    print "===================================="
    print ""
    print "ID-P-COB Cannot be reached. Please check manually."

#end
driver.close()

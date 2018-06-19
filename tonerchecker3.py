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
awChecker = False
awHeadIP = "http://192.168.62."
driver.set_page_load_timeout(22)

#printers list
printersBW = {
	'203':'536027#',
	'204':'579558#',
	'206':'596442#'
	}
printersColor = {
	'36':'520486#',
	'202':'520300#'
	}

#get toners condition in color printers
for key,value in printersColor.items():

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
                print "Please Reorder "+trColor+" toner"
                awChecker = True
            else:
                print "prewarning,"
                awChecker = False

        #CYAN
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[6]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "CYAN"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "Please Reorder "+trColor+" toner"
                awChecker = True
            else:
                print "prewarning,"
                awChecker = False
            
        #MAGENTA
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[8]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "MAGENTA"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "Please Reorder "+trColor+" toner"
                awChecker = True
            else:
                print "prewarning,"
                awChecker = False

        #YELLOW
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[2]//table[@bgcolor='#E3E7F1']/tbody/tr[10]")))
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "YELLOW"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "Please Reorder "+trColor+" toner"
                awChecker = True
            else:
                print "prewarning,"
                awChecker = False

        #WASTE
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body/table[4]//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        trColor = "WASTE"
        #check if reorder status has shown up
        if "Reorder" in trScr.text:
                print "Please Reorder "+trColor+" toner"
                awChecker = True
        else:
                awChecker = False


        if awChecker == False:
                print "no action needed"
        else:
                print "Call: 1500345 -> 2 (for supply)"
                print "Machine Part Number: "+value
                #get total impression
                driver.get('http://192.168.62.'+key+'/prcnt.htm')
                impColPrint = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[5]/td[2]"))).text)
                impColCopy = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[8]/td[2]"))).text)
                impBWPrint = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[6]/td[2]"))).text)
                impBWCopy = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[9]/td[2]"))).text)
                impTot = impColPrint + impColCopy + impBWPrint + impBWCopy
                print "Total Impression: " + str(impTot)
                print "KOMPAK's phone number: 021 8067 5000"
			
    except TimeoutException:
        print awHeadIP+key+" cannot be reached. Please check manually."

#for BW printers
for key,value in printersBW.items():

    try:
        driver.get('http://192.168.62.'+key+'/stsply.htm')

        print ""
        print "===================================="
        print ""
        print "Printer IP Address: 192.168.62."+key
        awChecker = False
        
        #BLACK
        trScr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[4]")))
        #check if toner level is below 25%
        trBN = int(filter(unicode.isdecimal,trScr.text))
        trColor = "BLACK"
        if trBN <= 25:
            print trColor + " is low (" + str(trBN) + "%)"
            #check if reorder status has shown up
            if "Reorder" in trScr.text:
                print "Please Reorder "+trColor+" toner"
                awChecker = True
            else:
                print "prewarning,"
                awChecker = False

        if awChecker == False:
            print "no action needed"
        else:
            print "Call: 1500345 -> 2 (for supply)"
            print "Machine Part Number: "+value
            #get total impression
            driver.get('http://192.168.62.'+key+'/prcnt.htm')
            impBWPrint = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[5]/td[2]"))).text)
            impBWCopy = int(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//table[@bgcolor='#E3E7F1']/tbody/tr[6]/td[2]"))).text)
            impTot = impBWPrint + impBWCopy
            print "Total Impression:" + str(impTot)

    except TimeoutException:
        print awHeadIP+key+" cannot be reached. Please check manually."

driver.close()

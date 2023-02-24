import pyfiglet
import requests
from colorama import just_fix_windows_console
from termcolor import colored
from bs4 import BeautifulSoup
from datetime import datetime

just_fix_windows_console()

ascii_banner = pyfiglet.figlet_format("WEBSCRAPER")

URL = "https://kerekparszerelo.info/nyitvatartas.html"
results = requests.get(URL)

soup = BeautifulSoup(results.content, "html.parser")

elements = soup.find_all('footer')

for element in elements:
    name_element = soup.find('h2')
    text_element = soup.find('p')
    phone_element = soup.find('p')
    print(colored(ascii_banner, 'cyan'))
    print("-" * 50)
    print("Started at: " + str(datetime.now()))
    print('URL:', URL)
    print("-" * 50)
    print("\n")
    print(name_element.string)
    print(text_element.string)
    print(phone_element.string)
    print("\n")
    print("-" * 50)
    print(colored('Made with <3 Bujdosone Kovacs Brigi', 'red'))
    print("-" * 50)

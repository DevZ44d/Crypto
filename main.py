import time
import cloudscraper
import bs4 , colorama

class Crypto:
    def __init__(self , coin: str):
        self.url: str = "https://www.coingecko.com/en/coins/"
        self.scraper = cloudscraper.create_scraper()
        self.HtmL_Parser = self.scraper.get(self.url+coin).text

    def scrapping(self):
        return bs4.BeautifulSoup(
            self.HtmL_Parser,
            "html.parser"
        )


    def price(self):
        price_div = self.scrapping().find("div",class_="tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-3xl md:tw-text-4xl tw-leading-10")
        if price_div:
            span = price_div.find("span", attrs={"data-converter-target": "price"})
            if span:
                print(colorama.Fore.RED + span.text.strip() + "\n")
            else:
                print(f"[ {colorama.Fore.RED}* {colorama.Fore.WHITE}] Not Found This Crypto `{colorama.Fore.RED}{coin}{colorama.Fore.WHITE}`")
        else:
            print(f"[ {colorama.Fore.RED}* {colorama.Fore.WHITE}] Not Found This Crypto `{colorama.Fore.RED}{coin}{colorama.Fore.WHITE}`")


logo: str = fr'''{colorama.Fore.RED}
_________                        __          
\_   ___ \_______ ___.__._______/  |_  ____  
/    \  \/\_  __ <   |  |\____ \   __\/  _ \ 
\     \____|  | \/\___  ||  |_> >  | (  <_> )
 \______  /|__|   / ____||   __/|__|  \____/ 
        \/        \/     |__|                \
        
   {colorama.Fore.BLUE} - {colorama.Fore.WHITE}Tool For {colorama.Fore.RED}Price {colorama.Fore.WHITE}Of Crypto .
    
'''

for _ in logo.splitlines():
    time.sleep(0.005)
    print(_)

while True:
    coin = input(f"{colorama.Fore.BLUE}- {colorama.Fore.WHITE}Enter Name Of {colorama.Fore.RED}Coin {colorama.Fore.WHITE}: ")
    Crypto(coin).price()
    if "exit" in coin :
        exit()




from bs4 import BeautifulSoup as BS
import json
import aiohttp
import asyncio

async def Get_Soup( URL : str ):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            '''
            print(response)
            print(response.text)
            print(await response.text())
            f = open("def.txt","w",encoding="utf-8")
            f.write( str(await response.text()).replace("><",">\n<") )
            f.close()
            '''
            return BS( await response.text(), features="lxml")

async def Define(word:str = "muxer"):
    BaseLink = "https://www.thefreedictionary.com/"
    #the site from where I am picking up the def
    MyLink = BaseLink + word.strip()
    Soup = await Get_Soup(MyLink)
    #WebScrapping not an API Call
    print(MyLink)#just a confirmation
    # pseg <- the Key Variable in div 
    AllDef = Soup.find_all('div', class_ = "pseg")#It classifies based on noun, adjective , verb , etc
    Definations = list()
    print(AllDef,end="\n###\n")
    for MyDef in AllDef:
        print(MyDef.text,end="\n###\n")
        Def = MyDef.find('div')
        if Def != None:
            try:
                temp = MyDef.text.split(Def.text)[0]
                print(temp,end="\n!@!@!@!@!@!@\n")
            except: print("\nNot Found!\n")
            print(Def,Def.text,sep='\n\n',end="\n###\n")
            Definations.append(Def.text)
    print(Definations)

asyncio.run(Define())

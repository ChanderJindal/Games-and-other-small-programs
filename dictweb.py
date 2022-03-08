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
    MyDict = dict()
    print(AllDef,end="\n###\n")
    for MyDef in AllDef:
        print(MyDef.text,end="\n###\n")
        Def = MyDef.find('div')
        if Def != None:
            try:
                Type = MyDef.text.split(Def.text)[0]                
            except: Type = "\nNot Found!\n"
            print(Type,end="\n!@!@!@!@!@!@\n")
            Definations = Def.text.split('.')
            if len(Definations[0]) == 1:
                Definations = Definations[1:]
            Definations = ".".join(Definations) 
            print(Def,Def.text,Definations,sep='\n\n',end="\n###\n")
            Definations.strip()
        MyDict[Type] = Definations

        for a,b in MyDict.items():
            print(a,b)

asyncio.run(Define())

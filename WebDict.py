from bs4 import BeautifulSoup as BS
import aiohttp
import asyncio

async def Get_Soup( URL : str ):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return BS( await response.text(), features="lxml")

async def Define(word:str = "muxer"):
    Link = f"https://www.thefreedictionary.com/{word}"
    Soup = await Get_Soup(Link)
    AllDef = Soup.find_all('div', class_ = "pseg")#Nouns , adverb , etc divider
    MyDict = dict()
    MyDict["Word"] = word
    for MyDef in AllDef:#MyDef has the meaning as per that part of Speech
        Def = MyDef.find('div')#I am picking up type Defination per Part of Speech
        if Def != None:#Incase something else came in like Idiom or something
            try:
                Type = MyDef.text.split(Def.text)[0]
                '''
                Spliting based on the First defination, so 2 parts are there, 
                1st one has any marking like n. for noun, adj. for adjective , etc
                2nd one has rest of definations
                '''          
            except: #if there is no TYPE, not possible, it's not worth it
                continue;
            Definations = Def.text.split('.')
            '''
            I got the TYPE of defination, but as in Definations themselves I need/wanna remove the 1. / a. / A. / etc 
            for that '.' is everywhere split it, see if it's only 1 length long, if yes remove it
            then join it back with same patch, and it's done.
            '''
            if len(Definations[0]) == 1:
                Definations = Definations[1:]
            Definations = ".".join(Definations) 
            Definations.strip()
        MyDict[Type] = Definations
    return MyDict

if __name__ == "__main__":
    print(asyncio.run(Define()))

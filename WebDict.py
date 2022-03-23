from itertools import count
from bs4 import BeautifulSoup as BS
import aiohttp
import asyncio

async def Get_Soup( URL : str ):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            #'''
            f = open("def.txt","w",encoding="utf-8")
            f.write(str(await response.text()).replace("><",">\n<"))
            f.close()
            #'''
            return BS( await response.text(), features="lxml")

def DictRefine(MyDict:dict,word:str)-> dict:
    counter = 0
    NewDict = dict()
    NewDict["Word"] = word
    NewDict["Source"] = f"https://www.thefreedictionary.com/{word}"
    if 'n.' in MyDict.keys():
        NewDict["Noun"] = MyDict['n.']
        MyDict.pop('n.')
        counter += 1
    if 'v.tr.' in MyDict.keys():
        NewDict["Verb Transitive"] = MyDict['v.tr.']
        MyDict.pop('v.tr.')
        counter += 1
    if 'v.intr.' in MyDict.keys():
        NewDict["Verb Intransitive"] = MyDict['v.intr.']
        MyDict.pop('v.intr.')
        counter += 1 
    if counter < 3:
        KeyLst = MyDict.keys()
        ValLst = MyDict.keys()
        for i in range(counter,3):
            NewDict[KeyLst[i]] = ValLst[i]
    return NewDict
    
async def DefineWorker(word:str)->dict():
    Link = f"https://www.thefreedictionary.com/{word}"
    Soup = await Get_Soup(Link)
    AllDef = Soup.find_all('div', class_ = "pseg")#Nouns , adverb , etc divider
    MyDict = dict()
    for MyDef in AllDef:#MyDef has the meaning as per that part of Speech
        Def = MyDef.find('div')#I am picking up type Defination per Part of Speech
        if Def != None:#Incase something else came in like Idiom or something
            try:
                Type = MyDef.text.split(Def.text)[0].strip()
                '''
                Spliting based on the First defination, so 2 parts are there, 
                1st one has any marking like n. for noun, adj. for adjective , etc
                2nd one has rest of definations
                '''          
            except: #if there is no TYPE, not possible, it's not worth it
                continue;
            #Wrong one here, pick the 2nd one, also try an iteration for sds after ds

            if Def.find('div',class_="sds-list") != None:
                Def = Def.find('div',class_="sds-list")


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
            MyDict[Type] = Definations.strip()
    #print(MyDict)
    #MyDict = DictRefine(MyDict=MyDict,word=word)
    return MyDict

def Define(word : str = "smoke") -> dict():
    return (asyncio.run(DefineWorker(word)))

if __name__ == "__main__":
    print(Define("subscriptable"))

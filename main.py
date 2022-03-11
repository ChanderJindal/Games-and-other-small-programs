from random_word import RandomWords
import WebDict as W

def printer(MyDict:dict)->None:
    for a,b in MyDict.items():
        print(a,b,sep=" - ")


r = RandomWords()
WordLen = 5
Word = r.get_random_word(hasDictionaryDef="true",excludePartOfSpeech="Article,Preposition,Conjunction",minLength=WordLen,maxLength=WordLen,minCorpusCount=3)
Meaning = W.Define(word=Word)
print(Word)
#for a,b in Meaning.items():
 #   print(a,b)

print("Can You Guess The Word?")
for i in range(WordLen):
    print(" ? ",end='')
print("\nYou have 5 Turns.\nGo!")
Mydict = dict()
for l in Word:
    if l not in Mydict:
        Mydict[l] = 1;
    Mydict[l] += 1

for i in range(0,5):
    val = input()
    val = val.strip().replace(" ","")[0:5].lower()
    print(val)
    if val == Word:
        print("Cg! You won!")
        break;
    if i > 4:
        print("You Lost!")
printer(Meaning)

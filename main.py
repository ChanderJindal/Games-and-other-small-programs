from random_word import RandomWords
import WebDict as W
r = RandomWords()
Word = r.get_random_word(hasDictionaryDef="true",excludePartOfSpeech="Article,Preposition,Conjunction",minLength=5,maxLength=5,minCorpusCount=3)
Meaning = W.Define(word=Word)
print(Word)
for a,b in Meaning.items():
    print(a,b)
from random_word import RandomWords
r = RandomWords()

Word = r.get_random_word(hasDictionaryDef="true",excludePartOfSpeech="Article,Preposition,Conjunction",minLength=5,maxLength=5,minCorpusCount=3)
print(Word)
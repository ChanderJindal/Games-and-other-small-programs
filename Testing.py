from random_word import RandomWords
r = RandomWords()
'''
# Return a single random word
a = r.get_random_word()
# Return list of Random words
b = r.get_random_words()
# Return Word of the day
c = r.word_of_the_day()

print(a,b,c)
'''
print( r.get_random_words(hasDictionaryDef="true" ,minLength=5,maxLength=5,limit =10 )  )
'''
hasDictionaryDef (string) - Only return words with dictionary definitions (optional)
includePartOfSpeech (string) - CSV part-of-speech values to include (optional)
excludePartOfSpeech (string) - CSV part-of-speech values to exclude (optional)
minCorpusCount (integer) - Minimum corpus frequency for terms (optional)
maxCorpusCount (integer) - Maximum corpus frequency for terms (optional)
minDictionaryCount (integer) - Minimum dictionary count (optional)
maxDictionaryCount (integer) - Maximum dictionary count (optional)
minLength (integer) - Minimum word length (optional)
maxLength (integer) - Maximum word length (optional)
'''
print( r.get_random_word(hasDictionaryDef="false",minLength=5,maxLength=5) )
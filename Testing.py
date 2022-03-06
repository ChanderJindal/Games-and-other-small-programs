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
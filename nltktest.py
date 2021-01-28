import nltk

s = '@This+ is a line.'
#print(nltk.word_tokenize(s))
#print(nltk.pos_tag(s))


from translate import Translator
t = Translator(to_lang='ur')

#print(t.translate('Good Morning'))


from spellchecker import SpellChecker
sc = SpellChecker()
wrong = sc.unknown(['good','toh'])
for i in wrong:
    print(sc.correction(i))
    print(sc.candidates(i))

import enchant
import wx
from enchant.checker import SpellChecker
from enchant.checker.CmdLineChecker import CmdLineChecker

def spelcheker(dict1, dict2, sent):
    txt = [] #to store new word
    my_dict = enchant.DictWithPWL(dict1, dict2)
    chek = SpellChecker(my_dict)
    chek.set_text(sent)
    for err in chek:
        print(f'Error : {err.word} ')
        sugg = err.suggest()
        sug = dict(zip(range(len(sugg)),sugg))
        
        print(f'How about this: {sug}')
        a=input("Select option or enter word to replace: ")
        if a.isnumeric():
            chek.replace(sug[int(a)])
        else:
            chek.replace(a)
            txt.append(a)

    return(chek.get_text())
    
dict1 = "en_US"
dict2 = "myword.txt"
sent = "Hi ths is to chek"
spelcheker(dict1, dict2, sent)

import enchant
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
        elif (not a):
            chek.replace(err.word)
            txt.append(err.word)
        else:
            chek.replace(a)
            txt.append(a)
    file=open("word.txt",'w')
    file.writelines(txt)
    file.close()

    return(chek.get_text())

dict1 = "en_US"
dict2 = "myword.txt"
sent = "Hi ths is to centrufel compreser mani"
spelcheker(dict1, dict2, sent)

import enchant
from enchant.checker import SpellChecker

def check(txt):
    
    chek = SpellChecker("en_US")
    chek.set_text(txt)
    for err in chek:
        print(f'{err.word} : {err.suggest()}')
        w=input("Enter word to replace :")
        chek.replace(w)

    return chek.get_text()
        
    


if __name__=="__main__":
    txt = input("Add text here: ")
    print(f'Before : {txt} \n')
    print(f'After : {check(txt)}')

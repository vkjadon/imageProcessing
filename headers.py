__version__='1.0.0'

def mainhead(title):
    lenofTitle=len(title)
    spacingLeft=39-int(lenofTitle/2)
    print('\n')
    print(' '*spacingLeft,'-'*lenofTitle)
    print(' '*spacingLeft,title)
    print(' '*spacingLeft,'-'*lenofTitle)

def subhead(title):
    lenofTitle=len(title)
    print('\n')
    print(title)
    print('-'*lenofTitle)

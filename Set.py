######################
#Set
def main():
    myset = {'apple', 'banana', 'berry'}
    yourset = {'man', 'woman', 'human'}

    x = list(yourset)
    x.append('male')
    
    print(myset)
    print(x)
    print(type(myset))
    print(type(yourset))
    print(type(x))
main()
def asciicnv(phr):
    l=[ord(c) for c in phr]     
    #l=[n1,n2,n3...]
    n=map(str,l)                
    #n=['n1','n2','n3',...]
    n=''.join(n)                
    #n='n1n2n3...'
    n=int(n)                    
    #n=n1n2n3
    if n>1:
        for i in range(2,n//2):
            if (n%i)==0:
                print ('n=',n,'is not a prime number')
                break
        else:
            print ('n=',n,'is a prime number')
    else:
        print ('n=',n,'is not a prime number')


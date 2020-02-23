fname=input("type file name:")
fin=open(fname,"r")
text=fin.read()
fin.close()
words=text.split()
#αύξουσα ταξινόμηση λέξεων με βάση το μέγεθος τους 
sortedwords=sorted(words,key=len)
#αντριστροφή στοιχείων λίστας ώστε η ταξινόμηση να είναι φθίνουσα
sortedwords=sortedwords[-1::-1]
vowels=("a","e","i","o","u")
#5 πρώτα στοιχεία==5 μεγαλύτερες λέξεις
for i in range(5):
    #προσπέλαση του κάθε στοιχείου/γράμματος του string 
    for x in sortedwords[i].lower():
        if x in vowels:
            #αντικατάσταση φωνηέντων με whitespace
            sortedwords[i]=sortedwords[i].replace(x,"")
for i in range(5):
    print(sortedwords[i][::-1])

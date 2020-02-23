fname=input("type file name:")
fin=open(fname,"r")
text=fin.read()
fin.close()
words=text.split()
for i in range(len(words)):
    if len(words[i])>3:
        words[i]+=words[i][0]+"ay"
        #αφαιρώ το πρώτο γράμμα ξεκινώντας το string από την επόμενη θέση
        words[i]=words[i][1:]
print(words)
        

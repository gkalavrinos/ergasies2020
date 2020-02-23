def luhn(n):
    evenSum=0
    oddSum=0
    length=len(n)
    valid=0
    if length==16:
        #προσπέλαση αντίστροφα από το τελευταίο ψηφίο
        for i in range(length-1,-1,-1):            #αλλιώς range(15-1,-1,-1)
            #άθροισμα ψηφίων σε περιττές θέσεις
            if i%2==1:
                digit=int(n[i])
                oddSum+=digit
            #διπλασιασμός και άθροισμα ψηφίων σε ζυγές θέσεις
            else:
                digit=2*int(n[i])
                digitSum=digit//10+digit%10       #d1d2//10==d1, d1d2%10==d2
                evenSum+=digitSum
        totalSum=evenSum+oddSum
        if totalSum%10==0:
            valid=1
    return valid


ccn=input("Type credit card number:")
if luhn(ccn):
    print("Credit card number is valid")
else:
    print("Credit card number in not valid")

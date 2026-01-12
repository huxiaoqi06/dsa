class fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __str__(self):
        if self.denominator==1:
            return self.numerator
        return f"{self.numerator}/{self.denominator}"
    def __add__(self,other):
        numerator=self.numerator*other.denominator+other.numerator*self.denominator
        denominator=self.denominator*other.denominator
        a=numerator
        b=denominator
        while b!=0:
            a,b=b,a%b
        numerator//=a
        denominator//=a
        return fraction(numerator,denominator)
    
l=list(input().split(' '))
print(str(fraction(int(l[0]),int(l[1]))+fraction(int(l[2]),int(l[3]))))
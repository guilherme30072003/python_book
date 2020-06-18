#Calcula o Máximo Divisor Comum(MDC) entre dois números a e b, onde a>b
def mdc(a,b):
    if b==0:
        return a
    elif a>b:
        return mdc(b,a%b)
print(mdc(2,0))
print(mdc(12,8))
print(mdc(18,12))
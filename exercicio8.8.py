#Calcula o Mínimo Múltiplo Comum(MMC) a partir da função do MDC, feito no exercicio8.7.py
def mmc(a,b):
    return abs(a*b)/mdc(a,b)
def mdc(a,b):
    if b==0:
        return a
    elif a>b:
        return mdc(b,a%b)
print(mmc(12,8))
print(mmc(18,12))
print(mmc(55,23))
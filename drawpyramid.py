n = int(input("pyramid height (floor): "))
m = ''
for i in range(n+1):
    m = abs(i-n)
    c =" "*m+"*"*(i-1)+"*"*i
    print(c)
    
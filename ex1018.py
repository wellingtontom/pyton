valor = int(input())
h = int(valor/60/60)
m = int((valor / 60) - (h * 60))
s = int(valor - ((h*60*60) + (m * 60)))
print(str(h)+':'+str(m)+':'+str(s))
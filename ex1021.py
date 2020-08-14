N = float(input('Digite um valor:'))

notas = [100.00,50.00,20.00,10.00,5.00,2.00,1.00]
print ("notas :")
for x in notas:
    print ("%i nota(s) de R$ %.2f"%((N/x),x))
    N %= (x)
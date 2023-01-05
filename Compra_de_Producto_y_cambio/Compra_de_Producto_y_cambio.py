# Construir un programa que, al recibir como datos el costo de un articulo vendido
#y la candidad de dinero entregada por el cliente calcule:
    #1 El cambio que se debe entregar al cliente, si el pago afectuado es mayor que el precio del producto
    #2 Que pasa si el cliente paga exactamente lo que vale el producto?
    #3 La cantidad de dinero que falta por pagar, si el pago afectuado es menor que el precio del producto
    
pre=float(input("Ingrese el precio del articulo:"))
pag=float(input("cuanto ha pagado el cliente?:"))

cambio=pag-pre
faltante=pre-pag

if(cambio<0):
    print("Falta dinero en el pago. El dinero faltante es ",faltante)
    
elif(cambio==0):
    print( "Se a pagado exacto. No es necesario dar cambio")
    
if(cambio>0):
    print ("El cambio a dar es", cambio)        
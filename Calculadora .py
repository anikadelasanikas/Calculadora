def suma( a, b):
return a + b:

def resta (a, b ):
return  a - b:

def multiplicacion (a, b):
return a * b:

def division (a, b):
return a // b:

while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
        
    opcion = input("Elige una opción (1-5):")
    
    if opcion == "5":
        print("Saliendo del programa...")
        break
    
    a = float(input("Pon un numero:"))
              
    b = float(input("Pon un segundo numero:"))
              
   if opcion == "1":
       print (f"Resultado {suma(a,b)}")
   elif opcion == "2":
       print (f"Resultado {resta(a,b)}")
              
   elif opcion == "3":
       print (f"Resultado {multiplacion(a,b)}")
              
   elif opcion == "4":
              
       print (f"Resultado {division(a,b)}")
              
              
             
    

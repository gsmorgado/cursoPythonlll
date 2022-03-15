def def_number(number: int)-> bool:    
    contador = 0
    for i in range(1,number+1):
        if i==1 or i ==number:        
            continue
        if  number%i == 0:
            contador=+1    
    if contador==0:
        return True
    else:
        return False
    

def run():
    try:
        number = int(input("Escribe un numero: "))
        if def_number(number):
            print ("Es número primo")
        else :
            print ( "No es número primo"  )
    except ValueError:
        print("Solo debes ingresar numeros")

if __name__=='__main__':
    run()

 



import sys  #Import del paquete "Sys" para manipular la consola desde el programa
 
class Usuario:  #Clase "Usuario" es la clase de los objetos que se utilizarán en el programa
    
    def __init__ (self, NombreComp, ID, Tipo, Saldo):
        self.NombreComp = NombreComp
        self.ID = ID
        self.Tipo = Tipo
        self.Saldo = Saldo
        
usuarios = [] #Se crea la lista vacía "usuarios" a utilizarse más adelante
IDs = 0 #Se declara la variable global IDs que llevará registro de los usuarios 

def Buscar_ID(ID_Buscado):
    
    for usuario in usuarios:
        
        if usuario.ID == ID_Buscado:
            return usuario
        else: 
            return None #Función "Buscar_ID" tiene como parámetro un ID a buscar en la lista "usuarios" y devuelve el objeto al que se le atribuye el ID buscado mediante una comparación simple

def Mod_Saldo(ID,Monto):
    
    for usuario in usuarios:
        
        if usuario.ID == ID:
            usuario.Saldo += Monto  #Función "Mod_Saldo" utilizada para cualquier movimiento de saldo, busca el objetivo comparando un atributo con un valor buscado para modificar otro atributo del objeto

def Buscar_Nombre(Nombre):
    
    for usuario in usuarios:
        if usuario.NombreComp == Nombre:
            return usuario
        else:
            return None #Función "Buscar_Nombre" tiene como parámetro un nombre a buscar en la lista "usuarios" y devuelve el objeto al que se le atribuye el nombre buscado mediante una comparación simple

def Registra():
        global IDs
        
        Apellidos = input("\n Apellidos de usuario :  ")
        Nombre = input(" Nombre de usuario  :  ")
        ID = IDs+1
        try:
            Saldo = int(input(" Deposito inicial:  "))
        except:
            print("Eso no es un numero, saldo inicial declarado a 0")
            Saldo = 0
        Tipo = 'Plata'
        NombreComp = Nombre + " " + Apellidos
        NombreComp = NombreComp.title()
        
        usuario = Usuario(NombreComp,ID,Tipo,Saldo)
        usuarios.append(usuario)
        print("\nSe agrego con exito a " + NombreComp + " con el ID " + str(ID))
        Correct = input("\nEsta operacion fue correcta? Y/N")
        if Correct == "Y" or Correct =="y":
            print("")
        else:
            usuarios.pop()
            IDs -= 1
            
            
        return None #Función "Registra" recopila datos del usuario y los pasa la función constructor de la clase Usuario

def Del_Acount():
    
    Trgt = int(input("Conoce el ID de la cuenta a eliminar, de ser asi, teclee el ID, en caso contrario, presione 0\n\t"))
    if Trgt > 0:
         try:
            ObjIn = Buscar_ID(Trgt)
         except:
            print("Usuario no encontrado")
    else:
         NomBusq = input("Cual es el nombre completo del cuentahabiente?")
    try:
         ObjIn = Buscar_Nombre(NomBusq)
    except:
         print("Usuario no encontrado")

    print("\nLa informacion de la cuenta es: \n Usuario: "+ObjIn.NombreComp+ "\n ID: "+str(ObjIn.ID)+"\n Tipo de miembro: "+ObjIn.Tipo)
    Correct = input("\nEs la informacion correcta? Y/N")
    if Correct == "Y" or Correct =="y":
        del usuarios[ObjIn.ID]
        print("\nSe elimino con exito a " + ObjIn.NombreComp + " con el ID " + str(ObjIn.ID)) #Función "Del_Acount" elimina una cuenta objetivo identificándola con las funciones anteriores de búsqueda

def Cash_In(): 
    
    Trgt = int(input("Conoce el ID de la cuenta a realizar el ingreso, de ser asi, teclee el ID, en caso contrario, presione 0\n\t"))
    if Trgt > 0:
        try:
                        ObjIn = Buscar_ID(Trgt)
        except:
                        print("Usuario no encontrado")
    else:
        NomBusq = input("Cual es el nombre completo del cuentahabiente?")
        try:
                        ObjIn = Buscar_Nombre(NomBusq)
        except:
                        print("Usuario no encontrado")                       
    print("\nLa informacion de la cuenta es: \n Usuario: "+ObjIn.NombreComp+ "\n ID: "+str(ObjIn.ID)+"\n Tipo de miembro: "+ObjIn.Tipo)
    Correct = input("\nEs la informacion correcta? Y/N")
    if Correct == "Y" or Correct =="y":
        Monto = int(input("\nCuanto desea ingresar? "))
        Mod_Saldo(ObjIn.ID,Monto)
        print("Operacion realizada con exito")
        print("Su nuevo balance es: "+str(ObjIn.Saldo))
    else:
       print("Operacion cancelada") #Función "Cash_In" identifica una cuenta a ingresar efectivo con las funciones de búsqueda y modifica su saldo

def Cash_Out():
    
    Trgt = int(input("Conoce el ID de la cuenta a realizar el retiro, de ser asi, teclee el ID, en caso contrario, presione 0\n\t"))
    if Trgt > 0:
       try:
          ObjIn = Buscar_ID(Trgt)
       except:
          print("Usuario no encontrado")
    else:
       NomBusq = input("Cual es el nombre completo del cuentahabiente?")
       try:
          ObjIn = Buscar_Nombre(NomBusq)
       except:
          print("Usuario no encontrado")              
    print("\nLa informacion de la cuenta es: \n Usuario: "+ObjIn.NombreComp+ "\n ID: "+str(ObjIn.ID)+"\n Saldo: "+str(ObjIn.Saldo))
    Correct = input("\nEs la informacion correcta? Y/N")
    if Correct == "Y" or Correct =="y":
       Monto = int(input("\nCuanto desea retirar? "))
       if ObjIn.Saldo >= Monto:
           Mod_Saldo(ObjIn.ID,-Monto)
           print("Operacion realizada con exito")
           print("Su nuevo balance es: "+str(ObjIn.Saldo))
       else:
           print("Saldo insuficiente")
    else:
        print("Operacion cancelada") #Función "Cash_Out" identifica una cuenta a retirar efectivo con las funciones de búsqueda y modifica su saldo

def Transfer():
    
    Trgt = int(input("Conoce el ID de la cuenta destinataria de la transferencia, de ser asi, teclee el ID, en caso contrario, presione 0\n\t"))
    if Trgt > 0:
        try:
            ObjIn = Buscar_ID(Trgt)
        except:
            print("Usuario no encontrado")
    else:
        NomBusq = input("Cual es el nombre completo del cuentahabiente?")
    try:
        ObjIn = Buscar_Nombre(NomBusq)
    except:
        print("Usuario no encontrado")
        
    print("\nLa informacion de la cuenta es: \n Usuario: "+ObjIn.NombreComp+ "\n ID: "+str(ObjIn.ID)+"\n Tipo de miembro: "+ObjIn.Tipo)
    Correct = input("\nEs la informacion correcta? Y/N")
    if Correct == "Y" or Correct =="y":
        Trgt2 = int(input("Conoce el ID de la cuenta remitente de la transferencia, de ser asi, teclee el ID, en caso contrario, presione 0\n\t"))
    if Trgt2 > 0:
        try:
           ObjIn2 = Buscar_ID(Trgt2)
        except:
           print("Usuario no encontrado")
        else:
           NomBusq2 = input("Cual es el nombre completo del cuentahabiente?")
        try:
           ObjIn2 = Buscar_Nombre(NomBusq2)
        except:
           print("Usuario no encontrado")
           
        print("\nLa informacion de la cuenta es: \n Usuario: "+ObjIn2.NombreComp+ "\n ID: "+str(ObjIn2.ID)+"\n Saldo: "+str(ObjIn2.Saldo))
        Correct = input("\nEs la informacion correcta? Y/N")
        if Correct == "Y" or Correct =="y":
             Monto = int(input("\nCuanto desea transferir? "))
             if ObjIn2.Saldo >= Monto:
                 Mod_Saldo(ObjIn2.ID,-Monto)
                 Mod_Saldo(ObjIn.ID,Monto)
                 print("Operacion realizada con exito")
                 print("Su nuevo balance es: "+str(ObjIn2.Saldo))
             else:
                 print("Saldo insuficiente")
        else:
            print("")
    else:
        print("Operacion cancelada") #Función "Transfer" identifica 2 cuentas para transferir efectivo de una a otra

def Menu():
    global IDs
    try:
        Opt = int(input("\n Bienvenido al sistema \n Elija la operacion a realizar \n 1.- Registrar usuario \n 2.- Eliminar usuario \n 3.- Registrar ingreso \n 4.- Registrar retiro \n 5.- Registrar transaccion \n 6.- Salir \n"))
    except:
        print("Eso no es un numero")
    try:
        match Opt:
            case 1: #Registro de usuarios nuevos
            
                Registra()
                IDs+=1    
            
            case 2: #Borrado de cuentas
                
                Del_Acount()
                
            case 3: #Depósito a una cuenta
            
                Cash_In()
        
            case 4: #Retiro de una cuenta
                
                Cash_Out()
        
            case 5: #Transferencia entre 2 cuentas
            
                Transfer()           
            
            case 6: #Salir
                sys.exit()
    
    except:
        if Opt == 6:
            sys.exit()
        else:
            print("  Opcion invalida") #Función "Menu" que permite mediante una estructura match la elección del trámite a realizar
    
Admin = Usuario("Admin",0,"Platino", 17) #Construccion de un usuario predeterminado para pruebas
usuarios.append(Admin)
while (1):  #Ciclado de Menú hasta que se elija la opción "Salir"

    Menu()
    

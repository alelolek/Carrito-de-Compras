import time
import math

RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'



listaProducto = [ [1,"Audifono",69.9],
[2,"Iphone 14",6999.0],
[3,"Cargador tipo C",39.9],
[4,"Case iphone 7p",29.9],
[5,"Apple pencil",280.0],
[6,"Ipad mini 1",350.50],
[7,"Mouse",50.90],
[8,"Macbook",7700.9],
[9,"Airpods",740.0],
[10,"Bateria portatil",199.50]]

listaCarrito = []
     


# print(lista)


def mostrarProductos(unalista):

    valor = print ("{:<8} {:<20} {:<10}".format('CODIGO','PRODUCTO',"PRECIO"))
    
    for v in unalista:
        cod, pro,pre = v
        print ("{:<8} {:<20} {:<10}".format( cod, pro,pre))
    print("\n"+51*"*"+"\n")
    return valor

# def mostrarCarrito(unalista):

#     valor = print ("{:<8} {:<18} {:<10}".format('CODIGO','PRODUCTO',"PRECIO"))
        
#     for v in unalista:
#             cod, pro,pre = v
#             print ("{:<8}  {:<18} {:<10}".format( cod,  pro,pre))
    
#     return valor
    


def menu():
    respuesta1 = ""
    while respuesta1 !="4":
        print("\n"+"\n"+20*"*","MENU PRINCIPAL","*"*20,"\n")
        print("1. Escoger producto")
        print("2. Buscar producto")
        print("3. Ver carrito")
        print("4. Salir")
        respuesta1 = input("Elige una opcion: ")
        

        if respuesta1 == "1":
            print("")
            escogerProducto()
        elif respuesta1 == "2":
            buscarProducto()
        elif respuesta1 == "3":
            print("")
            mostrarProductos(listaCarrito)  
            if(len(listaCarrito) != 0):
                suma = []
                for i in listaCarrito:
                    suma.append(i[2])
                preciototal = math.fsum(suma)
                time.sleep(1)
                print("\n"+"El total a pagar es: "+ str(preciototal),"\n")
            else:
                print("\n"+"El carrito de compras esta vacio","\n")

        elif respuesta1 == "4":
            print("Hasta luego!")
            respuesta1 = "4"
        else:
            respuesta1 = input("Ingresa una opcion valida: ")

        time.sleep(2)
        
def añadirCarrito(producto):
    listaCarrito.append(producto)


def buscarProducto():
    respuesta = ""
    while respuesta != "1":
        producto =  input("Ingresa el producto por buscar: ")
        # producto = producto.capitalize()
        for pro in listaProducto:
            # print(pro[2])
            if pro[1] == producto:
                print(pro)
                print("\n"+"1. Añadir producto")
                print("2. Buscar otro producto ")
                print("3. Ir al menu principal")
                respuesta = input("elige una opcion: ") 
                if respuesta == "1":
                    añadirCarrito(pro)
                    print("Se añadio el producto al carrito de compras.")
                elif respuesta == "2":
                    respuesta == "2"
                elif respuesta == "3":
                    menu()
                else: 
                    respuesta = input("Elige una opcion valida : ")
            else:
                print("Lo siento! NO contamos con ese producto.")

                menu()
                break
                

    # if producto in listaCarrito:
    #    producto[0]



def escogerProducto():
    print("\n"+"\n"+20*"*","CATÄLOGO","*"*20+"\n")
    mostrarProductos(listaProducto)
    time.sleep(2)
    print("Ingresa el código del producto a comprar")
    respuesta = int(input("Añade a tu carrito de compras: "))
    producto = listaProducto[respuesta-1]

    añadirCarrito(producto)
    time.sleep(1)
    print("\n"+"Excelente, has añadido un "+producto[1]+" al carrito de compras")
    


if __name__=="__main__":
    menu()



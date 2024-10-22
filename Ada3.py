
class Postres:
    def __init__(self):
        self.productos = []  

    def insertar(self, postre, ingredientes):
        self.productos.append((postre, ingredientes))
        print(f"Postre '{postre}' agregado con ingredientes: {', '.join(ingredientes)}")

    def listar_ingre(self, postre):
        encontrado = False
        for p, ing in self.productos:
            if p == postre:
                print(f"Ingredientes de '{postre}': {', '.join(ing)}")
                encontrado = True
        if not encontrado:
            print("Postre no encontrado.")

    def agregar_ingre(self, postre, ingrediente):
        for i, (p, ing) in enumerate(self.productos):
            if p == postre:
                self.productos[i][1].append(ingrediente)
                print(f"Ingrediente '{ingrediente}' agregado a '{postre}'.")
                return
        print("Postre no encontrado.")

    def eliminar_ingre(self, postre, ingrediente):
        for i, (p, ing) in enumerate(self.productos):
            if p == postre:
                if ingrediente in ing:
                    ing.remove(ingrediente)
                    print(f"Ingrediente '{ingrediente}' eliminado de '{postre}'.")
                    return
                else:
                    print(f"Ingrediente '{ingrediente}' no encontrado en '{postre}'.")
                    return
        print("Postre no encontrado.")

    def eliminar_postre(self, postre):
        self.productos = [(p, ing) for p, ing in self.productos if p != postre]
        print(f"Postre '{postre}' eliminado si existía.")

    def mostrar_postres(self):
        if self.productos:
            print("\nEstado actual de los postres:")
            for postre, ingredientes in self.productos:
                print(f"[[{postre}] = [{', '.join(ingredientes)}]]")
        else:
            print("No hay postres disponibles.")

    def eliminar_duplicados(self):
        seen = set()
        self.productos = [x for x in self.productos if not (x[0] in seen or seen.add(x[0]))]
        print("Duplicados de postres eliminados.")

def menu():
    mnus = Postres()
    
    while True:
        print("\nMenu de opciones:")
        print("1. Agregar postre")
        print("2. Listar ingredientes de un postre")
        print("3. Agregar ingrediente a un postre")
        print("4. Eliminar ingrediente de un postre")
        print("5. Eliminar postre")
        print("6. Eliminar duplicados de postres")
        print("7. Salir")
        
        opcion = input("Inserte la opción que desea realizar: ")

        if opcion == '1':
            postre = input("Nombre del postre: ")
            ingredientes = input("Ingredientes (separados por coma): ").split(',')
            ingredientes = [ing.strip() for ing in ingredientes]  
            mnus.insertar(postre, ingredientes)

        elif opcion == '2':
            postre = input("Nombre del postre: ")
            mnus.listar_ingre(postre)

        elif opcion == '3':
            postre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a agregar: ")
            mnus.agregar_ingre(postre, ingrediente)

        elif opcion == '4':
            postre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a eliminar: ")
            mnus.eliminar_ingre(postre, ingrediente)

        elif opcion == '5':
            postre = input("Nombre del postre a eliminar: ")
            mnus.eliminar_postre(postre)

        elif opcion == '6':
            mnus.eliminar_duplicados()

        elif opcion == '7':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")
        
        mnus.mostrar_postres()

menu()

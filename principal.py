from BD.conexion import DAO
import funciones
def menu_principal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            print("================ MENÚ PRINCIPAL ==============")
            print("1.- Listar contactos")
            print("2.- Registar contacto")
            print("3.- Actualizar contacto")
            print("4.- Eliminar contacto")
            print("5.- Salir")
            print("==============================================")
            opcion = int(input("Seleccionar una opción: "))
            if not 0 < opcion < 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcion_correcta = True
                ejecutar_opcion(opcion)

def ejecutar_opcion(opcion):
    dao = DAO()
    match opcion:
        case 1:
            try:
                print("Opción 1: Listar contactos")
                contactos = dao.listar_contactos()
                funciones.listar_contactos(contactos) if len(contactos) > 0 else print("No se encontrarón contactos...")
            except:
                print("Ocurrio un error...")
        case 2:
            try:
                print("Opción 2: Registro")
                contacto = funciones.pedir_registro_contacto()
                dao.registrar_contacto(contacto)
            except:
                print("Ocurrio un error...")
        case 3:
            try:
                print("Opción 3: Actualización")
                contactos = dao.listar_contactos()
                if len(contactos) > 0:
                    actualizar_contacto = funciones.actualizar_contacto(contactos)
                    if actualizar_contacto is not None:
                        dao.actualizar_contacto(actualizar_contacto)
                    else:
                        print("Actualización cancelada.")
                else:
                    print("No se encontrarón contactos para actualizar...")
            except:
                print("Ocurrio un error...")
        case 4:
            print("Opción 4: Eliminación")
            try:
                contactos = dao.listar_contactos()
                if len(contactos) > 0:
                    id_contacto_eliminar = funciones.pedir_datos_eliminar(contactos)
                    if id_contacto_eliminar is not None:
                        dao.eliminar_contacto(id_contacto_eliminar)
                    else:
                        print("Eliminación cancelada.")
                else:
                    print("No se encontrarón contactos...")

            except:
                print("Ocurrio un error...")
        case _:
            print("Opción no válida...")


menu_principal()


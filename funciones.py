def listar_contactos(lista_contactos):
    print("\nContactos: \n")
    contador = 1
    for contacto in lista_contactos:
        datos = f"id_contact: {contacto[0]} | name_contact: {contacto[1]} | phone: {contacto[2]} | birthdate: {contacto[3]} | country: {contacto[4]}"
        print(f"{contador}.- {datos}")
        contador += 1
    print()

def pedir_registro_contacto():
    nombre_contacto = str(input("Ingrese el nombre del contacto: "))
    numero_telefono = int(input("Ingrese el número de telefono: "))
    fecha_nacimiento = str(input("Ingrese fecha nacimiento formato (año-mes-día) ejemplo: '1983-01-25': "))
    pais = str(input("Ingrese país de origen: "))
    datos = (nombre_contacto, numero_telefono, fecha_nacimiento, pais)
    return datos


def actualizar_contacto(contactos):
    while True:
        listar_contactos(contactos)
        lista_id_contact = [str(contacto[0]) for contacto in contactos]
        print("Opciones id_contact:", lista_id_contact)
        id_contacto_actualizar = input("Ingrese el número del id_contact a actualizar (o 'q' para cancelar): ")
        if id_contacto_actualizar == "q":
            return None
        elif id_contacto_actualizar.isdigit() and id_contacto_actualizar in lista_id_contact:
            actualizacion_datos = pedir_registro_contacto()
            print(actualizacion_datos)
            return [actualizacion_datos, int(id_contacto_actualizar)]
        else:
            print("El id_contact no es válido. Por favor, ingrese un ID válido.")




def pedir_datos_eliminar(contactos):
    while True:
        listar_contactos(contactos)
        lista_id_contact = [str(contacto[0]) for contacto in contactos]
        print("Opciones id_contact:", lista_id_contact)
        id_contact = input("Ingrese el número del id_contact a eliminar (o 'q' para cancelar): ")

        if id_contact == 'q':
            return None  # El usuario canceló la eliminación
        elif id_contact.isdigit() and id_contact in lista_id_contact:
            return int(id_contact)
        else:
            print("El id_contact no es válido. Por favor, ingrese un ID válido.")


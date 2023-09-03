import mysql.connector
from mysql.connector import Error
class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                user="root",
                password="root",
                host="localhost",
                port="3306",
                database="contacts"
            )
        except Error as err:
            print("Error al internar hacer la conexión {0}".format(err))

    def listar_contactos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM `contacts`")
                contactos = cursor.fetchall()
                return contactos

            except Error as err:
                print(f"Error al intentar la conexión: {err}")
            finally:
                self.conexion.close()

    def registrar_contacto(self, contacto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO `contacts`(name_contact, phone, birthdate, country) VALUES ('{0}', {1}, '{2}', '{3}')"
                cursor.execute(sql.format(contacto[0], contacto[1], contacto[2], contacto[3]))
                self.conexion.commit()
                print("¡Registro realizado con éxito!\n")
            except mysql.connector.Error as err:
                print(f"Error al intentar la conexión: {err}")
            finally:
                self.conexion.close()

    def actualizar_contacto(self, nuevo_contacto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                datos, id = nuevo_contacto
                sql = f"""UPDATE `contacts` SET name_contact = '{datos[0]}', phone = {datos[1]}, birthdate = '{datos[2]}', 
                country = '{datos[3]}' WHERE id_contact = {id}"""
                cursor.execute(sql)
                self.conexion.commit()
                print("Actualización realizado con éxito.")

            except mysql.connector.Error as err:
                print(f"Error al intentar la conexión: {err}")
            finally:
                self.conexion.close()


    def eliminar_contacto(self, id_contact):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM `contacts` WHERE id_contact = {0}"
                cursor.execute(sql.format(id_contact))
                self.conexion.commit()
                print("Eliminación exitosa.")
            except Error as err:
                print("Ha surgido un error en la eliminación {0}".format(err))
            finally:
                self.conexion.close()



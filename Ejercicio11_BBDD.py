import sqlite3

def crear_conexion(base_datos):
    try:
        conn=sqlite3.connect(base_datos)
        return conn
    except sqlite3.Error as error:
        print('Se ha producido un error al crar la conexión: ',error)

def borrar_tabla(conn,tabla):
    sqlBorrarTabla='''DROP TABLE %s;'''%tabla
    cursor=conn.cursor()
    cursor.execute(sqlBorrarTabla)
    conn.commit()

def crear_tabla(conn, sentencia):   
    cursor=conn.cursor()
    cursor.execute(sentencia)
    conn.commit()

def mostrar_tabla(conn):
    sqlMostrarTabla='''SELECT name FROM sqlite_master WHERE type="table"''' 
    cursor=conn.cursor()
    cursor.execute(sqlMostrarTabla)
    tablas=cursor.fetchall()
    for t in tablas:
        print("Nombre de la tabla: ",t[0])

def insertar_alumnos(conn):
    variosAlumnos=[
        (1,"Juan","Perez"),
        (2,"Jorge","Lopez"),
        (3,"Pablo","Gonzalez"),
        (4,"Soe","Segovia"),
        (5,"Lu","Castro"),
        (6,"Ro","Pared"),
        (7,"Yesica","Gutierrez"),
        (8,"Liz","Lucich")       
    ]
    cursor=conn.cursor()
    cursor.executemany('''INSERT INTO Alumnos VALUES(?,?,?)''', variosAlumnos)
    conn.commit()

def recuperar_alumnos(conn):
    sqlRecuperarRegistros='''SELECT * FROM Alumnos;'''
    cursor=conn.cursor()
    cursor.execute(sqlRecuperarRegistros)
    alumnos=cursor.fetchall()
    for a in alumnos:
        print(a)

def recuperar_alumnos_por_nombre(conn, nombre):
    sqlRecuperarPorNombre='''SELECT * FROM Alumnos WHERE Nombre=?;'''
    cursor=conn.cursor()
    cursor.execute(sqlRecuperarPorNombre,(nombre,))
    alumnosPorNombre=cursor.fetchall()
    if alumnosPorNombre==[]:
        print("No hay coincidencias en la base de datos")
    else:
        for a in alumnosPorNombre:
            print(a)

def main():

    conectarTabla=crear_conexion("BBDD_alumnos.db")

    sqlCrearTabla='''CREATE TABLE Alumnos (id_alumno INTEGER,Nombre VARCHAR(40),Apellido VARCHAR(40))'''

    borrar_tabla(conectarTabla, "Alumnos")

    crear_tabla(conectarTabla,sqlCrearTabla)

    mostrar_tabla(conectarTabla)

    insertar_alumnos(conectarTabla)

    recuperar_alumnos(conectarTabla)
    print()
    nombre=input("Ingrese un nombre de alumno para buscar: ")
    print("Registros con nombre %s..." % nombre)
    recuperar_alumnos_por_nombre(conectarTabla,nombre)

    if conectarTabla:
        conectarTabla.close()

if __name__=='__main__':
    main()  

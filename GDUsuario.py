"""
    UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
                
                Proyecto Unidad 1

        Autor:Jorge Gabriel Caicedo Viteri

        Materia: Sistema de Base de Datos
    
    Modelado de un Sistema Academico para Niños Parvulos

                   2022-2023

"""
'''Libreria que ofrece herramientas para la manipulación y análisis de datos, 
como tablas númericas y series temporales'''
import pandas as pd
'''Libreria de generación aleatoria de UUID a partir de 32 digitos
hexadecimales'''
import uuid
'''Modulo para generación de números aleatorios'''
import random
'''Libreria que genera datos falsos como Nombres,Apellidos,Direcciones,etc'''
from faker import Faker
'''Modulo para manipular fechas y horas'''
import datetime

'''Total de registros a generar'''
num_registros = 10000
#Libreria que usaremos para generar algunos datos aleatorios
faker = Faker('es_CO')

"""
Definicion de los atributos de la entidad Usuario.

ID(IdU)=El id del Usuario que sera unico para cada uno.
Nombre(NombreU)=El nombre del Usuario.
Password(PasswordU)=El password que tiene el Usuario.
Foto(FotoU)=Foto que sirva como password.
Estado(EstadoU)=Estado del Usuario.

"""
CaracteristicasUsuario = [
    "IdU" ,
    "NombreU" ,
    "PasswordU",
    "FotoU",
    "EstadoU"
    ]

def Id_Usuario_Gen():
    """
    Funcion para generar ids para el Usuario sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids del Usuario

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="U00"
        if contador < 10:
            Nombre=Nombre+"00000"+str(contador)
        if contador >= 10 and contador <100:
            Nombre=Nombre+"0000"+str(contador)
        if contador >= 100 and contador <1000:
            Nombre=Nombre+"000"+str(contador)
        if contador >= 1000 and contador <10000:
            Nombre=Nombre+"00"+str(contador)
        if contador >= 10000 and contador <100000:
            Nombre=Nombre+"0"+str(contador)
        Lista.append(Nombre)
        contador = contador + 1 

    return Lista
def Password_Usuario_Gen():
    """
    Funcion para generar el password del usuario sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con los telefonos de los docentes

    """
    contador=0
    Lista=[]
    while contador < num_registros:
        Numero=str(random.randint(0,10000)) + "*" + str(random.randint(0,10000))
        if Numero in Lista:
            Numero=""
        else:
            Lista.append(Numero)
            contador = contador + 1

    return Lista
def emailGen(nombre,apellido,duplicateFound=False):
    """
    Funcion para generar emails aleatorios de acuerdo al nombre y apellido del estudiante.

    Parametros
    ----------

        nombre : str
            
            Variable tipo String del nombre del estudiante que espera  la función.

        apellido : str
            
            Variable tipo String del apellido del estudiante que espera  la función.

        duplicateFound : bool
            
            Variable tipo Bool que funcionara para identificar duplicados.

    Retorna
    -------

        Retornara el email del estudiante de acuerdo a sus datos.

    """
    dom = "@educacion.edu.ec" #Dominio de la institucion academica
    nombre = nombre.lower().split(" ")
    apellido = apellido.lower().split(" ")
    chars = [".","_"]
    nuevo_nombre = nombre[0] + random.choice(chars) + apellido[0]
    
    if duplicateFound:#En caso de encontrar duplicados
        num = random.randint(0,100)
        nuevo_nombre = nuevo_nombre + str(num)
    
    return nuevo_nombre + dom

def fotoGen(nombre,apellido,duplicateFound=False):
    """
    Funcion para generar urls aleatorios de la foto del estudiante de acuerdo al nombre y apellido del estudiante.

    Parametros
    ----------

        nombre : str
            
            Variable tipo String del nombre del estudiante que espera  la función.

        apellido : str
            
            Variable tipo String del apellido del estudiante que espera  la función.

        duplicateFound : bool
            
            Variable tipo Bool que funcionara para identificar duplicados.

    Retorna
    -------

        Retornara el url de la foto del estudiante de acuerdo a sus datos.

    """
    url ="https://www.mcb.edu.ec/"#Sitio de almacenamiento
    link = ".png"#formato de la imagen
    nombre = nombre.lower().split(" ")
    apellido = apellido.lower().split(" ")
    chars = ["_"]
    nuevo_nombre = nombre[0] + random.choice(chars) + apellido[0]
    
    if duplicateFound:
        num = random.randint(0,100)
        nuevo_nombre = nuevo_nombre + str(num)
    
    return url + nuevo_nombre + link
#Elaboración del dataframe
df = pd.DataFrame(columns=CaracteristicasUsuario)
#Generacion de los ids del Usuario
df['IdU'] = Id_Usuario_Gen()
#Llamar al csv Estudiante
dfestudiante = pd.read_csv("Estudiante.csv")
#Arrays para guardar los emails y urls de las fotos
emails = []
fotos=[]
index = 0
#Creacion de los emails y urls de las fotos
for nombre in dfestudiante['NombreE']:
    apellido = dfestudiante.loc[index]['ApellidoE']#Obtener el apellido de la misma posicion que el nombre en el registro
    index += 1
    email = emailGen(nombre,apellido)
    foto = fotoGen(nombre,apellido)
    while email in emails:
        email = emailGen(nombre,apellido,duplicateFound=True)
        foto = fotoGen(nombre,apellido,duplicateFound=True)
    
    emails.append(email)#Añadir el email al array de email
    fotos.append(foto)#Añadir el url al array de urls

df['NombreU'] = emails#Asignar los datos del array de email a la columna "email" del dataframe
df['FotoU'] = fotos#Asignar los datos del array de urls a la columna "foto" del dataframe
#Generacion de los ids del Usuario
df['PasswordU'] = Password_Usuario_Gen()
#Generacion aleatoria del estado del Usuario
Estados = ["Activo", "Inactivo"]

df['EstadoU'] = random.choices(
    Estados,
    k=num_registros
    )
#Generacion del archivo Usuario.csv donde se guardaran los datos
df.to_csv('Usuario.csv')
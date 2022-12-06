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
Definicion de los atributos de la entidad Docente

ID(IdD)=El id del docente que sera unico para cada uno
Nombre(NombreD)=El nombre del docente generado aleatoriamente.
Apellido(ApellidoD)=El apellido del docente generado aleatoriamente.
Fecha de Nacimiento(FechaNacD)=La fecha de nacimiento del docente.
Edad(EdadD)=La edad del docente.
Genero(GeneroD)=El genero del docente que sera masculino o femenino.
Titulo(TituloD)=El titulo del docente.
Telefono(TelefonoD)=El telefono del docente.
"""
Caracteristicasdocente = [
    "IdD" ,
    "NombreD" ,
    "ApellidoD" ,
    "FechaNacD" ,
    "EdadD",
    "GeneroD" ,
    "TituloD" ,
    "TelefonoD"
    ]
def Id_docente_Gen():
    """
    Funcion para generar ids para el docente sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids de los docentes

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="D00"
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
def Telefono_docente_Gen():
    """
    Funcion para generar el telefono del docente sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con los telefonos de los docentes

    """
    contador=0
    dfRepresentante=pd.read_csv("Representante.csv")
    Lista=[]
    while contador < num_registros:
        Numero="098" + str(random.randint(0,9)) + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
        if Numero in Lista or Numero in dfRepresentante["TelefonoR"]:
            Numero=""
        else:
            Lista.append(Numero)
            contador = contador + 1

    return Lista
def nombre_gen(genero):
    """
    Funcion para generar nombres aleatorios de acuerdo al genero.

    Parametros
    ----------

        genero : str
            
            Variable tipo String del genero que espera  la función.

    Retorna
    -------

        Retornara el nombre dependiendo si es masculino o femenino

    """

    if genero=='Masculino':
        return faker.first_name_male()
    elif genero=='Femenino':
        return faker.first_name_female()
def random_dob(start, end, n):
    """
    Funcion para generar fechas de nacimiento de acuerdo a 2 fechas que funcionan como limites.

    Parametros
    ----------

        start : str
            
            Variable tipo String de la fecha maxima que espera  la función.

        end : str
            
            Variable tipo String de la fecha minima que espera  la función.

        n : int
            
            Variable tipo int que tiene el numero total de registros a crear.

    Retorna
    -------

        Retornara un array con diferentes fechas de nacimiento.

    """
    frmt = "%Y-%m-%d"
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    td = etime - stime
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]
    return times
def edadGen(fecha):
    """
    Funcion para devolver la edad de acuerdo a su fecha de nacimiento.

    Parametros
    ----------

        fecha : str
            
            Variable tipo String de la fecha de nacimiento que espera  la función.


    Retorna
    -------

        Retornara un int con la edad.

    """
    frmt = "%Y-%m-%d"
    Actualidad = datetime.datetime.today()
    nac = datetime.datetime.strptime(fecha, frmt)
    edad = Actualidad.year - nac.year - ((Actualidad.month, Actualidad.day) < (nac.month, nac.day))
    return edad
#Elaboración del dataframe
df = pd.DataFrame(columns=Caracteristicasdocente)
#Generacion aleatoria del id del docente
df['IdD'] = Id_docente_Gen()
#Generacion aleatoria del genero del docente
generos = ["Masculino", "Femenino"]

df['GeneroD'] = random.choices(
    generos,
    weights=(60,40),
    k=num_registros
    )
#Generacion Aleatoria del nombre del docente
df['NombreD'] = [nombre_gen(i) for i in df['GeneroD']]
#Generacion Aleatoria del apellido del docente
df['ApellidoD'] = [faker.last_name() for i in df['GeneroD']]
#Generacion aleatoria de fechas de nacimiento de los docentes
df['FechaNacD'] = random_dob("1973-01-01","1997-12-31",num_registros)
#Generacion de las edades de los docentes
df['EdadD'] = [edadGen(i) for i in df['FechaNacD']]
#Generacion aleatoria de los titulos de los Docentes
titulos = ["Bachillerato","Licenciado","Tecnologo","Maestria","Doctorado"]
df['TituloD'] = random.choices(
    titulos,
    weights=(20,30,20,20,10),
    k=num_registros
    )
#Generacion Aleatoria del telefono del docente
df['TelefonoD'] = Telefono_docente_Gen()
#Generacion del archivo docente.csv donde se guardaran los datos
df.to_csv('Docente.csv')

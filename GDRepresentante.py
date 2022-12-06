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
Definicion de los atributos de la entidad Representante

ID(IdR)=El id del representante que sera unico para cada uno
Nombre(NombreR)=El nombre del representante generado aleatoriamente.
Apellido(ApellidoR)=El apellido del representante generado aleatoriamente.
Fecha de Nacimiento(FechaNacR)=La fecha de nacimiento del representante.
Edad(EdadR)=La edad del representante.
Genero(GeneroR)=El genero del representante que sera masculino o femenino.
Telefono(TelefonoR)=El telefono del representante.
"""
Caracteristicasrepresentante = [
    "IdR" ,
    "NombreR" ,
    "ApellidoR" ,
    "FechaNacR" ,
    "EdadR",
    "GeneroR" ,
    "TelefonoR"
    ]
def Id_representante_Gen():
    """
    Funcion para generar ids para el representante sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids de los representantes

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="R00"
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
def Telefono_representante_Gen():
    """
    Funcion para generar el telefono del representante sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con los telefonos de los representantes

    """
    contador=0
    Lista=[]
    while contador < num_registros:
        Numero="098" + str(random.randint(0,9)) + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
        if Numero in Lista:
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
df = pd.DataFrame(columns=Caracteristicasrepresentante)
#Generacion aleatoria del id del representante
df['IdR'] = Id_representante_Gen()

#Generacion aleatoria del genero del representante
generos = ["Masculino", "Femenino"]

df['GeneroR'] = random.choices(
    generos,
    weights=(60,40),
    k=num_registros
    )
#Generacion Aleatoria del nombre del representante
df['NombreR'] = [nombre_gen(i) for i in df['GeneroR']]
#Generacion Aleatoria del apellido del representante
df['ApellidoR'] = [faker.last_name() for i in df['GeneroR']]
#Generacion aleatoria de fechas de nacimiento de los representantes
df['FechaNacR'] = random_dob("1973-01-01","1997-12-31",num_registros)
#Generacion de las edades de los representantes
df['EdadR'] = [edadGen(i) for i in df['FechaNacR']]
#Generacion Aleatoria del telefono del representante
df['TelefonoR'] = Telefono_representante_Gen()
#Generacion del archivo Representante.csv donde se guardaran los datos
df.to_csv('Representante.csv')

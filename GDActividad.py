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
Definicion de los atributos de la entidad Actividad

ID(IdA)=El id de la actividad que sera unico para cada una
Tema(TemaA)=El tema de la actividad generado aleatoriamente.
Descripcion(DescripcionA)=Descripcion de la actividad generado aleatoriamente.
Estado(EstadoA)=El estado en el que se encuentra la actividad como activo o inactivo.

"""
caracteristicasActividad = [
    "IdA" ,
    "TemaA" ,
    "DescripcionA" ,
    "EstadoA"
    ]

def Id_Actividad_Gen():
    """
    Funcion para generar ids para la Actividad sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids de las Acividades

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="A00"
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
#Generacion del dataframe
df = pd.DataFrame(columns=caracteristicasActividad)
#Generacion de los ids de las actividad
df['IdA'] = Id_Actividad_Gen()
#Generacion aleatoria del tema de la actividad
df['TemaA'] = [faker.sentence() for i in df['IdA']]
#Generacion aleatoria de la descripcion de la actividad
df['DescripcionA'] = [faker.sentence() for i in df['IdA']]
#Generacion del estado de la actividad
Estado = ["Activo","Inactivo"]
df['EstadoA'] = random.choices(
    Estado,
    k=num_registros
    )
#Generacion del archivo Actividad.csv donde se guardaran los datos
df.to_csv('Actividad.csv')
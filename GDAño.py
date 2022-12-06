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
Definicion de los atributos de la entidad Año_Escolar

ID(IdAño)=El id del año escolar que sera unico para cada uno.
Nombre(NombreAño)=El nombre del periodo escolar.
Estado(EstadoAño)=El estado en el que se encuentra el año escolar.

"""
CaracteristicasAño = [
    "IdAño" ,
    "NombreAño" ,
    "EstadoAño"
    ]

def Id_Año_Gen():
    """
    Funcion para generar ids para el Año Escolar sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids del Año Escolar

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="Año00"
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
#Elaboración del dataframe
df = pd.DataFrame(columns=CaracteristicasAño)
#Generacion de los ids del año escolar
df['IdAño'] = Id_Año_Gen()
#Generacion aleatoria del nombre del año escolar
df['NombreAño'] = [faker.sentence() for i in df['IdAño']]

Estados = ["Activo", "Inactivo"]

df['EstadoAño'] = random.choices(
    Estados,
    k=num_registros
    )
#Generacion del archivo Año_Escolar.csv donde se guardaran los datos
df.to_csv('Año_Escolar.csv')
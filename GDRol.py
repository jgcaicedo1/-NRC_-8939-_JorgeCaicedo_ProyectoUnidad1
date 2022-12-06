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
Definicion de los atributos de la entidad Rol.

ID(IdRol)=El id del Rol que sera unico para cada uno.
Descripcion(DescripcionRol)=La descripcion del rol.
Estado(EstadoRol)=El estado en el que se encuentra el rol.

"""
CaracteristicasRol = [
    "IdRol" ,
    "DescripcionRol" ,
    "EstadoRol"
    ]

def Id_Rol_Gen():
    """
    Funcion para generar ids para el Rol sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids del Rol

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="Rol00"
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
df = pd.DataFrame(columns=CaracteristicasRol)
#Generacion de los ids del rol
df['IdRol'] = Id_Rol_Gen()
#Generacion aleatoria de la descripcion del rol
df['DescripcionRol'] = [faker.sentence() for i in df['IdRol']]
#Generacion aleatoria del estado del rol
Estados = ["Activo", "Inactivo"]

df['EstadoRol'] = random.choices(
    Estados,
    k=num_registros
    )
#Generacion del archivo Rol.csv donde se guardaran los datos
df.to_csv('Rol.csv')
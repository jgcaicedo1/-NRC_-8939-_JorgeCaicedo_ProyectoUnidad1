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
Definicion de los atributos de la entidad Aula.

ID(IdAu)=El id del aula que sera unico para cada uno.
Numero(NumAu)=El numero del aula.
Estado(EstadoAu)=El estado en el que se encuentra el aula.

"""
CaracteristicasAula = [
    "IdAu" ,
    "NumAu" ,
    "EstadoAu"
    ]

def Id_Aula_Gen():
    """
    Funcion para generar ids para el Aula sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids del Aula

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="Au00"
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

def Num_Aula_gen():
    """
    Funcion para devolver el numero del aula.

    Parametros
    ----------

        No Contiene Parametros


    Retorna
    -------

        Retornara el array con los num de las Aulas.

    """
    bloques = ["A","B","C","D","Coliseo","Patio","Salon Interactivo"]
    contador=1
    Lista=[]
    while contador <= num_registros:
        aula=random.choice(bloques)
        if aula == "Coliseo" or aula=="Patio" or aula=="Salon Interactivo":
            Lista.append(aula)
        else:
            aula=aula+"-"+str(random.randint(1,10000))
            Lista.append(aula)
        contador = contador + 1
    return Lista
#Elaboración del dataframe
df = pd.DataFrame(columns=CaracteristicasAula)
#Generacion de los ids del Aula
df['IdAu'] = Id_Aula_Gen()
#Generacion aleatoria del numero del Aula
df['NumAu'] = Num_Aula_gen()
#Generacion aleatoria del estado del Aula
Estados = ["Ocupado", "Disponible","Mantenimiento"]

df['EstadoAu'] = random.choices(
    Estados,
    k=num_registros
    )
#Generacion del archivo Aula.csv donde se guardaran los datos
df.to_csv('Aula.csv')
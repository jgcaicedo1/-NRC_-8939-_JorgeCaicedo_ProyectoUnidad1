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
Definicion de los atributos de la entidad Institucion

ID (Id_Institucion)=El id de la institucion que sera unico para cada una.
Nombre (Nombre_Institucion)=El Nombre de la Institucion generado aleatoriamente.
Tipo de Educacion (Tipo_Educacion_Institucion)=La Educacion que se da en la institucion ya sea Especial, Ordinaria, Artistica o Popular Permanente.
Sostenimiento (Sostenimiento_Institucion)=Como se sostiene la institucion ya sea Fiscal, Fiscomisional, Municipal o Particular.
Area de la Institucion (Area_Institucion)=El Area de la Institucion que puede ser Rural o Urbana.
Regimen Escolar (Regimen_Institucion)=El Regimen que maneja la Institucion que puede ser Sierra o Costa.
Modalidad (Modalidad_Institucion)= La modalidad con la que trabaja la Institucion ya sea Presencial,Presencial y SemiPresencial, Semipresencial o Virtual.
Jornada (Jornada_Institucion)= La Jornada que se trabaja ya sea Matutina o Vespertina.
"""

CaracteristicasInstitucion = [
    "IdI",
    "NombreI" ,
    "TipoEduI",
    "SostenimientoI" ,
    "AreaI",
    "RegimenI",
    "ModalidadI",
    "JornadaI" ,
    "EstadoI"
    ]
def Id_Institucion_Gen():
    """
    Funcion para generar ids para la Institucion sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el array con las ids de las Instituciones

    """
    contador=1
    Lista=[]
    while contador <= num_registros:
        Nombre="I00"
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
def Nombre_Institucion_Gen():
    """
    Funcion para generar nombres aleatorios para la Institucion sin repeticion.

    Parametros
    ----------

        No Contiene Parametros

    Retorna
    -------

        Retornara el nombre de la Institucion

    """
    contador=0
    Lista=[]
    while contador < num_registros:
        Numero=[""," I"," II"," III"," IV"," V"," VI"]
        Nombre="Unidad Educativa " + faker.first_name() + " " + faker.last_name() + random.choice(Numero)
        if Nombre in Lista:
            Nombre=""
        else:
            Lista.append(Nombre)
            contador = contador + 1 

    return Lista
#Generacion del dataframe
df_Institucion = pd.DataFrame(columns=CaracteristicasInstitucion)

#Generacion aleatoria de las ids de las aulas
df_Institucion['IdI'] = Id_Institucion_Gen()

#Generacion Aleatoria del nombre de la Institucion
df_Institucion['NombreI'] = Nombre_Institucion_Gen()
#Generacion aleatoria del tipo de educación de la Institucion
tipos = ["Especial","Ordinaria","Artistica","Popular Permanente"]
df_Institucion['TipoEduI'] = random.choices(
    tipos,
    k=num_registros
    )

#Generacion aleatoria del sostenimiento de la Institucion
sostenimiento = ["Fiscal","Fiscomisional","Municipal","Particular"]
df_Institucion['SostenimientoI'] = random.choices(
    sostenimiento,
    k=num_registros
    )

#Generacion aleatoria del area de la Institucion
area = ["Rural","Urbano"]
df_Institucion['AreaI'] = random.choices(
    area,
    k=num_registros
    )

#Generacion aleatoria del regimen de la Institucion
regimen = ["Sierra","Costa"]
df_Institucion['RegimenI'] = random.choices(
    regimen,
    k=num_registros
    )

#Generacion aleatoria de la modalidad de la Institucion
modalidad = ["Presencial","Presencial y SemiPresencial","Semipresencial","Virtual"]
df_Institucion['ModalidadI'] = random.choices(
    modalidad,
    k=num_registros
    )

#Generacion aleatoria de la jornada de la Institucion
jornada = ["Matutina","Vespertina"]
df_Institucion['JornadaI'] = random.choices(
    jornada,
    weights=(80,20),
    k=num_registros
    )

#Generacion aleatoria de la jornada de la Institucion
Estado = ["Activo","Inactivo"]
df_Institucion['EstadoI'] = random.choices(
    Estado,
    k=num_registros
    )


#Generacion del archivo Institucion.csv donde se guardaran los datos
df_Institucion.to_csv('Institucion.csv')
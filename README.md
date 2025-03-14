# Proyecto Urban Grocers 

## Nombre completo y cohort 
Espiridion Acosta Torres 
QA-24

## Descripción del proyecto

Este proyecto incorpora pruebas automatizadas utilizando el módulo Pytest para verificar la creación de una nueva cuenta 
y un kit.

El código incluye un total de nueve pruebas, tanto positivas como negativas. Los enlaces del servidor están almacenados 
en el archivo configuración.py , mientras que los datos de prueba se encuentran en data.py. Las funciones necesarias 
para el proceso están en sender_stand_request , y finalmente, las pruebas están ubicadas en creat_kit_name_kit_test.py

## Requisitos
Para poder ejecutar las pruebas necesarias se requiere instalar: Python, Pytest y el paquete request

## Documentación 
La documentación que se utilizo es la API de Urban.grocers, del apartado "Crear un Kit" y "Creación de cuenta".

## Instrucciones para ejecutar las pruebas 
1. Abrir este proyecto (qa-project-Urban-Grocers-app-es) en PyCharm.
2. En el botón Python Packages, asegurarse que los paquetes requests y pytest estén descargados y actualizados.
3. En caso de no estar disponibles, instalados/actualizados, descargar/actualizar ambos paquetes.
4. Seleccionar el archivo configuration.py. En el campo URL_SERVICE, cambiar la URL existente por la de un servidor nuevo.
5. Seleccionar el archivo create_kit_name_kit_test.py. En la barra superior de PyCharm, verifique que la lista desplegable al lado del botón de "Play" diga "Current file".
6. Hacer click en el botón de "Play" o ejecutando el comando "python -m pytest" en la terminal de Pycharm.


## Descripción de tecnologías y técnicas utilizadas
Se empleó Python como lenguaje de programación, mientras que para la ejecución de las pruebas se utilizó
Pytest, un marco de trabajo diseñado para realizar pruebas unitarias en software desarrollado con Python.

En cuanto a las técnicas utilizadas, se optó por organizar el código en distintos archivos para mejorar 
su estructura y claridad. 




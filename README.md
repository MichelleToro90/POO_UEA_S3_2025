# POO_UEA_S3_2025
# Proyecto POO Clima con GUI

## Descripción

Este proyecto es un sistema desarrollado en **Python** que permite registrar la información diaria del clima, calcular promedios semanales y mostrar los datos en una **interfaz gráfica (GUI)** usando **Tkinter**.  

El proyecto está diseñado siguiendo el paradigma de **Programación Orientada a Objetos (POO)**, aplicando conceptos de **encapsulamiento**, **herencia** y **polimorfismo** donde corresponde.

---

## Funcionalidades

- Registrar datos diarios de clima:
  - Temperatura (°C)
  - Humedad (%)
  - Precipitación (mm)
- Mostrar automáticamente una **tabla con los datos ingresados**.
- Calcular y mostrar los **promedios semanales**.
- Validación de datos: solo se aceptan valores numéricos (enteros o decimales).

---

## Estructura del proyecto
POO_Clima/
│

├─ clima.py # Clase ClimaDiario y ClimaSemanal

├─ interfaz_clima.py # Clase AplicacionClima (interfaz gráfica)

├─ main.py # Script principal para ejecutar la aplicación

├─ README.md # Este archivo

└─ .gitignore # Archivos a ignorar por Git (opcional)

---

## Cómo ejecutar

1. Clonar el repositorio:

```bash [xxxxx](https://github.com/MichelleToro90/POO_UEA_S3_2025.git)
Asegurarse de tener Python 3.x instalado.

Ejecutar la aplicación:

python main.py


Ingresar los valores de temperatura, humedad y precipitación, y presionar Agregar Día para registrar el dato.

Presionar Calcular Promedio para ver los promedios semanales.

Capturas de pantalla

(Opcional: agrega aquí capturas de la interfaz gráfica si quieres)

Requisitos

Python 3.x

Tkinter (generalmente incluido en Python)

Licencia

Este proyecto está bajo la licencia MIT.


# Herramienta para la detección rápida de neumonía

En este repositorio se presenta el desarrollo y creación de una herramienta basada en generación de texto, específicamente recetas de cocina, se establece el uso de los siguientes dos modelos de lenguaje, los cuales fueron seleccionados considerando su eficacia, su capacidad para generar texto en idioma español y los recursos computacionales disponibles:

1. GPT2-Small-Spanis: es un modelo de lenguaje basado en GPT-2 Small, optimizado para la generación de texto en español. Fue desarrollado por Datificate y afinado con datos de Wikipedia en español, utilizando técnicas avanzadas de aprendizaje profundo con las bibliotecas de Hugging Face y fastai v2. Su principal aplicación es la generación automática de recetas de cocina a partir de ingredientes proporcionados por el usuario. Requiere Python 3.8+, PyTorch o TensorFlow, y puede ejecutarse en GPU para mayor eficiencia. El modelo tiene licencia Apache 2.0, con restricciones sobre su uso y distribución.

2. TinyLlama - 1.1B: es un modelo de generación de texto basado en la arquitectura LLaMA 2, diseñado para ser compacto y eficiente en hardware limitado. Con 1.1B de parámetros, fue optimizado mediante técnicas como reducción de capas y atención de consultas agrupadas, logrando un tamaño de 600MB en disco. Su entrenamiento incluyó 3 trillones de tokens y se realizó con 16 GPUs, usando datasets como Slim Pijama y Starcoderdata. Su principal aplicación es la generación de recetas de cocina a partir de ingredientes proporcionados por el usuario. Cuenta con licencia Apache 2.0, con restricciones sobre su uso y distribución.

El repositorio incluye diversos scripts para cada una de las funciones de la herramienta, así como el módulo de integración. También se detallan los requisitos necesarios para su funcionamiento óptimo, las instrucciones de instalación, las pruebas unitarias realizadas para garantizar su correcto desempeño y la licencia correspondiente.

# Tabla de contenido
- [Introducción](#introducción)
    - [Generación automática de recetas con modelos de lenguaje](#neumonía)
- [Estructura del repositorio](#Estructura-del-repositorio)
- [Archivos del repositorio](#archivos-del-repositorio)
    - [app.py](#app-py)
    - [read_img.py](#read-img-py) 
    - [preprocess_img.py](#preprocess-img-py)
    - [load_model.py](#load-model-py)  
    - [grad_cam.py](#grad-cam-py)  
    - [integrator.py](#integrator-py)       
 - [Requerimientos para usar la herramienta de detección](#requerimientos-para-usar-la-herramienta-de-detección)
 - [Dockerización](#Dockerización)
 - [Integrantes del proyecto](#Integrantes-del-proyecto)

---

# Introducción

 ## Generación automática de recetas con modelos de lenguaje
La generación automática de recetas de cocina es un campo en crecimiento dentro de la inteligencia artificial, permitiendo a los usuarios obtener recetas personalizadas a partir de los ingredientes disponibles. Mediante el uso de modelos de lenguaje avanzados, se pueden crear platos diversos, optimizando el tiempo en la cocina y reduciendo el desperdicio de alimentos.

Los modelos GPT2-Small-Spanish y TinyLlama-1.1B han sido seleccionados por su capacidad de generar texto en español y su eficiencia en términos computacionales. GPT2-Small-Spanish es un modelo ligero y optimizado para el idioma español, mientras que TinyLlama-1.1B, basado en LLaMA 2, es un modelo compacto y eficiente diseñado para hardware con recursos limitados.

Estos modelos han sido entrenados con grandes volúmenes de datos y técnicas avanzadas de aprendizaje profundo para mejorar su coherencia y precisión en la generación de recetas. Gracias a su integración con la plataforma Hugging Face y el uso de frameworks como PyTorch, su implementación en entornos de producción y de investigación resulta accesible y versátil.

El desarrollo de esta herramienta no solo facilita la exploración culinaria, sino que también abre nuevas posibilidades para la personalización de recetas, la innovación gastronómica y la investigación en generación de texto aplicada a la cocina.

# Estructura del repositorio

A nivel general, la estructura del proyecto es la siguiente:

1. Directorios principales:

- Images/ Contiene las imágenes utilizadas en el proyecto.
- Src (Source)/ Contiene el código fuente del proyecto, organizado en los siguientes subdirectorios:
  - Models/ almacena el modelo entrenado y el script necesario para su gestión y uso.
  - Visualizations/ Contiene scripts para la generación de la interfaz de usuario. 
- Test/ Almacena las pruebas unitarias del proyecto.

2. Archivos en la raíz del proyecto:
- gitignore: Define los archivos y carpetas que deben ser ignorados en el control de versiones con Git.
- Dockerfile: Especifica las instrucciones para construir el contenedor Docker del proyecto.
- main.py: Archivo principal que sirve como punto de entrada al programa.
- README.md: Documento con información detallada sobre el uso y configuración del proyecto.
- requirements.txt: Lista de dependencias de Python necesarias para la ejecución del proyecto.
- LICENSE.txt: Contiene la licencia del proyecto, especificando los términos de uso y distribución del código.
   
# Archivos del repositorio

## app.py

Este script define la interfaz de usuario utilizando Streamlit. Permite al usuario ingresar ingredientes y generar recetas basadas en modelos de lenguaje preentrenados. 

A través de la interfaz, se pueden seleccionar diferentes modelos de generación de texto y enviar solicitudes para obtener recetas personalizadas. Se implementan validaciones y manejo de errores para mejorar la experiencia del usuario.

## config.py

Este script almacena la configuración global del proyecto, incluyendo las opciones de modelos de lenguaje y sus respectivas rutas. Además, define parámetros clave para la generación de recetas, como la temperatura, la penalización por repetición y la estrategia de muestreo. 

Centralizar la configuración en este archivo facilita la modificación y mantenimiento del sistema sin afectar otros módulos.

## model.py

Este script maneja la carga del modelo de lenguaje utilizado para generar recetas. Se encarga de inicializar el modelo y su tokenizador, así como de transferirlos al dispositivo adecuado para su ejecución.

Al separar esta funcionalidad, se garantiza un mejor desacoplamiento del sistema, permitiendo reutilizar el modelo en diferentes partes de la aplicación.

## ui.py

Este script define la lógica de la interfaz de usuario en Streamlit. Proporciona los elementos gráficos para la interacción, como cuadros de entrada, botones y mensajes de respuesta. 

Además, gestiona la comunicación con el modelo de generación de recetas y maneja posibles errores o advertencias para mejorar la experiencia del usuario.


# Requerimientos para usar la herramienta de detección

Para ejecutar correctamente la herramienta de detección de neumonía, siga los siguientes pasos:

1. Se debe clonar la información del repositorio uao-neumonia  el cual se encuentra en el siguiente enlace  https://github.com/halejosm/uao-neumonia.git 
2. Asegúrate de tener Python instalado en tu ordenador. Se recomienda usar la versión Python 3.10.
3. crear y configurar un entorno virtual: Puede craer su entorno virtual desde la consola del sistema o puede usar VS Code. Nota: Un entorno virtual es un espacio aislado dentro de tu sistema donde puedes instalar bibliotecas y dependencias necesarias para un proyecto, sin afectar el resto del sistema ni otras aplicaciones.
- Si desea usar VS Code estas son las instrucciones a seguir:
- Inicia Visual Studio Code desde el directorio donde has clonado el repositorio del proyecto.
- Puedes abrir la barra de comandos presionando ctrl + Shift + P.
- Escribe y busca la opción "Python: Crear un entorno virtual" para crear el entorno virtual.
- Selecciona la opción "Crear entorno virtual (.venv)
- Asegúrate de elegir la versión Python 3.10
- No olvides seleccionar el archivo requirements.txt. Este archivo contiene todas las bibliotecas y dependencias necesarias para el funcionamiento correcto del proyecto.

# Uso de la interfaz gráfica

Al ejecutar el script detector_neumonia.py, se abrirá una ventana con la interfaz gráfica, la cual debe verse de la siguiente manera:

![interfaz 1](Images/Interfaz_1.PNG)

Siga los siguientes pasos

1. Escriba la cédula del paciente en la casilla correspondiente.
2. Haga clic en el botón "Cargar Imagen" y seleccione la radiografía de tórax desde su ordenador. La imagen puede estar en formato .dcm (DICOM) u otros formatos comunes como JPEG, PNG, etc.Una vez cargada la imagen, debería verla en la parte izquierda de la interfaz tal como se ve a continuación

![interfaz 2](Images/carga.PNG)

3. Haga clic en el botón "Predecir" para ejecutar el modelo y obtener el resultado.Tras la predicción, verá lo siguiente:

![interfaz 3](Images/resultado.PNG)

- Imagen de la radiografía en la parte izquierda de la pantalla.
- Imagen con el mapa de calor en la parte derecha, destacando las áreas más influyentes en la predicción.
- El resultado predicho por el modelo (bacteriana, viral, o neumonía).
- El valor de probabilidad en porcentaje con el que el modelo determinó la clasificación.

4. Si lo desea, puede guardar los datos obtenidos haciendo clic en el botón "Guardar". Esto generará un archivo llamado "historial.csv" con los resultados.
5. Puede guardar una copia del reporte visual generado por el entorno haciendo clic en el botón "PDF". Esto creará un archivo en formato PDF y JPG con la captura de la interfaz y los resultados de la predicción.
6. Si necesita realizar una corrección o una nueva predicción, puede borrar todos los datos ingresados haciendo clic en el botón "Borrar".

# Dockerización

La Dockerización es el proceso de empaquetar una aplicación junto con todas sus dependencias, configuraciones y bibliotecas necesarias en un contenedor Docker. Esto permite que la aplicación se ejecute de manera consistente y reproducible en cualquier entorno, sin importar el sistema operativo o la configuración de la máquina en la que se ejecute.

1. Creación del Docker File
   
Docker File es un archivo de texto que contiene una serie de instrucciones para construir una imagen de Docker, este se un archivo de texto que contiene una serie de instrucciones para construir una imagen de Docker, este archivo debe estar dentro de la raíz del proyecto y se configura de la siguiente manera:

- Se usa una imagen base (se especifica la versión de Python) - (FROM python:3.11.2)
- Se instalan dependencias necesarias: (OpenCV y Xvfb
RUN apt-get update -y && \
    apt-get install -y \
    python3-tk \
    x11-utils)
- Se establece el directorio de trabajo dentro del contenedor
 (WORKDIR /home/src)
- Se copian los archivos del proyecto contenedor
( COPY . /home/src/) 
- Se instalan los requirements o dependencias necesarias
( RUN pip install -r requirements.txt)
- Configura el DISPLAY para apuntar al host de Windows
(ENV DISPLAY=host.docker.internal:0.0)
- Se establece el comando para ejecutar la aplicación
( CMD ["python", "main.py"] )

2. Crear la imagen

La imagen es un archivo liviano, autónomo y ejecutable que incluye todo lo necesario para ejecutar una aplicación o servicio. Este archivo contiene el código de la aplicación, las bibliotecas necesarias, dependencias, herramientas, configuraciones y el sistema operativo base.

Para crear la imagen, sigue estos pasos

- Abre la terminal de tu sistema operativo o en VS CODE
- Navega al directorio del proyecto donde se encuentra el Dockerfile. Puedes usar el comando cd para cambiar de directorio.
- crea la imagen usando el siguiente comando Docker build –t nombre de la imagen.

4. Iniciar la imagen y crear el contenedor Docker

Para ejecutar la imagen y crear el contenedor Docker se usa el siguiente comando

docker run -it --rm "nombre de la iamgen"

Las imagenes para probar esta en home/src/data/raw como se ve en la siguiente imagen

![imagen_2](Images/load.PNG)

Bibliografía
https://docs.docker.com/get-started/docker-overview/
https://www.docker.com
https://docs.oracle.com/cd/E37929_01/html/E36693/gmcdr.html

# Integrantes del proyecto

- Francisco Javier Rivera Rozo
- Carlos Armando Daza Rendón
- Andrés Felipe Coral
- Alejandro Sànchez Murillo

   









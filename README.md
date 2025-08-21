# Conversor de Sistemas Numéricos

## Descripción
Esta aplicación permite convertir números entre diferentes sistemas numéricos: Decimal, Binario, Octal y Hexadecimal.  
La interfaz gráfica está desarrollada en **Python** utilizando **Tkinter**, ofreciendo una experiencia sencilla e intuitiva para el usuario.

---

## Objetivos principales
- Permitir ingresar un número en cualquier sistema soportado (Decimal, Binario, Octal, Hexadecimal).  
- Validar la entrada del usuario y mostrar errores en caso de números inválidos.  
- Mostrar la conversión a los otros sistemas numéricos.  
- Proporcionar botones para convertir y limpiar los campos de manera sencilla.

---

## Tecnologías utilizadas
- Python 3.13.5  
- Tkinter (interfaz gráfica)  
- PyInstaller (para generar ejecutables `.exe` de la aplicación)  
- Re (expresiones regulares para validación de entrada)
- Visual Studio Code (entorno de desarrollo y edición del código)

---

## Instrucciones de instalación y uso

1. Requisitos previos
     **Sistema operativo** 
     Windows 10 o superior. 

     **Python** 
     versión 3.x (solo si se ejecuta el script `.py`).  
     No se requieren librerías adicionales ya que Tkinter viene incluido con Python.  

2. Acceder al repositorio en GitHub:  
   `https://github.com/tu_usuario/nombre_repositorio`  

3. Revisar los archivos directamente en línea o descargar el proyecto completo como archivo ZIP usando **Code → Download ZIP**.  
     **Archivos principales**
     -appConversor.py → Código fuente de la aplicación 
     -dist/ → Ejecutable generado por PyInstaller (appConversor.exe).
     -README.md → Documentación del proyecto.

4. Ejecutar la aplicación:  

   - **Opción 1:** Ejecutar desde Python
     ```bash
     python appConversor.py
     ```
     Requiere tener Python 3.x instalado.

   - **Opción 2:** Ejecutar el ejecutable `.exe` directamente
     1. Navegar a la carpeta `dist/`.
     2. Hacer doble clic en `appConversor.exe`. No requiere Python ni dependencias adicionales.

5. Descripción rápida de la interfaz
   La aplicación “Conversor de Sistemas Numéricos” tiene una interfaz clara e intuitiva:

     **Título principal** 
     Muestra el nombre de la app con estilo destacado.

     **Sección de entrada**
     - Botones de radio para elegir el sistema numérico (Decimal, Binario, Octal, Hexadecimal).
     - Campo de texto para ingresar el número a convertir.
     - Etiqueta de ayuda debajo, que muestra instrucciones o errores según el sistema seleccionado.

     **Resultados de conversión**
     - Campos de solo lectura para cada sistema diferente al de entrada.
     - Cada sistema tiene un color distinto para diferenciar: Decimal (azul oscuro), Binario (rojo), Octal (morado), Hexadecimal (azul celeste).

     **Botones de acción**
     - “Convertir” → realiza la conversión.
     - “Limpiar” → borra entrada y resultados.

     **Mensajes dinámicos**
     - Actualiza instrucciones automáticamente al cambiar el sistema.
     - Muestra errores de validación en rojo sobre la etiqueta de ayuda.

     **Interactividad**
     - Presionar Enter realiza la conversión sin usar el botón.
     - Todos los campos de resultado se actualizan automáticamente.
 
## Capturas de pantalla

![AppConversor](Capturas/Captura%20de%20pantalla%20%20(10).png)
![Prueba de que los resultados no se muestren hasta oprimir el boton de convertir](Capturas/Captura%20de%20pantalla%20%20(8).png)
![Prueba de número decimal](Capturas/Captura%20de%20pantalla%20%20(9).png)    
![Prueba de número binario](Capturas/Captura%20de%20pantalla%20%20(2).png)    
![Prueba de número octal](Capturas/Captura%20de%20pantalla%20%20(3).png)    
![Prueba de número hexadecimal](Capturas/Captura%20de%20pantalla%20%20(4).png) 
![Prueba en caso de error de número decimal](Capturas/Captura%20de%20pantalla%20%20(1).png)    
![Prueba en caso de error de número binario](Capturas/Captura%20de%20pantalla%20%20(7).png)    
![Prueba en caso de error de número octal](Capturas/Captura%20de%20pantalla%20%20(6).png)    
![Prueba en caso de error de número hexadecimal](Capturas/Captura%20de%20pantalla%20%20(5).png)    

Notas

- Esta aplicación fue desarrollada y probada utilizando Visual Studio Code como entorno de desarrollo.

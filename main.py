import datetime
from pathlib import Path

my_list = []

# Define el nombre de la carpeta que quieres crear
nombre_carpeta = Path("listas")

# Crea la carpeta
nombre_carpeta.mkdir(parents=True, exist_ok=True)

contador = 0

while True:
    
    if contador % 5 == 0:
        print("Para salir del bucle escribe x.")
    
    val1 = str(input("Ingresa las palabras que necesitas obtener su significado: "))

    # Usar f-string para formatear val2 correctamente
    val2 = f"Que tipo de palabra es '{val1}' y que significado tiene, dame 1 ejemplo, en ingles y español."

    my_list.append(val2)
    
    contador += 1

    # Salir del bucle si el usuario ingresa 'x'
    if val1.lower() == 'x':
        break

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()

# Formatear la fecha y hora
formato = ahora.strftime("%H-%M-%S - %d-%m-%Y")

# Crear la ruta del archivo con la fecha y hora
nombre_archivo = Path(f"listas/mi_archivo - {formato}.txt")

# Abrir el archivo en modo de escritura ('w')
with open(nombre_archivo, "w") as archivo:
    for item in my_list:
        archivo.write(item + "\n")

print("Contenido de la lista añadido al archivo.")

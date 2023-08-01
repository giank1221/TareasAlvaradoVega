

def obtener_nombre():
    nombre = input("¡Hola! Por favor, ingresa tu nombre: ")
    return nombre

def imprimir_mensaje_personalizado(nombre):
    mensaje = f"Hola, {nombre}! ¡Bienvenido al infierno!"
    print(mensaje)

if __name__ == "__main__":
    nombre_usuario = obtener_nombre()
    imprimir_mensaje_personalizado(nombre_usuario)
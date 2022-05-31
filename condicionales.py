
#aqui asignamos el valor donde el usuario va introducir la cantidad"
#cali = int(input("Introduce la calificación A-Z900: "))

#Este es un if donde si es menor a 699 o igual y el usuario introduce un numero menor a eso o igual se le va mostrar el contenido del print
#if cali <= 699:
    #print("No pasaste") #Si es menor a 700 muestra esto

#Este es un elif donde si es mayor a 1001 o igual y el usuario introduce un numero menor a eso o igual se le va mostrar el contenido del print
#elif cali >= 1001:
    #print("Introduce un valor correcto") 


#Si no cumplen ninguna de las condicionales se le va mostrar el contenido del print
#else: #Si no se cumpla la condicional if ejecuta esto
    #print("Pasaste kvronnnn")
    


# Asignamos una variable con el nombre edad donde le asignamos que el usuario introduzca su edad
edad = int(input("Introduzca su edad: "))


# Este es un if donde hace una escala del 18 al 100 donde si esta dentro de ese rango o es igual a 18 y 100 se le imprime el contenido del print
if edad >= 18 and edad <= 100 :
    print("Pasale al antro joven: ")


# Este es un elif donde si la variable edad introducida supera la cantidad de 100 se le mostrara el contenido del print
elif edad > 100:
    print("Si vienes acompañado de alguien mayor jajaja ")

# Este es un elif donde si la variable edad introducida es menor a 0 se le mostrara el contenido del print
elif edad < 0:
    print("Mientes weeee ")
# Este else significa donde si todas las condiciones no se cumplen imprima el contenido del print
else:
    print("No puedes entrar kvron ")


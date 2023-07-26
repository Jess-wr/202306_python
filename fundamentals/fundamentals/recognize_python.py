num1 = 42           #declaración de variable, inicializar número
num2 = 2.3          #declaración de variable, inicializar número decimal
boolean = True          #declaración de variable, inicializar booleano
string = 'Hello World'          #declaración de variable, inicializar cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']          #declaración de variable, inicializar lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}          #declaración de variable, inicializar diccionario     
fruit = ('blueberry', 'strawberry', 'banana')           #declaración de variable, inicializar tuple
print(type(fruit))          #imprimir en consola, tipo de variable
print(pizza_toppings[1])            #imprimir en consola el segundo item de la lista
pizza_toppings.append('Mushrooms')          #agregar un elemento a la lista
print(person['name'])               #imprimir en consola el valor del elemento name del diccionario
person['name'] = 'George'           #cambiar el valor del elemento name del diccionario
person['eye_color'] = 'blue'            #camnbiar el valor del elemento eye_color del diccionario
print(fruit[2])         #imprimir el tercer elemento de tuple

if num1 > 45:                   #condicional if
    print("It's greater")       #imprimir en consola 
else:                           #condicional else
    print("It's lower")         #imprimir en consola

if len(string) < 5:             #condicional if
    print("It's a short word!") #imprimir en consola
elif len(string) > 15:          #condicional elif
    print("It's a long word!")  #imprimir en consola
else:                           #condicional else
    print("Just right!")        #imprimir en consola

for x in range(5):              #for loop de 0 a 4
    print(x)                    #imprimir en consola
for x in range(2,5):            #for loop de 2 a 4
    print(x)                    #imprimir en consola
for x in range(2,10,3):         #for loop de 2 a 9, cada 3 numeros
    print(x)                    #imprimir en consola
x = 0                           #declaración de variable, inicializar número
while(x < 5):                   #while loop
    print(x)                    #imprimir en consola
    x += 1                      #incrementar                 

pizza_toppings.pop()            #eliminar el último valor de la lista
pizza_toppings.pop(1)           #eliminar el valor de la lista por su indice

print(person)                   #imprimir en consola
person.pop('eye_color')         #eliminar la clave del diccionario
print(person)                   #imprimir en consola

for topping in pizza_toppings:          #for loop de una lista
    if topping == 'Pepperoni':          #condicional if
        continue                        #continuar
    print('After 1st if statement')     #imprimir en consola
    if topping == 'Olives':             #condicional if
        break                           #detener loop

def print_hello_ten_times():            #declarción de función
    for num in range(10):               #for loop de 0 a 9
        print('Hello')                  #imprimir en consola

print_hello_ten_times()                 #llamar función

def print_hello_x_times(x):             #declarción de función con parámetro 
    for num in range(x):                #for loop según parámetro
        print('Hello')                  #imprimir en consola

print_hello_x_times(4)                  #llamar función

def print_hello_x_or_ten_times(x = 10): #declaración de función, parámetro inicializado
    for num in range(x):                #for loop según parámetro
        print('Hello')                  #imprimir en consola

print_hello_x_or_ten_times()            #llamar función
print_hello_x_or_ten_times(4)           #llamar función con parámetro


"""             
Bonus section                               #comment multiline
"""

# print(num3)                               #comment single line
# num3 = 72                                 #comment single line
# fruit[0] = 'cranberry'                    #comment single line
# print(person['favorite_team'])            #comment single line
# print(pizza_toppings[7])                  #comment single line
#   print(boolean)                          #comment single line
# fruit.append('raspberry')                 #comment single line
# fruit.pop(1)
class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
    def hacer_retiro(self, amount):     #haz que este método reduzca el balance del usuario en la cantidad especificada 
        self.balance_cuenta -= amount
    def mostrar_balance_usuario(self):  #haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
        print("Usuario:", self.name, ", Balance:", self.balance_cuenta)
    def transfer_dinero(self, Usuario, amount):
        self.balance_cuenta -= amount
        Usuario.balance_cuenta += amount
        self.mostrar_balance_usuario()
        Usuario.mostrar_balance_usuario()



guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
rosa = Usuario("Rosa Bertha", "rosa@email.com")
print(guido.name)
print(monty.name)
print(rosa.name)

guido.hacer_depósito(100)
guido.hacer_depósito(200)
guido.hacer_depósito(200)
guido.hacer_retiro(200)
guido.mostrar_balance_usuario()	# salida: 300
monty.hacer_depósito(100)
monty.hacer_depósito(50)
monty.hacer_retiro(50)
monty.hacer_retiro(50)
monty.mostrar_balance_usuario()	# salida: 50
rosa.hacer_depósito(1000)
rosa.hacer_retiro(300)
rosa.hacer_retiro(300)
rosa.hacer_retiro(300)
rosa.mostrar_balance_usuario()	# salida: 100
guido.transfer_dinero(rosa, 100)
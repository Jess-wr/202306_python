class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self
    def hacer_retiro(self, amount):     #haz que este método reduzca el balance del usuario en la cantidad especificada 
        self.balance_cuenta -= amount
        return self
    def mostrar_balance_usuario(self):  #haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
        print("Usuario:", self.name, ", Balance:", self.balance_cuenta)
        return self
    def transfer_dinero(self, Usuario, amount):
        self.balance_cuenta -= amount
        Usuario.balance_cuenta += amount
        self.mostrar_balance_usuario()
        Usuario.mostrar_balance_usuario()



guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
rosa = Usuario("Rosa Bertha", "rosa@email.com")

guido.hacer_depósito(100).hacer_depósito(200).hacer_depósito(200).hacer_retiro(200).mostrar_balance_usuario()	# salida: 300
monty.hacer_depósito(100).hacer_depósito(50).hacer_retiro(50).hacer_retiro(50).mostrar_balance_usuario()	# salida: 50
rosa.hacer_depósito(1000).hacer_retiro(300).hacer_retiro(300).hacer_retiro(300).mostrar_balance_usuario()	# salida: 100
guido.transfer_dinero(rosa, 100)
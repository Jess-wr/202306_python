class CuentaBancaria:
    # atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, tasa_int=0.03, balance=0):
        self.tasa_int = tasa_int
        self.balance = balance
        self.interes_generado = self.balance * tasa_int
        CuentaBancaria.todas_las_cuentas.append(self)
    def depósito(self, amount):
        self.balance += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self
    def retiro(self, amount):
        self.balance -= amount
        return self
    def mostrar_info_cuenta(self):
        print("Balance:", self.balance)
        return self
    def generar_interés(self):
        self.balance += self.interes_generado
        return self
    



class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.cuenta = CuentaBancaria(tasa_int=0.02, balance=0)
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self
    def hacer_retiro(self, amount):     #haz que este método reduzca el balance del usuario en la cantidad especificada 
        self.cuenta -= amount
        return self
    def mostrar_balance_usuario(self):  #haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
        print("Usuario:", self.name, ", Balance:", self.cuenta)
        return self
    def transfer_dinero(self, Usuario, amount):
        self.cuenta -= amount
        Usuario.cuenta += amount
        self.mostrar_balance_usuario()
        Usuario.mostrar_balance_usuario()
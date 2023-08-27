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




cuenta1 = CuentaBancaria(balance=200)
print(cuenta1.tasa_int)
print(cuenta1.balance)
cuenta2 = CuentaBancaria(0.04, 300)
print(cuenta2.tasa_int)
print(cuenta2.balance)
cuenta1.depósito(50).depósito(20).depósito(30).retiro(50).generar_interés().mostrar_info_cuenta()
cuenta2.depósito(200).depósito(100).retiro(50).retiro(50).retiro(50).retiro(50).generar_interés().mostrar_info_cuenta()

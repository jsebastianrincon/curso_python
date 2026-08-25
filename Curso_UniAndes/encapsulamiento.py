class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial #protegido
        self.__pin = "0000" #privado

    def retirar(self, cantidad, pin):
        if cantidad > 0 and pin == self.__pin and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

    def consignar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def cambiar_pin(self, pin_actual,pin_nuevo):
        if pin_actual == self.__pin:
            self.__pin = pin_nuevo
            return True
        return False

cuenta = CuentaBancaria("Sebastian",100000)
print(cuenta.titular)
print(cuenta._saldo)
print(cuenta._CuentaBancaria__pin)
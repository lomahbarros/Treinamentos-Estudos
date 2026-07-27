class ContaBancaria:
    def __init__(self, titular , saldo_inicial =0):
        self.titular = titular
        self.saldo_inicial = saldo_inicial #Encapsulamento privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= self.__saldo:
            return True
        return False

    def consultar_saldo(self):
        return self.__saldo

class ContaCorrente(ContaBancaria): #Heranca
    def __init__(self, titular, saldo_inicial=0, liminte = 1000):
        super().__init__(titular, saldo_inicial)    
        self.limite = limite

    def sacar(self, valor): #Polimorfismo
        if valor <= self.consultar_saldo() + self.limite:
            return super().sacar(valor)
        return False

conta = ContaCorrente("Alice", 500, limite=200)
conta.sacar(600) # Pode sacar até 700 (saldo + limite)
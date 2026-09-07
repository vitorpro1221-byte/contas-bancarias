class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
         self.saldo = valor + self.saldo

    def sacar(self, valor):
       if self.saldo >= valor:
        self.saldo = self.saldo - valor
       else:
           print("SALDO INSUFICIENTE")

    def mostrar(self):
        print(self.saldo)
        print(self.titular)

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_juros):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def render_juros(self):
        self.saldo += (self.saldo * self.taxa_juros)

    def mostrar(self):
         super().mostrar()
         print(self.taxa_juros)

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            
        else:
            print("LIMITE EXCEDIDO")
    
class ContaInvestimento(ContaBancaria):
    def __init__(self, titular, saldo, taxa_imposto):
        super().__init__(titular, saldo)
        self.taxa_imposto = taxa_imposto

    def sacar(self, valor):
        if self.saldo >= valor + (valor * self.taxa_imposto):
            self.saldo -= valor + (valor * self.taxa_imposto)
        else:
            print("SALDO INSUFICIENTE")

    def mostrar(self):
         super().mostrar()
         print(self.taxa_imposto)



conta1 = ContaBancaria("Luis", 100)
conta2 = ContaInvestimento("Marcio", 50, 0.02)
conta3 = ContaPoupanca("Roberto", 500, 1000)
contas_cadastradas = [conta1, conta2, conta3]

for contas in contas_cadastradas:
    contas.mostrar()
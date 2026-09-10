class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_valor):
        if novo_valor >= 0:
            self._saldo = novo_valor
        else:
            print(f"Erro Saldo Indisponivel:{self._saldo}")

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

conta = ContaBancaria("Ana", 1000)
print(conta.saldo)
conta.saldo = 2000
print(conta.saldo)
conta.saldo = -50
print(conta.saldo)
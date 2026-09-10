class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._historico = []

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_valor):
        if novo_valor >= 0:
            self._saldo = novo_valor
        else:
            print(f"Erro Saldo Indisponivel:{self._saldo}")

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        if titular.strip():
            self._titular = titular
        else:
            print("Obrigatorio o Nome de um Titular.")

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
         self.saldo = valor + self.saldo
         self._historico.append(f"Deposito:{valor}")

    def sacar(self, valor):
       if self.saldo >= valor:
        self.saldo = self.saldo - valor
        self._historico.append(f"Saque:{valor}")
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
        super().__init__(titular, saldo, )
        self.limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= -self.limite:
            self._saldo = valor
        else:
            print("LIMITE EXCEDIDO")

    def sacar(self, valor):
        novo_saldo = self._saldo - valor
        self.saldo = novo_saldo
        if self._saldo == novo_saldo:
            if novo_saldo < 0:
                self._historico.append(f"Saque de Cheque-Especial R${valor}")
            else:
                self._historico.append(F"Saque R${novo_saldo}")
        
    
class ContaInvestimento(ContaBancaria):
    def __init__(self, titular, saldo, taxa_imposto):
        super().__init__(titular, saldo,)
        self.taxa_imposto = taxa_imposto
        

    def sacar(self, valor):
        if self.saldo >= valor + (valor * self.taxa_imposto):
            self.saldo -= valor + (valor * self.taxa_imposto)
        else:
            print("SALDO INSUFICIENTE")

    def mostrar(self):
         super().mostrar()
         print(self.taxa_imposto)





conta = ContaCorrente("Ana", 1000, limite=200)
conta.sacar(1200)
print(conta.historico)

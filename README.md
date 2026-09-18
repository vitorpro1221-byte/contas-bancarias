# 🏦 Contas Bancárias — POO em Python

> Projeto de estudo de Programação Orientada a Objetos (POO) em Python, explorando **herança**, **polimorfismo** e **encapsulamento** através de um sistema de contas bancárias.

---

## 📌 Sobre

Este projeto simula diferentes tipos de conta bancária, todos herdando de uma classe base `ContaBancaria`. Cada subclasse tem regras de negócio próprias para saque, e o encapsulamento é feito com `@property`/`@setter`, validando dados antes de alterá-los.

## 🧩 Estrutura de classes

### `ContaBancaria` (classe base)

Atributos encapsulados via `@property`:

| Propriedade | Validação no setter |
|---|---|
| `saldo` | Só aceita valores `>= 0` (mensagem de erro caso contrário) |
| `titular` | Não aceita nome vazio/em branco |
| `historico` | Somente leitura (`@property` sem setter) — lista de transações |

Métodos:
- **`depositar(valor)`** → soma ao saldo e registra no histórico.
- **`sacar(valor)`** → verifica se há saldo suficiente; se sim, debita e registra; senão, imprime `"SALDO INSUFICIENTE"`.
- **`mostrar()`** → imprime saldo e titular.

### `ContaPoupanca`

- Adiciona `taxa_juros`.
- **`render_juros()`** → aplica o rendimento: `saldo += saldo * taxa_juros`.
- **`mostrar()`** → sobrescreve o método base (via `super()`) e também imprime a taxa de juros.

### `ContaCorrente`

- Adiciona `limite` (valor do cheque especial).
- **Sobrescreve a `property saldo`**: em vez de bloquear saldo negativo, permite até `-limite`.
- **Sobrescreve `sacar(valor)`**: calcula o novo saldo e tenta aplicá-lo via `self.saldo = novo_saldo`. Se a operação for aceita, registra no histórico com uma mensagem diferente dependendo do resultado:
  - Saldo ficou negativo → `"Saque de Cheque-Especial R$‌..."`
  - Saldo ficou positivo/zero → `"Saque R$‌..."`

### `ContaInvestimento`

- Adiciona `taxa_imposto`.
- **Sobrescreve `sacar(valor)`**: cobra imposto proporcional sobre o valor sacado — só permite o saque se `saldo >= valor + (valor * taxa_imposto)`.
- **`mostrar()`** → sobrescreve o método base e também imprime a taxa de imposto.

## ▶️ Exemplo de uso (código atual do arquivo)

```python
conta = ContaCorrente("Ana", 1000, limite=200)
conta.sacar(1200)
print(conta.historico)

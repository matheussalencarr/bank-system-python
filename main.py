def depositar(saldo, valor):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo
    return saldo + valor, f"Depósito: R$ {valor:.2f}\n"

def sacar(saldo, valor, numero_saques, LIMITE_SAQUES, limite):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, "", numero_saques

    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, "", numero_saques

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, "", numero_saques

    if valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, "", numero_saques

    return saldo - valor, f"Saque: R$ {valor:.2f}\n", numero_saques + 1

def exibir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, operacao = depositar(saldo, valor)
            extrato += operacao

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, operacao, numero_saques = sacar(saldo, valor, numero_saques, LIMITE_SAQUES, limite)
            extrato += operacao

        elif opcao == "e":
            exibir_extrato(extrato, saldo)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()

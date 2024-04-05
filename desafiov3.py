import textwrap

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

def menu():
    opcoes = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(opcoes)).strip()

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta.saldo += valor
        conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
def sacar(conta, limite=500, limite_saques=3):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta.saldo
    excedeu_limite = valor > limite
    excedeu_saques = conta.numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        conta.saldo -= valor
        conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        conta.numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    if cpf in usuarios:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return None
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario = Usuario(nome, cpf, data_nascimento, endereco)
    usuarios[cpf] = usuario
    print("=== Usuário criado com sucesso! ===")
    return usuario

def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = usuarios.get(cpf)
    if usuario:
        numero_conta = len(contas) + 1
        conta = Conta(agencia, numero_conta, usuario)
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
        return conta
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.usuario.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    agencia = "0001"
    usuarios = {}
    contas = []
    
    while True:
        opcao = menu()
        if opcao == "d" and contas:
            depositar(contas[0])  # Exemplo com a primeira conta
        elif opcao == "s" and contas:
            sacar(contas[0])  # Exemplo com a primeira conta
        elif opcao == "e" and contas:
            exibir_extrato(contas[0])  # Exemplo com a primeira conta
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(agencia, contas, usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()

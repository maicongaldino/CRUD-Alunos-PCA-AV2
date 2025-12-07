from src.repositories.aluno_repository import carregar_alunos, salvar_dados
from src.services.aluno_service import inserir
from enum import Enum

class OpcaoMenu(Enum):
    INSERIR = "1"
    PESQUISAR = "2"
    SAIR = "3"

def solicitar_entrada(mensagem):
    return input(mensagem)

def exibir_menu_principal():
    print("\n=== TRABALHO PRÁTICO AV2 - MENU ===")
    print("1 - INSERIR")
    print("2 - PESQUISAR")
    print("3 - SAIR")
    entrada = solicitar_entrada("Escolha uma opção: ").strip()
    mapa = {
        "1": OpcaoMenu.INSERIR,
        "2": OpcaoMenu.PESQUISAR,
        "3": OpcaoMenu.SAIR,
    }
    return mapa.get(entrada)

def processar_insercao(alunos):
    print("\n== Inserir Aluno ==")
    dados = {
        "Nome": solicitar_entrada("Nome: ").strip(),
        "Rua": solicitar_entrada("Rua: ").strip(),
        "Número": solicitar_entrada("Número: ").strip(),
        "Bairro": solicitar_entrada("Bairro: ").strip(),
        "Cidade": solicitar_entrada("Cidade: ").strip(),
        "UF": solicitar_entrada("UF (2 letras): ").strip(),
        "Telefone": solicitar_entrada("Telefone: ").strip(),
        "Email": solicitar_entrada("Email: ").strip(),
    }
    try:
        alunos, novo = inserir(alunos, dados)
        salvar_dados(alunos)
        print(f"Aluno cadastrado com matrícula {novo.matricula}.")
    except ValueError as e:
        print(f"Erro: {e}")
    return alunos

def main():
    alunos = carregar_alunos()
    
    while True:
        opcao = exibir_menu_principal()
        
        match opcao:
            case OpcaoMenu.INSERIR:
                alunos = processar_insercao(alunos)
            case OpcaoMenu.SAIR:
                processar_saida()
                break
            case None:
                print("Opção inválida.")

if __name__ == "__main__":
    main()

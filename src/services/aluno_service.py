import re
import unicodedata
from src.models.aluno_models import Aluno, Endereco, Contato

PADRAO_VALIDACAO_UF = re.compile(r"^[A-Z]{2}$")

def validar_uf(uf):
    valor = uf.upper().strip()
    
    if not PADRAO_VALIDACAO_UF.fullmatch(valor):
        raise ValueError("UF inválida")
    
    return valor

def gerar_proxima_matricula(alunos):
    if not alunos:
        return "1"
    
    numeros = [int(re.sub(r"\D", "", a.matricula) or 0) for a in alunos]
    
    return str(max(numeros) + 1)

def inserir(alunos, dados):
    uf = validar_uf(dados.get("UF", ""))
    endereco = Endereco(
        rua=dados.get("Rua", ""),
        numero=dados.get("Número", ""),
        bairro=dados.get("Bairro", ""),
        cidade=dados.get("Cidade", ""),
        uf=uf,
    )
    contato = Contato(
        telefone=dados.get("Telefone", ""),
        email=dados.get("Email", ""),
    )
    
    matricula = gerar_proxima_matricula(alunos)
    
    aluno = Aluno(matricula=matricula, nome=dados.get("Nome", ""), endereco=endereco, contato=contato)
    nova_lista = alunos + [aluno]
    
    return nova_lista, aluno
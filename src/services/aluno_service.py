import re
import unicodedata
from src.models.aluno_models import Aluno, Endereco, Contato

PADRAO_VALIDACAO_UF = re.compile(r"^[A-Z]{2}$")

def normalizar_texto(texto):
    texto = unicodedata.normalize("NFD", str(texto))
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

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

def pesquisar_por_termo(alunos, termo):
    termo = str(termo).strip()
    
    if termo == "":
        return []
    if termo.isdigit():
        return [a for a in alunos if a.matricula == termo]
    
    alvo = normalizar_texto(termo)
    
    return [a for a in alunos if alvo in normalizar_texto(a.nome)]

def campos_editaveis():
    return ["Nome", "Rua", "Número", "Bairro", "Cidade", "UF", "Telefone", "Email"]

def editar_campo(aluno, campo, valor):
    if campo == "Matrícula":
        raise ValueError("Matrícula não é editável")
    
    if campo == "UF":
        valor = validar_uf(valor)

    if campo == "Nome":
        aluno.nome = valor
    elif campo == "Rua":
        aluno.endereco.rua = valor
    elif campo == "Número":
        aluno.endereco.numero = valor
    elif campo == "Bairro":
        aluno.endereco.bairro = valor
    elif campo == "Cidade":
        aluno.endereco.cidade = valor
    elif campo == "UF":
        aluno.endereco.uf = valor
    elif campo == "Telefone":
        aluno.contato.telefone = valor
    elif campo == "Email":
        aluno.contato.email = valor
    else:
        raise ValueError("Campo inválido")

    return aluno

def remover_por_matricula(alunos, matricula):
    return [a for a in alunos if a.matricula != matricula]

def formatar_aluno(aluno):
    return [
        f"Matrícula: {aluno.matricula}",
        f"Nome: {aluno.nome}",
        f"Rua: {aluno.endereco.rua}",
        f"Número: {aluno.endereco.numero}",
        f"Bairro: {aluno.endereco.bairro}",
        f"Cidade: {aluno.endereco.cidade}",
        f"UF: {aluno.endereco.uf}",
        f"Telefone: {aluno.contato.telefone}",
        f"Email: {aluno.contato.email}",
    ]

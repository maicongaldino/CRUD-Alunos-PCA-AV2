# CRUD de Alunos (AV2 PCA)

## Desenvolvedores
- Aluno 1:
  - Matrícula: 06009810
  - Nome: Maicon Galdino Cunha
- Aluno 2:
  - Matrícula: 06013890
  - Nome: Guilherme Henrique Quintanilha

## Descrição
- Sistema CLI para cadastro, pesquisa, edição e remoção de alunos.
- Persistência em `alunos.csv` na raiz do projeto.
- Pesquisa por nome/matrícula com normalização (sem acentos, minúsculas, sem pontuação).

## Instruções de Uso
- Pré-requisitos: `Python 3.10+` e `pip`.
- Instalar dependências: `pip install -r requirements.txt`
- Executar: `python main.py`
- Exemplo de fluxo:
  - Escolher opção `1` para inserir e preencher os campos.
  - Escolher opção `2` para pesquisar por matrícula ou nome.
  - Confirmar edição/remoção quando solicitado.

## Estrutura do Projeto
- `main.py`: menu e interação de linha de comando.
- `src/models/aluno_models.py`: modelos (`Aluno`, `Endereco`, `Contato`).
- `src/services/aluno_service.py`: regras de negócio (inserir, pesquisar, editar, remover, normalização de texto).
- `src/repositories/aluno_repository.py`: leitura/escrita do CSV na raiz.
- `alunos.csv`: base de dados (gerado/atualizado automaticamente).

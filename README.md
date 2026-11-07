# Controle de despesas pessoais

Aplicação web local em Python e Django para controle de despesas pessoais, com
SQLite para armazenar os dados no computador. O planejamento das funcionalidades
está em [BACKLOG.md](BACKLOG.md), e a escolha das tecnologias está em
[TECNOLOGIAS.md](TECNOLOGIAS.md).

Atualmente, o projeto apresenta uma página inicial com uma saudação e possui um
teste dessa página. Cadastro, consulta, edição, exclusão, filtros, resumo mensal
e cópia de segurança das despesas ainda estão previstos no backlog.

## Pré-requisitos e versões utilizadas

Os comandos abaixo são para um terminal Bash no Linux, dentro da pasta do
projeto, onde estão `manage.py` e `requirements.txt`.

| Componente | Versão verificada no ambiente de desenvolvimento |
| --- | --- |
| Python | 3.13.0 |
| Django | 6.1.3 |
| python-dotenv | 1.2.4 |
| SQLite | 3.45.1, acessado pelo módulo `sqlite3` do Python |

É necessário ter Python 3.13 com suporte a `venv` e `pip`, ferramentas de criação
de ambientes virtuais e instalação de dependências, além de um navegador.
Não é necessário instalar um serviço de banco de dados separado.

No computador usado na verificação, `python3` fora do ambiente virtual aponta
para Python 3.12.3. Por isso, a preparação abaixo usa explicitamente
`python3.13`. Confira a versão antes de criar o ambiente.

## 1. Preparar e ativar o ambiente virtual

Um ambiente virtual mantém as dependências deste projeto separadas das de outros
projetos. Na primeira preparação, execute:

```bash
python3.13 --version
python3.13 -m venv .venv
```

Se já houver uma `.venv` preparada com Python 3.13, use-a sem recriá-la. Ative o
ambiente no terminal em que trabalhará e confira a versão:

```bash
source .venv/bin/activate
python --version
```

A versão esperada neste projeto é `Python 3.13.0`. A ativação vale apenas para o
terminal atual; repita `source .venv/bin/activate` ao abrir outro terminal.
Nos próximos passos, mantenha o ambiente ativado.

## 2. Instalar as dependências registradas

```bash
python -m pip install -r requirements.txt
python -m django --version
```

O arquivo `requirements.txt` registra as versões das dependências. A versão
esperada do Django é `6.1.3`.

## 3. Configurar a SECRET_KEY

`SECRET_KEY` é uma chave privada usada pelo Django para assinar dados. O projeto
usa `python-dotenv` para carregar essa configuração do arquivo `.env`.

Copie o modelo sem sobrescrever um `.env` existente:

```bash
cp -n .env.example .env
```

Se já tiver um `.env` configurado, preserve sua chave. Para uma nova configuração,
gere uma chave no terminal:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Abra `.env` em um editor e preencha `SECRET_KEY` com o resultado, substituindo o
texto de exemplo abaixo:

```dotenv
SECRET_KEY=cole_aqui_a_chave_gerada
```

Não deixe o valor vazio nem compartilhe a chave. `.env`, `.venv` e `db.sqlite3`
estão ignorados pelo Git. `.env.example` é apenas o modelo, sem uma chave real.

## 4. Verificar a configuração

```bash
python manage.py check
```

O resultado esperado é `System check identified no issues (0 silenced).`
Esse comando verifica a configuração; os testes são executados separadamente.

## 5. Iniciar e acessar a aplicação

```bash
python manage.py runserver
```

Mantenha esse terminal aberto. Quando o servidor indicar que iniciou, abra
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador do mesmo computador.
A página atual apresenta:

> Olá, Bem-vindo ao controlador de despesas pessoais.

O servidor Django é o programa Python que recebe as solicitações e devolve as
páginas. O navegador acessa e apresenta essas páginas. Fechar a aba do navegador
mantém o servidor em execução; encerrar o servidor impede novos acessos.

### SQLite e migrações

O banco local está configurado como `db.sqlite3`, na raiz do projeto, ao lado de
`manage.py`. Os dados pertencem a essa instalação no computador do servidor;
outro navegador que acessar o mesmo servidor utilizará o mesmo banco.

O modelo de despesa e sua migração ainda não foram implementados. Migrações são
arquivos que descrevem a criação ou alteração das tabelas. A geração e a aplicação
das migrações de despesas, com seus comandos, serão documentadas em **B10**.

Na verificação atual, a inicialização avisou sobre **18 migrações pendentes** dos
componentes internos `admin`, `auth`, `contenttypes` e `sessions`. A página inicial
respondeu normalmente porque não consulta o banco; isso não comprova que as
tabelas desses componentes estejam prontas. Nenhuma migração foi aplicada nesta
tarefa. O roteiro atual permite verificar a saudação e seu teste sem essa etapa.

### Acesso pelo celular

Com o comando acima, o endereço `127.0.0.1` permite acesso pelo próprio computador.
No celular, esse endereço aponta para o celular, e não para o computador.

O uso em um celular físico depende de o computador continuar ligado, com o Django
em execução, e de ambos estarem em uma rede local que permita a comunicação.
Também exige configurar o endereço de escuta do servidor, `ALLOWED_HOSTS` no
Django e as permissões de rede do computador, usando o IP local do computador no
navegador do celular. Essa preparação ainda não foi realizada. Por enquanto, a
simulação de telas pequenas pode ser feita nas ferramentas de desenvolvimento do
navegador do computador.

## 6. Executar os testes

Em outro terminal na raiz do projeto, ative o ambiente e execute:

```bash
source .venv/bin/activate
python manage.py test
```

Atualmente, o comando descobre **1 teste**, que verifica se a página inicial
retorna HTTP 200, código de resposta que indica sucesso. O resultado esperado é
`Ran 1 test` e `OK`. O servidor não precisa estar em execução para esse teste.

O teste usa `SimpleTestCase`, pois não acessa o banco; o Django dispensa a criação
do banco de testes. Quando forem introduzidos testes de persistência em B10,
será usado `TestCase`, com um banco separado gerenciado pelo Django. O banco
local de dados pessoais não deve ser usado como banco de testes.

## 7. Encerrar o processo local

No terminal em que `runserver` está em execução, pressione **Ctrl+C** e aguarde
o retorno do prompt. Isso encerra o servidor, preservando o arquivo SQLite.

Para sair do ambiente virtual, execute em cada terminal em que ele foi ativado:

```bash
deactivate
```

## Verificações realizadas em 07/11/2026

No ambiente virtual existente, foram executados:

| Verificação | Resultado observado |
| --- | --- |
| `.venv/bin/python -B manage.py check` | Nenhum problema apontado pela verificação de configuração. |
| `.venv/bin/python -B manage.py test --noinput --verbosity 2` | 1 teste executado, resultado `OK`; criação do banco de testes dispensada. |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B manage.py runserver --noreload` | Servidor iniciado em `http://127.0.0.1:8000/`, com aviso das 18 migrações pendentes. |
| `curl --fail --silent --show-error -i http://127.0.0.1:8000/` | HTTP 200 e a saudação esperada. |
| `Ctrl+C` no terminal do servidor | Processo encerrado com código de saída 0. |

`-B` e `PYTHONDONTWRITEBYTECODE=1` evitam gerar arquivos de cache do Python;
`--noreload` desativa o reinício automático durante a verificação do servidor.
Nessa verificação, o acesso foi conferido por uma requisição HTTP no terminal,
sem abertura visual no navegador ou teste em celular físico.

### Validação da preparação em ambiente virtual novo

Também em 07/11/2026, o desenvolvedor seguiu o roteiro em uma cópia temporária do
projeto em `/tmp`, sem reutilizar a `.venv`, o `.env` ou o banco de dados do
projeto original. As saídas compartilhadas confirmaram:

- Python `3.13.0` disponível fora do ambiente virtual existente.
- Criação de uma nova `.venv` com `python3.13 -m venv .venv` e ativação com
  `source .venv/bin/activate`; Python `3.13.0` e pip `24.2` nesse ambiente.
- Instalação bem-sucedida com `python -m pip install -r requirements.txt`:
  Django `6.1.3`, asgiref `3.13.0`, python-dotenv `1.2.4` e sqlparse `0.6.1`.
- Django `6.1.3` confirmado com `python -m django --version`.

O desenvolvedor também configurou um novo `.env` a partir de `.env.example`,
com uma nova `SECRET_KEY` gerada localmente, sem compartilhar a chave.

| Verificação na cópia temporária | Resultado observado |
| --- | --- |
| `python manage.py check` | `System check identified no issues (0 silenced).` |
| `python manage.py runserver` | Servidor iniciado em `http://127.0.0.1:8000/`, com aviso das 18 migrações pendentes de `admin`, `auth`, `contenttypes` e `sessions`. |
| Acesso pelo navegador do computador | Requisição `GET /` com HTTP 200 no log; o desenvolvedor confirmou a saudação na página. |
| `Ctrl+C` no terminal do servidor | Servidor encerrado, com retorno ao prompt. |
| `python manage.py test` | 1 teste descoberto e executado, resultado `OK`. |

Nenhuma migração foi aplicada. Com essas evidências, a validação do roteiro da
B05 em um ambiente virtual novo foi concluída.

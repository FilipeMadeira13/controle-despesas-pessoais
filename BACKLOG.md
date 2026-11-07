# Backlog — Controle de despesas pessoais

## Objetivo e escopo do MVP

Construir uma aplicação web responsiva para registrar e consultar despesas pessoais, entender os gastos mensais e manter uma cópia de segurança dos dados. MVP significa a primeira versão pequena e útil do produto.

Decisões já tomadas:

- Uso individual, sem login, por uma interface web responsiva.
- Python + Django para regras de negócio, formulários e páginas HTML; SQLite para persistência; HTML e CSS para a interface; ferramentas de testes do Django para verificações automatizadas. A escolha e sua justificativa estão registradas em [TECNOLOGIAS.md](TECNOLOGIAS.md).
- Django executado localmente no computador, com as despesas guardadas em um arquivo SQLite nesse computador. O navegador acessa as páginas geradas pelo servidor Python.
- Uso no celular depende de o computador estar ligado e acessível pela rede local, com configuração específica antes desse acesso. A revisão visual pode começar pela simulação de telas pequenas no navegador do computador.
- Cadastro, listagem, edição e exclusão de despesas.
- Consulta por mês e categoria, total dos registros filtrados e resumo mensal por categoria.
- Exportação e restauração de uma cópia de segurança em JSON, um formato de dados em texto.
- Formulários e navegação com páginas geradas pelo Django; uma API separada não é necessária para este MVP.

Estado verificado em **06/11/2026**: o Git reconhece o repositório e a branch atual é `iniciar-projeto`. B01, B02 e B03 já estão marcadas como concluídas. Há uma estrutura inicial Django com o app `expenses`, SQLite configurado e uma página inicial que responde com uma saudação. Na revisão anterior, `manage.py check` não apontou problemas, a consulta à rota `/` pelo cliente de testes retornou HTTP 200 e `manage.py test` encontrou **0 testes**. A página não foi aberta no navegador nessa revisão. A configuração de um teste inicial permanece pendente em B04; cadastro e persistência de despesas ainda não foram implementados.

## Como trabalhar com este backlog

- Execute uma microtarefa por vez, seguindo a ordem sugerida e conferindo suas dependências.
- Você escreverá os testes e a implementação; a mentoria oferecerá explicações, dicas e revisão.
- Nas funcionalidades com regras testáveis, use TDD: **RED**, escrever um teste e observar a falha esperada; **GREEN**, implementar o mínimo para passar; **REFACTOR**, melhorar o código preservando o comportamento e os testes.
- Para ajustes visuais e acessibilidade, combine verificações manuais com os testes que fizerem sentido.
- Antes de instalações, alterações de arquivos, mudanças no Git ou operações externas, explique o impacto e obtenha autorização para a etapa correspondente. A autorização para criar este backlog não autoriza implementar a aplicação.
- Marque uma tarefa somente após demonstrar seu critério de aceitação e registrar o resultado da verificação. Os testes descritos abaixo são previstos; execuções já verificadas devem ter seus resultados registrados explicitamente.
- Se uma tarefa ficar grande para uma sessão, divida-a em subtarefas como `B10.1` e `B10.2`, preservando o ID original.

### Critério de conclusão de cada tarefa

O resultado esperado está demonstrável; as verificações pertinentes foram executadas; eventuais limitações foram anotadas; o escopo foi respeitado. Quando houver mudança de código, registre os comandos de verificação e seus resultados, sem afirmar ausência de bugs.

### Marcos

| Marco | Tarefas | Entrega observável |
| --- | --- | --- |
| 1. Preparação | B01–B05 | Projeto inicia localmente e possui uma forma de executar testes |
| 2. Cadastro e persistência | B06–B12 | Uma despesa válida é guardada e continua disponível após recarregar |
| 3. Consulta e correção | B13–B18 | Despesas podem ser consultadas, editadas e excluídas |
| 4. Filtros e resumo | B19–B23 | Usuário entende os gastos por mês e categoria |
| 5. Cópia de segurança | B24–B26 | Dados podem ser exportados e restaurados com validação |
| 6. Qualidade e fechamento | B27–B30 | Fluxo completo verificado, interface revisada e documentação atualizada |

## Regras compartilhadas

- **Despesa:** identificador único, descrição, valor, data e categoria. Descrição, valor, data e categoria são obrigatórios; descrição formada apenas por espaços é inválida.
- **Moeda:** real brasileiro, com valores positivos armazenados em centavos inteiros e apresentados em reais com duas casas decimais. A entrada segue a notação brasileira, como `12,50`; rejeitar entradas inválidas ou com mais de duas casas decimais.
- **Precisão:** definir limites explícitos para valores e totais, compatíveis com o campo inteiro escolhido no Django e com o SQLite. Aplicar os mesmos limites no formulário e na restauração; cálculos e conversões não devem introduzir arredondamentos silenciosos nem usar `float`, tipo numérico de ponto flutuante que pode perder precisão.
- **Data:** data civil válida, sem horário, representada por `date` em Python e `DateField` no Django, exportada como `AAAA-MM-DD` e apresentada como `DD/MM/AAAA`. O dia informado deve permanecer o mesmo independentemente do fuso horário.
- **Categorias fixas:** Alimentação, Moradia, Transporte, Saúde, Educação, Lazer e Outros. Gerenciar categorias personalizadas não faz parte do MVP.
- **Consulta:** começar no mês atual de uso da aplicação, incluindo o ano. Como a página será gerada no servidor, usar a data local no fuso configurado no Django, inicialmente `America/Fortaleza`. A lista combina mês e categoria e apresenta as datas mais recentes primeiro.
- **Totais:** o total dos registros exibidos respeita os dois filtros. O resumo por categoria considera o mês inteiro, com esse alcance indicado na interface.
- **Persistência:** dados pertencem à instalação local da aplicação e ficam no SQLite; trocar de navegador não cria outra coleção de despesas. Acesso ao mesmo servidor utiliza o mesmo banco, sem cópias independentes por dispositivo. Só confirmar o sucesso de uma alteração depois de concluir a gravação.
- **Requisições:** consultas não alteram dados. Cadastro, edição, exclusão e confirmação de restauração usam `POST`, método de envio de formulários, com a proteção CSRF do Django contra submissões forjadas por outros sites. Após uma alteração bem-sucedida, redirecionar para uma consulta para evitar repetir o envio ao atualizar a página.
- **Banco de dados:** mudanças de estrutura usam migrações do Django, arquivos que descrevem a criação ou alteração das tabelas. Testes que acessam o banco usam o banco de testes gerenciado pelo Django, separado dos dados pessoais.
- **Backup:** exportar todas as despesas, independentemente dos filtros, com identificação da versão do formato. Restaurar significa substituir todas as despesas atuais, após validação completa no servidor e confirmação explícita; não mesclar registros no MVP. A substituição usa uma transação, que aplica todas as alterações ou desfaz todas em caso de falha.

## Marco 1 — Preparação

- [x] **B01 — Comparar alternativas e escolher a tecnologia**
  - **Objetivo:** escolher a base técnica com orientação, considerando experiência atual, ferramentas necessárias e facilidade de testar e manter uma aplicação local.
  - **Dependências:** nenhuma.
  - **Aceitação:** registrar a alternativa escolhida, uma justificativa curta, os comandos previstos e a forma de iniciar e testar o projeto. Não instalar ferramentas nesta tarefa.
  - **Verificação:** explicar com suas palavras como a escolha atende aos requisitos do MVP e quais conhecimentos precisará praticar.
  - **Decisão registrada:** Python + Django, SQLite, HTML e CSS e testes do Django, conforme [TECNOLOGIAS.md](TECNOLOGIAS.md). Com o ambiente virtual ativado, os comandos são `python manage.py runserver` para iniciar localmente, `python manage.py check` para verificar a configuração e `python manage.py test` para executar os testes. As evidências já obtidas estão no estado verificado acima.
  - **Risco:** adicionar ferramentas sem necessidade e aumentar a dificuldade inicial.

- [x] **B02 — Preparar repositório Git e branch de trabalho**
  - **Objetivo:** estabelecer o controle de versão e uma branch para o desenvolvimento.
  - **Dependências:** B01.
  - **Aceitação:** após autorização dos comandos, o Git reconhece o repositório e a branch atual é diferente de `main` e `master`. Preservar o `BACKLOG.md`, o `TECNOLOGIAS.md` e qualquer trabalho existente; não fazer commit, push ou configurar serviços externos nesta tarefa.
  - **Verificação:** conferir o estado do repositório, a branch atual e os arquivos existentes antes e depois da preparação.
  - **Risco:** sobrescrever arquivos ou executar operações sobre uma branch incorreta.

- [x] **B03 — Criar a estrutura mínima da aplicação**
  - **Objetivo:** preparar um projeto Django com um app de despesas, unidade que reúne os arquivos dessa funcionalidade.
  - **Dependências:** B01, B02.
  - **Aceitação:** depois das autorizações necessárias, preparar um ambiente virtual Python, registrar as dependências, configurar SQLite e o fuso `America/Fortaleza`, e criar uma rota para uma página inicial identificada como controle de despesas. O endereço local padrão é `http://127.0.0.1:8000/`, após iniciar com `python manage.py runserver`. A resposta inicial pode usar `HttpResponse`; os templates, modelos HTML preenchidos pelo Django, serão introduzidos em B09. Ignorar no Git o ambiente virtual, o banco local e outros arquivos gerados ou sensíveis.
  - **Verificação:** executar `python manage.py check` e o comando de inicialização, abrir a página no navegador e registrar os resultados. Distinguir a verificação pelo cliente de testes da verificação no navegador. A estrutura das tabelas de despesas será criada em B10.
  - **Risco:** introduzir dependências ou configurações além do necessário para começar.

- [x] **B04 — Configurar a execução dos testes**
  - **Objetivo:** disponibilizar testes reproduzíveis usando as ferramentas integradas do Django.
  - **Dependências:** B03.
  - **Aceitação:** `python manage.py test` descobre e executa um teste inicial da página; uma falha intencional temporária produz uma falha reconhecível. Usar `SimpleTestCase` para testes sem banco e `TestCase` para testes com banco, sem direcioná-los ao arquivo SQLite de uso pessoal.
  - **Verificação:** conferir a quantidade de testes executados, observar a falha controlada, restaurar o teste correto e registrar a execução passando. Confirmar o isolamento do banco quando os primeiros testes de persistência forem adicionados em B10.
  - **Evidências:** o desenvolvedor confirmou a falha intencional ao trocar a expectativa de HTTP 200 por HTTP 404. Na revisão, com a expectativa correta de HTTP 200, o comando `.venv/bin/python -B manage.py test --noinput --verbosity 2` descobriu e executou 1 teste com resultado `OK`; o Django dispensou a criação do banco de testes por não haver acesso ao banco.
  - **Risco:** ter um comando que termina com sucesso sem realmente descobrir ou executar testes.

- [x] **B05 — Registrar instruções para iniciar e verificar o projeto**
  - **Objetivo:** documentar pré-requisitos e comandos efetivamente utilizados.
  - **Dependências:** B04.
  - **Aceitação:** documentação apresenta versões utilizadas, preparação e ativação do ambiente virtual, instalação das dependências registradas, configuração de `SECRET_KEY` a partir de `.env.example`, `python manage.py check`, inicialização com `python manage.py runserver`, testes com `python manage.py test` e encerramento do processo local. Distinguir o servidor Django do navegador e explicar onde fica o SQLite; documentar migrações quando introduzidas em B10 e a condição de acesso pelo celular.
  - **Verificação:** seguir as instruções na ordem escrita e registrar qualquer ajuste necessário.

## Marco 2 — Cadastrar e guardar despesas

- [ ] **B06 — Definir os campos e exemplos de uma despesa**
  - **Objetivo:** registrar os campos previstos para o modelo Django e exemplos que orientarão os testes. Modelo é a representação dos dados em Python ligada a uma tabela do banco.
  - **Dependências:** B01.
  - **Aceitação:** identificador, descrição, centavos inteiros, data civil e categoria têm suas representações e campos Django previstos documentados conforme as regras compartilhadas, com exemplos válidos e inválidos. Definir limites de texto, valor e totais, além da representação de identificadores e datas no backup; a criação do modelo e de sua migração ocorre em B10.
  - **Verificação:** representar uma despesa de R$ 12,50 e explicar como valor e data serão preservados.
  - **Risco:** misturar valores formatados para exibição com os valores usados em cálculos.

- [ ] **B07 — Testar as regras de preenchimento**
  - **Objetivo:** escrever testes em Python para as validações do formulário Django antes da implementação das regras.
  - **Dependências:** B04, B06.
  - **Aceitação:** testes cobrem uma despesa válida, campos ausentes, descrição em branco, valor zero, negativo ou inválido, precisão excessiva, categoria desconhecida e data impossível.
  - **Verificação:** executar `python manage.py test` e observar falhas causadas pela ausência das regras, distinguindo-as de erros de configuração. Verificar a validação no servidor, sem depender das restrições dos campos HTML.
  - **Risco:** escrever testes que não exercitam o comportamento pretendido.

- [ ] **B08 — Implementar as validações e o tratamento dos valores**
  - **Objetivo:** implementar o mínimo para satisfazer os testes de B07 e tornar os cálculos previsíveis.
  - **Dependências:** B07.
  - **Aceitação:** o formulário Django valida as entradas no servidor; entradas válidas produzem dados normalizados e entradas inválidas indicam o campo a corrigir. Valores em notação brasileira são convertidos em centavos inteiros sem passar por `float` nem arredondar silenciosamente; datas são tratadas como datas civis. As regras devem poder ser reutilizadas na edição e na validação do backup.
  - **Verificação:** executar B07 e casos monetários como R$ 0,10 + R$ 0,20 = R$ 0,30; verificar conversão de R$ 12,50 em 1250 centavos e rejeição de valores fora dos limites definidos em B06. Refatorar apenas com os testes passando.
  - **Risco:** usar cálculos decimais imprecisos ou aceitar parcialmente uma entrada malformada.

- [ ] **B09 — Criar o formulário de cadastro**
  - **Objetivo:** apresentar o formulário Django em um template HTML usando as regras já testadas.
  - **Dependências:** B03, B08.
  - **Aceitação:** campos possuem rótulos, seletor de categoria e ação de salvar; o formulário usa `POST` com proteção CSRF. Erros retornados pelo Django são visíveis junto aos campos e não apagam o preenchimento. A estrutura HTML e CSS já permite adaptação a telas pequenas.
  - **Verificação:** preencher um caso válido e corrigir casos inválidos usando teclado e navegador; nesta etapa, validar o formulário sem anunciar persistência ainda inexistente.

- [ ] **B10 — Salvar uma despesa no SQLite com Django**
  - **Objetivo:** criar o modelo de despesa e conectar o formulário válido à persistência no SQLite.
  - **Dependências:** B09.
  - **Aceitação:** o modelo corresponde aos campos definidos em B06; sua migração é gerada, revisada e aplicada ao banco local após autorização. Registrar os comandos de migração na documentação. Salvar por `POST` cria um identificador único e persiste a despesa; entradas inválidas não são gravadas. A confirmação de sucesso e o redirecionamento ocorrem somente após a gravação.
  - **Verificação:** escrever testes com o banco isolado do Django e conferir duas despesas com identificadores diferentes; uma terceira entrada inválida não altera os dados. Conferir as migrações aplicadas e verificar que consultas por `GET` e a atualização da página após o redirecionamento não criam despesas. Se necessário, dividir em B10.1 para modelo e migração e B10.2 para salvamento pelo formulário.
  - **Risco:** sobrescrever registros anteriores ou indicar sucesso antes de concluir a gravação.

- [ ] **B11 — Recuperar os dados ao abrir a aplicação**
  - **Objetivo:** consultar as despesas persistidas no SQLite ao acessar a aplicação usando o ORM do Django, ferramenta que permite consultar o banco por meio de Python.
  - **Dependências:** B10.
  - **Aceitação:** uma tabela sem despesas retorna uma coleção vazia; registros salvos são recuperados com os mesmos valores, datas e identificadores após recarregar a página ou reiniciar o servidor local. Acesso por outro navegador ao mesmo servidor consulta os mesmos registros.
  - **Verificação:** comparar os dados antes e depois do recarregamento e do reinício do servidor; verificar o comportamento vazio no banco de testes, sem apagar dados pessoais, e conferir o acesso à mesma instalação por outro navegador.

- [ ] **B12 — Tratar falhas de acesso ao banco**
  - **Objetivo:** tornar falhas de leitura e gravação compreensíveis e preservar o trabalho do usuário.
  - **Dependências:** B11.
  - **Aceitação:** falhas de consulta e de gravação, incluindo banco indisponível ou bloqueado, geram mensagens claras; não confirmar salvamento, tratar falha de consulta como lista vazia, recriar automaticamente o banco ou perder o formulário preenchido. A estrutura do banco é preparada por migrações, não como reação a uma falha de acesso.
  - **Verificação:** simular as falhas com dados de teste e confirmar que os registros anteriores permanecem iguais e uma nova tentativa é possível após a recuperação; não danificar o arquivo SQLite pessoal para realizar a verificação.
  - **Risco:** apresentar uma falha como sucesso ou ausência de despesas e causar perda de dados.

## Marco 3 — Consultar e corrigir despesas

- [ ] **B13 — Exibir a lista de despesas**
  - **Objetivo:** tornar os registros recuperados consultáveis na interface.
  - **Dependências:** B11.
  - **Aceitação:** o template Django apresenta descrição, data, categoria e valor em reais; a consulta ordena as datas mais recentes primeiro, sem mudar o dia informado. Descrições usam o escape padrão do template para serem exibidas como texto.
  - **Verificação:** usar despesas de datas distintas e valores como R$ 0,10 e R$ 12,50, conferindo ordem e formatação. Descrições devem ser exibidas como texto.

- [ ] **B14 — Exibir o estado sem despesas**
  - **Objetivo:** orientar quem ainda não possui registros.
  - **Dependências:** B13.
  - **Aceitação:** uma coleção vazia exibe mensagem clara e uma orientação para cadastrar a primeira despesa.
  - **Verificação:** abrir com dados de teste vazios e confirmar que a mensagem desaparece após o primeiro cadastro.

- [ ] **B15 — Abrir uma despesa para edição**
  - **Objetivo:** permitir selecionar um registro e alterar seu preenchimento sem gravar imediatamente.
  - **Dependências:** B13.
  - **Aceitação:** editar preenche os campos com os dados do registro selecionado; cancelar abandona as alterações e mantém os dados persistidos.
  - **Verificação:** selecionar registros diferentes, modificar os campos e cancelar, conferindo que nenhum registro foi alterado.
  - **Risco:** associar a edição à posição na lista em vez de ao identificador estável.

- [ ] **B16 — Validar e salvar uma edição**
  - **Objetivo:** persistir alterações em uma despesa existente reutilizando as regras de cadastro.
  - **Dependências:** B08, B15.
  - **Aceitação:** o formulário Django reutiliza as regras de cadastro; salvar por `POST` altera apenas o registro selecionado, preservando seu identificador. Entradas inválidas são rejeitadas e uma edição salva permanece após recarregar. Um identificador inexistente recebe uma resposta compreensível, sem criar outro registro.
  - **Verificação:** testar uma edição válida, uma inválida e uma falha de gravação; conferir que os demais registros permanecem iguais e o formulário não se perde na falha.
  - **Risco:** duplicar a despesa ou alterar outro registro.

- [ ] **B17 — Solicitar confirmação antes de excluir**
  - **Objetivo:** permitir revisar a intenção de excluir um registro.
  - **Dependências:** B13.
  - **Aceitação:** uma página de confirmação identifica a despesa e oferece ações claras de cancelar ou excluir. Abrir a página por `GET` ou cancelar não modifica os dados; a confirmação envia um formulário `POST` protegido por CSRF.
  - **Verificação:** abrir e cancelar a confirmação para registros diferentes, inclusive usando o teclado.

- [ ] **B18 — Excluir a despesa confirmada**
  - **Objetivo:** remover somente o registro cuja exclusão foi confirmada.
  - **Dependências:** B17.
  - **Aceitação:** somente o `POST` de confirmação remove a despesa do SQLite; a exclusão persiste após recarregar. Os demais registros são preservados e falha no banco não é apresentada como exclusão concluída. Um identificador inexistente recebe uma resposta compreensível.
  - **Verificação:** excluir um registro entre vários e depois o último registro; confirmar persistência, estado vazio e tratamento de falha. Verificar que um acesso por `GET` não exclui despesas.
  - **Risco:** excluir o registro incorreto ou perder a coleção inteira.

## Marco 4 — Filtros e resumo mensal

- [ ] **B19 — Selecionar o mês consultado**
  - **Objetivo:** restringir a consulta a um mês e ano selecionados.
  - **Dependências:** B13.
  - **Aceitação:** o mês atual no fuso configurado da aplicação é selecionado inicialmente. Enviar o filtro por `GET` consulta o SQLite e apresenta somente registros desse mês e ano; meses sem registros exibem uma mensagem apropriada. Um mês malformado recebe tratamento compreensível.
  - **Verificação:** usar datas no último e no primeiro dia de meses consecutivos e na virada de dezembro para janeiro; verificar o mês inicial com uma data controlada no teste, incluindo um instante em que o mês em UTC difere do mês em `America/Fortaleza`.
  - **Risco:** comparar apenas o número do mês, misturar anos ou deslocar datas por fuso.

- [ ] **B20 — Filtrar as despesas por categoria**
  - **Objetivo:** combinar a categoria escolhida com o mês consultado.
  - **Dependências:** B19.
  - **Aceitação:** o formulário de filtros envia mês e categoria por `GET`; selecionar uma categoria restringe os registros do mês e “Todas as categorias” remove somente essa restrição. Ausência de resultados não sugere que todos os dados foram apagados. Uma categoria desconhecida recebe tratamento compreensível.
  - **Verificação:** combinar meses e categorias com e sem registros; trocar cada filtro preservando o valor do outro.

- [ ] **B21 — Calcular e mostrar o total das despesas filtradas**
  - **Objetivo:** apresentar o valor total dos registros efetivamente exibidos.
  - **Dependências:** B20.
  - **Aceitação:** o total corresponde à soma dos centavos dos registros filtrados, formatada em reais; ausência de resultados apresenta R$ 0,00.
  - **Verificação:** conferir totais conhecidos, como R$ 0,10 + R$ 0,20, em diferentes combinações de filtros, e o tratamento de limites de precisão.
  - **Risco:** somar valores já formatados, incluir registros ocultos ou perder precisão.

- [ ] **B22 — Mostrar os totais por categoria no mês**
  - **Objetivo:** apresentar a distribuição dos gastos mensais entre categorias.
  - **Dependências:** B19.
  - **Aceitação:** o resumo considera todas as despesas do mês selecionado, independentemente do filtro de categoria da lista, e informa esse alcance; a soma dos grupos é igual ao total mensal.
  - **Verificação:** usar um mês com várias categorias, trocar o mês e conferir a soma; trocar apenas a categoria da lista não altera a distribuição mensal.
  - **Risco:** apresentar totais com alcances diferentes sem identificá-los na interface.

- [ ] **B23 — Atualizar lista e resumo após alterações**
  - **Objetivo:** manter a consulta coerente com os dados salvos por meio de redirecionamento e nova geração da página pelo Django, sem exigir uma atualização manual.
  - **Dependências:** B16, B18, B21, B22.
  - **Aceitação:** após cadastro, edição ou exclusão bem-sucedidos, o Django redireciona para a consulta preservando mês e categoria; a página recalcula lista, total filtrado e resumo mensal. Uma falha de persistência mantém o formulário e seus erros sem anunciar sucesso.
  - **Verificação:** cadastrar no mês selecionado, editar data e categoria para sair do filtro e excluir um registro; conferir todos os resultados e simular uma gravação malsucedida.
  - **Risco:** atualizar apenas uma parte da tela ou apresentar uma alteração não persistida.

## Marco 5 — Cópia de segurança

- [ ] **B24 — Exportar as despesas em JSON**
  - **Objetivo:** permitir baixar pelo navegador uma cópia das despesas consultadas pelo Django no SQLite.
  - **Dependências:** B11.
  - **Aceitação:** uma ação explícita solicita ao Django um arquivo JSON para download, contendo a versão do formato e todas as despesas, sem depender dos filtros ativos. Identificadores, centavos inteiros, datas civis e categorias seguem o formato definido em B06. A exportação não altera os dados atuais.
  - **Verificação:** exportar uma coleção conhecida, conferir campos e quantidade, repetir com coleção vazia e com um filtro que oculta parte dos registros.
  - **Risco:** produzir uma cópia incompleta ou perder identificadores, centavos ou datas.

- [ ] **B25 — Validar um arquivo antes da restauração**
  - **Objetivo:** receber o arquivo por um formulário Django e verificar integralmente a cópia no servidor antes de permitir qualquer substituição.
  - **Dependências:** B24.
  - **Aceitação:** aceitar apenas o formato e a versão suportados, com registros válidos segundo as regras compartilhadas e identificadores únicos. JSON inválido, versão desconhecida ou qualquer registro inválido rejeitam o arquivo inteiro sem alterar dados atuais. A validação reutiliza as regras aplicáveis do cadastro e respeita os limites do modelo; o resultado preparado para confirmação não é uma restauração parcial.
  - **Verificação:** testar o envio de uma cópia válida, arquivo malformado, versão incompatível, campo ausente, identificadores repetidos, valor não inteiro ou fora dos limites, categoria desconhecida e data impossível; conferir que nenhuma despesa muda antes da confirmação.
  - **Risco:** confiar no arquivo importado ou aplicar uma restauração parcial antes de terminar a validação.

- [ ] **B26 — Restaurar os dados com confirmação**
  - **Objetivo:** substituir os registros atuais por uma cópia integralmente validada.
  - **Dependências:** B25.
  - **Aceitação:** informar que todas as despesas atuais serão substituídas e apresentar a quantidade de registros da cópia. Cancelar preserva tudo; confirmar por `POST` protegido por CSRF aplica somente o conteúdo validado no servidor. Garantir a validação do conteúdo efetivamente restaurado, sem confiar em campos enviados pelo navegador como prova de validação. Excluir as despesas anteriores e inserir as novas em uma única transação com `transaction.atomic()`; uma falha desfaz toda a substituição. Confirmar sucesso e atualizar a tela apenas após a conclusão. Não mesclar coleções nem substituir tabelas internas do Django.
  - **Verificação:** no banco de testes, restaurar a exportação de B24 e comparar os registros; testar cancelamento, uma falha após o início da substituição, conteúdo alterado após a validação e uma cópia vazia válida, que também exige confirmação. Conferir que a falha preserva integralmente as despesas anteriores e que um novo cadastro após a restauração recebe um identificador único.
  - **Risco:** perda dos registros atuais por substituição não confirmada ou falha tratada como sucesso.

## Marco 6 — Qualidade e fechamento do MVP

- [ ] **B27 — Adaptar formulários, lista e resumo ao celular**
  - **Objetivo:** revisar o uso responsivo dos fluxos já implementados.
  - **Dependências:** B23, B26.
  - **Aceitação:** campos, valores, filtros, ações e confirmações ficam legíveis e utilizáveis em telas pequenas, sem conteúdo essencial cortado nem rolagem horizontal da página.
  - **Verificação:** percorrer cadastro, consulta, edição, exclusão e backup em larguras de referência de 360, 768 e 1280 pixels; conferir também descrições longas e valores maiores. Validar o layout pela simulação do navegador; acesso por celular físico depende de preparação específica da rede local, sem publicação online.

- [ ] **B28 — Verificar teclado, foco e mensagens acessíveis**
  - **Objetivo:** revisar a operação dos fluxos sem depender de mouse ou apenas de cores.
  - **Dependências:** B27.
  - **Aceitação:** campos têm rótulos associados; ações são alcançáveis por teclado; foco é visível e segue uma ordem compreensível; erros identificam o problema em texto; confirmações permitem cancelar e retornar ao fluxo anterior.
  - **Verificação:** percorrer as ações com Tab, Shift+Tab e teclas de ativação adequadas; provocar erros e verificar sua associação aos campos; revisar a identificação de controles com uma ferramenta de acessibilidade disponível.
  - **Risco:** controles visualmente presentes, mas inacessíveis pelo teclado ou sem identificação compreensível.

- [ ] **B29 — Validar o fluxo completo e corrigir regressões**
  - **Objetivo:** conferir a integração entre os marcos e corrigir falhas demonstradas. Regressão é um comportamento que funcionava e deixou de funcionar após uma mudança.
  - **Dependências:** B28.
  - **Aceitação:** cadastrar, recarregar, editar, filtrar, consultar totais, exportar, excluir e restaurar funcionam em sequência com um conjunto de dados conhecido; verificações automatizadas pertinentes passam e limitações ficam registradas.
  - **Verificação:** executar `python manage.py check`, `python manage.py test` e o roteiro completo com dados de teste, incluindo centavos, limites de mês/ano, falhas do banco e restauração interrompida. Incluir verificações dos formulários, respostas e redirecionamentos com o cliente de testes do Django e conferir a proteção CSRF em verificações específicas. Para cada falha corrigida, acrescentar uma verificação que detecte sua repetição quando adequado.
  - **Risco:** validar apenas funções isoladas e deixar inconsistências entre armazenamento, lista e totais.

- [ ] **B30 — Atualizar a documentação e revisar o aprendizado**
  - **Objetivo:** encerrar o MVP com instruções atuais, evidências e uma revisão ativa.
  - **Dependências:** B29.
  - **Aceitação:** documentação reflete os comandos reais, ambiente virtual, dependências, migrações, localização do SQLite, inicialização do servidor, testes, funcionalidades, exportação/restauração, condições de acesso pelo celular, limitações conhecidas e verificações executadas; o backlog marca apenas tarefas realmente concluídas.
  - **Verificação:** seguir a documentação e responder: por que guardar dinheiro em centavos? Como evitar mudança do dia por fuso? Qual a diferença entre o banco local e o banco de testes? Por que validar a cópia inteira e usar uma transação na restauração? Registrar também uma dificuldade e uma decisão que você consegue explicar sem ajuda.

## Melhorias posteriores ao MVP

Estes itens ainda não são compromissos de implementação. Priorize e divida cada um em microtarefas somente depois de validar o MVP:

- Registro de receitas e cálculo de saldo mensal.
- Criação, edição e organização de categorias personalizadas.
- Orçamento mensal e limites por categoria.
- Despesas recorrentes.
- Compras parceladas.
- Gráficos de evolução e distribuição dos gastos.
- Exportação em CSV para planilhas.

## Fora do escopo do MVP

- Login e cadastro de contas.
- Banco de dados remoto e sincronização de cópias independentes entre dispositivos. Navegadores que acessam a mesma instalação Django consultam o mesmo SQLite.
- API separada e aplicação frontend independente das páginas geradas pelo Django.
- Compartilhamento de despesas entre pessoas.
- Integrações com bancos, cartões ou serviços financeiros.
- Publicação online, configuração de hospedagem e deploy.

Adicionar qualquer um desses itens exige revisar o escopo e planejar suas próprias tarefas. Este backlog não autoriza instalações, mudanças no Git, implementação da aplicação, operações externas ou deploy.

## Próxima microtarefa

**B04 — Configurar a execução dos testes.** Escrever um teste inicial da página usando `SimpleTestCase` e o cliente de testes do Django, conferir que ele é descoberto e demonstrar a falha controlada antes de restaurar a expectativa correta. B01, B02 e B03 mantêm as marcações existentes; esta correção documental não executa B04 nem conclui outras tarefas.

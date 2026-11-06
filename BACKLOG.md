# Backlog — Controle de despesas pessoais

## Objetivo e escopo do MVP

Construir uma aplicação web responsiva para registrar e consultar despesas pessoais, entender os gastos mensais e manter uma cópia de segurança dos dados. MVP significa a primeira versão pequena e útil do produto.

Decisões já tomadas:

- Uso individual, sem login, no navegador do computador ou celular.
- Dados persistidos no `localStorage`, armazenamento do próprio navegador, sem servidor ou API remota.
- Cadastro, listagem, edição e exclusão de despesas.
- Consulta por mês e categoria, total dos registros filtrados e resumo mensal por categoria.
- Exportação e restauração de uma cópia de segurança em JSON, um formato de dados em texto.
- Tecnologia a escolher em **B01**, antes de instalar ferramentas ou escrever a aplicação.

Estado inicial verificado: ainda não há implementação no diretório, e o Git não reconheceu um repositório válido. Este documento não conclui nenhuma tarefa de implementação.

## Como trabalhar com este backlog

- Execute uma microtarefa por vez, seguindo a ordem sugerida e conferindo suas dependências.
- Você escreverá os testes e a implementação; a mentoria oferecerá explicações, dicas e revisão.
- Nas funcionalidades com regras testáveis, use TDD: **RED**, escrever um teste e observar a falha esperada; **GREEN**, implementar o mínimo para passar; **REFACTOR**, melhorar o código preservando o comportamento e os testes.
- Para ajustes visuais e acessibilidade, combine verificações manuais com os testes que fizerem sentido.
- Antes de instalações, alterações de arquivos, mudanças no Git ou operações externas, explique o impacto e obtenha autorização para a etapa correspondente. A autorização para criar este backlog não autoriza implementar a aplicação.
- Marque uma tarefa somente após demonstrar seu critério de aceitação e registrar o resultado da verificação. Os testes descritos abaixo são previstos, ainda não executados.
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
- **Precisão:** validar valores dentro da capacidade segura de inteiros da tecnologia escolhida; cálculos e conversões não devem introduzir arredondamentos silenciosos.
- **Data:** data civil válida, sem horário, representada como `AAAA-MM-DD` e apresentada como `DD/MM/AAAA`. O dia informado deve permanecer o mesmo independentemente do fuso horário.
- **Categorias fixas:** Alimentação, Moradia, Transporte, Saúde, Educação, Lazer e Outros. Gerenciar categorias personalizadas não faz parte do MVP.
- **Consulta:** começar no mês atual do dispositivo, incluindo o ano. A lista combina mês e categoria e apresenta as datas mais recentes primeiro.
- **Totais:** o total dos registros exibidos respeita os dois filtros. O resumo por categoria considera o mês inteiro, com esse alcance indicado na interface.
- **Persistência:** dados pertencem ao navegador, perfil e origem utilizados; não há sincronização entre dispositivos. Só confirmar o sucesso de uma alteração depois de persistir os dados.
- **Backup:** exportar todos os registros, independentemente dos filtros, com identificação da versão do formato. Restaurar significa substituir todos os dados atuais, após validação completa e confirmação explícita; não mesclar registros no MVP.

## Marco 1 — Preparação

- [x] **B01 — Comparar alternativas e escolher a tecnologia**
  - **Objetivo:** escolher a base técnica com orientação, considerando experiência atual, ferramentas necessárias e facilidade de testar e manter uma aplicação local.
  - **Dependências:** nenhuma.
  - **Aceitação:** registrar a alternativa escolhida, uma justificativa curta, os comandos previstos e a forma de iniciar e testar o projeto. Não instalar ferramentas nesta tarefa.
  - **Verificação:** explicar com suas palavras como a escolha atende aos requisitos do MVP e quais conhecimentos precisará praticar.
  - **Risco:** adicionar ferramentas sem necessidade e aumentar a dificuldade inicial.

- [ ] **B02 — Preparar repositório Git e branch de trabalho**
  - **Objetivo:** estabelecer o controle de versão e uma branch para o desenvolvimento.
  - **Dependências:** B01.
  - **Aceitação:** após autorização dos comandos, o Git reconhece o repositório e a branch atual é diferente de `main` e `master`. Preservar o `BACKLOG.md` e qualquer trabalho existente; não fazer commit, push ou configurar serviços externos nesta tarefa.
  - **Verificação:** conferir o estado do repositório, a branch atual e os arquivos existentes antes e depois da preparação.
  - **Risco:** sobrescrever arquivos ou executar operações sobre uma branch incorreta.

- [ ] **B03 — Criar a estrutura mínima da aplicação**
  - **Objetivo:** preparar somente os arquivos e ferramentas necessários à tecnologia escolhida.
  - **Dependências:** B01, B02.
  - **Aceitação:** depois das autorizações necessárias, uma página inicial identificada como controle de despesas abre pelo endereço local documentado.
  - **Verificação:** executar o comando de inicialização e abrir a página no navegador; registrar o resultado.
  - **Risco:** introduzir dependências ou configurações além do necessário para começar.

- [ ] **B04 — Configurar a execução dos testes**
  - **Objetivo:** disponibilizar um comando reproduzível de testes.
  - **Dependências:** B03.
  - **Aceitação:** um teste inicial pertinente à página ou inicialização executa com sucesso; uma falha intencional temporária produz uma falha reconhecível no comando.
  - **Verificação:** observar a falha controlada, restaurar o teste correto e registrar a execução passando.
  - **Risco:** ter um comando que termina com sucesso sem realmente descobrir ou executar testes.

- [ ] **B05 — Registrar instruções para iniciar e verificar o projeto**
  - **Objetivo:** documentar pré-requisitos e comandos efetivamente utilizados.
  - **Dependências:** B04.
  - **Aceitação:** documentação apresenta como preparar o ambiente, iniciar a aplicação, executar os testes e encerrar o processo local.
  - **Verificação:** seguir as instruções na ordem escrita e registrar qualquer ajuste necessário.

## Marco 2 — Cadastrar e guardar despesas

- [ ] **B06 — Definir os campos e exemplos de uma despesa**
  - **Objetivo:** registrar o modelo mínimo e exemplos que orientarão os testes.
  - **Dependências:** B01.
  - **Aceitação:** identificador, descrição, centavos, data civil e categoria têm suas representações documentadas conforme as regras compartilhadas, com exemplos válidos e inválidos.
  - **Verificação:** representar uma despesa de R$ 12,50 e explicar como valor e data serão preservados.
  - **Risco:** misturar valores formatados para exibição com os valores usados em cálculos.

- [ ] **B07 — Testar as regras de preenchimento**
  - **Objetivo:** escrever os testes de validação antes da implementação das regras.
  - **Dependências:** B04, B06.
  - **Aceitação:** testes cobrem uma despesa válida, campos ausentes, descrição em branco, valor zero, negativo ou inválido, precisão excessiva, categoria desconhecida e data impossível.
  - **Verificação:** executar os testes e observar falhas causadas pela ausência das regras, distinguindo-as de erros de configuração.
  - **Risco:** escrever testes que não exercitam o comportamento pretendido.

- [ ] **B08 — Implementar as validações e o tratamento dos valores**
  - **Objetivo:** implementar o mínimo para satisfazer os testes de B07 e tornar os cálculos previsíveis.
  - **Dependências:** B07.
  - **Aceitação:** entradas válidas produzem dados normalizados; entradas inválidas indicam o campo a corrigir. Valores são convertidos em centavos inteiros sem arredondamento silencioso.
  - **Verificação:** executar B07 e casos monetários como R$ 0,10 + R$ 0,20 = R$ 0,30; verificar conversão de R$ 12,50 em 1250 centavos e rejeição de valores fora da faixa segura. Refatorar apenas com os testes passando.
  - **Risco:** usar cálculos decimais imprecisos ou aceitar parcialmente uma entrada malformada.

- [ ] **B09 — Criar o formulário de cadastro**
  - **Objetivo:** permitir preencher uma despesa usando as regras já testadas.
  - **Dependências:** B03, B08.
  - **Aceitação:** campos possuem rótulos, seletor de categoria e ação de salvar; erros são visíveis junto aos campos e não apagam o preenchimento. A estrutura já permite adaptação a telas pequenas.
  - **Verificação:** preencher um caso válido e corrigir casos inválidos usando teclado e navegador; nesta etapa, validar o formulário sem anunciar persistência ainda inexistente.

- [ ] **B10 — Salvar uma despesa no navegador**
  - **Objetivo:** conectar o formulário válido ao armazenamento local.
  - **Dependências:** B09.
  - **Aceitação:** salvar cria um identificador único e persiste a despesa; entradas inválidas não são gravadas. Sucesso e limpeza do formulário ocorrem somente após a gravação.
  - **Verificação:** salvar duas despesas, conferir identificadores diferentes e inspecionar os registros persistidos; uma terceira entrada inválida não altera os dados.
  - **Risco:** sobrescrever registros anteriores ou indicar sucesso antes de concluir a gravação.

- [ ] **B11 — Recuperar os dados ao abrir a aplicação**
  - **Objetivo:** carregar os registros persistidos na inicialização.
  - **Dependências:** B10.
  - **Aceitação:** ausência de dados inicia uma coleção vazia; registros salvos são recuperados com os mesmos valores, datas e identificadores após recarregar a página.
  - **Verificação:** comparar os dados antes e depois do recarregamento e repetir em uma origem sem registros, sem apagar os dados de uso pessoal.

- [ ] **B12 — Tratar falhas de armazenamento**
  - **Objetivo:** tornar falhas de leitura e gravação compreensíveis e preservar o trabalho do usuário.
  - **Dependências:** B11.
  - **Aceitação:** indisponibilidade de armazenamento, falha de gravação e conteúdo ilegível geram mensagens claras; não confirmar salvamento, apagar automaticamente dados existentes ou perder o formulário preenchido.
  - **Verificação:** simular cada falha com dados de teste e confirmar que uma nova tentativa é possível quando o armazenamento volta a funcionar.
  - **Risco:** tratar uma falha de leitura como uma coleção vazia e sobrescrever dados existentes.

## Marco 3 — Consultar e corrigir despesas

- [ ] **B13 — Exibir a lista de despesas**
  - **Objetivo:** tornar os registros recuperados consultáveis na interface.
  - **Dependências:** B11.
  - **Aceitação:** cada registro mostra descrição, data, categoria e valor em reais; a ordenação apresenta as datas mais recentes primeiro, sem mudar o dia informado.
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
  - **Aceitação:** apenas o registro selecionado muda, preservando seu identificador; entradas inválidas são rejeitadas; uma edição salva permanece após recarregar.
  - **Verificação:** testar uma edição válida, uma inválida e uma falha de gravação; conferir que os demais registros permanecem iguais e o formulário não se perde na falha.
  - **Risco:** duplicar a despesa ou alterar outro registro.

- [ ] **B17 — Solicitar confirmação antes de excluir**
  - **Objetivo:** permitir revisar a intenção de excluir um registro.
  - **Dependências:** B13.
  - **Aceitação:** a confirmação identifica a despesa e oferece ações claras de cancelar ou excluir; cancelar não modifica os dados.
  - **Verificação:** abrir e cancelar a confirmação para registros diferentes, inclusive usando o teclado.

- [ ] **B18 — Excluir a despesa confirmada**
  - **Objetivo:** remover somente o registro cuja exclusão foi confirmada.
  - **Dependências:** B17.
  - **Aceitação:** a exclusão persiste após recarregar; os demais registros são preservados; falha ao gravar não é apresentada como exclusão concluída.
  - **Verificação:** excluir um registro entre vários e depois o último registro; confirmar persistência, estado vazio e tratamento de falha.
  - **Risco:** excluir o registro incorreto ou perder a coleção inteira.

## Marco 4 — Filtros e resumo mensal

- [ ] **B19 — Selecionar o mês consultado**
  - **Objetivo:** restringir a consulta a um mês e ano selecionados.
  - **Dependências:** B13.
  - **Aceitação:** o mês atual é selecionado inicialmente; mudar a seleção mostra apenas registros desse mês e ano; meses sem registros exibem uma mensagem apropriada.
  - **Verificação:** usar datas no último e no primeiro dia de meses consecutivos e na virada de dezembro para janeiro; verificar o mês inicial com uma data controlada no teste.
  - **Risco:** comparar apenas o número do mês, misturar anos ou deslocar datas por fuso.

- [ ] **B20 — Filtrar as despesas por categoria**
  - **Objetivo:** combinar a categoria escolhida com o mês consultado.
  - **Dependências:** B19.
  - **Aceitação:** selecionar uma categoria restringe os registros do mês; a opção “Todas as categorias” remove somente essa restrição. Ausência de resultados não sugere que todos os dados foram apagados.
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
  - **Objetivo:** manter a consulta coerente com os dados salvos, sem recarregar manualmente a página.
  - **Dependências:** B16, B18, B21, B22.
  - **Aceitação:** cadastro, edição e exclusão atualizam lista, total filtrado e resumo mensal após persistência bem-sucedida, preservando os filtros selecionados.
  - **Verificação:** cadastrar no mês selecionado, editar data e categoria para sair do filtro e excluir um registro; conferir todos os resultados e simular uma gravação malsucedida.
  - **Risco:** atualizar apenas uma parte da tela ou apresentar uma alteração não persistida.

## Marco 5 — Cópia de segurança

- [ ] **B24 — Exportar as despesas em JSON**
  - **Objetivo:** permitir guardar uma cópia dos dados fora do armazenamento do navegador.
  - **Dependências:** B11.
  - **Aceitação:** uma ação explícita gera um arquivo JSON com a versão do formato e todos os registros, sem depender dos filtros ativos. A exportação não altera os dados atuais.
  - **Verificação:** exportar uma coleção conhecida, conferir campos e quantidade, repetir com coleção vazia e com um filtro que oculta parte dos registros.
  - **Risco:** produzir uma cópia incompleta ou perder identificadores, centavos ou datas.

- [ ] **B25 — Validar um arquivo antes da restauração**
  - **Objetivo:** verificar integralmente a cópia antes de permitir qualquer substituição.
  - **Dependências:** B24.
  - **Aceitação:** aceitar apenas o formato e a versão suportados, com registros válidos segundo as regras compartilhadas e identificadores únicos. JSON inválido, versão desconhecida ou qualquer registro inválido rejeitam o arquivo inteiro sem alterar dados atuais.
  - **Verificação:** testar uma cópia válida, arquivo malformado, versão incompatível, campo ausente, identificadores repetidos, valor inválido, categoria desconhecida e data impossível.
  - **Risco:** confiar no arquivo importado ou aplicar uma restauração parcial antes de terminar a validação.

- [ ] **B26 — Restaurar os dados com confirmação**
  - **Objetivo:** substituir os registros atuais por uma cópia integralmente validada.
  - **Dependências:** B25.
  - **Aceitação:** informar que os dados atuais serão substituídos e apresentar a quantidade de registros da cópia. Cancelar preserva tudo; confirmar substitui os dados e atualiza a tela somente após gravação bem-sucedida. Não mesclar coleções.
  - **Verificação:** restaurar a exportação de B24, recarregar e comparar os registros; testar cancelamento, falha de gravação e uma cópia vazia válida, que também exige confirmação.
  - **Risco:** perda dos registros atuais por substituição não confirmada ou falha tratada como sucesso.

## Marco 6 — Qualidade e fechamento do MVP

- [ ] **B27 — Adaptar formulários, lista e resumo ao celular**
  - **Objetivo:** revisar o uso responsivo dos fluxos já implementados.
  - **Dependências:** B23, B26.
  - **Aceitação:** campos, valores, filtros, ações e confirmações ficam legíveis e utilizáveis em telas pequenas, sem conteúdo essencial cortado nem rolagem horizontal da página.
  - **Verificação:** percorrer cadastro, consulta, edição, exclusão e backup em larguras de referência de 360, 768 e 1280 pixels; conferir também descrições longas e valores maiores.

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
  - **Verificação:** executar os testes disponíveis e o roteiro completo com dados de teste, incluindo centavos, limites de mês/ano e falhas de armazenamento. Para cada falha corrigida, acrescentar uma verificação que detecte sua repetição quando adequado.
  - **Risco:** validar apenas funções isoladas e deixar inconsistências entre armazenamento, lista e totais.

- [ ] **B30 — Atualizar a documentação e revisar o aprendizado**
  - **Objetivo:** encerrar o MVP com instruções atuais, evidências e uma revisão ativa.
  - **Dependências:** B29.
  - **Aceitação:** documentação reflete os comandos reais, funcionalidades, uso local, exportação/restauração, limitações conhecidas e verificações executadas; o backlog marca apenas tarefas realmente concluídas.
  - **Verificação:** seguir a documentação e responder: por que guardar dinheiro em centavos? Como evitar mudança do dia por fuso? Por que validar a cópia inteira antes de substituir os dados? Registrar também uma dificuldade e uma decisão que você consegue explicar sem ajuda.

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
- Banco de dados remoto e sincronização entre dispositivos.
- Compartilhamento de despesas entre pessoas.
- Integrações com bancos, cartões ou serviços financeiros.
- Publicação online, configuração de hospedagem e deploy.

Adicionar qualquer um desses itens exige revisar o escopo e planejar suas próprias tarefas. Este backlog não autoriza instalações, mudanças no Git, implementação da aplicação, operações externas ou deploy.

## Próxima microtarefa

**B01 — Comparar alternativas e escolher a tecnologia.** Primeiro, listar o que você já conhece e comparar alternativas compatíveis com o MVP; depois, registrar a escolha e os comandos previstos. Não iniciar automaticamente B02 ou a implementação.

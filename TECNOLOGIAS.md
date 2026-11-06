# Tecnologias escolhidas — Controle de despesas pessoais

Decisão registrada em **06/11/2026**.

## Escolha para o MVP

O projeto utilizará **Python + Django**, **SQLite**, **HTML e CSS** e as **ferramentas de testes do Django**. MVP é a primeira versão pequena e útil da aplicação.

| Tecnologia | Responsabilidade | Documentação |
| --- | --- | --- |
| **Python + Django** | Implementar regras de negócio, validar formulários e gerar as páginas HTML. | [Visão geral do Django](https://docs.djangoproject.com/en/stable/intro/overview/) |
| **SQLite** | Guardar despesas em um arquivo de banco de dados, sem precisar de um serviço de banco separado. | [SQLite na documentação do Python](https://docs.python.org/3/library/sqlite3.html) |
| **HTML e CSS** | Construir telas acessíveis e adaptadas ao computador e ao celular. | — |
| **Testes do Django** | Testar regras, formulários e persistência usando ferramentas integradas ao framework. | [Escrita e execução de testes no Django](https://docs.djangoproject.com/en/stable/topics/testing/overview/) |

## Justificativa

O desenvolvedor possui uma base maior em Python do que em JavaScript. A escolha aproveita esse conhecimento e permite concentrar o aprendizado nos conceitos de desenvolvimento web.

Django reúne recursos para trabalhar com páginas, formulários, banco de dados e testes. HTML e CSS serão usados para construir a interface apresentada pelo navegador.

## Funcionamento previsto

- O navegador apresenta as páginas HTML e CSS geradas pelo Django.
- Django executa em um servidor local: um programa Python em execução que recebe as solicitações do navegador, aplica as regras e devolve as páginas.
- As despesas são persistidas em um arquivo SQLite no computador que executa a aplicação.
- A exportação e a restauração em JSON continuam como funcionalidades previstas no MVP.
- Para usar a aplicação pelo celular, o computador que executa Django precisa estar ligado e acessível ao celular, com o acesso pela rede devidamente configurado.

## Impacto sobre o backlog existente

Esta decisão substitui a proposta anterior de persistir as despesas no `localStorage` e executar toda a aplicação no navegador.

O arquivo [BACKLOG.md](BACKLOG.md) ainda descreve a arquitetura anterior e precisa ser revisado para refletir Django e SQLite, especialmente nas tarefas de preparação, persistência, tratamento de falhas e testes. Essa revisão é uma etapa posterior a este registro.

As versões das ferramentas e os comandos de preparação, inicialização e testes serão definidos e verificados nas próximas etapas.

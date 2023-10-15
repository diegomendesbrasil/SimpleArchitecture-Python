## Projeto XPTO - Guia do Repositório

Este arquivo tem como objetivo auxiliá-lo na navegação pelos repositórios do projeto, tornando mais simples o entendimento do que foi criado para este processo. O repositório está organizado da seguinte forma:

1. **Pasta Arquitetura:** Contém a apresentação da arquitetura proposta para implementação na empresa.
2. **Pasta Scripts:** Contém os scripts SQL que devem ser executados para criar as tabelas e procedures relacionadas ao Desafio 2.
3. **Pasta Imagens:** Contém as imagens usadas neste README.
4. **Arquivos 00_import_files.py e connect_api.py:** Fazem parte dos artefatos do Projeto 2.

A organização para o desenvolvimento deste desafio foi totalmente gerenciada no Trello em formato de tarefas. Cada tarefa representa uma user story, e dentro delas, temos verificações que representam as tarefas concluídas para aquela história.

<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/diegomendesbrasil/gavb/blob/master/image/Trello.png" alt="Logo do Projeto">
  </a>
</p>

## Desafio 2 - Organização

Neste Desafio 2, utilizei Databricks para a execução do código Python e Azure SQL para a persistência das informações no banco de dados. Para que tudo funcione perfeitamente, siga as etapas abaixo:

1. Acesse a pasta "Scripts" e execute a criação das tabelas SQL, bem como o script de criação de procedimentos.
2. Realize o clone deste projeto no Databricks e execute na seguinte ordem:
    2.1. **Script 00_import_files.py:** Faça o upload dos arquivos para o repositório do Databricks no DBFS ("/dbfs/FileStore"). Em seguida, execute o script que importará os arquivos e fará a carga no banco de dados.

Abaixo, está a organização do processo de execução deste item.

<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/diegomendesbrasil/gavb/blob/master/image/files_arquitetura.png" alt="Logo do Projeto">
  </a>
</p>

3. **Script connect_api.py:** Ao executar este script, você coletará os dados do Twitter com base na variável preestabelecida e fará a carga na tabela de tweets.

A organização desta arquitetura ficou da seguinte maneira:

<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/diegomendesbrasil/gavb/blob/master/image/twitter_arquitetura_final.png" alt="Logo do Projeto">
  </a>
</p>

Por favor, sinta-se à vontade para fazer melhorias adicionais ou esclarecer mais detalhes, se necessário.

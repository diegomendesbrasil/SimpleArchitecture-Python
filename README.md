## Projeto XPTO
<div align="center">

</div>
Este arquivo visa auxiliá-los na navegação nos repositórios do projeto para facilitar o entendimento do que foi criado para esse processo.
O repositório está organizado da seguinte maneira:

<b></b>
 
 1. Pasta Arquitetura > contém a apresentação da arquitetura que será proposta para implementação na empresa.
 2. Pasta Scripts > Contém os scripts sql que devem ser executados para criação das tabelas e procedures que fazem parte do desafio 2.
 3. Pasta Image > Contém as Imagens que estou utilizando nesse README
 4. Arquivo 00_import_files.py e conect_api.py > fazem parte dos artefatos do projeto 2.
 
 A organização para desenvolvimento desse desafio foi totalmente feita no trello em formato de tasks, cada task representa uma user story e dentro delas temos checks que representam as tasks entregues para aquela story.
 
<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/diegomendesbrasil/gavb/blob/master/image/Trello.png" alt="Project logo">
 </a>
</p>

## Desafio 2 - Organização
<div align="center">

Para o desafio 2 utilizei databricks para execução do código python e azure sql para persistência das informações no banco de dados, para que tudo rode perfeitamente você deverá:

1. Acessar a pasta scripts e executar a criação das tabelas SQL e também o script de criação de procedure
2. Realizar o clone desse projeto no databricks e executar na seguinte ordem:
  2.1. Script 00_import_files.py<b></b>
    <b></b>Suba os arquivos para o repositório do databricks no dbfs "/dbfs/FileStore"<b></b>
    <b></b>Execute o script que realizará a importação dos arquivos e carga no banco de dados<b></b>
<b></b>Abaixo está a organização do processo de execução desse item.
    
 <p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/diegomendesbrasil/gavb/blob/master/image/files_arquitetura.png" alt="Project logo">
 </a>
</p>

3. Script conect_api.py<b></b>
  Ao executar esse script você coletará os dados do twiiter com base na variável pre-estabelecida e a carga na tabela de twiites será realizada.
<b></b>A organização desse arquitetura ficou da seguinte maneira:

   <p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/diegomendesbrasil/gavb/blob/master/image/twiiter_arquitetura_final.png" alt="Project logo">
 </a>
</p>

  
  


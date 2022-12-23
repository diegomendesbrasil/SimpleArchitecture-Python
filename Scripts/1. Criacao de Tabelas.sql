--- CRIANDO STG PARA RECEBER OS VALORES DOS ARQUIVOS EXCEL
create schema stg
create schema consume

create table stg.stg_vendas (
	id_marca int,
	marca varchar(100),
	id_linha int,
	linha varchar(100),
	data_venda date,
	qtd_venda int
)

--- CRIANDO TABELAS DE CONSUMO
create schema consume

create table consume.tab_vendas_anomes (
	per_venda varchar(7) not null,
	qtd_venda int not null
)
;
create table consume.tab_vendas_marca_linha (
	ds_marca varchar(100) not null,
	ds_linha varchar(100) not null,
	qtd_venda int not null
)
;
create table consume.tab_vendas_marca_anomes (
	ds_marca varchar(100) not null,
	per_venda varchar(7) not null,
	qtd_venda int not null
)
;
create table consume.tab_vendas_linha_anomes (
	ds_linha varchar(100) not null,
	per_venda varchar(7) not null,
	qtd_venda int not null
)
;

CREATE TABLE [consume].[tab_twitterApi](
	[User] [varchar](50) NOT NULL,
	[Texto] [varchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO





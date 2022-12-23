CREATE PROCEDURE sp_tab_vendas_anomes
AS

MERGE consume.tab_vendas_anomes AS Destino USING
  (SELECT convert(char(7), data_venda, 102) AS mes_ano,
          sum(qtd_venda) AS qtd_vendas
   FROM stg.stg_vendas stg
   GROUP BY convert(char(7), data_venda, 102)) Origem ON (Destino.per_venda = Origem.mes_ano) 
WHEN MATCHED THEN
UPDATE
SET Destino.qtd_venda = Origem.qtd_vendas WHEN NOT MATCHED THEN
INSERT
VALUES (Origem.mes_ano,Origem.qtd_vendas);

;

CREATE PROCEDURE sp_tab_vendas_marca_linha
AS

MERGE consume.tab_vendas_marca_linha AS Destino USING
	(select 
			marca as ds_marca,
			linha as ds_linha,
			sum(qtd_venda) as qtd_vendas 
		from 
			stg.stg_vendas
				group by marca,linha
		) Origem ON (Destino.ds_marca = Origem.ds_marca and Destino.ds_linha = Origem.ds_linha) 
WHEN MATCHED THEN
	UPDATE
		SET Destino.qtd_venda = Origem.qtd_vendas 
WHEN NOT MATCHED THEN
INSERT
VALUES (Origem.ds_marca,Origem.ds_linha,Origem.qtd_vendas);

;

CREATE PROCEDURE sp_tab_vendas_marca_anomes
AS

MERGE consume.tab_vendas_marca_anomes AS Destino USING
	(select 
		marca as ds_marca,
		convert(char(7),data_venda,102) as mes_ano,
		sum(qtd_venda) as qtd_vendas 
	from 
		stg.stg_vendas
	group by marca,convert(char(7),data_venda,102)
		) Origem ON (Destino.ds_marca = Origem.ds_marca and Destino.per_venda = Origem.mes_ano) 
WHEN MATCHED THEN
	UPDATE
		SET Destino.qtd_venda = Origem.qtd_vendas 
WHEN NOT MATCHED THEN
INSERT
VALUES (Origem.ds_marca,Origem.mes_ano,Origem.qtd_vendas);

;

CREATE PROCEDURE sp_tab_vendas_linha_anomes
AS

MERGE consume.tab_vendas_linha_anomes AS Destino USING
	(select 
		linha as ds_linha,
		convert(char(7),data_venda,102) as mes_ano,
		sum(qtd_venda) as qtd_vendas 
	from 
		stg.stg_vendas
	group by linha,convert(char(7),data_venda,102)
		) Origem ON (Destino.ds_linha = Origem.ds_linha and Destino.per_venda = Origem.mes_ano) 
WHEN MATCHED THEN
	UPDATE
		SET Destino.qtd_venda = Origem.qtd_vendas 
WHEN NOT MATCHED THEN
INSERT
VALUES (Origem.ds_linha,Origem.mes_ano,Origem.qtd_vendas);


;

Create procedure sp_exec_carga 
AS

Exec sp_tab_vendas_anomes;
Exec sp_tab_vendas_marca_linha;
Exec sp_tab_vendas_marca_anomes;
Exec sp_tab_vendas_linha_anomes


from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, MetaData, Float, Integer,ForeignKey,DateTime, Boolean, String, Column
from datetime import datetime


from config import mssq_datawharehouselocal

engine = mssq_datawharehouselocal()
metadata = MetaData()
metadata_obj = MetaData(schema="extracoes")



google_shopping = Table(
    "google_shopping",
metadata,
Column('cod_ambiente',Integer,primary_key=True),
Column('ref_produto',Integer),
Column('cod_barras',String),
Column('ref_categoria',Integer),
Column('ref_marca',Integer),
Column('preco_custo',Float),
Column('preco_venda',Float),
Column('nome_produto',String),
Column('preco_custo',Float),
Column('nome_concorrente',String),
Column('loja_venda',String),
Column('url_loja',String),
Column('preco_concorrente',Float),
Column('url_google',String),
Column('diferenca_preco',Float),
Column('canal_venda',String),
Column('data_atualizacao',DateTime),
Column('categoria',String),
Column('marca',String)
,schema="extracoes",implicit_returning=False,extend_existing=True)



url_base_seller_ecommerce = Table(
    "url_base_seller_ecommerce",
     metadata,
    Column('cod_url',Integer,primary_key=True),
    Column('cod_google',String),
    Column('cod_loja',Integer),
    Column('ref_categoria',Integer),
    Column('url_coleta',String),
    Column('url_base',String),
    Column('cod_barras', String),
    Column('ref_produto',String),
    Column('codigoFabricante',String),
    Column('data_atualizado',DateTime)
   
,schema="extracoes",extend_existing=True)



urls_franquia = Table(
    "url_base_franquia",
metadata,
Column('cod_anuncio',Integer,primary_key=True),
Column('id_franquia',Integer),
Column('url_anuncio',String),
Column('url_base',String),
Column('categoria',String),
Column('faixa_preco',String),
Column('nome_franquia',String),
Column('data_atualizacao',DateTime),
schema="extracoes",implicit_returning=False,extend_existing=True)



atributos_franchising = Table(
    "atributos_franchising",
    metadata,
    Column('id',Integer, primary_key=True),
    Column('id_franquia',Integer),
    Column('nome',String),
    Column('investimento_minimo',Float),
    Column('url',String),
    Column('total_unidades',Integer),
    Column('retorno',String),
    Column('sede',String),
    Column('atributos',String),
    Column('data_atualizacao',DateTime),
    Column('uf',String),
    Column('site_franquia',String),
    Column('regiao',String),
    Column('quantidade_loja',Integer),
    Column('tipo_loja',String),
    schema="extracoes",implicit_returning=False,extend_existing=True)



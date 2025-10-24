from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from geoalchemy2 import Geography
from models.transform import WGS_EPSG

Base = declarative_base()

class Bairros(Base):
    __tablename__ = 'bairros'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(Integer, nullable=False, default=0)
    tipo = Column(String(80), nullable=False, default='Bairro')
    name = Column(String(100), nullable=False, default='Sem nome')
    geom = Column(Geography(geometry_type='POLYGON', srid=WGS_EPSG, nullable=False))
    area_km2 = Column(Float(3), nullable=False, default=0)
    perimeter = Column(Float(3), nullable=False, default=0)
    
class PontoOnibus(Base):
    __tablename__ = 'ponto_onibus'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_linha = Column(String(10), nullable=False, default="NA")
    nome_linha = Column(String(100), nullable=False, default='Sem nome')
    nome_sub = Column(String(100), nullable=False, default='Sem nome')
    origem = Column(String(100), nullable=True)
    geom = Column(Geography(geometry_type='POINT', srid=WGS_EPSG, nullable=False))
    
class AtividadeEconomica(Base):
    __tablename__ = 'atividade_economica'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column(String())
    cnae_principal = Column(Integer, nullable=False)
    cnae_desc = Column(String(300), nullable=False, default='Sem descrição')
    data_inicio = Column(Date, nullable=False)
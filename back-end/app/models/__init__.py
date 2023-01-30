import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.database import db
from sqlalchemy_serializer import SerializerMixin

class Cnab(db.Model,SerializerMixin):
    __tablename__ = "cnab"

    id = sa.Column(sa.Integer,primary_key=True)
    data = sa.Column(sa.String)
    valor = sa.Column(sa.String)
    cpf = sa.Column(sa.String)
    cartao = sa.Column(sa.String)
    hora = sa.Column(sa.String)
    dono_da_loja = sa.Column(sa.String)
    nome_da_loja = sa.Column(sa.String)
    tipo_id = sa.Column(sa.Integer,sa.ForeignKey("tipo.id"))
    tipo = relationship("Tipo",cascade="all")

class Tipo(db.Model,SerializerMixin):
    __table_name__ = "tipo"

    id = sa.Column(sa.Integer,primary_key=True)
    descricao = sa.Column(sa.String)
    sinal = sa.Column(sa.String)
    natureza = sa.Column(sa.String)

    def __init__(self,descricao,sinal,natureza) -> None:
        self.descricao = descricao
        self.sinal = sinal
        self.natureza = natureza
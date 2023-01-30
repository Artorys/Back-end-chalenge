from app.server import db
from app.models import Cnab,Tipo
from app.utils.populate_type import TIPOS

def cnab_post_service(data : dict):
    tipo_id = data["tipo"]

    for tipo in TIPOS:
        id = tipo.get("id")
        if(id == int(tipo_id)):
            tipo = db.session.query(Tipo).filter_by(id=id).first()
            data["tipo"] = tipo

    cnab = db.session.query(Cnab).filter_by(**data).first()
    if(not cnab):
        cnab = Cnab(data=data["data"],valor=data["valor"],cpf=data["cpf"],cartao=data["cartao"],hora=data["hora"],dono_da_loja=data["dono_da_loja"],nome_da_loja=data["nome_da_loja"],tipo=data["tipo"])
    db.session.add(cnab)
    db.session.commit()

def cnab_get_service():
    list = []
    cnabs = Cnab.query.all()
    for cnab in cnabs:
        list.append(cnab.to_dict())
    return list
    
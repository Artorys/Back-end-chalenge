from sqlalchemy import inspect

TIPOS =  [{
        "id" : 1,
        "descricao" : "debito",
        "sinal" : "+" ,
        "natureza" : "entrada"
        },
        {
        "id" : 2,
        "descricao" : "boleto",
        "sinal" : "-" ,
        "natureza" : "saida"
        },
        {
        "id" : 3,
        "descricao" : "financiamento",
        "sinal" : "-" ,
        "natureza" : "saida"
        },
        {
        "id" : 4,
        "descricao" : "credito",
        "sinal" : "+" ,
        "natureza" : "entrada"
        },
        {
        "id" : 5,
        "descricao" : "recebimento emprestimo",
        "sinal" : "+" ,
        "natureza" : "entrada"
        },
          {
        "id" : 6,
        "descricao" : "vendas",
        "sinal" : "+" ,
        "natureza" : "entrada"
        },
        {
        "id" : 7,
        "descricao" : "recebimento TED",
        "sinal" : "+" ,
        "natureza" : "entrada"
        },
         {
        "id" : 8,
        "descricao" : "recebimento DOC",
        "sinal" : "+" ,
        "natureza" : "entrada"
        },
         {
        "id" : 9,
        "descricao" : "aluguel",
        "sinal" : "-" ,
        "natureza" : "saida"
        },]

def populate_type(db,instance):
    inspector = inspect(db.engine)
    if(inspector.has_table("tipo")):
        for tipo in TIPOS:
       
          descricao = tipo["descricao"]
          sinal = tipo["sinal"]
          natureza = tipo["natureza"]

          tipo = db.session.query(instance).filter_by(**tipo).first()
          if(not tipo):
              tipo = instance(descricao=descricao,natureza=natureza,sinal=sinal)
          db.session.add(tipo)
          db.session.commit()
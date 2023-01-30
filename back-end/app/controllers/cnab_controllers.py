from app.services.cnab_services import cnab_get_service,cnab_post_service
from flask import request
from werkzeug.utils import secure_filename
from app.config import ALLOWED_EXTENSIONS,UPLOAD_FOLDER
import os

def check_extesions(filename:str):
    if("." in filename):
       return filename.rsplit(".")[1] in ALLOWED_EXTENSIONS

    return False

def cnab_post_controller():
    file = request.files

    if(not "cnab" in file):
        print(file)
        return {"message" : "Only cnab file"}, 400

    file = file["cnab"]
    if(check_extesions(file.filename) == False):
        return {"message" : "Only cnab.txt file"}

    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER,filename)
    file.save(path)
    cnabList = []
    with open(path,"r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n","")
            cnabList.append(line)
    for cnab in cnabList:
        tipo = cnab[0]
        data = cnab[1:9]
        valor = cnab[9:19]
        cpf = cnab[19:30]
        cartao = cnab[30:42]
        hora = cnab[42:48]
        dono_da_loja = cnab[48:62]
        nome_da_loja = cnab[62:81]
        data = {
            "tipo" : tipo,
            "data" : data,
            "valor" : valor,
            "cpf" : cpf,
            "cartao" : cartao,
            "hora" : hora,
            "dono_da_loja" : dono_da_loja,
            "nome_da_loja" : nome_da_loja,
        }
        cnab_post_service(data)
        
    return {"message" : "Upload has successfully"}

    
def cnab_get_controller():

    cnab = cnab_get_service()
    return cnab,200
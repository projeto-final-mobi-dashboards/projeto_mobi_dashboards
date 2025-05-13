from flask import Blueprint, Response, stream_with_context,jsonify
from models import Usuarios,Itinerario,Trecho,Enderecos
from time import sleep
from json import dumps

sent_eventBlueprint=Blueprint("SSE",__name__)



def get_contagem_atual(classe):
    return classe.query.count() # query com o count de usuarios

@sent_eventBlueprint.route("/refreshEvent", methods=["GET","POST"])
def sent_event():
    #Pega a contagem de registros na tabela no inicio da aplicação
    count_usuarios = Usuarios.query.count()
    count_itinerarios = Itinerario.query.count()
    count_enderecos = Enderecos.query.count()
    count_trechos = Trecho.query.count()

    def evento(): # informação no artigo deste link https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56
        nonlocal count_usuarios,count_itinerarios,count_enderecos,count_trechos

        while True:
            usuarios_atuais=get_contagem_atual(Usuarios) # o nome da função diz oq faz, eu deveria separar isso numa função get_data
            itinerarios_atuais=get_contagem_atual(Itinerario)
            enderecos_atuais=get_contagem_atual(Enderecos)
            trechos_atuais=get_contagem_atual(Trecho)

            if( # se a contagem original for diferente da contagem em outro momento da aplicação deve ter ocorrido mudança, faz sentido na minha cabeça
                count_usuarios !=usuarios_atuais    
                or count_itinerarios != itinerarios_atuais  
                or count_enderecos != enderecos_atuais 
                or count_trechos != trechos_atuais
               ):
                
                count_usuarios=usuarios_atuais # atualiza as contagens anteriores
                count_itinerarios=itinerarios_atuais
                count_enderecos=enderecos_atuais
                count_trechos=trechos_atuais
                data = dumps({"update":"True"})
                yield f"data:{data}\n\n" #captura o valor sem quebrar da iteração/função, estudar mais disso

            sleep(10) # tempo entre cada checagem ao banco        

    return Response(stream_with_context(evento()), mimetype='text/event-stream' ) # retorna a resposta quando ter um valor
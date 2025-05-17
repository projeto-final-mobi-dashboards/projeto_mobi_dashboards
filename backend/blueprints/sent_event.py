from flask import Blueprint, Response, stream_with_context,current_app,jsonify
from models import Usuarios,Itinerario,Trecho,Enderecos,engine
from sqlalchemy.orm import Session
from time import sleep
from json import dumps
# Para testes deste arquivo curl -N http://127.0.0.1:5000/refreshEvent
sent_eventBlueprint=Blueprint("SSE",__name__)




@sent_eventBlueprint.route("/refreshEvent", methods=["GET"])
def sent_event(): 

    def evento(): # informação no artigo deste link https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56
        first_loop=True
        with Session(engine) as session: # conta os usuarios
            count_usuarios = None
            count_itinerarios = None
            count_enderecos = None
            count_trechos = None


        while True:
            with current_app.app_context():
                with Session(engine) as session:
                    # dados iniciais do banco
                    usuarios_atuais=session.query(Usuarios).count() 
                    itinerarios_atuais=session.query(Itinerario).count()
                    enderecos_atuais=session.query(Enderecos).count()
                    trechos_atuais=session.query(Trecho).count()


                    if first_loop:
                        # Seta os dados da contagem "anterior no primeiro loop"
                        count_usuarios=usuarios_atuais
                        count_itinerarios=itinerarios_atuais
                        count_enderecos=enderecos_atuais
                        count_trechos=trechos_atuais
                        first_loop=False

                    else:
                        print(f"\ncount_atual:{usuarios_atuais} \ncount_anterior:{count_usuarios}") # mostra a contagem

                        if( # Compara, se for diferente
                            count_usuarios !=usuarios_atuais    
                            or count_itinerarios != itinerarios_atuais  
                            or count_enderecos != enderecos_atuais 
                            or count_trechos != trechos_atuais
                        ):
                            print(f'\nMudança percebida')

                            #atualiza a anterior com atual
                            count_usuarios=usuarios_atuais
                            count_itinerarios=itinerarios_atuais
                            count_enderecos=enderecos_atuais
                            count_trechos=trechos_atuais



                            data = dumps({"update": True})
                            yield f"data:{data}\n\n" #captura o valor sem quebrar da iteração/função e bota pra enviar ele
                        else: 
                            print("\nsem mudanças detectadas")

            sleep(10) # tempo entre cada checagem ao banco        
    headersSSE={
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",        
    }
    return Response(stream_with_context(evento()), headers=headersSSE ) # retorna a resposta quando ter um valor
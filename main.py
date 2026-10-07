from fastapi import FastAPI, HTTPException
from schemas import Chamado, ChamadoStatus, ChamadoResposta
from services import (
    obter_chamados, 
    criar_chamado, 
    consultar_chamado, 
    alterar_status, 
    deletar_chamado_service
)

app = FastAPI()
@app.get("/chamados", response_model=list[ChamadoResposta])
def listar_chamados_api():
    return obter_chamados()
    
@app.post("/chamados")
def criar_chamado_api(chamado: Chamado):
    return criar_chamado(chamado)
    
@app.get("/chamados/{id_chamado}")
def consultar_chamado_api(id_chamado: int):
   chamado = consultar_chamado(id_chamado)
   if chamado is None:
       raise HTTPException(
        status_code=404,
        detail="Chamado não encontrado."
        )
   return chamado

@app.put("/chamados/{id_chamado}/status")
def alterar_status_api(id_chamado: int, status: ChamadoStatus):

    chamado = alterar_status(id_chamado, status.status)

    if chamado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )

    return chamado

@app.delete("/chamados/{id_chamado}")
def deletar_chamado_api(id_chamado: int):

    resultado = deletar_chamado_service(id_chamado)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )

    return {"message": "Chamado deletado com sucesso."}
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
    
@app.post("/chamados", status_code=201, response_model=ChamadoResposta)
def criar_chamado_api(chamado: Chamado):
    try:    
        return criar_chamado(chamado)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao criar chamado: {e}"
        )

    
@app.get("/chamados/{id_chamado}", response_model=ChamadoResposta)
def consultar_chamado_api(id_chamado: int):
   chamado = consultar_chamado(id_chamado)
   if chamado is None:
       raise HTTPException(
        status_code=404,
        detail="Chamado não encontrado."
        )
   return chamado

@app.put("/chamados/{id_chamado}/status",response_model=ChamadoResposta)
def alterar_status_api(id_chamado: int, status: ChamadoStatus):
    try:
        resultado = alterar_status(id_chamado, status.status)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao alterar status do chamado: {e}"
        )
    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )
    return resultado

@app.delete("/chamados/{id_chamado}", status_code=204)
def deletar_chamado_api(id_chamado: int):
    try:
        resultado = deletar_chamado_service(id_chamado)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao deletar chamado: {e}"
        )
    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )
    


from fastapi import FastAPI, HTTPException
from backend.schemas import Chamado, ChamadoStatus, ChamadoResposta
from fastapi.middleware.cors import CORSMiddleware
from backend.services import (
    obter_chamados, 
    criar_chamado, 
    consultar_chamado, 
    alterar_status, 
    deletar_chamado_service
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/chamados/estatisticas")
def obter_estatisticas():
    chamados = obter_chamados()

    total_chamados = len(chamados)

    total_abertos = sum(
        1 for chamado in chamados
        if chamado["status"] == "Aberto"
    )

    total_em_andamento = sum(
        1 for chamado in chamados
        if chamado["status"] == "Em andamento"
    )

    total_concluidos = sum(
        1 for chamado in chamados
        if chamado["status"] == "Concluído"
    )

    return {
        "total_chamados": total_chamados,
        "total_abertos": total_abertos,
        "total_em_andamento": total_em_andamento,
        "total_concluidos": total_concluidos
    }

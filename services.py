from banco import (
    listar_chamados,
    inserir_chamado,
    deletar_chamado,
    buscar_chamado_por_id, 
    alterar_status as alterar_status_banco
)

def obter_chamados():
    chamados = listar_chamados()
    return [{
        "id": chamado[0],
        "nome": chamado[1],
        "descricao": chamado[2],
        "categoria": chamado[3],
        "status": chamado[4]
    } for chamado in chamados]

def criar_chamado(chamado):
    id_chamado = inserir_chamado(
        nome=chamado.nome,
        descricao=chamado.descricao,
        categoria=chamado.categoria,
        status="Aberto"
    )

    return {
        "id": id_chamado,
        "nome": chamado.nome,
        "descricao": chamado.descricao,
        "categoria": chamado.categoria,
        "status": "Aberto"
    }

def consultar_chamado(id_chamado):
    chamado = buscar_chamado_por_id(id_chamado)
    if chamado is None:
        return None
    return {
        "id": chamado[0],
        "nome": chamado[1],
        "descricao": chamado[2],
        "categoria": chamado[3],
        "status": chamado[4]
    }

def deletar_chamado_service(id_chamado):

    resultado = deletar_chamado(id_chamado)
    if resultado is False:
        return None
    
    return True

def alterar_status(id_chamado, novo_status):
    resultado = alterar_status_banco(id_chamado, novo_status)
    if resultado is False:
        return None
    chamado_atualizado = buscar_chamado_por_id(id_chamado)
    return {
        "id": chamado_atualizado[0],
        "nome": chamado_atualizado[1],
        "descricao": chamado_atualizado[2],
        "categoria": chamado_atualizado[3],
        "status": chamado_atualizado[4]
    }

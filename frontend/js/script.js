let totalChamados = 0;
let andamentoChamados = 0;
let finalizadosChamados = 0;

async function atualizarEstatisticas() {
    const resposta = await fetch('http://127.0.0.1:8000/chamados/estatisticas');
    const estatisticas = await resposta.json();

    if (resposta.ok) {
        totalChamados = estatisticas.total_chamados;
        andamentoChamados = estatisticas.total_em_andamento;
        finalizadosChamados = estatisticas.total_concluidos;

        document.getElementById('totalChamados').innerText = totalChamados;
        document.getElementById('chamadosAndamento').innerText = andamentoChamados;
        document.getElementById('chamadosConcluidos').innerText = finalizadosChamados;
    } else {
        console.error('Erro ao atualizar estatísticas:', estatisticas.detail);
    }
}

const formulario = document.getElementById('criarChamadoForm');

formulario.addEventListener('submit', async (event) => {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const categoria = document.getElementById('categoria').value;

    const dados = {
        nome: nome,
        descricao: descricao,
        categoria: categoria
    };

    const resposta = await fetch('http://127.0.0.1:8000/chamados', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();

    if (resposta.ok) {
        document.getElementById('resultadoCriacao').innerText =
            'Chamado criado com sucesso!';

        formulario.reset();
        atualizarEstatisticas();
    } else {
        document.getElementById('resultadoCriacao').innerText =
            'Erro ao criar chamado: ' + resultado.detail;
    }
});


const listarChamadosBtn = document.getElementById('listarChamadosBtn');
const listaChamadosDiv = document.getElementById('resultadoListagem');

listarChamadosBtn.addEventListener('click', async () => {
    const resposta = await fetch('http://127.0.0.1:8000/chamados');
    const chamados = await resposta.json();

    if (resposta.ok) {
        let html = '<ul>';

        for (const chamado of chamados) {
            html += `
                <li>
                    <strong>ID:</strong> ${chamado.id} <br>
                    <strong>Nome:</strong> ${chamado.nome} <br>
                    <strong>Descrição:</strong> ${chamado.descricao} <br>
                    <strong>Categoria:</strong> ${chamado.categoria} <br>
                    <strong>Status:</strong> ${chamado.status}
                </li>
            `;
        }

        html += '</ul>';
        listaChamadosDiv.innerHTML = html;
    } else {
        listaChamadosDiv.innerHTML = 'Erro ao listar chamados.';
    }
});


const consultarChamadoForm = document.getElementById('consultarChamadoForm');
const resultadoConsulta = document.getElementById('resultadoConsulta');

consultarChamadoForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const id = document.getElementById('id_chamado').value;

    const resposta = await fetch(
        `http://127.0.0.1:8000/chamados/${id}`
    );

    const chamado = await resposta.json();

    if (resposta.ok) {
        resultadoConsulta.innerHTML = `
            <p><strong>ID:</strong> ${chamado.id}</p>
            <p><strong>Nome:</strong> ${chamado.nome}</p>
            <p><strong>Descrição:</strong> ${chamado.descricao}</p>
            <p><strong>Categoria:</strong> ${chamado.categoria}</p>
            <p><strong>Status:</strong> ${chamado.status}</p>
        `;
    } else {
        resultadoConsulta.innerHTML =
            'Erro ao consultar chamado: ' + chamado.detail;
    }
});


const atualizarStatusForm = document.getElementById('atualizarStatusForm');
const resultadoAtualizacao = document.getElementById('resultadoAtualizacao');

atualizarStatusForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const id = document.getElementById('id_chamado_status').value;
    const status = document.getElementById('novo_status').value;

    const resposta = await fetch(
        `http://127.0.0.1:8000/chamados/${id}/status`,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                status: status
            })
        }
    );

    const resultado = await resposta.json();

    if (resposta.ok) {
        resultadoAtualizacao.innerText =
            'Status atualizado com sucesso!';
        atualizarEstatisticas();
    } else {
        resultadoAtualizacao.innerText =
            'Erro ao atualizar status: ' + resultado.detail;
    }
});


const deletarChamadoForm = document.getElementById('deletarChamadoForm');
const resultadoDelecao = document.getElementById('resultadoDelecao');

deletarChamadoForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const id = document.getElementById('id_chamado_deletar').value;

    const resposta = await fetch(
        `http://127.0.0.1:8000/chamados/${id}`,
        {
            method: 'DELETE'
        }
    );

    if (resposta.ok) {
        resultadoDelecao.innerText =
            'Chamado deletado com sucesso!';

        deletarChamadoForm.reset();
        atualizarEstatisticas();
    } else {
        resultadoDelecao.innerText =
            'Erro ao deletar chamado.';
    }
});


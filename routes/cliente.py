from flask import Blueprint, render_template, request
from database.models.cliente import Cliente 

cliente_route = Blueprint('cliente', __name__)  

from flask import Blueprint, render_template

@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)
    

@cliente_route.route('/', methods=['POST']) 
def inserir_cliente(): 
    data = request.json 

    novo_usuario = Cliente.create(
        nome = data['nome'], 
        email =data['email']
        )
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>/editar')
def form_editar_cliente(cliente_id):
    cliente = Cliente.get(Cliente.id == cliente_id)
    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['POST'])
def atualizar_cliente(cliente_id):
        data = request.json
        cliente_editado = Cliente.get(Cliente.id == cliente_id)
        cliente_editado.nome = data['nome']
        cliente_editado.email = data['email']
        cliente_editado.save()
  
        return render_template('item_cliente.html', cliente=cliente_editado)
        

@cliente_route.route('/<int:cliente_id>/excluir', methods=['DELETE'])
def deletar_cliente(cliente_id):
    cliente_deletado = Cliente.get(cliente_id)
    cliente_deletado.delete_instance()
    return {'deleted': 'ok'}
dadosCliente ={
    'Nome':'Renan',
    'Endereço':'Rua Cruzeiro do Sul',
    'Telefone':'9999-9999'
}
print('Todos o dicionario',dadosCliente)
print('Valor da Key "Nome"\n',dadosCliente['Nome'])

dadosCliente['idade'] = 40

print('Adicionar Key idade e valor 40\n',dadosCliente)

dadosCliente.pop('Telefone',None)

print('Deletar key Telefone" \n',dadosCliente)

del dadosCliente['idade']

print('Deletar key e value idade \n',dadosCliente)

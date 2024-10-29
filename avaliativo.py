
def adicionar_produto(estoque_loja):
    nome_produto = input("Digite o nome do produto: ")
    quantidade_produto = int(input("Digite a quantidade do produto: "))
    valor_produto = float(input("Digite o valor do produto: "))

    estoque_loja[nome_produto] = {
        'quantidade': quantidade_produto,
        'valor': valor_produto
    }
    
    return estoque_loja

def visualizar_produto(estoque_loja):
    nome = input("Digite o nome do produto que deseja visualizar: ")

    if nome in estoque_loja:
        print("Produto:  ", nome ,estoque_loja[nome])
    
def vender_produto(estoque_loja, vendas):
    nome = input("Digite o nome do produto vendido: ")
    quantidade_vendida = int(input("Digite a quantidade vendida: "))
    
    if nome in estoque_loja:
        produto = estoque_loja[nome]
        if quantidade_vendida <= produto['quantidade']:
            produto['quantidade'] -= quantidade_vendida
            valor_total = quantidade_vendida * produto['valor']
            vendas.append({
                'nome': nome,
                'quantidade': quantidade_vendida,
                'valor_total': valor_total
            })
            print(f"Venda realizada: {quantidade_vendida} de '{nome}' por R$ {valor_total:.2f}.")
        else:
            print("Quantidade solicitada excede o estoque disponível.")
    else:
        print("Produto não encontrado.")

def relatorio_vendas(vendas):
    if not vendas:
        print("Não houve vendas realizadas.")
        return
    print("Relatório de Vendas:")
    for venda in vendas:
        print(f"Produto: {venda['nome']}, Quantidade: {venda['quantidade']}, Valor Total: R$ {venda['valor_total']:.2f}")


def main():
    estoque_loja = {}
    vendas = []

    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar Produto")
        print("2 - Buscar Produto")
        print("3 - Visualizar Produtos")
        print("4 - Vender Produto")
        print("5 - Relatório de Vendas")
        print("6 - Sair")
        
        escolha = input("Opção: ")
        
        if escolha == '1':
            adicionar_produto(estoque_loja)
        elif escolha == '2':
            visualizar_produto(estoque_loja)
        elif escolha == '3':
            print(estoque_loja)
        elif escolha == '4':
            vender_produto(estoque_loja, vendas)
        elif escolha == '5':
            relatorio_vendas(vendas)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

    
main()

catalogo = {}
carrinho = {}
total_comp = 0
nome = input("Digite seu nome: ")

print(f"\n Seja bem vindo ao nosso sitema {nome}, faça a seleção dos produtos que deseja compar. ")
menu = """
1 - Adicionar um ao catalogo
2 - Visualizar o catalogo de itens
3 - Editar a quantidade de itens do catálogo
4 - Editar valores no catálogo
5 - Pesquisa de produto no catálogo
6 - Remover um produto do catálogo
7 - Adicionar produtos no carrinho 
8 - Remover produtos do carrinho
9 - Ver produtos adicionados no carrinho
10 - Finalizar compras 
11 - Sair 
"""


def cadast_prod_cat():
    while True:
        menu = """
1 - Continuar para cadastro
2 - Cancelar    
    """
        op = input(menu)
        if op == "1":
            print("Cadastro de produtos no catálogo")
            produto = input("Digite o produto que será cadastrado: ")
            if produto in catalogo:
                print("O produto já se encontra presente no catálogo!")
                print("Deseja cadastrar outro produto?")
            else:
                quantidade = int(input(f"Informe a quantidade de {produto}: "))
                valor = float(input(f"Informe o valor de {produto}: "))
                catalogo[produto] = {"quantidade": quantidade,
                                     "valor": valor}
                print(f'O produto {produto} foi cadastrado com sucesso.')
                print(f"Seu catálogo agora contém os itens: {catalogo}")
        elif op == "2":
            print("Cancelando ação...")
            break
        else:
            print("Opção informada inválida")


def edit_quant_prod_cat():
    while True:
        menu = """
        1 - Continuar
        2 - Cancelar
        
        """
        op = input(menu)
        if op == "2":
            print("Cancelando..")
            break

        elif op == "1":

            produto = input("Informe o produto que terá sua quantidade editada no catálogo:")
            if produto not in catalogo:
                print("Erro, o produto não se encontra no catálogo...")

            elif produto in catalogo:
                print("Menu de edição de quantidade em um item no catálogo")
                menu = """"
1 - Soma
2 - Subtração
3 - Cancelar 
"""
                op = input(menu)

                if op == "1":
                    soma = int(input(f"Digite a quantidade a ser somada em {produto}: "))

                    total = catalogo[produto]["quantidade"] + soma
                    catalogo[produto]["quantidade"] = total
                    print("A soma foi realiada com suesso")
                    print(f"A nova quantidade de {produto} é: {catalogo[produto]['quantidade']}")

                elif op == "2":
                    sub = int(input(f"Informe a quantidade que será subtraída de {produto}"))
                    if sub <= catalogo[produto]['quantidade']:
                        total = catalogo[produto]["quantidade"] - sub
                        catalogo[produto]["quantidade"] = total
                        print("A subtração foi realizada com sucesso")
                        print(f"A nova quantidade de {produto} é: {catalogo[produto]['quantidade']}")
                    else:
                        print("Subtração não realizada, quantiade de produtos disponível no catálogo é menor.")

                else:
                    print("Cancelando ação...")
                    break


def val_prod_cat():
    while True:
        produto = input("Digite o produto que será editado: ")
        if produto not in catalogo:
            print("produto não encontrado")

        if produto in catalogo:
            menu = """"
1 - Continuar
2 - Cancelar
"""
            op = input(menu)
            if op == "1":
                valor = float(input("Informe o novo valor do produto"))
                if valor <= catalogo[produto]['valor']:
                    catalogo[produto]["valor"] = valor
                    print(f"O novo valor do item{produto} é R$: {valor}")
                    print("Deseja alterar o valor de outro produto?")

            elif op == "2":
                print("Cancelando operação...")
                break
            else:
                print("Opção não encontrada")


def pesquisa():
    while True:
        print("Pesquisa de produto")
        menu = """
1 - Continuar
2 - Cancelar
"""
        op = input(menu)
        if op == "1":
            produto = input("Informe o produto que deseja pesquisar:  ")
            if produto not in catalogo:
                print("O produto informa não existe no catálogo.")

            elif produto in catalogo:

                print(
                    f"O produto está disponível, a quantidade de {produto} é: {catalogo[produto]['quantidade']} "
                    f"unidades")
                print(f"O valor de cada unidade deste produto é: R$ {catalogo[produto]['valor']}")
                print("Deseja pesquisar outro item?")

        else:
            print("Operação cancelada")


def remov_prod_cat():
    while True:
        print("Menu de remoção para itens no catálogo")
        menu = """
1 - Continuar
2 - Cancelar    
"""
        op = input(menu)
        if op == "2":
            print("Operação cancelada")
            print("Retornando ao menu principal...")
            break

        if op == "1":
            produto = input("Informe o produto que deseja remover do catálogo:  ")
            if produto in catalogo:
                del catalogo[produto]
                print(f"O produto {produto} foi removido do catálogo com sucesso!")
                print(f"Seu novo catálogo é {catalogo}")
                print("Deseja remove outro item?")
            else:
                print("O produto não se encontra no catálogo.")
                print("Deseja realizar uma nova busca?")
        else:
            print("Opção informada inválida.")


def adc_prod_car():
    global total_comp
    while True:
        print("Adicionar produto no carrinho")
        menu = """
1 - Continuar
2 - Cancelar    
"""
        op = input(menu)
        if op == "2":
            print("Operação cancelada")
            print("Retornando ao menu inicial..")
            break

        if op == "1":
            produto = input("Informe o produto que deseja adicionar ao carrinho:  ")
            if produto in catalogo:
                if produto in carrinho:
                    print("O produto informado já se encontra no carrinho")
                    print("Informe o que deseja fazer: ")
                    menu2 = """
                1 - Adicionar mais
                2 - Cancelar ação            
                """
                    op = input(menu2)

                    if op == "2":
                        print("Operação Cancelada")
                        adc_prod_car()
                    if op == "1":
                        exced = float(input("Informe a quantidade que será adicionada:  "))
                        if catalogo[produto]['quantidade'] >= exced:
                            nova_quant = carrinho[produto]['quantidade'] + exced
                            carrinho[produto]['quantidade'] = nova_quant
                            novo_val = catalogo[produto]["valor"] * exced
                            novo_v = carrinho[produto]['valor'] + novo_val
                            carrinho[produto]['valor'] = novo_v
                            total_comp += novo_val
                            novo_cat = catalogo[produto]['quantidade'] - exced
                            catalogo[produto]['quantidade'] = novo_cat
                            print("Operação concluida com sucesso")
                            print(f"A nova quantidade de {produto} no seu carrinho é {carrinho[produto]}")
                            print(f"O novo valor total do seu carrinho é: R$ {total_comp}")
                        else:
                            print("A quantidade de produtos disponivel no catálogo é insuficiente.")
                    else:
                        print("A opção informada não existe.")

                if produto not in carrinho:
                    quantidade = int(input("Informe a quantidade que será adicionada:  "))

                    if catalogo[produto]['quantidade'] >= quantidade:
                        carrinho[produto] = {"quantidade": quantidade,
                                             "valor": catalogo[produto]['valor'] * quantidade
                                             }
                        val = catalogo[produto]['valor'] * quantidade
                        total_comp += val
                        print(f"{produto} foi adicionado ao seu carrinho de compras")
                        nova_quant_cat = catalogo[produto]['quantidade'] - carrinho[produto]['quantidade']
                        catalogo[produto]['quantidade'] = nova_quant_cat
                        print(f"Seu carrinho de compras contém: {carrinho}")
                        print(f"O novo valor dos itens no seu carrinho é: R$ {total_comp}")
                    else:
                        print(f"A quantidade de {produto} disponivel no catálogo é insuficiente")
            else:
                print("O produto não existe.")


def remov_prod_Car():
    global total_comp
    while True:
        print("Menu de remoção para itens no carrinho")
        menu = """
    1 - Remover a quantidade de um produto 
    2 - remover um produto completamente
    3 - Cancelar    
    """
        op = input(menu)
        if op == "3":
            print("Operação cancelada")
        if op == "2":
            produto = input("Informe o produto que deseja remover do carrinho:  ")
            if produto in carrinho:
                valor = carrinho[produto]['valor']
                total_comp -= valor
                quantidade = carrinho[produto]['quantidade']
                catalogo[produto]['quantidade'] = quantidade + catalogo[produto]['quantidade']
                del carrinho[produto]
                print(f"O produto {produto} foi removido do carrinho com sucesso!")
                print(f"Seu novo carrinho é {carrinho}")
                print(f"O seu carrinho atual contém: {carrinho}")
                print(f"O valor dos itens em seu carrinho é: R$ {total_comp}")
            else:
                print("O produto não se encontra no catálogo.")
        if op == "1":
            produto = input("Informe o produto que deseja remover a quantidade: ")
            if produto in carrinho:
                quantidade = float(input("Informe a quantidade a ser subtraída:  "))
                if quantidade <= carrinho[produto]['quantidade']:
                    total = carrinho[produto]['quantidade'] - quantidade
                    carrinho[produto]['quantidade'] = total
                    valor = catalogo[produto]['valor'] * total
                    carrinho[produto]['valor'] = valor
                    total2 = quantidade * catalogo[produto]['valor']
                    total_comp -= total2
                    novo_cat = catalogo[produto]['quantidade'] + quantidade
                    catalogo[produto]['quantidade'] = novo_cat
                    print("Operação realizada com sucesso!")
                    print(f"A nova quantidade de {produto} no carrinho é: {carrinho[produto]['quantidade']}")
                    print(f"O novo valor dos itens no seu carrinho é R$: {total_comp}")
                else:
                    print("O produto não se encontra no carrinho")

            else:
                print("Quantiade informada é inválida")

        else:
            print("Opção informada inválida.")


def finalizar():
    global total_comp
    while True:
        print("Menu de finalização de compras")
        menu = """
1 - Finalizar compras
2 - Continuar comprando
3 - Não levar nada
"""
        op = input(menu)

        if op == "3":
            print("Encerrando compras...")
            print(f"Obrigado por escolher nosso supermercado {nome}")
            break

        if op == "2":
            print("Voltando ao menu incial")
            break

        if op == "1":
            print(f"O total das compras é: R$ {total_comp}")
            print(f"O seu carrinho final é: {carrinho}")
            print(f"Obrigado por comprar conosco {nome}")
            break


def itens_catalogo():
    for chave in catalogo:
        print(chave, catalogo[chave])


def itens_carrinho():
    for chave in carrinho:
        print(chave, carrinho[chave])
    print(f"O valor dos itens em seu carrinho é: R$ {total_comp}")


while True:
    op = input(menu)
    if op > "9":
        print("A opção escolhida não existe")

    elif op == "1":
        cadast_prod_cat()
    if op == "2":
        itens_catalogo()
    if op == "3":
        edit_quant_prod_cat()
    if op == "4":
        val_prod_cat()
    if op == "5":
        pesquisa()
    if op == "6":
        remov_prod_cat()
    if op == "7":
        adc_prod_car()
    if op == "8":
        remov_prod_Car()
    if op == "9":
        itens_carrinho()
    if op == "10":
        finalizar()
    if op == "11":
        print("Obrigado por usar nosso sistema, encerrando...")
        break

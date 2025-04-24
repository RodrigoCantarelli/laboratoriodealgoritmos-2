def avaliar_expressao_booleana(tokens):
    operadores = []
    operandos = []

    precedencia = {
        'or': 1,
        'and': 2,
        'not': 3
    }

    def aplicar_operador(operador):
        if operador == 'not':
            if len(operandos) < 1:
                raise ValueError("Faltando operando para 'not'")
            valor = operandos.pop()
            operandos.append(not valor)
        elif operador in ('and', 'or'):
            if len(operandos) < 2:
                raise ValueError(f"Faltando operandos para '{operador}'")
            valor_direito = operandos.pop()
            valor_esquerdo = operandos.pop()
            if operador == 'and':
                operandos.append(valor_esquerdo and valor_direito)
            elif operador == 'or':
                operandos.append(valor_esquerdo or valor_direito)

    for token in tokens:
        if token in ('True', 'False'):
            operandos.append(token == 'True')
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                aplicar_operador(operadores.pop())
            if not operadores:
                raise ValueError("Parênteses sem abertura")
            operadores.pop()
        elif token in precedencia:
            while (operadores and operadores[-1] in precedencia and
                   precedencia[operadores[-1]] >= precedencia[token]):
                aplicar_operador(operadores.pop())
            operadores.append(token)
        else:
            raise ValueError(f"Token inválido: {token}")

    while operadores:
        if operadores[-1] == '(':
            raise ValueError("Parênteses sem fechamento")
        aplicar_operador(operadores.pop())

    if len(operandos) != 1:
        raise ValueError("Expressão inválida ou mal formada")

    return operandos[0]

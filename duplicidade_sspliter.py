#worth

nome = 'guilherme'
inic= 2
fim = 4

def sspliter(string, index):
    resultado = ''
    for c in range(index):
        recebe = string[c]
        resultado += recebe
    return resultado

def sspliter2(string, start, end):
    atual = end
    if end <= 3:
        resultado = ''
        start -= 1
        end += start
        for c in range(start, end):
            recebe = string[c]
            resultado += recebe
        return resultado
    else:
        if end <= 4:
            resultado = ''
            start -= 1
            end += start
            for c in range(start, end):
                recebe = string[c - (atual - 2)]
                resultado += recebe
            return resultado


if __name__ == '__main__':
   teste = sspliter(nome, inic)
   print(teste)
   teste2 = sspliter2(nome, inic, fim)
   print(teste2)
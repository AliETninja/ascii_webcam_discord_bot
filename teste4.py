from array_nova import text_turner
from duplicidade_sspliter import sspliter

a = text_turner('C:\poar mano\discord_web_cam\img18.jpg')
# print(a)
def ajuste(param):
    enter = '\n'
    variavel = ''
    pa = param
    divv = pa.split('\n')
    divv.pop(len(divv) - 1)
    divv.pop(len(divv) - 1)
    divv.pop(len(divv) - 1)
    divv.pop(len(divv) - 1)
    divv.pop(len(divv) - 1)
    divv.pop(len(divv) - 1)

    for c in range(len(divv) - 1):
        divv[c] = sspliter(divv[c], 50)

    for c in range(len(divv) - 1):
        variavel += divv[c] + enter

    return variavel

if __name__ == '__main__':
    kleber = ajuste(a)
    print(a)
    print(kleber)






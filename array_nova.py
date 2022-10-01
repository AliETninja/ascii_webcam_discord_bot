import pywhatkit

def text_turner(local):
    pywhatkit.image_to_ascii_art(local, 'agr_em_text.text')
    arquivo = open('agr_em_text.text.txt', 'r')
    p = arquivo.read()
    a = p.replace('*', '░')
    a = a.replace('S', '░')
    a = a.replace('#', '░')
    a = a.replace('!', '░')
    a = a.replace(':', '░')
    a = a.replace('.', '░')
    a = a.replace('O', '░')
    a = a.replace('%', '█')
    a = a.replace('@', '▒')
    a = a.replace('&', '▒')
    a = a.replace('$', '█')
    return a

if __name__ == '__main__':
    rr = 'F:\code\discord_web_cam\img18.jpg'
    aqui = text_turner(rr)
    print(aqui)
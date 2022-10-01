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
    arquivo.close()
    return a

if __name__ == '__main__':
    rr = 'C:\your_directory\your_img.jpg' # debug only
    aqui = text_turner(rr)
    print(aqui)

import re 

def regex_hashtags(fichero):
    patron = re.compile("#\w+")
    resultado = patron.findall(fichero)
    return resultado
def regex_username(fichero):
    patron = re.compile("@\w{4,15}")
    resultado = patron.findall(fichero)
    return resultado
def regex_url(fichero):
    patron = re.compile("https://[\w\./\?#%=\-\&]+")
    resultado = patron.findall(fichero)
    return resultado
def regex_hora(fichero):
    patron = re.compile("(?:1[3-9]|2[0-3]):[0-5]\d(?:\s?[hH]rs|\s?[hH]oras)?|(?:0\d|\d|1[0-2]):[0-5]\d(?:\s?[hH]rs|\s?[hH]oras|\s?[aApP][mM]|\s?[dD]e\sla\s(?:mañana|tarde))?|(?:\d|1[0-2])(?:\s?[hH]rs|\s?[hH]oras|\s?[aApP][mM]|\s?[dD]e\sla\s(?:mañana|tarde))|(?:1[3-9]|2[0-3])(?:\s?[hH]rs|\s?[hH]oras)")
    resultado = patron.findall(fichero)
    return resultado
def regex_asciiemoji(fichero):
    patron = re.compile("[3O<>]?[:;=][\-\.\|^']*[\(\)\[\]<>OoDdPpVv3\*\\/]|[8B]\-?[\(\)\|]|[oO]\.[Oo]|<.3|\([^\s]_[^\s]\)|[xX][dDpP\)\(]")
    resultado = patron.findall(fichero)
    return resultado
def regex_emoji(fichero):
    patron = re.compile('[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F550-\U0001F567]|[\U0001F0A0-\U0001F0FF]|[\U0001F1E6-\U0001F1FF]|[\U00002600-\U000027BF]|[\U0001F300-\U0001F5FF]')
    resultado = patron.findall(fichero)
    return resultado
def top_ten(lista):
    diccionario = {}
    print(lista)
    print("Frecuencia: ",len(lista))
    for elemento in lista:
        if elemento in diccionario:
            diccionario[elemento] = diccionario[elemento] + 1
        else:
            diccionario[elemento] = 1
    ordenada = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
    print("Top 10")
    conter = 0
    for item in ordenada:
        if conter==10:
            break
        print("Item:",item[0], " Frecuencia:",item[1])
        conter = conter + 1
    print("\n")
if __name__ == '__main__':
    with open('./tweets.csv', 'r',encoding='utf-8') as archivo:
        fichero = archivo.read()
        hashtag = regex_hashtags(fichero)
        top_ten(hashtag)
        username = regex_username(fichero)
        top_ten(username)
        url = regex_url(fichero)
        top_ten(url)
        hora = regex_hora(fichero)
        top_ten(hora)
        ascii = regex_asciiemoji(fichero)
        top_ten(ascii)
        emoji = regex_emoji(fichero)
        top_ten(emoji)

vl={'a': '__|', 'b': '|__|', 'c': '|__', 'd': '==|', 'e': '|==|', 'f': '|==', 'g': '--|', 'h': '|--|', 'i': '|--', 'j': '__.|', 'k': '|_._|', 'l': '|.__', 'm': '==.|', 'n': '|=.=|', 'o': '|.==', 'p': '-.-|', 'q': '|-.-|', 'r': '|.--', 's': '\\/', 't': '<', 'u': '/\\', 'v': '>', 'w': '\\./', 'x': '<.', 'y': '/.\\', 'z': '.>'}

def encrypt(text: str):
    words = text.split(' ')
    encrypted_text = ''
    for i in words:
        letters=list(i)
        for j in letters:
            encrypted_text+=vl[j] + ' '
        encrypted_text+=' '
    return encrypted_text

def decrypt(en_text: str):
    words = en_text.split('  ')
    decrypted_text = ''
    vs = list(vl.values())
    words.pop(-1)
    for i in words:
        letters=i.split(' ')
        for j in letters: 
            try:index_of_letter=vs.index(j)
            except:pass
            decrypted_text += list(vl.keys())[index_of_letter]
        decrypted_text += ' '
    return decrypted_text


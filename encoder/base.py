class Encoder:
    alphabet_num_str = {
        1:'a',
        2:'b',
        3:'c',
        4:'d',
        5:'e',
        6:'f',
        7:'g',
        8:'h',
        9:'i',
        10:'j',
        11:'k',
        12:'l',
        13:'m',
        14:'n',
        15:'o',
        16:'p',
        17:'q',
        18:'r',
        19:'s',
        20:'t',
        21:'u',
        22:'v',
        23:'w',
        24:'x',
        25:'y',
        0:'z'
    }
    alphabet_str_num = {}
    for k,v in alphabet_num_str.items():
        alphabet_str_num[v] = k

    def __init__(self, text_to_encode = None):
        if text_to_encode:
            self.text = text_to_encode
        else:
            self.text = ""
    


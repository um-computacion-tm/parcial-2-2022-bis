class Encoder:

    def encode(self, string):
        encode_dict = {}
        posicion = 0
        for letter in string:
            posicion += 1
            if letter in encode_dict:
                encode_dict[letter].append(posicion)
            else:
                encode_dict[letter] = [posicion]
        return encode_dict

    def decode(self, encode):
        posicion = 0
        string = ""
        finalizado = False
        while not finalizado:
            posicion += 1
            encontrado = False
            for key in encode:
                if posicion in encode[key]:
                    string += key
                    encontrado = True
            if not encontrado:
                finalizado = True
        return string


if __name__ == '__main__':
    frase = 'Hola mundo'
    encoder = Encoder()
    encode_dict = encoder.encode(frase)
    print(encode_dict)
    decode = encoder.decode(encode_dict)
    print(decode)

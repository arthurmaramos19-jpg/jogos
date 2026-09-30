meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "HATER":"pessoa que está constantemente criticando os outros",                                
            "VLW": "abreviação da palavra valeu",                                                        
            "BISCOITAR": "postar algo apenas para chamar a atenção"}

palavra = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if palavra in meme_dict.keys():
    print(meme_dict[palavra])
else:
    print("Não conheço essa palavra")

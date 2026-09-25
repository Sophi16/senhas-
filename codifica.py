def codifica(texto, deslocamento):
    resultado = ""

    for caractere in texto:

        # Letras minúsculas
        if caractere.islower():
            resultado += chr(
                (ord(caractere) - ord('a') + deslocamento) % 26 + ord('a')
            )

        # Letras maiúsculas
        elif caractere.isupper():
            resultado += chr(
                (ord(caractere) - ord('A') + deslocamento) % 26 + ord('A')
            )

        # Números
        elif caractere.isdigit():
            resultado += chr(
                (ord(caractere) - ord('0') + deslocamento) % 10 + ord('0')
            )

        # Outros caracteres permanecem iguais
        else:
            resultado += caractere

    return resultado

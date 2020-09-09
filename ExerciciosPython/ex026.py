frase = input('\nEntre com a frase: ')
print("""\nVezes que aparece a letra "a": {}
Posição que "a" aparece pela primeira vez: {}
Posição que "a" aparece pela última vez: {}"""
      .format(frase.count('a'), frase.find('a'), len(frase) - 1 - frase[::-1].find('a')))

# Chocolate com Pimenta

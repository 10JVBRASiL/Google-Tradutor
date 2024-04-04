# Bibliotecas :
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator() 
texto = input("escreva seu texto aqui :")
traducao = tradutor.translate(texto)
print(traducao)
import re

texto = 'Hola, ¡a todos los itc ñoños de este grupo!'
resultado = re.findall(r'\w+', texto, re.IGNORECASE | re.ASCII)
print(resultado)

resultado = re.search(r'I[ST]C', texto, re.IGNORECASE)
if resultado:
    print(resultado)
    print(resultado.span())
    print(resultado.string)
    print(resultado.group())

expreg = r'(\b\w+(?:(a)|(o))\b)'
texto = 'La pelota se encuentra sobre el perro.'
print(re.findall(expreg, texto))

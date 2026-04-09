import re

print(re.sub(r'[eiou]', 'a', 'una mosca parada en la pared'))
print(re.sub(r'feo|oloroso|chiquito',
             '#$%^&',
             'el feo y oloroso perro está muy chiquito'))
print(re.sub(r'([aeiou])',
             r'\1f\1',
             'una mosca parada en la pared'))

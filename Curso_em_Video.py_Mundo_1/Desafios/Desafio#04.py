a= input('Digite algo: ')
print('O tipo primivo dele é',type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Tem letra maiúscula?', a.isupper())
print('Tem letra minúscula?', a.islower())
print('Está capitalizada? {com maiúsculas e minúscula}', a.istitle())
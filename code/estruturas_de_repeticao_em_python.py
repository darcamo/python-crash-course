
# sample(for)
palavras = ['gato', 'janela', 'paralelepípedo']
for palavra in palavras:
    print (palavra.upper())
# end-sample

# sample(range)
range(5, 10)          # 5, 6, 7, 8, 9
range(0, 10, 3)       # 0, 3, 6, 9
range(-10, -100, -30) # -10, -40, -70
range(-10, -101, -30) # -10, -40, -70 -100
# end-sample

# sample(while)
# Vamos calcular o fatorial de 6 e guardar na variável 'f'
N = 6
f = 1
while N > 1:
    f = f * N
    N -= 1  # Não existe ++ ou -- em Python
# end-sample

# sample(while-infinito)
while True:
    pass
# end-sample

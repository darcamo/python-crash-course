# sample(frutas)
precos = {"banana prata": 3.50,
          "coco verde": 2.0,
          "maçã nacional": 4.50,
          "manga tommy": 5.0,
          "uva red glob": 5.0}
minhas_compras = {"banana prata": 1.2,
                  "coco verde": 6,
                  "uva red glob": 0.6}

# Usa um list comprehension para gerar uma lista e soma os seus valores
conta = sum([precos[fruta] * minhas_compras[fruta] for fruta in minhas_compras])
print("Eu precisei pagar o total de R$ {0:.2f} em frutas".format(conta))
# end-sample


# sample(palavras_em_um_texto)
texto = '''"Aonde fica a saída?", Perguntou Alice ao gato que ria.
"Depende", respondeu o gato.
"De quê?", replicou Alice;
"Depende de para onde você quer ir..."'''
palavras = texto.split()
print("O texto tem {0} palavras, sendo {1} delas diferentes.".format(
    len(palavras), len(set(palavras))))
# end-sample


# sample(escalares)
# Não é necessário declarar variáveis
idade = 4            # Inteiro (int)
nome = "Kadu"        # String (str)
peso = 10.4          # Float (float)
vacinado = True      # Booleano (bool)
dono_anterior = None # Representa um tipo vazio (None)
peso_int = int(peso) # Inteiro convertido a partir de um float
c = 1-3j             # Número complexo
# end-sample


print("Nome:", nome)
print("Idade:", idade, "\nPeso:", peso)
if vacinado:
    print("{0} está vacinado".format(nome))


# sample(containers)
uma_lista = [2, 3, 5.5, 7, 11, "lala"] # Lista (list, [])
uma_tupla = (2, "lala", 4)             # Tupla (tuple, ())
um_dict = {'nome': "Silvio Santos",    # Dicionário (dict)
          'idade': 86,
          "profissões": ["apresentador", "empresário"]}
um_conjunto = {1, 4, 8, 10, "lala"}    # Conjunto (set)
# end-sample

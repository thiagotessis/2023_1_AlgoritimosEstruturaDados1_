from Fisica import Fisica
from Cidade import Cidade
#from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(2, "Capão da Canoa")

joao = Fisica("João", "3322-4455", c1, "000.111.222-33")
maria = Fisica("Maria", "2233-4455", c2, "555.444.333-22")
jose = Fisica("Jose", "2233-4455", c2, "222.333.444-55")
dosul = Juridica("Supermercado Dosul", "234-4321", c1, "00.111.222/0001-02" )

dosul.imprimir()
#pf.imprimir()


#pj1.addFuncionario(pf1)
#pj1.addFuncionario(pf2)

#pj1.imprimir()
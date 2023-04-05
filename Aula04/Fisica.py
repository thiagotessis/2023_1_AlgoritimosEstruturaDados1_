from Pessoa import Pessoa
#from Juridica import Juridica

class Fisica( Pessoa ):

    def __init__(self, nome, fone, cidade, cpf= None, empresa = None ):
        super().__init__( nome, fone, cidade)
        self.cpf = cpf
        self.empresa = empresa
    
    def setEmpresa(self, empresa):
        self.empresa = empresa
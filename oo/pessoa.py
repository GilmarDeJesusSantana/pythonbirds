class Pessoa:
    '''Este método é execultado toda vez que um novo objeto é instanciado.
        Para que se possa atribuir valores aos atributos no momento que as instancias
        são criados devesse criar parametros conforme abaixo.'''
    def __init__(self, nome = None, idade=36):
        self.idade = idade
        self.nome = nome

    '''Modelagem da classe Pessoa, com um método.'''
    def cumprimentar(self):
        return f'Olá {id(self)}'
'''Teste da classe Pessoa.'''
if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Gilmar'
    print(p.nome)

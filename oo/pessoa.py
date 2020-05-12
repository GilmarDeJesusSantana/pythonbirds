class Pessoa:

    olhos = 2 #'Este é um atributo de classe.'
    '''Este método é execultado toda vez que um novo objeto é instanciado.
        Para que se possa atribuir valores aos atributos no momento que as instancias
        são criados devesse criar parametros conforme abaixo.'''
    def __init__(self,*filhos, nome = None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    '''Modelagem da classe Pessoa, com um método.'''
    def cumprimentar(self):
        return f'Olá {id(self)}'
'''Teste da classe Pessoa.'''
if __name__ == '__main__':
    gilmar = Pessoa(nome='Gilmar')
    luciano = Pessoa(gilmar,nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    luciano.olhos = 1
    del luciano.filhos

    print(id(Pessoa.olhos), id(gilmar.olhos), id(luciano.olhos))
    print(Pessoa.olhos)
    print(gilmar.olhos)
    print(luciano.olhos)
    print(luciano.__dict__)
    print(gilmar.__dict__)
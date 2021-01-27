#decida por mim
import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, voce deve fazer isso!',
            'Não sei, voce que sabe',
            'Não faz isso!',
            'Acho que ta na hora certa!'
        ]
    
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.Iniciar()

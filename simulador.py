import PySimpleGUI as sg
import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout
        self.layout = [
            [sg.Text('Jogar o dado')],
            [sg.Button('sim'),sg.Button('nao')]
        ]
        
    def Iniciar(self):
        #criar uma janela
        self.janela = sg.Window('Simulador da Dado',Layout=self.layout)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores
       
        while True:
            try:
                     if self.eventos == 'sim' or self.eventos == 's' :
                            self.GerarValorDoDado()
                     elif self.eventos == 'não' or self.eventos =='n':
                            print('Agradecemos a participação!')
                     else:
                            print('Favor digitar sim ou não')
            except:
                print('Ocorreu um erro ao receber sua resposta')
        

    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
import requests
import json
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()

class Funcoes():

    def retornar_text(self, cep):
        cria = f'https://viacep.com.br/ws/{cep}/json/'
        page = requests.get(cria)
        soup = BeautifulSoup(page.text, 'lxml').text
        cep = json.loads(soup)
        texto = 'cep: {}\n' \
                '\nlogradouro: {}\n' \
                '\ncomplemento: {}\n' \
                '\nbairro: {}\n' \
                '\nlocalidade: {}\n' \
                '\nuf: {}\n' \
                '\nddd: {}'.format(cep['cep'], cep['logradouro'], cep['complemento'], cep['bairro'], cep['localidade'],
                                   cep['uf'], cep['ddd'])
        return texto


class Tela(Funcoes):

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_resposta()
        self.frame_entrada()
        self.frame_bttn()
        root.mainloop()

    def tela(self):
        self.root.title('Pesquisa CEP')
        self.root.configure(background='#4E6070')
        self.root.geometry('800x600')
        self.root.minsize(width=400, height=300)

    def frame_resposta(self):
        self.frame1 = Label(root, text='', font=('verdana', 10, 'bold'), justify=LEFT, anchor=NW)
        self.frame1.place(relx=0.055, rely=0.2, relwidth=0.89, relheight=0.7)

    def frame_entrada(self):
        self.lb_nome = Label(self.root, text='digite o CEP', font=('verdana', 9, 'bold'), background='#4E6070')
        self.lb_nome.place(relx=0.058, rely=0.02)
        self.entrada = Entry(self.root, font=('verdana', 8, 'bold'))
        self.entrada.place(relx=0.055, rely=0.075, relwidth=0.55, relheight=0.1)

    def frame_bttn(self):
        self.btt_pesquisar = Button(self.root, text= 'Pesquisar', bd=3, font=('verdana', 9, 'bold'), command = self.funcao)
        self.btt_pesquisar.place(relx=0.646, rely=0.029, relwidth=0.3, relheight=0.15)


    def funcao(self):
        self.frame1['text'] = self.retornar_text(self.entrada.get())

if __name__ == '__main__':

    Tela()



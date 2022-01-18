import requests
from bs4 import BeautifulSoup

class Relatorio():

    def __init__(self, fiis):
        self.fiis = fiis
        self.req = requests.get(f'https://www.fundsexplorer.com.br/funds/{fiis}')
        self.sopa = BeautifulSoup(self.req.text, 'lxml')
        self.scrapping()
        self.__str__()

    def __str__(self):
        print (f'Nome do Fundo: {self.nome_fundo}\n'
                f'\nRazao Social: {self.razao_fundo}\n'
                f'\nPreço atual: {self.preco}'
                f'\nDividend Yeld: {self.dividend_yeld}'
                f'\nPatrimônio Líquido: {self.patrimonio_liq}'
                f'\nValor Patrimonial: {self.valor_patr}'
                f'\nP/VP: {self.pvp}'
                f'\nSegmento: {self.segmento}'
                f'\nTaxa de Performance: {self.tx_perfor}'
                f'\nTaxa de Gestão: {self.tx_gestao}'
                f'\nTaxa de Administração: {self.tx_admin}'
                f'\nTaxa de Gerenciamento: {self.tx_geren}')

    def ret_func_indicator(self, index):
        self.func = self.sopa.find_all(class_="indicator-value")[index].text.lstrip()
        return self.func

    def ret_func_descrip(self, index):
        self.func = self.sopa.find_all(class_="description")[index].text.lstrip()
        return self.func

    def ret_outros(self, element):
        self.func = self.sopa.find(class_=element).text.lstrip()
        return self.func

    def scrapping(self):
        self.nome_fundo = self.ret_outros('section-title')
        self.razao_fundo = self.ret_outros('section-subtitle')
        self.preco = self.ret_outros('price')
        self.dividend_yeld = self.ret_func_indicator(2)
        self.patrimonio_liq = self.ret_func_indicator(3)
        self.valor_patr = self.ret_func_indicator(4)
        self.pvp = self.ret_func_indicator(6)
        self.tx_perfor = self.ret_func_descrip(6)
        self.tx_gestao = self.ret_func_descrip(7)
        self.tx_admin = self.ret_func_descrip(13)
        self.tx_geren = self.ret_func_descrip(14)
        self.segmento = self.ret_func_descrip(11)

if __name__ == '__main__':
    Relatorio('ELDO11B')
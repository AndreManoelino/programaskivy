# importar o App, builder (GUI)
## criar o nosso aplicativo
## criar a funçao build


from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.pegar_cotacao("USD")
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao(':BTC')}"
        self.root.ids["moeda4"].text = f"Rúpia Indiana R${self.pegar_cotacao('INR')}"
        
    def pegar_cotacao(Self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        print(requisicao.json())
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao
MeuAplicativo().run()   
    
   

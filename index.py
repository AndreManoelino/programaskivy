# importar o App, builder (GUI)
# criar o nosso aplicativo
# criar a funçao build


from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids.moeda1.text = f"Dólar: R${self.pegar_cotacao('USD')}"
        self.root.ids.moeda2.text = f"Euro: R${self.pegar_cotacao('EUR')}"
        self.root.ids.moeda3.text = f"Bitcoin: R${self.pegar_cotacao('BTC')}"
        
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        data = requisicao.json()
        
        if f"{moeda}-BRL" in data:
            cotacao = data[f"{moeda}-BRL"]["bid"]
            return cotacao
        else:
            return "N/A"
        
        
    def atualizar_cotacoes(self):
        moedas = {
            "moeda1": {"nome": "Dólar", "codigo": "USD"},
            "moeda2": {"nome": "Euro", "codigo": "EUR"},
            "moeda3": {"nome": "Bitcoin", "codigo": "BTC"}
        }
        
        for moeda_id, info in moedas.items():
            cotacao = self.pegar_cotacao(info["codigo"])
            self.root.ids[moeda_id].text = f"{info['nome']}: R${cotacao}" 
        
        print("Programa rodou com sucesso !")

if __name__ == '__main__':
    MeuAplicativo().run()
   
    
   

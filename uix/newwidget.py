from kivy.lang import Builder
from kivy.GridLayout import GridLayout

Builder.load_string("""
NewWidget:
  

 Label:
      id: moeda1
      text: "1º texto"
  Label:
      id: moeda2
      text: "2º texto"
  Label:
      id: moeda3
      text: "3º texto"
  Label:
      id: moeda4
      text: "3º texto"    
     
""")

class NewWidget(GridLayout):
	pass
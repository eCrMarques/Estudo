from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from login import Login
from home import Home
from signup import Signup
from kivy.utils import get_color_from_hex
#import requests
# from kivy.core.window import Window
# Window.size = (720, 1460)


class Main(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.add_widget(Home(name='home'))
        sm.add_widget(Signup(name='signup'))
        self.title='Gestão Financeira'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = '900'
        return sm

    def show_expense(self):
        if self.root.ids.expense.active:
            print("Opção selecionada: Despesas")
            # Lógica para exibir resposta visual para a opção "Despesas"
        else:
            # Lógica para remover resposta visual para a opção "Despesas"
            pass

    def show_income(self):
        if self.root.ids.income.active:
            print("Opção selecionada: Rendas")
            # Lógica para exibir resposta visual para a opção "Rendas"
        else:
            # Lógica para remover resposta visual para a opção "Rendas"
            pass

    def get_active_color(self, active):
        if active:
            return get_color_from_hex("#00FF00")  # Cor quando selecionado (verde)
        else:
            return get_color_from_hex("#FF0000")  # Cor quando deselecionado (vermelho)


    # def on_start(self):
    #     id_usuario = 1
    #     requisition = requests.get(f"https://database-projeto-default-rtdb.firebaseio.com/{id_usuario}.json")
    #     req_dict = requisition.json()

if __name__ == '__main__':
    Main().run()
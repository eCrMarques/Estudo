from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import matplotlib as mpl
from matplotlib import pyplot as plt
from garden_matplotlib import FigureCanvasKivyAgg

from kivy.metrics import dp

from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.floatlayout import MDFloatLayout

from kivy.core.text.markup import MarkupLabel

from kivymd.uix.card import MDCard


from kivymd.app import MDApp
from kivy.properties import StringProperty


mpl.rc('text', color='#ffffff')
mpl.rc('axes', labelcolor='#ffffff')
mpl.rc('xtick', color='#ffffff')
mpl.rc('ytick', color='#ffffff')


Builder.load_file('home.kv')

class CustomRow(MDBoxLayout):
    name = StringProperty('')

class Home(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in ["","Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items=menu_items,
            width_mult=4,
        )

        self.data = [
            {'name': 'Aluguel', 'value': '350R$', 'date': '06/07', 'type': 'Despesa Fixa', 'status': 'Pago'},
            {'name': 'Internet', 'value': '60R$', 'date': '06/07', 'type': 'Despesa Fixa', 'status': 'Pago'},
            {'name': 'Energia', 'value': '120R$', 'date': '06/07', 'type': 'Despesa', 'status': 'Pago'},
            {'name': 'Água', 'value': '25R$', 'date': '06/07', 'type': 'Despesa', 'status': 'Pago'},
            
        ]

    def on_enter(self):
        self.ids.table.data = [
            {
                'viewclass': 'CustomRow',
                'name': "{:^10}{:^10}{:^14}{:^14}{:^10}".format(item["name"], item["value"], item["date"], item["type"], item["status"])
            }
            for item in self.data
        ]

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        pass
     
    def go_home(self):
        self.manager.current = 'home'

    def go_login(self):
        self.manager.current = 'login'
        print('Deslogando...')

    def abrir_card(self):
        self.add_widget(AddCard())

class TableApp(MDApp):
    pass



class AddCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class PlotWidgetPie(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(self.plot_pie()))
 
    def plot_pie(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        fig = plt.Figure(figsize=(5, 3), dpi=90)
        fig.patch.set_facecolor('#263238')
        ax = fig.add_subplot(111)
        list_category = ['Renda', 'Despesa', 'Saldo']
        list_values = [1200,750,450]

        explode = []
        for i in list_category:
            explode.append(0.05)
        ax.pie(list_values, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
        ax.legend(list_category, labelcolor='#263238', loc="center left", bbox_to_anchor=(0, 0))

        return fig
    

class PlotWidgetBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(self.plot_bar()))

    def plot_bar(self):
        colors = ['#b4abd4', '#888fc3','#5679ad', '#ee9944', '#444466', '#bb5555']
        list_category = ['Renda', 'Despesa', 'Saldo']
        list_values = [1200,750,450]
        

        fig = plt.Figure(figsize=(4, 3.45), dpi=60)
        fig.patch.set_facecolor('#263238')
        ax = fig.add_subplot(111)
        ax.bar(list_category, list_values,  color=colors, width=0.9)

        c = 0

        for i in ax.patches:
            ax.text(i.get_x()-.001, i.get_height()+.5,
                    str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='#ffffff')

            c += 1

        ax.set_xticklabels(list_category,fontsize=16)
        ax.patch.set_facecolor('#263238')
        ax.spines['bottom'].set_color('#ffffff')
        ax.spines['bottom'].set_linewidth(1)
        ax.spines['right'].set_linewidth(0)
        ax.spines['top'].set_linewidth(0)
        ax.spines['left'].set_color('#ffffff')
        ax.spines['left'].set_linewidth(1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(bottom=False, left=False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(False, color='#ffffff')
        ax.xaxis.grid(False)


        return fig
  


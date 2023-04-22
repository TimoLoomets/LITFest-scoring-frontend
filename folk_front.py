import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
  
import read_data

kivy.require('1.11.1')

column_heads = ['#', 'Alagrupp', 'Robot', 'Eelvoor 1', 'Eelvoor 2', 'Eelvoor 3', 'Poolfinaal', 'Finaal']
competitions = ['Folkrace', 'Paadiralli']

cur_competition_index = 0

class ScoreApp(App):
    def populate_table(table, data):
        table.clear_widgets()
        for head in column_heads:
            table.add_widget(Label(text=head))

        data = data.sort_values(['Koht, finaal', 'Koht, poolfinaal', 'Koht, eelvoorud'])
        data = data.reset_index(drop=True)

        for index, row in data.iterrows():
            table.add_widget(Label(text=str(index + 1)))
            table.add_widget(Label(text=str(row['Grupp'])))
            table.add_widget(Label(text=str(row['Roboti nimi'])))
            table.add_widget(Label(text=str(row['Kohapunktid, eelvoor 1'])))
            table.add_widget(Label(text=str(row['Kohapunktid, eelvoor 2'])))
            table.add_widget(Label(text=str(row['Kohapunktid, eelvoor 3'])))
            table.add_widget(Label(text=str(row['Kohapunktid, poolfinaal'])))
            table.add_widget(Label(text=str(row['Sõidupunktid, finaal'])))

    def build(self):
        Clock.schedule_interval(lambda dt: self.update_time(), 30)

        data = read_data.read_from_web()
        master_layout = BoxLayout(orientation='vertical')
        master_layout.add_widget(Label(text='Folkrace', size_hint=(1.0, 0.1)))

        layout = GridLayout(cols=len(column_heads), size_hint=(1.0, 0.9))
        ScoreApp.populate_table(layout, data)
        master_layout.add_widget(layout)

        return master_layout
    
    def update_time(self):
        global cur_competition_index 
        cur_competition_index = (cur_competition_index + 1) % len(competitions)

        data = read_data.read_from_web(competitions[cur_competition_index])

        self.root.children[1].text = competitions[cur_competition_index]
        ScoreApp.populate_table(self.root.children[0], data)

ScoreApp().run()               
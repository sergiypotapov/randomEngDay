__author__ = 'Serg'
import kivy
import cycle
import todays_day

kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

#TODO �� ������� ������ ���������� ���������� ���������. ��� ��������� ������� - ��� ���� ��������� � ��� �����
#TODO ���� �� �� - ���� �� ���������� �������� ��������
#TODO ���� �� - ���� �� ���������� �������
#TODO ���� �� �������

class MyApp(App):

    def build(self):
        random = cycle.cycle()
        random = str(random)
        to_day = todays_day.today_day()
        to_day = str(to_day)

        print("random is", random, "today is", to_day )
        if to_day == random:
            return Label(text=random, font_size= '900sp')
        else:
            return Label(text=random)



if __name__ == '__main__':
    MyApp().run()

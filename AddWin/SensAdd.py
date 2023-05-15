from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.banner import MDBanner
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import FloatLayout
import SQL

BTN_SIZE = (.14, .1)


class New_Parameter(MDApp):

    def build(self):
        screen = FloatLayout()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        screen.add_widget(FitImage(source='pic\\1618529499_62-funart_pro-p-oboi-fon-material-dizain-62.png'))
        pk_list = [el[0] for el in SQL.query(SQL.my_cursor, 'SELECT Type_ID from type_of_sensor')]
        dep_list = [el[0] for el in SQL.query(SQL.my_cursor, 'SELECT Type_ID from sensor')]
        print(dep_list)
        def has_numbers(inputString):
            return any(char.isdigit() for char in inputString)

        def validate():

            But2.disabled = Field1.error or Field2.error or Field3.error

        def error_1(instance, value):
            Field1.error = False
            if Field1.text != "":
                try:
                    int(Field1.text)
                    if int(Field1.text) in pk_list:
                        Field1.helper_text = 'Этот ID уже используется'
                        Field1.error = True
                except ValueError:
                    Field1.error = True
                    Field1.helper_text = 'ID должен быть INT'
            else:
                Field1.error = True
            validate()

        def error_2(instance, value):
            Field2.error = False
            if has_numbers(Field2.text):
                Field2.error = True
                Field2.helper_text = 'Имя не должно содержать цифры'
            if Field2.text == "":
                Field2.error = True
            validate()

        def error_3(instance, value):
            Field3.error = False
            if has_numbers(Field3.text):
                Field3.error = True
                Field3.helper_text = 'Описание не должно содержать цифры'
            if Field3.text == "":
                Field3.error = True
            validate()


        Field1 = MDTextField(
            hint_text="Type_ID",
            pos_hint={"x": 0.05, "y": 0.7},
            size_hint={0.6, 0.05},
            multiline=False,
            helper_text_mode='on_error',
            max_text_length=64,
        )
        Field1.bind(focus=error_1)

        Field2 = MDTextField(
            hint_text="Name",
            pos_hint={"x": 0.05, "y": 0.6},
            size_hint={0.6, 0.05},
            multiline=False,
            helper_text_mode='on_error',
            max_text_length=64,
            required=True
        )
        Field2.bind(focus=error_2)

        Field3 = MDTextField(
            hint_text="Description",
            pos_hint={"x": 0.05, "y": 0.5},
            size_hint={0.6, 0.05},
            multiline=False,
            max_text_length=20,
            helper_text_mode='on_error',
            required=True
        )
        Field3.bind(focus=error_3)

        def new(instance):
            SQL.query(SQL.my_cursor, f'INSERT INTO type_of_sensor VALUES ({Field1.text},'
                                     f'\'{Field2.text}\',\'{Field3.text}\')')
            SQL.mydb.commit()
            MDApp.get_running_app().stop()


        But2 = MDRaisedButton(
            text='Применить',
            size_hint=BTN_SIZE,
            pos_hint={"x": 0.81, "y": 0.05},
            on_release=new,
            disabled=True
        )

        screen.add_widget(Field1)
        screen.add_widget(Field2)
        screen.add_widget(Field3)
        screen.add_widget(But2)
        return screen


if __name__ == "__main__":
    New_Parameter().run()
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''


class Example(MDApp):
    dialog = None
    def cancel (self,obj):
    	self.dialog.dismiss()
    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            
            self.dialog = MDDialog(
                radius=[50, 7, 50, 7],
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release = self.cancel
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],)
        self.dialog.open()


Example().run()
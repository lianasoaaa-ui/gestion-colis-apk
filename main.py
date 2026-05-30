# =====================================================
# GESTION DES COLIS MADAGASCAR
# VERSION APK COMPATIBLE (PDF DESACTIVE)
# =====================================================

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

from datetime import datetime
import json
import os

Window.clearcolor = (1,1,1,1)

FICHIER_COLIS = "colis.json"
FICHIER_USER = "users.json"

villes_madagascar = [
    "Antananarivo","Toamasina","Mahajanga","Fianarantsoa",
    "Toliara","Antsiranana","Antsirabe","Morondava",
    "Sambava","Nosy Be","ambanja","antsalaka"
]

# =====================================================
# USERS
# =====================================================

def charger_users():
    if os.path.exists(FICHIER_USER):
        try:
            with open(FICHIER_USER, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def sauvegarder_users(data):
    with open(FICHIER_USER, "w") as f:
        json.dump(data, f)

# =====================================================
# LOGIN
# =====================================================

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.username = TextInput(hint_text="Utilisateur", multiline=False)
        self.password = TextInput(hint_text="Mot de passe", password=True, multiline=False)

        btn_login = Button(text="LOGIN", background_color=(0,1,0,1))
        btn_register = Button(text="REGISTER", background_color=(0,0.5,1,1))

        btn_login.bind(on_press=self.login)
        btn_register.bind(on_press=self.register)

        layout.add_widget(Label(text="CONNEXION"))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(btn_login)
        layout.add_widget(btn_register)

        self.add_widget(layout)

    def login(self, instance):
        users = charger_users()
        u = self.username.text
        p = self.password.text

        if u in users and users[u] == p:
            self.manager.current = "gestion"
        else:
            Popup(title="Erreur", content=Label(text="Login incorrect"), size_hint=(0.7,0.3)).open()

    def register(self, instance):
        users = charger_users()
        u = self.username.text
        p = self.password.text

        if u and p:
            users[u] = p
            sauvegarder_users(users)
            Popup(title="OK", content=Label(text="Compte créé"), size_hint=(0.7,0.3)).open()

# =====================================================
# GESTION
# =====================================================

class GestionColis(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.data = []
        self.load()

        self.numero = TextInput(hint_text="Numero colis", multiline=False)
        self.mpanera = TextInput(hint_text="Mpanera", multiline=False)

        self.btn = Button(text="ENREGISTRER", background_color=(0,1,0,1))
        self.btn.bind(on_press=self.save)

        self.scroll = ScrollView()
        self.list = GridLayout(cols=1, size_hint_y=None)
        self.list.bind(minimum_height=self.list.setter('height'))

        self.scroll.add_widget(self.list)

        self.add_widget(self.numero)
        self.add_widget(self.mpanera)
        self.add_widget(self.btn)
        self.add_widget(self.scroll)

        self.show()

    def save(self, instance):
        self.data.append({
            "numero": self.numero.text,
            "mpanera": self.mpanera.text
        })
        self.save_file()
        self.show()

    def save_file(self):
        with open(FICHIER_COLIS, "w") as f:
            json.dump(self.data, f)

    def load(self):
        if os.path.exists(FICHIER_COLIS):
            try:
                with open(FICHIER_COLIS, "r") as f:
                    self.data = json.load(f)
            except:
                self.data = []

    def show(self):
        self.list.clear_widgets()

        for c in self.data:
            box = BoxLayout(size_hint_y=None, height=50)
            box.add_widget(Label(text=c["numero"]))
            box.add_widget(Label(text=c["mpanera"]))
            self.list.add_widget(box)

    # ❌ PDF DESACTIVE POUR APK
    def imprimer_un_colis(self, colis):
        Popup(
            title="Info",
            content=Label(text="Impression PDF désactivée"),
            size_hint=(0.7,0.3)
        ).open()

# =====================================================
# APP
# =====================================================

class MonApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(Screen(name="gestion"))

        sm.get_screen("gestion").add_widget(GestionColis())

        return sm

if __name__ == "__main__":
    MonApp().run()
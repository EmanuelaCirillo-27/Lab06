import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler

    def get_strumenti(self):
        return self._model.lista_strumenti


    def mostra_strumenti(self):
        strumenti = self._model.get_strumenti()

        self._view.lista_strumenti.controls.clear()
        #print(f"DEBUG - Strumenti arrivati al controller: {strumenti}")

        if strumenti:
            for el in strumenti:

                testo_strumento = ft.Text(str(el))
                self._view.lista_strumenti.controls.append(testo_strumento)

        else:
            self._view.lista_strumenti.controls.append(ft.Text("Database vuoto"))

        self._view.update()


    def mostra_tipo(self):

        tipo_inserito = self._view.input_tipo_strumento.value

        self._view.input_tipo_strumento.value=""

        # Se il campo è vuoto
        if not tipo_inserito:
            return

        tipo_strumenti = self._model.cerca_strumenti_per_tipo(tipo_inserito)

        self._view.lista_strumenti_ricerca.controls.clear()

        # Se la lista di strumenti per quel tipo indicato non è vuota
        if tipo_strumenti:
            for singolo in tipo_strumenti:
                testo_tipo = ft.Text(str(singolo))
                self._view.lista_strumenti_ricerca.controls.append(testo_tipo)
        # Se è vuota
        else:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text("Nessuno strumento trovato per quel tipo"))

        self._view.update()

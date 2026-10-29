from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile



    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        cnx=get_connection()
        cursore_dizionario=cnx.cursor(dictionary=True)

        query = "SELECT * FROM strumento"
        cursore_dizionario.execute(query)

        self.lista_strumenti = []

        for riga in cursore_dizionario:
            strumento=Strumento(riga['codice'], riga['tipo'], riga['marca'], riga['anno_acquisto'], riga['valore'], riga['disponibile'])
            self.lista_strumenti.append(strumento)

        #for riga in cursore_dizionario:
            #for chiave, valore in riga.items():
                #if type(valore).__name__ == 'Decimal':
                    #riga[chiave] = float(valore)
            #self.lista_strumenti.append(riga)

        cursore_dizionario.close()
        cnx.close()

        #print(f"DEBUG - Strumenti trovati dal database: {len(self.lista_strumenti)}")

        return self.lista_strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO

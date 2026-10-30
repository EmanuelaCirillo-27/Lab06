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


        cursore_dizionario.close()
        cnx.close()

        if self.lista_strumenti:
            return self.lista_strumenti
        else:
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """

        cnx = get_connection()
        cursore_dizionario1 = cnx.cursor(dictionary=True)

        query1= f""" SELECT *
                    FROM strumento
                    WHERE tipo= '{tipo}'"""

        cursore_dizionario1.execute(query1)

        self.lista_strumenti_ricerca = []

        for row in cursore_dizionario1:
            strumento_per_tipo=Strumento(row['codice'], row['tipo'], row['marca'], row['anno_acquisto'], row['valore'], row['disponibile'])
            self.lista_strumenti_ricerca.append(strumento_per_tipo)

        cursore_dizionario1.close()
        cnx.close()

        if self.lista_strumenti_ricerca:
            return self.lista_strumenti_ricerca
        else:
            return None
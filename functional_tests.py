from selenium import webdriver
import unittest

class NovoVisitanteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_pode_comecar_uma_lista_e_pegala_depois(self):
        # Pafúncio ouviu falar sobre um novo App de tarefas Ele vai chegar esse site usando o Firefox
        # Pafúncio abre o site
        self.browser.get('http://localhost:8000')

        # Ele vê que o título da página menciona lista de tarefas
        self.assertIn('Lista de Tarefas do Will', self.browser.title)
        self.fail('Acaba o teste!')

        # Ele é convidado a inserir um item à lista

        # Ele digita "Comprar polenta" dentro de um input

        # Quando ele pressiona Enter, a página atualiza e, agora, a
        # página lista:
        # 1: Comprar polenta

        # Ainda há uma caixa de texto convidando-o a adicionar outro
        # item. Ele digita "Comprar Guaraná Fruki"

        # A página atualiza de novo e agora mostra os dois itens

        # Pafúncio gostaria que o site se lembrasse da lista dele.
        # Ele vê que o site gerou uma URL única para ele. Há alguns
        # textos que explicam isso para ele

        # Ele visita a URL e sua lista ainda está lá

        # Satisfeito, ele volta a dormir


if __name__ == '__main__':
    unittest.main(warnings='ignore')
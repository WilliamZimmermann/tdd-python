from selenium import webdriver

# Pafúncio ouviu falar sobre um novo App de tarefas Ele vai chegar esse site usando o Firefox
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# Ele vê que o título da página menciona lista de tarefas
assert 'Lista de Tarefas do Will' in browser.title

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

browser.quit()
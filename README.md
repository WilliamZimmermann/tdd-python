# tdd-python
Hands On sobre TDD e Python para a MeetUp do grupo Rede Neural.
Aguarde, até o dia 28 de Junho disponibilizaremos os arquivos necessários para o Hands On da nossa MeetUp do dia 30 de Junho de 2018, na FTEC de Caxias do Sul (09:00).

# Requisitos

Se você desejar acompanhar na prática o TDD com Python e Django, recomendo:
* Que instale o Python (veja o próximo tópico);
* Que instale alguma IDE de desenvolvimento. Eu usarei o PyCharm (https://www.jetbrains.com/pycharm/) que também possui uma versão free para a comunidade. Outra excelente opção é o Visual Studio Code (VS Code, https://code.visualstudio.com) que também possui algumas extensões muito boas para Python;
* Que baixe o Firefox (https://www.mozilla.org/firefox/);


# Passo 1 - Instalação do Python

Baixe o arquivo de instalação do Python 3.7.*, se você ainda não tiver. Você pode baixar diretamente do site oficial:
* Para MacOSX: https://www.python.org/ftp/python/3.7.0/python-3.7.0-macosx10.9.pkg
* Para Windows 64bits: https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe
* Para Linux: versões mais recentes já tem o Python instalado por padrão. Se não tiver, dê um apt install python3.6-venv.

# Passo 2 - Ambiente virtual

O ambiente virtual é um ambiente onde os requisitos do seu projeto estarão instaldos. Com isso, você não precisará alterar suas configurações do Python globais toda vez que seu projeto for alterado - precisará alterar somente as configurações desse ambiente virtual.

Crie uma pasta onde você colocará seu projeto. Vamos chamá-lo de tddpy. Para fazer isso, abra seu Terminal (ou PowerShell no Windows). Digite:

**No Windows**
'''
$ cd myuser
$ mkdir tddpy
$ cd tddpy
$ py -3.7 -m venv virtualenv

**No Linux ou Mac**
'''
$ cd myuser
$ mkdir tddpy
$ cd tddpy
$ python3 -m venv virtualenv
'''

Durante o projeto, ativaremos e desativaremos o ambiente virtual. Para fazer isso, digite (você deve estar dentro do diretório tddpy):

**No Windows**
'''
source virtualenv/Scripts/activate
deactivate
'''

**No Linux ou Mac**
'''
source virtualenv/bin/activate
deactivate
'''

# Passo 3 - Instalação do Django e do Selenium
Abra seu terminal (console) e, estando com o ambiente virtual ativado, digite:

'''
(virtualenv) $ pip install "django" "selenium<4"
Collecting django....
Installing collected packages: pytz, django, selenium
Successfully installed django-2.0.6 pytz-2018.4 selenium-3.13.0
'''

É isso! O resto, faremos no evento! Até lá!

Ps: se ficar com alguma dúvida, coloque nos comentários. Estou à disposição.

# Referências

O tutorial que seguiremos é baseado no livro "Test Driven Development with Python". Ele está disponível para compras ou para leitura online gratuita no seguinte link: http://www.obeythetestinggoat.com/pages/book.html


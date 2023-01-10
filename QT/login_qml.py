from PySide6.QtCore import QObject, Slot
from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
import os
from httpx import get

      #É chamada pelo onClicked e pelo método que foi implementado aqui 
class Bridge(QObject):
    @Slot(str, result=list)
    def fetch_image(self, pokemon_id):
        image_path = Path('pokemon_image.png')
        try:
            if image_path.exists():
                print('Deletando imagem')
                image_path.unlink()

            response = get(
                f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
            ).json()

            image_url = response['sprites']['other']['home']['front_default']
            image_content = get(image_url).content

            with open('pokemon_image.png', 'wb') as poke_image:
                poke_image.write(image_content)
        except Exception as e:
            print(e)
        finally:
            return str(image_path), response['name'].capitalize() + '!'
filemain = 'C:\Users\vinix\Desktop\Prog\login_qml.qml'
app = QGuiApplication()

engine = QQmlApplicationEngine()
engine.load(filemain) #Carrega o arquivo qml
engine.load(os.path.join(os.path.dirname(__file__), "login_qml.py"))
bridge = Bridge()
context = engine.rootContext() 
context.setContextProperty('bridge', bridge) 

app.exec()


'''
Sem o Slot a def fetch_image não é uma função, porque é necessário
comunicar ao Qt que é necessário armazenar um dado para mandar para bridge
para armazenar isso na bridge, define-se tudo isso como um Slot
'''
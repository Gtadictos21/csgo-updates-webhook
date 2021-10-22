from __future__ import print_function
import requests
import os
import time
import pytz

from bs4 import BeautifulSoup
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from colorama import Fore 
from colorama import Style

# Cargamos el .env
load_dotenv()
API_KEY_WHATSAPP = os.getenv('API_KEY_WHATSAPP')
API_KEY_STEAM = os.getenv('API_KEY_STEAM')
NUM_TELEFONO = os.getenv('NUM_TELEFONO')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

memoria = None
memoria2 = None

tz = pytz.timezone('America/Argentina/Buenos_Aires')

while True:
    url = "https://blog.counter-strike.net/?feed=rss" # URL de la pagina a la cual le saca el contenido
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    resp = requests.get(url, headers=headers)
    print(f'{Fore.CYAN}Codigo de respuesta de{Fore.MAGENTA} \"{url}\": {Fore.GREEN}{resp.status_code}{Style.RESET_ALL}') # Dice el codigo de respuesta (200 = OK | 403 = Inaccesible)
    soup = BeautifulSoup(resp.content, features="html.parser")
    items = soup.findAll('item')
    news_items_title = []
    news_items_description = []
    news_items_link = []

    for item in items:
        news_item_title = {}
        news_item_title['title'] = item.title.text
        news_items_title.append(news_item_title)

    for item in items:
        news_item_description = {}
        news_item_description['description'] = item.description.text
        news_items_description.append(news_item_description)

    for item in items:
        news_item_link = {}
        news_item_link['guid'] = item.guid.text
        news_items_link.append(news_item_link)

    titulo = news_items_title[0]['title'] #Titulo del post
    descripcion = news_items_description[0]['description'] #Descripción del post
    link = news_items_link[0]['guid'] #Link al post 

    if memoria == None:    # Si no hay memoria
        memoria = link     # Guardamos el link actual en la memoria
        procesar_link1 = True
    elif memoria == link:  # Si hay memoria y es la misma que el link actual
        procesar_link1 = False           # continua
    else:                  # Sino
        memoria = link     # Guardamos el nuevo link en la memoria
        procesar_link1 = True
    
    if procesar_link1:
        # Fecha y hora
        now = datetime.now(tz)
        fecha = now.strftime("%d/%m/%Y")
        hora = now.strftime("%H:%M:%S")

        # Webhook Discord

        content = "<@503739646895718401>" # ID de usuario a mencionar
        allowed_mentions = {
            "parse": ["users"]
        }

        webhook = DiscordWebhook(url=f'{WEBHOOK_URL}', content=content, allowed_mentions=allowed_mentions)
        response = webhook.execute()

        embed = DiscordEmbed(title=f"{titulo}:", url=f"{link}", description=f"{descripcion}", color=0x2bff00)
        embed.set_footer(text=f'La actualización fue lanzada el dia: {fecha} a las: {hora}')
        embed.set_thumbnail(url='http://media.steampowered.com/apps/csgo/blog/images/fb_image.png?v=6') # Link de imagen
        webhook = DiscordWebhook(url=f'{WEBHOOK_URL}',embeds=[embed])
        response_on = webhook.execute()

        # Whatsapp API
        url_whatsapp = f"https://api.callmebot.com/whatsapp.php?phone={NUM_TELEFONO}&text=*{titulo}*%0ALink:%20{link}%0AFecha%20y%20hora:%20{fecha}%20{hora}&apikey={API_KEY_WHATSAPP}"
        response = requests.post(f"{url_whatsapp}")
        print(f'{Fore.CYAN}Codigo de respuesta de{Fore.MAGENTA} \"{url_whatsapp}\": {Fore.GREEN}{response.status_code}{Style.RESET_ALL}') # Dice el codigo de respuesta (200 = OK | 403 = Inaccesible)
                            
    url2 = "https://blog.counter-strike.net/index.php/category/updates/feed/" # URL de la pagina a la cual le saca el contenido
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    resp = requests.get(url2, headers=headers)
    print(f'{Fore.CYAN}Codigo de respuesta de{Fore.MAGENTA} \"{url2}\": {Fore.GREEN}{resp.status_code}{Style.RESET_ALL}') # Dice el codigo de respuesta (200 = OK | 403 = Inaccesible)
    soup = BeautifulSoup(resp.content, features="html.parser")
    items = soup.findAll('item')
    news_items_title = []
    news_items_description = []
    news_items_link = []

    for item in items:
        news_item_title = {}
        news_item_title['title'] = item.title.text
        news_items_title.append(news_item_title)

    for item in items:
        news_item_description = {}
        news_item_description['description'] = item.description.text
        news_items_description.append(news_item_description)

    for item in items:
        news_item_link = {}
        news_item_link['guid'] = item.guid.text
        news_items_link.append(news_item_link)

    titulo2 = news_items_title[0]['title'] #Titulo del post
    descripcion2 = news_items_description[0]['description'] #Descripción del post
    link2 = news_items_link[0]['guid'] #Link al post 

    if memoria2 == None:    # Si no hay memoria
        memoria2 = link2     # Guardamos el link actual en la memoria
        procesar_link2 = True
    elif memoria2 == link2:  # Si hay memoria y es la misma que el link actual
        procesar_link2 = False           # continua
    else:                  # Sino
        memoria2 = link2     # Guardamos el nuevo link en la memoria
        procesar_link2 = True
    
    if procesar_link2:

        # Fecha y hora
        now2 = datetime.now(tz)
        fecha2 = now2.strftime("%d/%m/%Y")
        hora2 = now2.strftime("%H:%M:%S")

        # Webhook Discord

        content = "<@503739646895718401>" # ID de usuario a mencionar
        allowed_mentions = {
            "parse": ["users"]
        }

        webhook = DiscordWebhook(url=f'{WEBHOOK_URL}', content=content, allowed_mentions=allowed_mentions)
        response = webhook.execute()

        embed = DiscordEmbed(title=f"{titulo2}:", url=f"{link2}", description=f"{descripcion2}", color=0x2bff00)
        embed.set_footer(text=f'La actualización fue lanzada el dia: {fecha2} a las: {hora2}')
        embed.set_thumbnail(url='http://media.steampowered.com/apps/csgo/blog/images/fb_image.png?v=6') # Link de imagen
        webhook = DiscordWebhook(url=f'{WEBHOOK_URL}',embeds=[embed])
        response_on = webhook.execute()

        # Whatsapp API
        url_whatsapp2 = f"https://api.callmebot.com/whatsapp.php?phone={NUM_TELEFONO}&text=*{titulo2}*%0ALink:%20{link2}%0AFecha%20y%20hora:%20{fecha2}%20{hora2}&apikey={API_KEY_WHATSAPP}"
        response2 = requests.post(f"{url_whatsapp2}")
        print(f'{Fore.CYAN}Codigo de respuesta de{Fore.MAGENTA} \"{url_whatsapp2}\": {Fore.GREEN}{response.status_code}{Style.RESET_ALL}') # Dice el codigo de respuesta (200 = OK | 403 = Inaccesible)

    time.sleep(10) #Tiempo del bucle (Se puede modificar a gusto, aunque para evitar ser blacklisteado, no es recomendable bajarlo de 10s)
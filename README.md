# Script que notifica por Discord y Whatsapp cuando una actualización del CS:GO es lanzada
## Este proyecto fue creado por [Julián](https://github.com/Gtadictos21/) y [Galo](https://github.com/Galo223344/)

Este script de Python hace un web scraping al RSS del [blog.counter-strike.net](https://blog.counter-strike.net/?feed=rss) y envia un webhook y un mensaje por Whatsapp con el titulo, la descripción y el link en cuanto una actualización es lanzada. La verificación se realiza cada 10 segundos, y se puede modificar desde el script.

El script utiliza la API de [callmebot.com](https://www.callmebot.com/) para enviar los mensajes por Whatsapp.

![webhook](https://user-images.githubusercontent.com/83682754/138393399-fa1ca4e7-e84d-4f49-9daa-96f6a646ce09.jpg)

## Instalar WebHook y sus dependencias:
¡Este WebHook requiere Python3 version: 3.9.x, y pip!
```
https://github.com/Gtadictos21/csgo-updates-webhook.git
```
```
pip install discord-webhook
```
```
pip install pytz
```
```
pip install BeautifulSoup4
```
```
pip install python-dotenv
```
```
pip install colorama
```

**ATENCIÓN:** Tienen que agregar el [link a su WebHook](https://support.discord.com/hc/es/articles/228383668-Introducci%C3%B3n-a-los-webhook) en el archivo .env, y tienen que agregar su numero de celular, y la llave de la API de Whatsapp para que el script les envie un mensaje (Esto es opcional). Claro que pueden personalizar cada mensaje, y pueden adaptarlo a sus necesidades.

Para ejecutar el WebHook: `python3 Webhook.py`, o pueden hacerlo con [Systemd](https://github.com/Gtadictos21/csgo-updates-webhook/blob/main/webhook.service) (recomendable)

Ultima actualización: 22/10/2021 por: [Julián M.](https://github.com/Gtadictos21/) (Gtadictos21)

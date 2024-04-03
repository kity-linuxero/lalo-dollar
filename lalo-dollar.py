import time, json
import requests
from io import BytesIO
import os
import pytz

# Librería para pasar texto a voz
from gtts import gTTS

# Librería para reproducir audio.
from pygame import mixer

from datetime import datetime

# Constantes
INTERVALO = 30 # En minutos
TZ = pytz.timezone('America/Argentina/Buenos_Aires')

# Se usa la dolar api
# Ver doc: https://dolarapi.com/docs/
DOLAR_BLUE= "https://dolarapi.com/v1/dolares/blue"
DOLAR_MEP = "https://dolarapi.com/v1/dolares/bolsa"

# Definir texto que va a decir
TEXTO = 'El valor del dolar es'

# Configuración de audio
audio = 'audio.mp3'
language = 'es'


def generar_audio(valor_dolar):
    tx = f"{TEXTO} {valor_dolar}"
    tts = gTTS(tx, lang=language, slow=False, tld='com.ar')

    try:
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        return mp3_fp
    except Exception as error:
        raise Exception("Error al intentar guardar el archivo: {error}")


def decir_valor_dolar(valor):

    try:
        mixer.init()
        sound = valor
        sound.seek(0)
        mixer.music.load(sound, "mp3")
        mixer.music.play()
    except Exception as error:
        raise Exception(f"Error al intentar reproducir el audio: {error}")


# Main



while True:

    ahora = datetime.now(TZ)
    hora_actual = ahora.hour # La hora actual
    dia_semana = ahora.weekday() # 0: lunes, 1: martes, ..., 6: domingo

    if 10 <= hora_actual < 17 and 0 <= dia_semana <= 4:
        # Está en horario de mercado

        print(f"Hora tomada {hora_actual}")

        # Obtengo el json con el valor del dolar elegido
        response = requests.get(DOLAR_BLUE)      
        print(response.json())

        # Se elije al valor de venta
        valor = response.json()['venta']
        print (valor)

        try:
            a = generar_audio(valor)
            decir_valor_dolar(a)
        
        except Exception as e:
            print(f"Ocurrió algún error! {e}")

            if os.path.exists(audio):
                os.remove(audio)
            else:
                print("The file does not exist") 

    else:
        print("Fuera de horario de mercado.")

    time.sleep(INTERVALO*60)
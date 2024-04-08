import time, json
import requests
from io import BytesIO
import os
import pytz
import argparse


# Librería para pasar texto a voz
from gtts import gTTS


# Librería para reproducir audio.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

from datetime import datetime

# Constantes
TZ = pytz.timezone('America/Argentina/Buenos_Aires')



# Se usa la dolar api
# Ver doc: https://dolarapi.com/docs/
DOLAR_BLUE= "https://dolarapi.com/v1/dolares/blue"
DOLAR_MEP = "https://dolarapi.com/v1/dolares/bolsa"

# Definir texto que va a decir
TEXTO = 'El valor del dolar'

# Configuración de audio
audio = 'audio.mp3'
language = 'es'




def generar_audio(texto):

    
    tts = gTTS(texto, lang=language, slow=False, tld='com.ar')

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



def main():

    intervalo = 30
      
    # Parametros argv
    parser = argparse.ArgumentParser(description='Programa que te informa el valor del dolar. Como Lalo.')
    parser.description = "Ayuda"
    parser.add_argument('-i', '--intervalo', type=int, help='El intervalo en minutos que informará el dolar. Default: 30 minutos')
    parser.add_argument('-d', '--dolar', type=str, help='Un tipo de dolar a informar: blue/mep. Default: blue')

    args = parser.parse_args()
    tipo_dolar = DOLAR_BLUE

    if args.intervalo:
        print(f'Se ejecuta la consulta cada: {args.intervalo} minutos')
        intervalo = args.intervalo
    if args.dolar:
        if args.dolar == 'mep':
            tipo_dolar = DOLAR_MEP
        
    print(f'Se informa el dolar {tipo_dolar}\nControl + C para cancelar')

    # LOOP
    while True:

        ahora = datetime.now(TZ)
        hora_actual = ahora.hour # La hora actual
        dia_semana = ahora.weekday() # 0: lunes, 1: martes, ..., 6: domingo

        if 10 <= hora_actual <= 17 and 0 <= dia_semana <= 4:
            # Está en horario de mercado

            # print(f"Hora tomada {hora_actual}")

            # Obtengo el json con el valor del dolar elegido
            try:
                response = requests.get(tipo_dolar)
            except:
                print("No se puede conectar con la API. ¿Hay conexión a internet?")
                break
            # print(response.json())

            
            valor = response.json()['venta'] # Se elije al valor de venta
            
            tipo = response.json()['nombre'] # Tipo de dolar: blue/bolsa

            tex = (f'El valor del dolar {tipo} es {valor} pesos')
            
            print (tex)

            a = generar_audio(tex)
            
            decir_valor_dolar(a)
            
        else:
            print("Fuera de horario de mercado.")

        try:
            time.sleep(intervalo*60)
        except KeyboardInterrupt:
            break



# Main
if __name__ == '__main__':
    main()
    print ("Gracias por usar el Lalo-dollar :)")


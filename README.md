# lalo-dollar
Información del dolar siempre

![](./img/img_a.jpg)

Uso: 

- Descargar ejecutable: [binario exe](https://github.com/kity-linuxero/lalo-dollar/releases/download/v1.0/lalo-dollar.exe)

Por defecto informará cada 30 minutos el valor de venta del dolar blue.

#### Parámetros
- `-i` El intérvalo en minutos que informa. Por defecto 30 minutos.
- `-d` El tipo de dolar. Puede ser mep (bolsa) o blue. Por defecto se informará el blue.
- `-h` Imprime la siguiente ayuda

```bash

usage: lalo-dollar.py [-h] [-i INTERVALO] [-d DOLAR]

Ayuda

options:
  -h, --help            show this help message and exit
  -i INTERVALO, --intervalo INTERVALO
                        El intervalo en minutos que informará el dolar. Default: 30 minutos
  -d DOLAR, --dolar DOLAR
                        Un tipo de dolar a informar: blue/mep. Default: blue
```

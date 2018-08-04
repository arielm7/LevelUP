from prueba_lectura import lectura
from prueba_escritura import escritura
import time

global usuario
usuario = "Inicial"
t_end = time.time() + 0.25

while time.time() < t_end:
    usuario = escritura()
    lectura(usuario)
    hacer = lectura(usuario)

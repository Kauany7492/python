import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def carta():
    lyrics = [
        ("Bom dia", 0.11),
        ("Saiba que no lugar certo, você brilha diferente.", 0.07),
        ("Cuide do seu corpo. Você mora nele.", 0.09),
        ("Comece, não espere pela coragem, ela nos encontra caminhando.", 0.09),
        ("Se você pode imaginar algo, isso pode ser feito.", 0.10),
        ("Faça acontecer porque a única coisa que cai do céu é chuva", 0.09),
        ("Faça. Vão te criticar da mesma forma.", 0.11),
        ("Não diminua a meta, aumente o esforço.", 0.07),
    ]
    delays = [0.3, 2.2, 7.5, 10.0, 16.2, 20.5, 24.0, 26.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    carta()

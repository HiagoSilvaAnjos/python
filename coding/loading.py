import sys
import time

def progressbar(it, prefix="", size=60, out=sys.stdout): 
    count = len(it)
    start = time.time()  # Início da contagem de tempo

    def show(j):
        x = int(size * j / count)
        remaining = ((time.time() - start) / j) * (count - j) if j else 0
        mins, sec = divmod(remaining, 60)
        time_str = f"{int(mins):02}:{sec:03.1f}"
        print(f"{prefix}[{'█' * x}{'.' * (size - x)}] {j}/{count} Tempo Estimado: {time_str}", 
              end='\r', file=out, flush=True)

    show(0.1)  # Evita divisão por zero
    for i, item in enumerate(it):
        yield item
        show(i + 1)
        time.sleep(0.03)  #Reduzir o tempo de espera de 0.1 para 0.03

    print("\n", flush=True, file=out)

# Chamando a barra de progresso com tempo reduzido
for i in progressbar(range(100), "Gerando Novo Arquivo: ", 60):
    time.sleep(0.03)  # Reduzir o tempo de espera
print("Arquivo Gerado com sucesso!")

# Link: https://stackoverflow.com/questions/3160699/python-progress-bar
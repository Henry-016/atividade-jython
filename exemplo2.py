from java.util import ArrayList, Collections
from java.util.concurrent import Executors, Callable
from java.time import LocalDateTime
from java.time.format import DateTimeFormatter
import random

class CalculoParcial(Callable):
    def __init__(self, lote_id, valores):
        self.lote_id = lote_id
        self.valores = valores

    def call(self):
        maior = Collections.max(self.valores)
        menor = Collections.min(self.valores)
        soma = sum([v for v in self.valores])
        return "[Lote %d] Registros: %d | Min: %d | Max: %d | Soma: %d" % (
            self.lote_id, len(self.valores), menor, maior, soma
        )

def executar():
    print("=== Processamento Concorrente com Java ExecutorService & Collections ===")
    
    inicio = LocalDateTime.now()
    formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss")
    print("Inicio da execucao: " + inicio.format(formatador))

    executor = Executors.newFixedThreadPool(3)
    tarefas = ArrayList()

    for i in range(1, 4):
        lote = ArrayList()
        for _ in range(5):
            lote.add(random.randint(10, 100))
        tarefas.add(CalculoParcial(i, lote))

    print("\nDisparando " + str(tarefas.size()) + " tarefas concorrentes...")
    resultados = executor.invokeAll(tarefas)

    print("\n--- Resultados Retornados pelas Threads da JVM ---")
    for futuro in resultados:
        print(futuro.get())

    executor.shutdown()
    print("\nProcessamento finalizado com sucesso!")

if __name__ == "__main__":
    executar()

# -*- coding: utf-8 -*-
from javax.swing import JFrame, JButton, JProgressBar, JPanel, JLabel, BoxLayout
from java.awt import FlowLayout, Dimension, GraphicsEnvironment
from java.lang import Thread, Runnable

class TarefaProcessamento(Runnable):
    def __init__(self, barra, botao, rotulo):
        self.barra = barra
        self.botao = botao
        self.rotulo = rotulo

    def run(self):
        self.botao.setEnabled(False)
        self.rotulo.setText("Processando tarefa em Thread da JVM...")
        
        for i in range(101):
            Thread.sleep(15)
            self.barra.setValue(i)
        
        self.rotulo.setText("Processamento concluido com sucesso!")
        self.botao.setEnabled(True)
        print("[Thread JVM] Tarefa assincrona concluida com 100% de progresso.")

def iniciar_interface():
    is_headless = GraphicsEnvironment.isHeadless()
    print("[Swing GUI] Inicializando componentes graficos (Headless: " + str(is_headless) + ")...")

    frame = JFrame("Jython - Demonstracao de Swing & Threads")
    frame.setSize(420, 180)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setLocationRelativeTo(None)

    painel = JPanel()
    painel.setLayout(BoxLayout(painel, BoxLayout.Y_AXIS))

    rotulo = JLabel("Clique no botao para iniciar a tarefa em background:")
    rotulo.setAlignmentX(JPanel.CENTER_ALIGNMENT)

    barra = JProgressBar(0, 100)
    barra.setStringPainted(True)
    barra.setPreferredSize(Dimension(350, 25))
    barra.setAlignmentX(JPanel.CENTER_ALIGNMENT)

    botao = JButton("Executar Tarefa (Thread Java)")
    botao.setAlignmentX(JPanel.CENTER_ALIGNMENT)

    def ao_clicar(event=None):
        tarefa = TarefaProcessamento(barra, botao, rotulo)
        thread = Thread(tarefa)
        thread.start()
        thread.join()

    botao.actionPerformed = ao_clicar

    painel.add(rotulo)
    painel.add(barra)
    painel.add(botao)

    frame.getContentPane().add(painel)
    frame.setVisible(True)

    ao_clicar()

if __name__ == "__main__":
    iniciar_interface()

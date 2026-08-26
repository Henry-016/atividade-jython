# Atividade Prática: Interoperabilidade Python e Java com Jython

## 1. Descrição do Jython

O **Jython** é uma implementação de código aberto da linguagem de programação Python desenvolvida inteiramente em Java. Ao contrário da implementação padrão do Python (CPython, desenvolvida em C), o Jython compila o código Python diretamente para *bytecode* da **Java Virtual Machine (JVM)** em tempo de execução.

Essa arquitetura permite uma integração transparente e bidirecional entre as duas tecnologias:
* O código escrito em Python pode importar, instanciar e estender diretamente qualquer classe, interface ou biblioteca da plataforma Java.
* Permite acesso a recursos avançados do ecossistema Java (concorrência nativa com Threads da JVM, interfaces gráficas Swing/AWT, conectividade corporativa, criptografia e I/O de alto desempenho) utilizando a sintaxe dinâmica, expressiva e concisa do Python.

---

## 2. Descrição dos Programas Desenvolvidos

Para evidenciar a interoperabilidade na JVM, foram criados dois programas distintos com escopos práticos:

### Programa 1: Comunicação de Rede HTTP e Hashing Criptográfico (`exemplo1_rede_seguranca.py`)
Este programa realiza uma requisição HTTP do tipo GET a um endpoint público (`https://httpbin.org/get`), faz o streaming e leitura do corpo da resposta e, em seguida, calcula o hash criptográfico seguro (SHA-256) dos dados recebidos. Todas as operações de conexão de rede, leitura de fluxo de bytes e cálculo do digest criptográfico são delegadas diretamente aos pacotes padrão do Java.

### Programa 2: Interface Gráfica e Concorrência Multithreading (`exemplo2_swing_threads.py`)
Este programa cria uma interface gráfica de usuário (GUI) interativa contendo uma janela com botão e barra de progresso. Ao disparar o botão, uma tarefa de processamento em segundo plano é instanciada e executada em uma **Thread nativa da JVM**, atualizando o progresso da interface visual sem travar a thread de renderização da UI (Event Dispatch Thread).

---

## 3. Classes e Bibliotecas Java Utilizadas

### No Programa 1 (`exemplo1_rede_seguranca.py`):
* `java.net.URL`: Representa o endereço do recurso na web e gerencia a criação da conexão.
* `java.net.HttpURLConnection`: Gerencia a conexão HTTP, envio de cabeçalhos (`User-Agent`) e obtenção do código de status retornado.
* `java.io.InputStreamReader` e `java.io.BufferedReader`: Realizam a leitura eficiente em stream dos caracteres vindos da resposta HTTP.
* `java.security.MessageDigest`: Fornece o algoritmo criptográfico de hash seguro (`SHA-256`) para processar os bytes do conteúdo recebido.

### No Programa 2 (`exemplo2_swing_threads.py`):
* `javax.swing.JFrame`, `javax.swing.JButton`, `javax.swing.JProgressBar`, `javax.swing.JPanel`, `javax.swing.JLabel`, `javax.swing.BoxLayout`: Componentes visuais e gerenciadores de layout para a construção da interface gráfica (Java Swing).
* `java.awt.Dimension`: Define as dimensões e medidas dos componentes de tela.
* `java.lang.Thread`: Cria e gerencia a linha de execução paralela na JVM.
* `java.lang.Runnable`: Interface do Java implementada por uma classe Python para definir a rotina executada dentro da nova thread.

---

## 4. Integração entre Python e Java nos Exemplos

A interoperabilidade proporcionada pelo Jython é demonstrada na prática através de três aspectos centrais:

1. **Importação Direta de Pacotes Java:** A sintaxe tradicional de imports do Python (`from java.net import URL`, `from javax.swing import JFrame`) é utilizada diretamente para carregar classes do JDK sem necessidade de intermediários ou wrappers JNI (Java Native Interface).
2. **Implementação de Interfaces Java em Classes Python:** No Programa 2, a classe Python `TarefaProcessamento` herda da interface `java.lang.Runnable` e sobrescreve o método `run()`. O Jython converte essa classe Python em uma implementação válida de `Runnable` aceita pelo construtor de `java.lang.Thread`.
3. **Mapeamento Transparente de Eventos e Tipos:** Callbacks e listeners do Java (como `actionPerformed` do botão) recebem diretamente funções Python como manipuladores de evento, unindo o modelo orientado a eventos do Java à flexibilidade funcional do Python.

---

## 5. Instruções para Executar o Projeto

### Pré-requisitos
* **Java Development Kit (JDK)** versão 8 ou superior instalado.
* Arquivo JAR standalone do Jython (ex: `jython-standalone-2.7.3.jar`).

### Passo a Passo:
1. Certifique-se de que os arquivos dos scripts e o JAR do Jython estão na mesma pasta:
   ```
   ├── jython-standalone-2.7.3.jar
   ├── exemplo1_rede_seguranca.py
   ├── exemplo2_swing_threads.py
   └── README.md
   ```

2. Verifique se o Java está configurado no terminal:
   ```bash
   java -version
   ```

3. Execute o **Programa 1** (Rede e Criptografia):
   ```bash
   java -jar jython-standalone-2.7.3.jar exemplo1_rede_seguranca.py
   ```

4. Execute o **Programa 2** (Interface Gráfica e Threads):
   ```bash
   java -jar jython-standalone-2.7.3.jar exemplo2_swing_threads.py
   ```

---

## 6. Instruções para Executar o Projeto Utilizando o Editor / Ambiente Antigravity

Para executar diretamente no ambiente **Antigravity**:

1. Abra a pasta do projeto no Antigravity.
2. Abra o terminal integrado (`Ctrl + \`` ou através do menu superior **Terminal > New Terminal**).
3. Execute qualquer um dos comandos Java padrão diretamente pelo prompt do terminal:
   ```bash
   java -jar jython-standalone-2.7.3.jar exemplo1_rede_seguranca.py
   ```
4. Caso prefira executar como uma tarefa automatizada, configure o arquivo `.vscode/tasks.json` na raiz do projeto com o seguinte conteúdo:
   ```json
   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "Executar Script com Jython",
         "type": "shell",
         "command": "java -jar jython-standalone-2.7.3.jar ${file}",
         "group": {
           "kind": "build",
           "isDefault": true
         },
         "presentation": {
           "reveal": "always",
           "panel": "shared"
         }
       }
     ]
   }
   ```
   Com a task configurada, basta abrir o script desejado e executar a tarefa de build do editor.

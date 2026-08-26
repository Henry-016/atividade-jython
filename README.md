# Atividade Prática: Interoperabilidade Python e Java com Jython

## 1. Descrição do Jython

O **Jython** é uma implementação open-source de alta performance da linguagem Python desenvolvida totalmente em Java. Diferentemente do interpretador de referência (CPython, escrito em C), o Jython compila o código-fonte Python diretamente para *bytecode* executável pela **Java Virtual Machine (JVM)**.

Essa característica viabiliza interoperabilidade transparente e direta:
* Programas Python podem importar, instanciar classes, implementar interfaces e consumir bibliotecas do ecossistema Java nativamente.
* Elimina a necessidade de camadas intermediárias de comunicação (como pontes IPC ou JNI manuais), unindo a produtividade e sintaxe concisa do Python com a robustez e APIs corporativas da plataforma Java.

---

## 2. Estrutura do Repositório

Conforme solicitado nos requisitos da atividade, a estrutura de arquivos é a seguinte:

```text
atividade-jython/
├── README.md
├── Dockerfile
├── exemplo1.py
└── exemplo2.py
```

---

## 3. Descrição dos Programas Desenvolvidos

### Exemplo 1: Comunicação de Rede HTTP e Criptografia (`exemplo1.py`)
Realiza uma requisição HTTP `GET` para uma API pública (`https://httpbin.org/get`), consome a resposta através de streaming de entrada e gera o hash criptográfico seguro `SHA-256` da resposta. Toda a camada de rede, buffering de entrada e processamento criptográfico é delegada às classes fundamentais do Java.

### Exemplo 2: Interface Gráfica e Concorrência Multithreading (`exemplo2.py`)
Instancia componentes de interface gráfica de usuário (GUI) com **Java Swing** e executa uma tarefa concorrente em uma **Thread nativa da JVM** (`java.lang.Thread` e `java.lang.Runnable`), demonstrando o acoplamento de callbacks em Python aos eventos de componentes gráficos do Java.

---

## 4. Classes e Bibliotecas Java Utilizadas

| Programa | Classe/Interface Java | Pacote / Biblioteca | Finalidade |
| :--- | :--- | :--- | :--- |
| **Exemplo 1** | `URL` | `java.net` | Endereçamento e abertura de conexão HTTP |
| **Exemplo 1** | `HttpURLConnection` | `java.net` | Configuração de headers, verbos HTTP e leitura de status |
| **Exemplo 1** | `BufferedReader`, `InputStreamReader` | `java.io` | Leitura eficiente em fluxo (stream) da resposta da API |
| **Exemplo 1** | `MessageDigest` | `java.security` | Geração do hash criptográfico SHA-256 |
| **Exemplo 2** | `JFrame`, `JButton`, `JProgressBar`, `JPanel`, `JLabel`, `BoxLayout` | `javax.swing` | Criação e estilização da interface gráfica |
| **Exemplo 2** | `Dimension`, `GraphicsEnvironment` | `java.awt` | Dimensionamento e verificação do ambiente gráfico |
| **Exemplo 2** | `Thread` | `java.lang` | Gerenciamento e disparo de threads nativas da JVM |
| **Exemplo 2** | `Runnable` | `java.lang` | Interface implementada em classe Python para execução em background |

---

## 5. Explicação da Interoperabilidade Python/Java

1. **Importação Direta de Tipos Java:** Através de declarações como `from java.net import URL` ou `from javax.swing import JFrame`, o interpretador Jython localiza as classes carregadas no *classpath* da JVM e as expõe como módulos/tipos Python.
2. **Implementação de Interfaces Java em Classes Python:** No `exemplo2.py`, a classe Python `TarefaProcessamento(Runnable)` herda da interface Java `Runnable`. A JVM reconhece os objetos criados como instâncias legítimas de `Runnable`, permitindo passá-los diretamente para construtores Java (`Thread(tarefa)`).
3. **Mapeamento de Eventos e Callbacks:** Propriedades como `botao.actionPerformed` recebem diretamente funções e closures do Python, demonstrando a facilidade de acoplamento do modelo orientado a eventos do Java com funções de primeira classe do Python.

---

## 6. Instruções para Executar o Projeto

### Pré-requisitos
* **Java Development Kit (JDK)** versão 8 ou superior instalado.
* Arquivo JAR standalone do Jython (ex: `jython-standalone-2.7.3.jar` ou `jython.jar`).

### Execução via Terminal / VS Code:

1. No terminal ou terminal integrado do VS Code (`Ctrl + \``), execute o **Exemplo 1**:
   ```bash
   java -jar jython-standalone-2.7.3.jar exemplo1.py
   ```

2. Execute o **Exemplo 2**:
   ```bash
   java -jar jython-standalone-2.7.3.jar exemplo2.py
   ```

---

## 7. Instruções para Executar o Projeto Utilizando Docker

O projeto conta com um **Dockerfile** configurado que provisiona o ambiente Java, baixa automaticamente o Jython e configura suporte gráfico virtual (`Xvfb`), dispensando qualquer instalação prévia de Java ou Jython na máquina do avaliador.

### 1. Construir a Imagem Docker
Na raiz do projeto (`atividade-jython/`), execute:
```bash
docker build -t atividade-jython .
```

### 2. Executar o Contêiner
Execute a imagem construída para rodar os exemplos automaticamente:
```bash
docker run --rm atividade-jython
```

### 3. Executar um Exemplo Específico via Docker (Opcional)
Se desejar executar apenas um dos scripts de forma isolada dentro do contêiner:
```bash
# Executa apenas o Exemplo 1
docker run --rm atividade-jython java -jar jython.jar exemplo1.py

# Executa apenas o Exemplo 2
docker run --rm atividade-jython xvfb-run -a java -jar jython.jar exemplo2.py

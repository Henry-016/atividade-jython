# Interoperabilidade Python e Java com Jython

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

### Exemplo 2: Concorrência Multithreading e Coleções Java (`exemplo2.py`)
Executa processamento concorrente assíncrono utilizando um pool de threads gerenciado pelo ExecutorService da JVM. Lotes de dados numéricos armazenados em ArrayList são processados em paralelo via tarefas que implementam a interface Callable, aplicando funções utilitárias da classe Collections e formatação temporal com java.time.

---

## 4. Classes e Bibliotecas Java Utilizadas

| Programa | Classe/Interface Java | Pacote / Biblioteca | Finalidade |
| :--- | :--- | :--- | :--- |
| **Exemplo 1** | `URL` | `java.net` | Endereçamento e abertura de conexão HTTP |
| **Exemplo 1** | `HttpURLConnection` | `java.net` | Configuração de headers, verbos HTTP e leitura de status |
| **Exemplo 1** | `BufferedReader`, `InputStreamReader` | `java.io` | Leitura eficiente em fluxo (stream) da resposta da API |
| **Exemplo 1** | `MessageDigest` | `java.security` | Geração do hash criptográfico SHA-256 |
| **Exemplo 2** | `Executors`, `Callable` | `java.util.concurrent` | Gerenciamento de pool de threads e definição de tarefas assíncronas com retorno |
| **Exemplo 2** | `ArrayList`, `Collections` | `java.util` | Manipulação de listas e operações analíticas nativas (min/max) |
| **Exemplo 2** | `LocalDateTime`, `DateTimeFormatter` | `java.time, java.time.format` | Captura e formatação de timestamp no padrão brasileiro |

---

## 5. Explicação da Interoperabilidade Python/Java

1. **Importação Direta de Tipos Java:** Através de declarações como `from java.net import URL` ou `from java.util.concurrent import Executors`, o interpretador Jython localiza as classes carregadas no classpath da JVM e as expõe diretamente como módulos e tipos Python.
2. **Implementação de Interfaces Java em Classes Python:** No `exemplo2.py`, a classe Python `CalculoParcial(Callable)` herda da interface Java `Callable`. A JVM reconhece as instâncias dessa classe como tarefas executáveis válidas para o método `invokeAll()` do `ExecutorService`.
3. **Manipulação Fluida de Coleções:** Objetos `ArrayList` instanciados em Python interagem transparentemente com utilitários estáticos como `Collections.max()` e `Collections.min()`, além de permitirem iteração com recursos nativos da sintaxe Python (list comprehensions e laços `for`).

---

## 6. Instruções para Executar o Projeto

### Pré-requisitos
* **Java Development Kit (JDK)** versão 8 ou superior instalado.
* Arquivo JAR standalone do Jython (ex: `jython-standalone-2.7.3.jar` ou `jython.jar`).

### Execução via Terminal / VS Code:

1. No terminal ou terminal integrado do VS Code (`Ctrl + \``), execute o **Exemplo 1**:
   ```bash
   java -jar jython.jar exemplo1.py
   ```

2. Execute o **Exemplo 2**:
   ```bash
   java -jar jython.jar exemplo2.py
   ```

---

## 7. Instruções para Executar o Projeto Utilizando Docker

O projeto conta com um Dockerfile configurado que provisiona o ambiente Java e baixa automaticamente o Jython, dispensando qualquer instalação prévia de Java ou Jython na máquina do avaliador.

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

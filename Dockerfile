FROM eclipse-temurin:11-jre

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -Lo jython.jar https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.3/jython-standalone-2.7.3.jar

COPY . /app

CMD ["sh", "-c", "echo '>>> EXECUTANDO EXEMPLO 1' && java -jar jython.jar exemplo1.py && echo '' && echo '>>> EXECUTANDO EXEMPLO 2' && java -jar jython.jar exemplo2.py"]
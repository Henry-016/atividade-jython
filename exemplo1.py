from java.net import URL, HttpURLConnection
from java.io import BufferedReader, InputStreamReader
from java.security import MessageDigest

def executar():
    endpoint = "https://httpbin.org/get"
    print("[1] Conectando a: " + endpoint)
    
    url = URL(endpoint)
    conexao = url.openConnection()
    conexao.setRequestMethod("GET")
    conexao.setRequestProperty("User-Agent", "Jython-Client")
    
    codigo_resposta = conexao.getResponseCode()
    print("[2] Status HTTP retornado: " + str(codigo_resposta))

    leitor = BufferedReader(InputStreamReader(conexao.getInputStream()))
    linhas = []
    linha = leitor.readLine()
    while linha is not None:
        linhas.append(linha)
        linha = leitor.readLine()
    leitor.close()

    conteudo = "\n".join(linhas)
    print("\n--- Resposta da API (Primeiros 200 caracteres) ---")
    print(conteudo[:200] + "...\n")

    digest = MessageDigest.getInstance("SHA-256")
    hash_bytes = digest.digest(conteudo.encode("utf-8"))
    
    hash_hex = "".join(["%02x" % (b & 0xFF) for b in hash_bytes])
    print("[3] SHA-256 da resposta calculada via JVM:")
    print("    " + hash_hex)

if __name__ == "__main__":
    executar()

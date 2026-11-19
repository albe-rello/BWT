from BWT import BWT_TRANS
import socket as sck

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

with server:
    IP = "127.0.0.1"
    PORTA = 5000

    server.bind((IP, PORTA))
    server.listen(5)

    print("Server in ascolto su:", IP, " Porta:", PORTA)

    connessione, indirizzo_client = server.accept()

    with connessione:

        print("Socket di connessione:", connessione.getsockname())

        dati = connessione.recv(1024)

        #print("Messaggio ricevuto dal client:", dati.decode())

        parola=dati.decode()
        
        Risultato_finale = BWT_TRANS(parola)
        
        connessione.sendall(Risultato_finale.encode())

print("Server terminato")
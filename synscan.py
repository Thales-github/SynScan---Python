from scapy.all import IP, TCP, sr1, send

alvo = "127.0.0.1" # loopback(máquina local), mas poderia ser um IP/domínio externo: "www.google.com"

# 80 → HTTP, # 443 → HTTPS, # 8080 → HTTP alternativo, # 3306 → MySQL
portasProcuradas = [80, 443, 8080, 3306] # Poderia ser um rang(1,1024) para escanear todas as portas, mas isso pode ser demorado

for portaPercorrida in portasProcuradas:

    pacote = IP(dst=alvo) / TCP(dport=portaPercorrida, flags="S")
    resposta = sr1(pacote, timeout=1, verbose=0)

    if resposta is None:
        print(f"Porta {portaPercorrida}: FILTRADA ou sem resposta")

    elif resposta.haslayer(TCP):

        if resposta[TCP].flags == "SA":
            print(f"Porta {portaPercorrida}: ABERTA")
            send(IP(dst=alvo) / TCP(dport=portaPercorrida, flags="R"), verbose=0)

        elif resposta[TCP].flags == "RA":
            print(f"Porta {portaPercorrida}: FECHADA")
        
    else:
        print(f"Porta {portaPercorrida}: RESPOSTA DESCONHECIDA")
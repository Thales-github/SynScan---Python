# 🕵️‍♂️ Port Scanner com Scapy

Um projeto que demonstra, na prática, como funcionam técnicas de **reconhecimento (recon)** e **varredura de portas** utilizando pacotes TCP personalizados com a linguagem **Python** e a biblioteca **Scapy**.

Este projeto é ideal para quem deseja aprender mais sobre **segurança ofensiva(RED TEAM)**, **análise de redes**, **pentest básico** e **comportamento de flags TCP**.
---

## 📌 Conceitos Fundamentais

### 🚨 Reconhecimento (Recon) Ativo  
Interação direta com o sistema alvo para obter respostas.  
Aqui existe risco de detecção, pois você está literalmente “batendo na porta”.
Por este motivo o programa foi desenvolvido aplicando conceitos de SynScan, para evitar o rastreio de FireWall e Log´s de sistema.

---

## 📡 Flags TCP e Seus Significados

| Flag | Nome    | Significado                      |
| ---- | ------- | -------------------------------- |
| S    | SYN     | Solicita início de conexão       |
| A    | ACK     | Confirma recebimento             |
| SA   | SYN-ACK | Porta aberta (resposta positiva) |
| R    | RST     | Reset — conexão rejeitada        |
| RA   | RST-ACK | Porta fechada                    |
| F    | FIN     | Finaliza conexão de forma limpa  |

Essas respostas são essenciais para interpretar o estado de uma porta durante um scan.

---

## 🛠️ Instalação e Dependências

### 1️⃣ Instalar o Scapy

1. **Certifique-se de ter o Python e o pip instalados**  
   - O Scapy é uma biblioteca Python, então é necessário ter o Python instalado no sistema.
    ```bash
        pip install scapy
    ```
        
   - O pip (gerenciador de pacotes do Python) geralmente já vem junto com a instalação do Python.  
   - Para verificar se o pip está disponível, execute no terminal:
    ```bash
      pip --version
    ```

1. **Caso você utilize o S.O Windows**  
    1) baixar Npcap, para pacotes brutos no windows: https://npcap.com/#download
    2) Na instalação do Npcap, marcar o flag de modo de compatibilidade caso esteja desmarcado para evitar erros de permissão: "Install Npcap in WinPcap API-compatible Mode"
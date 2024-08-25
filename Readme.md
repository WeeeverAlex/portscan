# Port Scanner

## Descrição

Este projeto é uma ferramenta de escaneamento de portas desenvolvida em Python. O scanner permite identificar quais portas estão abertas em um host específico e relaciona essas portas com seus serviços bem conhecidos. A ferramenta é útil para administradores de rede e profissionais de segurança que precisam mapear portas abertas e serviços em uma rede.

## Funcionalidades

- **Escaneamento de Portas TCP:** Escaneia um intervalo de portas TCP em um host especificado.
- **Identificação de Serviços:** Relaciona as portas escaneadas com serviços bem conhecidos (por exemplo, HTTP, FTP, SSH).
- **Interface Gráfica Amigável:** Inclui uma interface gráfica (GUI) construída com Tkinter, tornando o uso simples e acessível.
- **Configuração de Intervalo de Portas:** Permite ao usuário inserir o intervalo de portas a serem escaneadas.
- **Compatibilidade:** Funciona em ambientes Windows, macOS e Linux.

## Como Usar

### 1. Requisitos

Certifique-se de ter o Python instalado. Este projeto foi desenvolvido usando Python 3.x. 

### 2. Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/WeeeverAlex/portscan.git
   ```

2. **Instale as dependências:**
   - Se estiver usando a interface gráfica (Tkinter), ela já está incluída na instalação padrão do Python.
   - Para instalar as dependências adicionais, caso necessário:
     ```bash
     pip install -r requirements.txt
     ```

### 3. Execução

1. **Execute o script:**
   ```bash
   python3 port_scanner.py
   ```

2. **Use a Interface Gráfica:**
   - Insira o endereço do host no campo "Host" (por exemplo, `localhost` ou o IP do servidor).
   - Insira o intervalo de portas para escanear (`Start Port` e `End Port`).
   - Clique em "Scan" para iniciar o escaneamento.

3. **Visualize os Resultados:**
   - As portas abertas serão listadas junto com o serviço associado, se identificado.

### 4. Testes

Para verificar o funcionamento da ferramenta, você pode testar portas com serviços ativos em sua máquina local, como iniciar um servidor HTTP em `localhost:8080` ou um servidor FTP em `localhost:21`.

```bash
# Exemplo para iniciar um servidor HTTP em localhost:8080
python3 -m http.server 8080
```

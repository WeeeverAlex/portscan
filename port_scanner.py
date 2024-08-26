import socket
import tkinter as tk
from tkinter import messagebox

# Dicionário com portas e serviços bem conhecidos
well_known_ports = {
    20: 'FTP Data',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    443: 'HTTPS',
    3389: 'Remote Desktop',
    8080: 'HTTP (Alternative)',
    # Adicione mais portas conforme necessário
}

# Função para resolver nome de domínio em IP
def resolve_host(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None

# Função para escanear uma única porta
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = well_known_ports.get(port, 'Unknown service')
            return f"Port {port} is open ({service})\n"
        else:
            return f"Port {port} is closed\n"
        sock.close()
    except Exception as e:
        return f"An error occurred: {e}\n"

# Função para escanear um intervalo de portas
def scan_ports_gui():
    host = host_entry.get()
    ip = resolve_host(host)
    if ip is None:
        result_text.insert(tk.END, f"Could not resolve {host}\n")
        return
    
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    result_text.delete(1.0, tk.END)
    
    result_text.insert(tk.END, f"Scanning {host} ({ip}) from port {start_port} to {end_port}\n")
    for port in range(start_port, end_port + 1):
        result = scan_port(ip, port)
        result_text.insert(tk.END, result)

# Função para iniciar o scanner
def start_scanner():
    menu_frame.pack_forget()
    scanner_frame.pack()

# Função para sair do programa
def exit_program():
    root.quit()

# Configuração da interface gráfica usando Tkinter
root = tk.Tk()
root.title("Port Scanner")

# Ajustar o tamanho da janela
root.geometry("600x400")  # Define o tamanho da janela para 600x400 pixels

# Frame do Menu Principal
menu_frame = tk.Frame(root)
tk.Label(menu_frame, text="Bem-vindo ao Port Scanner", font=('Helvetica', 20)).pack(pady=40)  # Fonte maior e mais espaçamento
tk.Button(menu_frame, text="Iniciar Scanner", command=start_scanner, width=30, height=2).pack(pady=20)  # Botão maior
tk.Button(menu_frame, text="Sair", command=exit_program, width=30, height=2).pack(pady=10)  # Botão maior
menu_frame.pack()

# Frame do Scanner de Portas
scanner_frame = tk.Frame(root)

# Campo para o endereço do host
tk.Label(scanner_frame, text="Host or IP:").grid(row=0, column=0, padx=10, pady=10)
host_entry = tk.Entry(scanner_frame)
host_entry.grid(row=0, column=1, padx=10, pady=10)

# Campo para a porta inicial
tk.Label(scanner_frame, text="Start Port:").grid(row=1, column=0, padx=10, pady=10)
start_port_entry = tk.Entry(scanner_frame)
start_port_entry.grid(row=1, column=1, padx=10, pady=10)

# Campo para a porta final
tk.Label(scanner_frame, text="End Port:").grid(row=2, column=0, padx=10, pady=10)
end_port_entry = tk.Entry(scanner_frame)
end_port_entry.grid(row=2, column=1, padx=10, pady=10)

# Botão para iniciar o escaneamento
scan_button = tk.Button(scanner_frame, text="Scan", command=scan_ports_gui)
scan_button.grid(row=3, column=0, columnspan=2, pady=20)

# Caixa de texto para mostrar os resultados
result_text = tk.Text(scanner_frame, height=10, width=50)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicializa a interface gráfica
root.mainloop()
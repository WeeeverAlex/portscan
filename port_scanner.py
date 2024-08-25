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

# Função para escanear uma única porta
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
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
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    result_text.delete(1.0, tk.END)
    
    for port in range(start_port, end_port + 1):
        result = scan_port(host, port)
        result_text.insert(tk.END, result)

# Configuração da interface gráfica usando Tkinter
root = tk.Tk()
root.title("Port Scanner")

# Campo para o endereço do host
tk.Label(root, text="Host:").grid(row=0, column=0)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1)

# Campo para a porta inicial
tk.Label(root, text="Start Port:").grid(row=1, column=0)
start_port_entry = tk.Entry(root)
start_port_entry.grid(row=1, column=1)

# Campo para a porta final
tk.Label(root, text="End Port:").grid(row=2, column=0)
end_port_entry = tk.Entry(root)
end_port_entry.grid(row=2, column=1)

# Botão para iniciar o escaneamento
scan_button = tk.Button(root, text="Scan", command=scan_ports_gui)
scan_button.grid(row=3, column=0, columnspan=2)

# Caixa de texto para mostrar os resultados
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, column=0, columnspan=2)

# Inicializa a interface gráfica
root.mainloop()

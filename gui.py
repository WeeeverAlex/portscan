import tkinter as tk
from tkinter import messagebox

def scan_ports_gui():
    host = host_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    result_text.delete(1.0, tk.END)
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                service = well_known_ports.get(port, 'Unknown service')
                result_text.insert(tk.END, f"Port {port} is open ({service})\n")
            sock.close()
        except Exception as e:
            result_text.insert(tk.END, f"An error occurred: {e}\n")

# Criação da interface Tkinter
root = tk.Tk()
root.title("Port Scanner")

tk.Label(root, text="Host:").grid(row=0, column=0)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1)

tk.Label(root, text="Start Port:").grid(row=1, column=0)
start_port_entry = tk.Entry(root)
start_port_entry.grid(row=1, column=1)

tk.Label(root, text="End Port:").grid(row=2, column=0)
end_port_entry = tk.Entry(root)
end_port_entry.grid(row=2, column=1)

scan_button = tk.Button(root, text="Scan", command=scan_ports_gui)
scan_button.grid(row=3, column=0, columnspan=2)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, column=0, columnspan=2)

root.mainloop()

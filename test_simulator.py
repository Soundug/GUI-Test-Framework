import tkinter as tk
from tkinter import ttk, filedialog
import time
import random

# Initialize main window
root = tk.Tk()
root.title("Infineon Test Automation Simulator")

# Device list
devices = ["Oscilloscope", "Multimeter", "Power Supply", "Signal Generator"]

# GUI Components
label = tk.Label(root, text="Select Device:")
label.pack(pady=5)

device_var = tk.StringVar()
device_dropdown = ttk.Combobox(root, textvariable=device_var)
device_dropdown['values'] = devices
device_dropdown.pack(pady=5)
device_dropdown.current(0)

log_display = tk.Text(root, height=20, width=70)
log_display.pack(pady=10)

# Function to simulate diagnostics and log output
logs = []

def run_test():
    selected_device = device_var.get()
    log_lines = []

    timestamp = time.strftime("[%H:%M:%S]")
    log_lines.append(f"{timestamp} {selected_device} initialized...")

    time.sleep(0.2)
    timestamp = time.strftime("[%H:%M:%S]")
    log_lines.append(f"{timestamp} Running diagnostics...")

    time.sleep(0.2)
    result = random.choice(["✅ Test passed", "❌ Test failed"])
    timestamp = time.strftime("[%H:%M:%S]")
    log_lines.append(f"{timestamp} {result}\n{'-'*60}")

    for line in log_lines:
        log_display.insert(tk.END, line + "\n")
        logs.append(line)

    log_display.see(tk.END)

# Function to export logs
def export_logs():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            for line in logs:
                f.write(line + "\n")

# Buttons
run_button = tk.Button(root, text="Run Test", command=run_test)
run_button.pack(pady=5)

export_button = tk.Button(root, text="Export Logs", command=export_logs)
export_button.pack(pady=5)

# Run the app
root.mainloop()
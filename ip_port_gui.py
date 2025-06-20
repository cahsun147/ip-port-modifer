import tkinter as tk
from tkinter import filedialog, messagebox

def append_port_to_ips(input_path, port, output_path):
    try:
        with open(input_path, 'r') as infile:
            ips = [line.strip() for line in infile if line.strip()]

        with open(output_path, 'w') as outfile:
            for ip in ips:
                outfile.write(f"{ip}:{port}\n")

        messagebox.showinfo("Success", f"✅ File saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"❌ {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text Files", "*.txt")])
    entry_input.delete(0, tk.END)
    entry_input.insert(0, file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(title="Save Output File As", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    entry_output.delete(0, tk.END)
    entry_output.insert(0, file_path)

def on_convert():
    input_path = entry_input.get()
    port = entry_port.get()
    output_path = entry_output.get()

    if not input_path or not output_path or not port:
        messagebox.showwarning("Missing Input", "Please fill in all fields.")
        return
    if not port.isdigit():
        messagebox.showwarning("Invalid Port", "Port must be a number.")
        return

    append_port_to_ips(input_path, port, output_path)

# GUI
root = tk.Tk()
root.title("IP Port Modifer | GUI Version - Made by Cahsun147")
root.geometry("500x300")
root.configure(bg="#1a1a1a")
root.resizable(False, False)

# Style for shadow effect and smooth corners
style = {"bg": "#2c2c2c", "fg": "#ffffff", "relief": "flat", "bd": 0, "highlightthickness": 0, "insertbackground": "#ffffff"}
shadow_style = {"bg": "#242424", "relief": "flat", "bd": 0, "highlightthickness": 0}

# Main frame with shadow effect
main_frame = tk.Frame(root, bg="#242424", padx=5, pady=5)
main_frame.pack(padx=1, pady=1, fill="both", expand=True)

# Inner frame for content
content_frame = tk.Frame(main_frame, bg="#2c2c2c", padx=10, pady=10)
content_frame.pack(fill="both", expand=True, padx=3, pady=3)

# Frame for Input File
frame_input = tk.Frame(content_frame, bg="#2c2c2c")
frame_input.pack(pady=5, fill="x")
tk.Label(frame_input, text="Input File:", bg="#2c2c2c", fg="#ffffff", font=("Arial", 10, "bold")).pack(side="left")
entry_input = tk.Entry(frame_input, width=35, bg="#2c2c2c", fg="#ffffff", relief="solid", bd=1, insertbackground="#ffffff", highlightthickness=1, highlightbackground="#ffffff")
entry_input.pack(side="left", padx=5, expand=True, fill="x")
tk.Button(frame_input, text="📂 Browse", command=select_input_file, bg="#3a3a3a", fg="#ffffff", font=("Arial", 8), padx=8, pady=3, relief="flat").pack(side="left")

# Frame for Port
frame_port = tk.Frame(content_frame, bg="#2c2c2c")
frame_port.pack(pady=5, fill="x")
tk.Label(frame_port, text="Port to Append:", bg="#2c2c2c", fg="#ffffff", font=("Arial", 10, "bold")).pack(side="left")
entry_port = tk.Entry(frame_port, width=20, bg="#2c2c2c", fg="#ffffff", relief="solid", bd=1, insertbackground="#ffffff", highlightthickness=1, highlightbackground="#ffffff")
entry_port.pack(side="left", padx=5)

# Frame for Output File
frame_output = tk.Frame(content_frame, bg="#2c2c2c")
frame_output.pack(pady=5, fill="x")
tk.Label(frame_output, text="Output File:", bg="#2c2c2c", fg="#ffffff", font=("Arial", 10, "bold")).pack(side="left")
entry_output = tk.Entry(frame_output, width=35, bg="#2c2c2c", fg="#ffffff", relief="solid", bd=1, insertbackground="#ffffff", highlightthickness=1, highlightbackground="#ffffff")
entry_output.pack(side="left", padx=5, expand=True, fill="x")
tk.Button(frame_output, text="💾 Save As", command=save_file, bg="#3a3a3a", fg="#ffffff", font=("Arial", 8), padx=8, pady=3, relief="flat").pack(side="left")

# Convert & Save button with hover effect
convert_button = tk.Button(content_frame, text="🚀 Convert & Save", command=on_convert, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=18, padx=8, pady=5, relief="flat")
convert_button.pack(pady=10)

def on_enter(e):
    convert_button['bg'] = "#45a049"

def on_leave(e):
    convert_button['bg'] = "#4CAF50"

convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# Footer Label
tk.Label(root, text="🛠 Made by Cahsun147", fg="#a0a0a0", bg="#1a1a1a", font=("Arial", 8)).pack(side="bottom", pady=5)

root.mainloop()

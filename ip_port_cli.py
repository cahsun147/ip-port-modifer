# ip_port_cli.py

import os

def banner():
    print(r'''


         _                      _                   _ _  __         
        (_)_ __   _ __  ___ _ _| |_   _ __  ___  __| (_)/ _|___ _ _ 
        | | '_ \ | '_ \/ _ \ '_|  _| | '  \/ _ \/ _` | |  _/ -_) '_|
        |_| .__/ | .__/\___/_|  \__| |_|_|_\___/\__,_|_|_| \___|_|  
        |_|      |_|                                                

                    📦 IP Port Modifier | CLI Version
                        🛠 Made by Cahsun147 🛠
    ''')

def get_user_input():
    input_file = input("📄 Enter input file name (e.g., host.txt): ").strip()
    while not os.path.exists(input_file):
        print("❌ File not found. Please try again.")
        input_file = input("📄 Enter input file name (e.g., host.txt): ").strip()

    port = input("🔌 Enter port to append (e.g., 8080): ").strip()
    while not port.isdigit():
        print("❌ Port must be a number.")
        port = input("🔌 Enter port to append (e.g., 8080): ").strip()

    output_file = input("💾 Enter output file name (e.g., host_with_port.txt): ").strip()
    if not output_file:
        output_file = "host_with_port.txt"

    return input_file, port, output_file

def append_port_to_ips(input_file, port, output_file):
    with open(input_file, 'r') as infile:
        ips = [line.strip() for line in infile if line.strip()]

    with open(output_file, 'w') as outfile:
        for ip in ips:
            outfile.write(f"{ip}:{port}\n")

    print(f"\n✅ Successfully saved to: {output_file}")

if __name__ == "__main__":
    banner()
    input_file, port, output_file = get_user_input()
    append_port_to_ips(input_file, port, output_file)

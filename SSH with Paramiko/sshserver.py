import os
import paramiko  # type: ignore
import socket
import sys
import threading

# Get the current script directory
CWD = os.path.dirname(os.path.realpath(__file__))

# Load unencrypted RSA host key
HOSTKEY_PATH = os.path.join(CWD, 'test_rsa.key')
try:
    HOSTKEY = paramiko.RSAKey.from_private_key_file(HOSTKEY_PATH)
except paramiko.PasswordRequiredException:
    print("[-] The private key file is encrypted. Please generate a key without a passphrase.")
    sys.exit(1)
except FileNotFoundError:
    print(f"[-] Key file not found at: {HOSTKEY_PATH}")
    sys.exit(1)

# SSH server class
class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == 'enter username' and password == 'enter password':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

# Start SSH server
if __name__ == '__main__':
    server_ip = 'Enter your IP'  # Change to your server's IP if needed
    ssh_port = 2222

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server_ip, ssh_port))
        sock.listen(100)
        print(f"[+] Listening for SSH connection on {server_ip}:{ssh_port}...")
        client, addr = sock.accept()
    except Exception as e:
        print(f"[-] Listen failed: {e}")
        sys.exit(1)

    print(f"[+] Got a connection from {addr}")

    try:
        bhSession = paramiko.Transport(client)
        bhSession.add_server_key(HOSTKEY)
        server = Server()
        bhSession.start_server(server=server)

        chan = bhSession.accept(20)
        if chan is None:
            print("[!] No channel.")
            sys.exit(1)

        print("[+] Authenticated!")
        chan.send(b'Welcome to bh_ssh\n')

        while True:
            try:
                command = input("Enter command: ").strip()
                if not command:
                    continue
                if command.lower() == 'exit':
                    chan.send(b'exit')
                    print("[*] Exiting.")
                    bhSession.close()
                    break
                chan.send(command.encode())
                response = chan.recv(8192)
                print(response.decode())
            except Exception as e:
                print(f"[!] Exception: {e}")
                break
    except KeyboardInterrupt:
        print("\n[*] Server interrupted by user.")
    finally:
        bhSession.close()

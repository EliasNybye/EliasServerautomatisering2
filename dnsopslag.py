import socket
hostname = input("Enter a domain/hostname: ").strip()
if not hostname:
    print("No hostname provided.")
else:
    try:
        ip = socket.gethostbyname(hostname)
        print(f'{hostname} IP: {ip}')
    except socket.gaierror as e:
        print(f'invalid hostname, error raised is {e}')
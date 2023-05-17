import socket

def is_internet_connected():
    try:
        # Attempt to resolve the Google DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False

if is_internet_connected():
    print("Connected to the internet.")
else:
    print("Not connected to the internet.")
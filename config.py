import socket

def get_local_ip():
    """
    Get the local IP address of the machine.
    """
    # Create a socket connection to a public DNS server
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Connecting to a public DNS server
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        except Exception:
            # Fallback to hostname method if unable to connect
            local_ip = socket.gethostbyname(socket.gethostname())
    return local_ip

def print_website_url(port):
    """
    Print the website URL with the local IP address and specified port.
    """
    local_ip = get_local_ip()
    print(f"Access your website from your phone using this URL: http://{local_ip}:{port}")

if __name__ == "__main__":
    port = 5002  # The port your Flask app is running on
    print_website_url(port)
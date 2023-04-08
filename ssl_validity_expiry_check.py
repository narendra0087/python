import ssl
import socket
import datetime

def check_ssl_validity(url):
    hostname, port = url.split(':')[0], int(url.split(':')[1])
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.connect((hostname, port))
    certificate = conn.getpeercert()
    expires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
    return expires, (expires - datetime.datetime.now()).days

url = "www.suneratech.com:443"
expires, remaining_days = check_ssl_validity(url)
print(f"The SSL certificate for {url} expires on {expires} and has {remaining_days} days remaining.")

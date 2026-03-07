import socket
import time
import threading
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP: ")
n = int(input("Enter the number of ports to scan: "))
open_ports = 0
lock = threading.Lock()
print("Scanning target:", target)
start = time.perf_counter()

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port", port, "is OPEN")
        global open_ports
        open_ports = open_ports
        with lock:
            open_ports+=1
    s.close()

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan, range(1, n+1))
    
end = time.perf_counter()
print("Scanned " + str(n) + " ports in:", round(end-start, 3)," seconds")
print(open_ports, "Open ports found")
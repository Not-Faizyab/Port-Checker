import socket
import time

target = input("Enter target IP: ")
n = int(input("Enter the number of ports to scan: "))
timereq = int(input("Enter the number of seconds you want to complete the scan in(Note: Entering a value < 0.5 seconds may miss open ports): "))
print("Scanning target:", target)

start = time.perf_counter()
for port in range(1, n+1):
    print("scanning...", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timereq/n)
    st=time.perf_counter()
    result = s.connect_ex((target, port))
    en=time.perf_counter()
    if result == 0:
        print("Port", port, "is OPEN")
    s.close()
end = time.perf_counter()
print("Time taken to scan " + str(n) + " ports:", round(end-start, 3))
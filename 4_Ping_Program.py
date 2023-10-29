from ping3 import ping, verbose_ping
host = "google.com"  # Replace with the host you want to ping
# Simple ping
response_time = ping(host)
if response_time is not None:
    print(f"Ping to {host} took {response_time} ms.")
else:
    print(f"Ping to {host} failed.")

# Verbose ping with statistics
statistics = verbose_ping(host, count=4)  # Change count as needed
if statistics is not None:
    print(statistics)
else:
    print(f"Ping to {host} failed.")

import subprocess
def main():
    try:
        ip = input("Enter IP address or domain name: ")
        command = f"nslookup {ip}"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            output = result.stdout
            print(output)
        else:
            error = result.stderr
            print(error)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

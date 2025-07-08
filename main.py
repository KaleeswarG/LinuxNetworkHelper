import subprocess

def getio():
    print("YOUR IP:")
    subprocess.run(["hostname", "-I"])

def ping():
    site = input("ENTER WEBSITE: ")
    subprocess.run(["ping", "-c", "4", site])

def gtw():
    print("GATEWAY:")
    subprocess.run("ip route | grep default", shell=True)

def intc():
    print("NETWORK CONNECTION:")
    result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True)
    if result.returncode == 0:
        print("Connection working.")
    else:
        print("Not connected to the internet.")

while True:
    print("====== UBUNTU NETWORKING TOOL =====")
    print("1. SHOW IP ADDRESS")
    print("2. PING A WEBSITE")
    print("3. SHOW DEFAULT GATEWAY")
    print("4. CHECK INTERNET CONNECTIVITY")
    print("5. EXIT")
    
    ch = input("\nENTER CHOICE: ")

    match ch:
        case "1":
            getio()
        case "2":
            ping()
        case "3":
            gtw()
        case "4":
            intc()
        case "5":
            print("THANK YOU")
            break
        case _:
            print("INVALID INPUT")


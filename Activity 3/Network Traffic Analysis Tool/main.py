# Add a new Log to logs:
def addLog(logs):
    srcip=input("Enter source IP: ")
    desip=input("Enter desitination IP: ")
    protocol=input("Enter protocol: ")
    ip=int(input("Enter bytes transferred: "))

    logs.append((srcip,desip,protocol,ip))

    print("Log entry added successfully!")

# Display the logs in logs:
def displayLogs(logs):
    if len(logs) == 0:
        print("No Logs have been added!")
        return

    print("Network Traffic Logs:")
    
    for log in logs:
        print(f"Source IP: {log[0]}, Destination IP: {log[1]}, Protocol: {log[2]}, Bytes Transferred: {log[3]}")

# Search Log:
def search(logs):
    IP = input("Enter the IP to search: ")

    print(f"Log entries involving IP {IP}")
    try:
        found=False
        for log in logs:
            if log[0] == IP or log[1]== IP:
                found=True
                print(f"Source IP: {log[0]}, Destination IP: {log[1]}, Protocol: {log[2]}, Bytes Transferred: {log[3]}")
        
        if not found:
            raise Exception(f"No Log with IP {IP} in the logs")
    except Exception as err:
        print(str(err))

# Filter Logs:
def filterLogs(logs):
    protocol =  input("Enter the Protocol to filter: ")

    for Log in logs:
        if Log[2] == protocol:
            print(f"- {Log[0]}")

# Calcualate the bytes:
def calcBytesTrans(logs):
    totalBytes=0

    for log in logs:
        totalBytes+=log[3]

    print("Total bytes transfrred: ", totalBytes)


def main():
    # Shoping List:
    logs=[]
    print("Welcome to the Network Traffic Analysis Tool!")

    print("\n1. Add Log Entries")
    print("\n2. Display Log Entries")
    print("\n3. Search for Log Entries by IP")
    print("\n4. Calculate Total Bytes Transferred")
    print("\n5. Filter Log Entries by Protocol")
    print("\n6. Exit")

    while(True):
        choice=int(input("\nEnter your choice:"))

        if choice==1:
            addLog(logs)
        elif choice==2:
            displayLogs(logs)
        elif choice==3:
            search(logs)
        elif choice==4:
            calcBytesTrans(logs)
        elif choice==5:
            filterLogs(logs)
        elif choice==6:
            exit()
        else:
            print("Invalid Choice!")

if __name__=="__main__":
    main()
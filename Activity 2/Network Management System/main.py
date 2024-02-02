

# Add a new device to devices:
def addDevice(devices):
    name=input("Enter device name: ")
    type=input("Enter device type: ")
    ip=input("Enter IP address: ")

    devices.append([name,type,ip])

    print("Device added successfully!")

# Display the devices in devices:
def displayDevices(devices):
    if len(devices) == 0:
        print("Devices have been added!")
        return

    print("Network Devices:")
    
    for device in devices:
        print(f"Name: {device[0]}, Type: {device[1]}, IP Address: {device[2]}")

# Remove an item from devices:
def removeDevices(devices):
    device = input("Enter the device name to remove: ")
    
    try:
        found=False
        for item in devices:
            if item[0]== device:
                found=True
                devices.remove(item)
                print(f"{item} was removed from the devices")
        
        if not found:
            raise Exception(f"No device with name {device} in the devices")
    except Exception as err:
        print(str(err))

# Search device:
def search(devices):
    device = input("Enter the device name to search: ")

    try:
        found=False
        for item in devices:
            if item[0] == device:
                found=True
                print("Device Found")
                print(f"Name: {item[0]}, Type: {item[1]}, IP Address: {item[2]}")
        
        if not found:
            raise Exception(f"No device with name {device} in the devices")
    except Exception as err:
        print(str(err))

# Filter Devices:
def filterDevices(devices):
    type =  input("Enter the device type to filter: ")

    for device in devices:
        if device[1] == type:
            print(f"- {device[0]}")


def main():
    # Shoping List:
    devices=[]
    print("Welcome to the Network Device Management System!")

    print("\n1. Add Device")
    print("\n2. Display Devices")
    print("\n3. Search for a Device")
    print("\n4. Filter Devices by Type")
    print("\n5. Remove Device")
    print("\n6. Exit")

    while(True):
        choice=int(input("\nEnter your choice:"))

        if choice==1:
            addDevice(devices)
        elif choice==2:
            displayDevices(devices)
        elif choice==3:
            search(devices)
        elif choice==4:
            filterDevices(devices)
        elif choice==5:
            removeDevices(devices)
        elif choice==6:
            exit()
        else:
            print("Invalid Choice!")

if __name__=="__main__":
    main()
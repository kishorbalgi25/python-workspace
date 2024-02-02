# Add a new Attendee to attendees:
def addAttendee(attendees):
    name = input("Enter the attendee name: ")

    attendees.add(name)

    print("Attendee entry added successfully!")

# Display the attendees in attendees:
def displayAttendees(attendees):
    if len(attendees) == 0:
        print("No Attendees have been added!")
        return

    print("Attendee Names:")
    
    for attendee in attendees:
        print(attendee)

# Search Attendee:
def checkAttendee(attendees):
    name = input("Enter the name: ")

    print(f"Attendee entries involving IP {name}")
    try:
        if name in attendees:
            print(f"{name} is present")
        else:
            raise Exception(f"No Attendee with name {name} in the attendees")
    except Exception as err:
        print(str(err))

def removeAttendee(attendees):
    name = input("Enter the name to be removed: ")

    if name in attendees:
        attendees.remove(name)
    else:
        print(f"No Attendee with name {name} in the attendees")

# Calcualate the bytes:
def calcStats(attendees):
    print(f"Total unique attendees: {len(attendees)}")


def main():
    # Shoping List:
    attendees=set()
    print("Welcome to the Event Attendance Tracking System!")

    print("\n1. Record Attendees")
    print("\n2. Display Attendees")
    print("\n3. Check Attendance")
    print("\n4. Remove Attendee")
    print("\n5. Calculate Attendee Statistics")
    print("\n6. Exit")

    while(True):
        choice=int(input("\nEnter your choice:"))

        if choice==1:
            addAttendee(attendees)
        elif choice==2:
            displayAttendees(attendees)
        elif choice==3:
            checkAttendee(attendees)
        elif choice==4:
            removeAttendee(attendees)
        elif choice==5:
            calcStats(attendees)
        elif choice==6:
            exit()
        else:
            print("Invalid Choice!")

if __name__=="__main__":
    main()
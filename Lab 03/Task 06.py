print("Firefighting Robot Simulation")
print()

environment = {
    'a': 'safe', 'b': 'safe', 'c': 'fire',
    'd': 'safe', 'e': 'fire', 'f': 'safe',
    'g': 'safe', 'h': 'safe', 'j': 'fire'
}

path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

def display_environment():
    rooms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    for i in range(0, 9, 3):
        row = rooms[i:i+3]
        for room in row:
            if environment[room] == "fire":
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()

print("Initial Environment State:")
display_environment()

for room in path:
    print("Robot moved to room", room)

    if environment[room] == "fire":
        print("Fire detected! Extinguishing fire...")
        environment[room] = "safe"
    else:
        print("Room is already safe")

    display_environment()

print("Final Environment: All rooms are safe")
display_environment()

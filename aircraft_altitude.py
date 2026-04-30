from aircraft import Aircraft

model = input("Enter aircraft model:\n")
plane = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

    if command == "X":
        break

    parts = command.split()

    if len(parts) != 2:
        continue

    action = parts[0]
    value = int(parts[1])

    if action == "A":
        plane.ascend(value)
    elif action == "D":
        plane.descend(value)

print(f"Final altitude: {plane.altitude} feet")
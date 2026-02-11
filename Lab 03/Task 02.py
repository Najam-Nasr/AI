import random

class ClassroomWorld:
    def __init__(self):
        self.presence = "No"
        self.light_state = "OFF"

    def sense(self):
        self.presence = random.choice(["Yes", "No"])
        return {"presence": self.presence, "light": self.light_state}

    def update_light(self, new_state):
        self.light_state = new_state


class SmartLightController:
    def __init__(self):
        self.memory = {"last_presence": None, "last_light": "OFF"}

    def decide_action(self, input_data):
        current_presence = input_data["presence"]
        current_light = input_data["light"]

        if current_presence == "Yes" and current_light == "OFF":
            decision = "Switch ON"
        elif current_presence == "No" and current_light == "ON":
            decision = "Switch OFF"
        else:
            decision = "Maintain State"

        self.memory["last_presence"] = current_presence
        self.memory["last_light"] = current_light
        print(f"Memory State: {self.memory}")

        return decision


def execute(controller, world, cycles):
    count = 0
    while count < cycles:
        sensed_data = world.sense()
        result = controller.decide_action(sensed_data)

        if result == "Switch ON":
            world.update_light("ON")
        elif result == "Switch OFF":
            world.update_light("OFF")

        print(f"Round {count + 1}: Input={sensed_data}, Output={result}")
        count += 1


execute(SmartLightController(), ClassroomWorld(), 8)

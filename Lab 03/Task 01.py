class RoadCondition:
    def __init__(self, congestion):
        self.congestion = congestion

    def perceive(self):
        return self.congestion


class SignalAgent:
    def decide(self, situation):
        if situation == "Heavy Traffic":
            return "Increase Green Duration"
        elif situation == "Light Traffic":
            return "Standard Green Duration"
        else:
            return "No Change"


def simulate(agent_obj, road_obj):
    current_state = road_obj.perceive()
    response = agent_obj.decide(current_state)
    print(f"Current State: {current_state} --> Decision: {response}")


traffic_controller = SignalAgent()
simulate(traffic_controller, RoadCondition("Heavy Traffic"))
simulate(traffic_controller, RoadCondition("Light Traffic"))

class RewardBasedSystem:
    def __init__(self):
        self.scores = {"Play": 0.0, "Rest": 0.0}
        self.learning_factor = 0.1

    def process(self):
        best_option = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)[0][0]
        points = 5 if best_option == "Play" else 1

        previous_value = self.scores[best_option]
        difference = points - previous_value
        self.scores[best_option] = previous_value + self.learning_factor * difference

        return best_option, points


system = RewardBasedSystem()

counter = 1
while counter <= 10:
    choice, value = system.process()
    if counter in [1, 5, 10]:
        print(f"Iteration {counter} -> Choice: {choice}, Reward: {value}")
    counter += 1

print("Final Score Table:", system.scores)

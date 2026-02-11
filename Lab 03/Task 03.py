class StudyGoalAgent:
    def __init__(self, subjects):
        self.subjects = subjects
        self.goal = "Complete all subjects"

    def act(self):
        if not self.subjects:
            return "Goal Achieved: All subjects completed"
        # Study one subject at a time
        subject_to_study = self.subjects.pop(0)
        return f"Studying {subject_to_study}"

agent = StudyGoalAgent(['AI', 'Math', 'Physics'])
while True:
    action = agent.act()
    print(action)
    if "Goal Achieved" in action:
        break

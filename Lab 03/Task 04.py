class DiningDecisionMaker:
    def choose(self, options):
        top_choice = None
        highest_score = float("-inf")

        for place, info in options.items():
            score = info["rating"] - info["distance"]
            print(f"{place} Score: {score}")

            if score > highest_score:
                highest_score = score
                top_choice = place

        return top_choice


places_data = {
    "A": {"distance": 3, "rating": 7},
    "B": {"distance": 5, "rating": 9}
}

decision_agent = DiningDecisionMaker()
result = decision_agent.choose(places_data)
print(f"Best Option: {result}")

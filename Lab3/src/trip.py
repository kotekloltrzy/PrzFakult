class Trip:
    def __init__(self, destination, duration, participant_list = []):
        self.destination = destination
        self.duration = duration
        self.participant_list = participant_list

    def calculate_cost(self):
        day = 100
        cost = self.duration * day
        return cost

    def add_participant(self, *participants):
        for participant in participants:
            if participant == "" :
                raise ValueError("Participant name cannot be empty")
            else:
                self.participant_list.append(participant)
class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        self.matches.append((location, team1, team2, timing))

    def search_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match[1], match[2])]
        return team_matches

    def search_by_location(self, location):
        location_matches = [match for match in self.matches if match[0] == location]
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = [match for match in self.matches if match[3] == timing]
        return timing_matches


def main():
    flight_table = FlightTable()

    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India South", "Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")

    while True:
        print("Search options:")
        print("1. List of all matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter team name: ")
            team_matches = flight_table.search_by_team(team_name)
            print("Matches for team", team_name)
            for match in team_matches:
                print(match)

        elif choice == 2:
            location = input("Enter location: ")
            location_matches = flight_table.search_by_location(location)
            print("Matches at location", location)
            for match in location_matches:
                print(match)

        elif choice == 3:
            timing = input("Enter timing: ")
            timing_matches = flight_table.search_by_timing(timing)
            print("Matches with timing", timing)
            for match in timing_matches:
                print(match)

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
print("hello")
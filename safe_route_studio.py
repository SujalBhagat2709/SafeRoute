"""
SafeRoute Studio
----------------
Interactive interface for the SafeRoute system.

This application allows users to:

- Add travel routes
- View all available routes
- Analyze a specific route
- Compare all routes
- Choose a travel preference
- Get the best route recommendation
"""

from safe_route import SafeRoute


class SafeRouteStudio:

    def __init__(self):

        self.system = SafeRoute()

    # ----------------------------------
    # Add Route
    # ----------------------------------
    def add_route(self):

        print(
            "\n========== ADD ROUTE ==========\n"
        )

        route_id = input(
            "Route ID: "
        ).strip()

        # Check duplicate route ID
        if self.system.find_route(route_id):

            print(
                "\nRoute ID already exists."
            )

            return

        name = input(
            "Route Name: "
        ).strip()

        # Distance
        while True:

            try:

                distance = float(
                    input(
                        "Distance (km): "
                    )
                )

                if distance <= 0:

                    print(
                        "Distance must be greater than 0."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # Travel time
        while True:

            try:

                travel_time = float(
                    input(
                        "Estimated Travel Time (minutes): "
                    )
                )

                if travel_time <= 0:

                    print(
                        "Travel time must be greater than 0."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # Traffic level
        valid_levels = [

            "low",
            "medium",
            "high"

        ]

        while True:

            traffic_level = input(
                "Traffic Level (Low/Medium/High): "
            ).strip().lower()

            if traffic_level in valid_levels:

                break

            print(
                "Please enter Low, Medium, or High."
            )

        # Road condition
        valid_conditions = [

            "good",
            "average",
            "poor"

        ]

        while True:

            road_condition = input(
                "Road Condition "
                "(Good/Average/Poor): "
            ).strip().lower()

            if road_condition in valid_conditions:

                break

            print(
                "Please enter Good, Average, or Poor."
            )

        # Safety reports
        while True:

            try:

                safety_reports = int(
                    input(
                        "Number of Safety Reports: "
                    )
                )

                if safety_reports < 0:

                    print(
                        "Safety reports cannot be negative."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # Lighting level
        while True:

            lighting_level = input(
                "Lighting Level "
                "(Good/Average/Poor): "
            ).strip().lower()

            if lighting_level in valid_conditions:

                break

            print(
                "Please enter Good, Average, or Poor."
            )

        route = self.system.add_route(

            route_id,
            name,
            distance,
            travel_time,
            traffic_level,
            road_condition,
            safety_reports,
            lighting_level

        )

        print(
            "\nRoute added successfully."
        )

        print(
            f"Route: {route['Name']}"
        )

    # ----------------------------------
    # View All Routes
    # ----------------------------------
    def view_routes(self):

        if not self.system.routes:

            print(
                "\nNo routes available."
            )

            return

        print(
            "\n========== AVAILABLE ROUTES ==========\n"
        )

        for route in self.system.routes:

            print(
                f"{route['ID']} | "
                f"{route['Name']}"
            )

            print(
                f"  Distance: "
                f"{route['Distance']} km"
            )

            print(
                f"  Travel Time: "
                f"{route['Travel Time']} minutes"
            )

            print(
                f"  Traffic: "
                f"{route['Traffic Level'].title()}"
            )

            print(
                f"  Road Condition: "
                f"{route['Road Condition'].title()}"
            )

            print(
                f"  Safety Reports: "
                f"{route['Safety Reports']}"
            )

            print(
                f"  Lighting: "
                f"{route['Lighting Level'].title()}"
            )

            print()

    # ----------------------------------
    # Get Preference
    # ----------------------------------
    def get_preference(self):

        valid_preferences = [

            "safest",
            "fastest",
            "balanced"

        ]

        while True:

            preference = input(
                "\nChoose Preference "
                "(Safest/Fastest/Balanced): "
            ).strip().lower()

            if preference in valid_preferences:

                return preference

            print(
                "Please enter Safest, Fastest, "
                "or Balanced."
            )

    # ----------------------------------
    # Analyze Specific Route
    # ----------------------------------
    def analyze_route(self):

        if not self.system.routes:

            print(
                "\nNo routes available."
            )

            return

        print(
            "\n========== ANALYZE ROUTE ==========\n"
        )

        route_id = input(
            "Enter Route ID: "
        ).strip()

        preference = self.get_preference()

        self.system.display_route_analysis(

            route_id,
            preference

        )

    # ----------------------------------
    # Compare Routes
    # ----------------------------------
    def compare_routes(self):

        if not self.system.routes:

            print(
                "\nNo routes available."
            )

            return

        print(
            "\n========== COMPARE ROUTES =========="
        )

        preference = self.get_preference()

        self.system.display_comparison(
            preference
        )

    # ----------------------------------
    # Get Recommendation
    # ----------------------------------
    def get_recommendation(self):

        if not self.system.routes:

            print(
                "\nNo routes available."
            )

            return

        print(
            "\n========== GET RECOMMENDATION =========="
        )

        preference = self.get_preference()

        self.system.display_recommendation(
            preference
        )

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print(
                "                  SAFEROUTE"
            )
            print("=" * 60)

            print("1. Add Route")
            print("2. View All Routes")
            print("3. Analyze Route")
            print("4. Compare Routes")
            print("5. Get Best Route Recommendation")
            print("6. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_route()

            elif choice == "2":

                self.view_routes()

            elif choice == "3":

                self.analyze_route()

            elif choice == "4":

                self.compare_routes()

            elif choice == "5":

                self.get_recommendation()

            elif choice == "6":

                print(
                    "\nThank you for using SafeRoute."
                )

                break

            else:

                print(
                    "\nInvalid choice. Please try again."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = SafeRouteStudio()

    studio.menu()

"""
SafeRoute
---------
File: safe_route.py

Purpose
-------
Compares available travel routes and recommends
the safest and most suitable route.

The system considers:

- Distance
- Estimated travel time
- Traffic level
- Road condition
- Safety reports
- Lighting level
- User priority

The goal is not always to choose the shortest route.
It calculates a route score based on multiple factors
and recommends the most suitable option.
"""


class SafeRoute:

    def __init__(self):

        self.routes = []

    # ----------------------------------
    # Add Route
    # ----------------------------------
    def add_route(
            self,
            route_id,
            name,
            distance,
            travel_time,
            traffic_level,
            road_condition,
            safety_reports,
            lighting_level):

        route = {

            "ID": route_id,

            "Name": name,

            "Distance": distance,

            "Travel Time": travel_time,

            "Traffic Level":
                traffic_level.lower(),

            "Road Condition":
                road_condition.lower(),

            "Safety Reports":
                safety_reports,

            "Lighting Level":
                lighting_level.lower()
        }

        self.routes.append(route)

        return route

    # ----------------------------------
    # Find Route
    # ----------------------------------
    def find_route(
            self,
            route_id):

        for route in self.routes:

            if route["ID"] == route_id:

                return route

        return None

    # ----------------------------------
    # Traffic Risk Score
    # ----------------------------------
    def traffic_score(
            self,
            traffic_level):

        scores = {

            "low": 10,
            "medium": 25,
            "high": 45

        }

        return scores.get(
            traffic_level.lower(),
            25
        )

    # ----------------------------------
    # Road Condition Risk Score
    # ----------------------------------
    def road_condition_score(
            self,
            road_condition):

        scores = {

            "good": 5,
            "average": 20,
            "poor": 40

        }

        return scores.get(
            road_condition.lower(),
            20
        )

    # ----------------------------------
    # Lighting Risk Score
    # ----------------------------------
    def lighting_score(
            self,
            lighting_level):

        scores = {

            "good": 5,
            "average": 20,
            "poor": 40

        }

        return scores.get(
            lighting_level.lower(),
            20
        )

    # ----------------------------------
    # Safety Report Risk
    # ----------------------------------
    def safety_report_score(
            self,
            safety_reports):

        # More reported incidents
        # means higher route risk.

        return min(
            safety_reports * 10,
            50
        )

    # ----------------------------------
    # Calculate Safety Risk
    # ----------------------------------
    def calculate_safety_risk(
            self,
            route):

        traffic_risk = self.traffic_score(
            route["Traffic Level"]
        )

        road_risk = self.road_condition_score(
            route["Road Condition"]
        )

        lighting_risk = self.lighting_score(
            route["Lighting Level"]
        )

        report_risk = self.safety_report_score(
            route["Safety Reports"]
        )

        total_risk = (

            traffic_risk
            +
            road_risk
            +
            lighting_risk
            +
            report_risk

        )

        return min(
            total_risk,
            100
        )

    # ----------------------------------
    # Travel Efficiency Score
    # ----------------------------------
    def efficiency_score(
            self,
            route):

        # Lower distance and lower
        # travel time are better.

        distance_penalty = (
            route["Distance"] * 2
        )

        time_penalty = (
            route["Travel Time"] * 1
        )

        penalty = (
            distance_penalty
            +
            time_penalty
        )

        return max(
            0,
            100 - penalty
        )

    # ----------------------------------
    # Calculate Route Score
    # ----------------------------------
    def calculate_route_score(
            self,
            route,
            preference="balanced"):

        safety_risk = (
            self.calculate_safety_risk(
                route
            )
        )

        efficiency = (
            self.efficiency_score(
                route
            )
        )

        safety_score = (
            100 - safety_risk
        )

        preference = preference.lower()

        # --------------------------------
        # Safety Priority
        # --------------------------------
        if preference == "safest":

            score = (

                safety_score * 0.75
                +
                efficiency * 0.25

            )

        # --------------------------------
        # Fastest / Shortest Priority
        # --------------------------------
        elif preference == "fastest":

            score = (

                safety_score * 0.30
                +
                efficiency * 0.70

            )

        # --------------------------------
        # Balanced Priority
        # --------------------------------
        else:

            score = (

                safety_score * 0.60
                +
                efficiency * 0.40

            )

        return round(
            score,
            2
        )

    # ----------------------------------
    # Risk Level
    # ----------------------------------
    def risk_level(
            self,
            safety_risk):

        if safety_risk >= 70:

            return "High Risk"

        elif safety_risk >= 40:

            return "Medium Risk"

        return "Low Risk"

    # ----------------------------------
    # Analyze Route
    # ----------------------------------
    def analyze_route(
            self,
            route,
            preference="balanced"):

        safety_risk = (
            self.calculate_safety_risk(
                route
            )
        )

        efficiency = (
            self.efficiency_score(
                route
            )
        )

        route_score = (
            self.calculate_route_score(
                route,
                preference
            )
        )

        return {

            "Route ID":
                route["ID"],

            "Route":
                route["Name"],

            "Distance":
                route["Distance"],

            "Travel Time":
                route["Travel Time"],

            "Safety Risk":
                safety_risk,

            "Risk Level":
                self.risk_level(
                    safety_risk
                ),

            "Efficiency Score":
                round(
                    efficiency,
                    2
                ),

            "Route Score":
                route_score

        }

    # ----------------------------------
    # Compare Routes
    # ----------------------------------
    def compare_routes(
            self,
            preference="balanced"):

        analysis = []

        for route in self.routes:

            result = self.analyze_route(

                route,
                preference

            )

            analysis.append(
                result
            )

        return sorted(

            analysis,

            key=lambda route:
            route["Route Score"],

            reverse=True

        )

    # ----------------------------------
    # Recommend Best Route
    # ----------------------------------
    def recommend_route(
            self,
            preference="balanced"):

        if not self.routes:

            return None

        routes = self.compare_routes(
            preference
        )

        return routes[0]

    # ----------------------------------
    # Display Route Analysis
    # ----------------------------------
    def display_route_analysis(
            self,
            route_id,
            preference="balanced"):

        route = self.find_route(
            route_id
        )

        if not route:

            print(
                "\nRoute not found."
            )

            return

        result = self.analyze_route(

            route,
            preference

        )

        print(
            "\n========== ROUTE ANALYSIS ==========\n"
        )

        for key, value in result.items():

            if key == "Travel Time":

                print(
                    f"{key:<18}: "
                    f"{value} minutes"
                )

            elif key == "Distance":

                print(
                    f"{key:<18}: "
                    f"{value} km"
                )

            else:

                print(
                    f"{key:<18}: "
                    f"{value}"
                )

    # ----------------------------------
    # Display Route Comparison
    # ----------------------------------
    def display_comparison(
            self,
            preference="balanced"):

        if not self.routes:

            print(
                "\nNo routes available."
            )

            return

        results = self.compare_routes(
            preference
        )

        print(
            "\n========== ROUTE COMPARISON ==========\n"
        )

        print(
            f"Preference: "
            f"{preference.title()}\n"
        )

        for index, route in enumerate(

                results,
                start=1):

            print(
                f"{index}. "
                f"{route['Route']}"
            )

            print(
                f"   Distance: "
                f"{route['Distance']} km"
            )

            print(
                f"   Travel Time: "
                f"{route['Travel Time']} minutes"
            )

            print(
                f"   Safety Risk: "
                f"{route['Safety Risk']}"
            )

            print(
                f"   Risk Level: "
                f"{route['Risk Level']}"
            )

            print(
                f"   Route Score: "
                f"{route['Route Score']}"
            )

            print()

    # ----------------------------------
    # Display Recommendation
    # ----------------------------------
    def display_recommendation(
            self,
            preference="balanced"):

        route = self.recommend_route(
            preference
        )

        if not route:

            print(
                "\nNo routes available."
            )

            return

        print(
            "\n========== SAFEROUTE RECOMMENDATION ==========\n"
        )

        print(
            f"Recommended Route: "
            f"{route['Route']}"
        )

        print(
            f"Distance: "
            f"{route['Distance']} km"
        )

        print(
            f"Travel Time: "
            f"{route['Travel Time']} minutes"
        )

        print(
            f"Safety Risk: "
            f"{route['Safety Risk']}"
        )

        print(
            f"Risk Level: "
            f"{route['Risk Level']}"
        )

        print(
            f"Final Route Score: "
            f"{route['Route Score']}"
        )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    system = SafeRoute()

    # ----------------------------------
    # Add Route 1
    # ----------------------------------
    system.add_route(

        "R001",

        "Main Road Route",

        8,

        25,

        "high",

        "good",

        1,

        "good"

    )

    # ----------------------------------
    # Add Route 2
    # ----------------------------------
    system.add_route(

        "R002",

        "City Center Route",

        10,

        35,

        "medium",

        "good",

        0,

        "good"

    )

    # ----------------------------------
    # Add Route 3
    # ----------------------------------
    system.add_route(

        "R003",

        "Shortcut Route",

        6,

        18,

        "low",

        "poor",

        4,

        "poor"

    )

    # Compare routes
    system.display_comparison(
        "balanced"
    )

    # Recommend safest route
    system.display_recommendation(
        "safest"
    )

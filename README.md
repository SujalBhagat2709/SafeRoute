# SafeRoute

## Overview

SafeRoute is a route comparison and recommendation system that helps users choose the most suitable travel route based on both **safety** and **travel efficiency**.

The system does not automatically recommend the shortest route. Instead, it analyzes multiple factors and calculates a score for every available route.

SafeRoute considers:

- Distance
- Estimated travel time
- Traffic level
- Road condition
- Safety reports
- Lighting level
- User preference

The user can choose whether they want to prioritize:

- Safest route
- Fastest route
- Balanced route

---

## Problem Statement

In real life, the shortest route is not always the best route.

For example, a shortcut may be faster but have:

- Poor road conditions
- Poor lighting
- Multiple reported safety issues

Another route may take longer but provide better road conditions and lower safety risk.

SafeRoute compares these factors and recommends the most suitable route according to the user's preference.

---

## Features

- Add travel routes
- View all available routes
- Analyze an individual route
- Calculate safety risk
- Calculate travel efficiency
- Compare multiple routes
- Classify route risk levels
- Choose travel preferences
- Recommend the best available route

---

## Project Structure

```text
safe-route/

├── safe_route.py
├── safe_route_studio.py
├── README.md
└── .gitignore

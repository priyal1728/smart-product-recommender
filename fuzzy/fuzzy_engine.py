import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def create_fuzzy_system():

    # Input variables
    camera = ctrl.Antecedent(np.arange(0, 101, 1), "camera")
    battery = ctrl.Antecedent(np.arange(0, 101, 1), "battery")
    performance = ctrl.Antecedent(
        np.arange(0, 101, 1),
        "performance"
    )
    price = ctrl.Antecedent(np.arange(0, 101, 1), "price")

    # Output variable
    recommendation = ctrl.Consequent(
        np.arange(0, 101, 1),
        "recommendation"
    )

    # -----------------------------
    # Membership Functions
    # -----------------------------

    camera["low"] = fuzz.trimf(
        camera.universe, [0, 0, 50]
    )
    camera["medium"] = fuzz.trimf(
        camera.universe, [25, 50, 75]
    )
    camera["high"] = fuzz.trimf(
        camera.universe, [50, 100, 100]
    )

    battery["low"] = fuzz.trimf(
        battery.universe, [0, 0, 50]
    )
    battery["medium"] = fuzz.trimf(
        battery.universe, [25, 50, 75]
    )
    battery["high"] = fuzz.trimf(
        battery.universe, [50, 100, 100]
    )

    performance["low"] = fuzz.trimf(
        performance.universe, [0, 0, 50]
    )
    performance["medium"] = fuzz.trimf(
        performance.universe, [25, 50, 75]
    )
    performance["high"] = fuzz.trimf(
        performance.universe, [50, 100, 100]
    )

    price["low"] = fuzz.trimf(
        price.universe, [0, 0, 50]
    )
    price["medium"] = fuzz.trimf(
        price.universe, [25, 50, 75]
    )
    price["high"] = fuzz.trimf(
        price.universe, [50, 100, 100]
    )

    # Output membership functions

    recommendation["low"] = fuzz.trimf(
        recommendation.universe, [0, 0, 50]
    )

    recommendation["medium"] = fuzz.trimf(
        recommendation.universe, [25, 50, 75]
    )

    recommendation["high"] = fuzz.trimf(
        recommendation.universe, [50, 100, 100]
    )

    # -----------------------------
    # Fuzzy Rules
    # -----------------------------

    rule1 = ctrl.Rule(
        camera["high"]
        & battery["high"]
        & performance["high"]
        & price["high"],
        recommendation["high"]
    )

    rule2 = ctrl.Rule(
        camera["high"]
        & battery["high"]
        & price["high"],
        recommendation["high"]
    )

    rule3 = ctrl.Rule(
        performance["high"]
        & battery["high"]
        & price["high"],
        recommendation["high"]
    )

    rule4 = ctrl.Rule(
        camera["high"]
        & performance["high"]
        & price["medium"],
        recommendation["high"]
    )

    rule5 = ctrl.Rule(
        camera["medium"]
        & battery["medium"]
        & performance["medium"]
        & price["medium"],
        recommendation["medium"]
    )

    rule6 = ctrl.Rule(
        camera["low"]
        & performance["low"],
        recommendation["low"]
    )

    rule7 = ctrl.Rule(
        battery["low"]
        & performance["low"],
        recommendation["low"]
    )

    rule8 = ctrl.Rule(
        price["low"],
        recommendation["low"]
    )

    rule9 = ctrl.Rule(
        camera["medium"]
        & performance["high"]
        & price["high"],
        recommendation["high"]
    )

    # -----------------------------
    # Control System
    # -----------------------------

    system = ctrl.ControlSystem([
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8,
        rule9
    ])

    return system


def calculate_fuzzy_score(
    camera,
    battery,
    performance,
    price
):

    system = create_fuzzy_system()

    simulation = ctrl.ControlSystemSimulation(system)

    # Input values
    simulation.input["camera"] = camera
    simulation.input["battery"] = battery
    simulation.input["performance"] = performance
    simulation.input["price"] = price

    # Fuzzy inference + defuzzification
    simulation.compute()

    return simulation.output["recommendation"]
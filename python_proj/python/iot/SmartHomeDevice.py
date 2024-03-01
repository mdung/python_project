# Beispiel für ein einfaches Automatisierungssystem für Haushaltsgeräte

import random
import time

class SmartHomeDevice:
    def __init__(self, name):
        self.name = name
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.name} eingeschaltet.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.name} ausgeschaltet.")

class SmartLight(SmartHomeDevice):
    def __init__(self, name):
        super().__init__(name)

    def change_color(self, color):
        print(f"{self.name} Farbe geändert zu {color}.")

class SmartThermostat(SmartHomeDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 20

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} Temperatur auf {temperature}°C eingestellt.")

# Beispiel für eine einfache KI-Entscheidungsfunktion
def smart_decision(device):
    # Simulieren Sie eine KI-Entscheidung basierend auf verschiedenen Kriterien
    if isinstance(device, SmartLight):
        return random.choice(["change_color", "turn_off"])
    elif isinstance(device, SmartThermostat):
        return random.choice(["set_temperature", "turn_off"])

if __name__ == "__main__":
    # Erstellen von Smart Home Geräten
    light = SmartLight("Wohnzimmerlicht")
    thermostat = SmartThermostat("Wohnzimmerthermostat")

    # Simulieren von Aktionen basierend auf KI-Entscheidungen
    for _ in range(5):
        time.sleep(2)  # Simuliert den Zeitablauf zwischen den Aktionen
        chosen_device = random.choice([light, thermostat])
        action = smart_decision(chosen_device)

        if action == "change_color" and isinstance(chosen_device, SmartLight):
            chosen_device.change_color(random.choice(["rot", "grün", "blau"]))
        elif action == "set_temperature" and isinstance(chosen_device, SmartThermostat):
            chosen_device.set_temperature(random.randint(18, 25))
        elif action == "turn_off":
            chosen_device.turn_off()
        else:
            chosen_device.turn_on()

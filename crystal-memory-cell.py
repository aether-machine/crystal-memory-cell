# Crystal-Based Analogue Memory Cell

# Description:
# This is a conceptual representation of a capacitor-like device using a crystal dielectric
# with memory properties derived from changes in structure due to external stimulus (sound, EM fields).
# The code simulates time-dependent dielectric response and stores charge-like state evolution.

import numpy as np
import matplotlib.pyplot as plt

class CrystalDielectric:
    def __init__(self, base_permittivity=10, sensitivity=0.05):
        self.base_permittivity = base_permittivity
        self.sensitivity = sensitivity  # change per unit stimulus
        self.history = []  # stores permittivity over time
        self.state = base_permittivity

    def apply_stimulus(self, stimulus_strength):
        delta = self.sensitivity * stimulus_strength
        self.state += delta
        self.state = max(self.base_permittivity, self.state)  # ensure no negative permittivity
        self.history.append(self.state)

    def decay(self, decay_factor=0.99):
        self.state *= decay_factor
        self.history.append(self.state)

    def reset(self):
        self.state = self.base_permittivity
        self.history = []

class CrystalCapacitor:
    def __init__(self, plate_area=1.0, plate_distance=0.01):
        self.plate_area = plate_area
        self.plate_distance = plate_distance
        self.dielectric = CrystalDielectric()

    def capacitance(self):
        eps_0 = 8.854e-12  # Vacuum permittivity
        return (eps_0 * self.dielectric.state * self.plate_area) / self.plate_distance

    def stimulate(self, stimulus_pattern):
        for s in stimulus_pattern:
            self.dielectric.apply_stimulus(s)

    def relax(self, steps=10):
        for _ in range(steps):
            self.dielectric.decay()

# Simulation
stimulus = np.sin(np.linspace(0, 2 * np.pi, 50)) * 10  # synthetic sound wave as input
capacitor = CrystalCapacitor()
capacitor.stimulate(stimulus)
capacitor.relax(20)

# Plotting
plt.plot(capacitor.dielectric.history)
plt.title("Crystal Dielectric Permittivity Over Time")
plt.xlabel("Time Step")
plt.ylabel("Effective Permittivity")
plt.grid(True)
plt.show()

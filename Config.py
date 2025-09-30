"""
config.py
Central configuration file for the project.
Store constants, pins, thresholds, and settings here.
"""

# --- Safety Settings ---
EMERGENCY_STOP_PIN = 17        # Example GPIO pin for e-stop
SAFETY_TIMEOUT_SEC = 5         # Seconds before auto shutdown

# --- Motor Settings ---
DEFAULT_DUTY_CYCLE = 0.6       # Default duty cycle (0.0–1.0)
MAX_RPM = 3000                 # Maximum safe RPM

# --- Hall Sensor Settings ---
HALL_SENSOR_PIN = 27           # GPIO pin for hall sensor
PULSES_PER_REV = 2             # Number of pulses per revolution

# --- Proximity Sensor Settings ---
PROX_THRESHOLD = 0.5           # Threshold for material detection

# --- Logger Settings ---
LOG_FILE = "logs.csv"          # Default log file path


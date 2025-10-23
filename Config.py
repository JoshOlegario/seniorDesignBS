"""
config.py
Central configuration file for the Raspberry Pi project.
Store constants, pins, thresholds, and settings here.
"""

# --- GPIO Pin Assignments ---
# Sensor Inputs
SENSOR_1_PIN = 22          # Sensor 1 input
SENSOR_2_PIN = 24          # Sensor 2 input
SENSOR_3_PIN = 26          # Sensor 3 input

# Motor Control (Brushless ESC)
MOTOR_ESC_PIN = 4          # ESC signal pin (PWM capable)

# Safety
EMERGENCY_STOP_PIN = 17    # GPIO pin for e-stop (active LOW)
MANUAL_RESTART_PIN = 27    # GPIO pin for manual restart button

# --- Safety Settings ---
ESTOP_ACTIVE_STATE = False     # E-stop is active when LOW (button pressed)
ESTOP_DEBOUNCE_TIME = 0.02     # E-stop debounce time in seconds
RESTART_BUTTON_DEBOUNCE = 0.1  # Restart button debounce time in seconds

# --- Brushless Motor Settings (ESC Control) ---
ESC_FREQUENCY = 50         # ESC PWM frequency in Hz
ESC_MIN_PULSE = 1.0        # Minimum pulse width in ms (motor stopped)
ESC_MAX_PULSE = 2.0        # Maximum pulse width in ms (full throttle)
ESC_ARM_PULSE = 1.0        # ESC arming pulse width in ms
ESC_ARM_TIME = 2.0         # Time to wait for ESC to arm (seconds)

# Motor speed settings (duty cycle 0.0-1.0)
MOTOR_IDLE_SPEED = 0.0     # Motor stopped
MOTOR_RUN_SPEED = 0.6      # Normal operating speed
MOTOR_MAX_SPEED = 1.0      # Maximum speed

# --- Proximity Sensor Settings ---
PROX_THRESHOLD = 0.5       # Threshold for material detection
SENSOR_DEBOUNCE_TIME = 0.05  # Sensor debounce time in seconds

# --- Logger Settings ---
LOG_FILE = "logs.txt"      # Default log file path
LOG_LEVEL = "INFO"         # Logging level: DEBUG, INFO, WARNING, ERROR

# --- System Settings ---
LOOP_DELAY = 0.1          # Main loop delay in seconds (100ms)

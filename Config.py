#include <Keypad.h>

// ========== PIN ASSIGNMENTS FOR MEGA 2560 ==========
// Motor (single MOSFET controlling both motors)
const int MOTOR_CONTROL = 30;

// Keypad Matrix - wired to pins 52 down to 46 (7 pins total)
byte rowPins[4] = {52, 51, 50, 49};    // Keypad pins 1-4 (Rows)
byte colPins[3] = {48, 47, 46};        // Keypad pins 5-7 (Columns)
// ==================================================

// Keypad layout
const byte ROWS = 4;
const byte COLS = 3;
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  // Set up motor control pin (MOSFET gate)
  pinMode(MOTOR_CONTROL, OUTPUT);
  
  // Initialize motor to OFF
  digitalWrite(MOTOR_CONTROL, LOW);
  
  Serial.begin(115200);
  Serial.println("=== Manual Motor Control - Mega 2560 ===");
  Serial.println("Keypad: Pins 52-46");
  Serial.println("Motor Control: Pin 30 (Single MOSFET)");
  Serial.println("\nPress 1 = Motors ON");
  Serial.println("Press 2 = Motors OFF");
  Serial.println("========================================\n");
}

void loop() {
  // Check for keypad input
  char key = keypad.getKey();
  
  if (key) {
    handleKeypadInput(key);
  }
  
  delay(100);
}

void handleKeypadInput(char key) {
  switch(key) {
    case '1':
      // Motors ON
      digitalWrite(MOTOR_CONTROL, HIGH);
      Serial.println(">>> MOTORS ON <<<");
      break;
      
    case '2':
      // Motors OFF
      digitalWrite(MOTOR_CONTROL, LOW);
      Serial.println(">>> MOTORS OFF <<<");
      break;
      
    default:
      // Other keys - no action
      Serial.print("Key pressed: ");
      Serial.println(key);
      break;
  }
}
```

## Your Wiring:
```
Keypad Pin → Arduino Mega Pin
──────────────────────────────
Pin 1 (R1) → 52
Pin 2 (R2) → 51
Pin 3 (R3) → 50
Pin 4 (R4) → 49
Pin 5 (C1) → 48
Pin 6 (C2) → 47
Pin 7 (C3) → 46

MOSFET Gate → Pin 30 (controls both motors)

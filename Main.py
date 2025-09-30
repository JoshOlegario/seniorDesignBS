#!/usr/bin/env python3
import sys, time, argparse
import RPi.GPIO as GPIO
import config as C
from motor import Motor
from hall_sensor import HallCounter
from prox_sensor import ProxSensors
from safety import Safety
from logger_csv import CsvLogger

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def teardown_gpio():
    try:
        GPIO.cleanup()
    except Exception:
        pass

def run_loop(target_duty: float, seconds: float, log_path: str):
    setup_gpio()
    log = CsvLogger(log_path)
    hall = HallCounter()
    prox = ProxSensors()
    safe = Safety(prox)
    motor = Motor()

    try:
        motor.set_duty(target_duty)
        t_end = time.time() + seconds if seconds > 0 else float("inf")

        while time.time() < t_end:
            # Safety interlocks
            faults = safe.faults()
            if faults:
                motor.stop()
                rpm = hall.read_rpm(0.5)
                log.write(0.0, rpm, prox.auger_covered(), prox.hopper_full(), faults)
                print(f"[FAULT] {faults} → motor stopped | RPM={rpm:.1f}")
                # stay stopped until cleared
                time.sleep(0.5)
                continue

            # Normal operation: read RPM over a short window
            rpm = hall.read_rpm(0.5)
            log.write(target_duty, rpm, prox.auger_covered(), prox.hopper_full(), [])
            print(f"duty={target_duty:.0f}% | rpm={rpm:.1f} | auger_covered={prox.auger_covered()} | hopper_full={prox.hopper_full()}")
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\n[INFO] Exiting…")
    finally:
        motor.shutdown()
        teardown_gpio()

def test_inputs(duration=10):
    """Quick sensor test without spinning the motor."""
    setup_gpio()
    hall = HallCounter()
    prox = ProxSensors()

    try:
        t_end = time.time() + duration
        while time.time() < t_end:
            rpm = hall.read_rpm(0.5)  # if you spin by hand you'll see counts
            print(f"rpm={rpm:.1f} | auger_covered={prox.auger_covered()} | hopper_full={prox.hopper_full()}")
            time.sleep(0.3)
    finally:
        teardown_gpio()

def calibrate_pwm():
    """Walk PWM duty in steps so we can map duty → RPM."""
    setup_gpio()
    hall = HallCounter()
    motor = Motor()
    try:
        for duty in range(0, 101, 10):
            motor.set_duty(duty)
            # settle
            time.sleep(1.0)
            rpm = hall.read_rpm(1.0)
            print(f"Duty {duty:3d}% → {rpm:7.1f} RPM")
        motor.stop()
    finally:
        motor.shutdown()
        teardown_gpio()

def main():
    parser = argparse.ArgumentParser(description="Auger controller (main + modules)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="run motor with safety + logging")
    p_run.add_argument("--duty", type=float, default=C.DEFAULT_DUTY, help="PWM duty percent")
    p_run.add_argument("--seconds", type=float, default=0, help="0 = run forever")
    p_run.add_argument("--log", type=str, default="run_log.csv", help="CSV log path")

    sub.add_parser("test", help="test sensors without spinning motor")
    sub.add_parser("calibrate", help="sweep duty and print RPM map")

    args = parser.parse_args()

    if args.cmd == "run":
        run_loop(args.duty, args.seconds, args.log)
    elif args.cmd == "test":
        test_inputs()
    elif args.cmd == "calibrate":
        calibrate_pwm()

if __name__ == "__main__":
    main()

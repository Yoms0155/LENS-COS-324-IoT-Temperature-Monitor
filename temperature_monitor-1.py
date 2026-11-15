"""LENS-COS 324: Python-Based IoT Temperature Monitoring System."""
import csv
import random
from pathlib import Path
import matplotlib.pyplot as plt

DATA_FILE = Path("temperature_readings.csv")
GRAPH_FILE = Path("temperature_graph.png")
NUMBER_OF_READINGS = 60
WARNING_LIMIT = 35.0


def simulate_temperature_readings(count):
    """Simulate temperature readings in degrees Celsius."""
    return [round(random.uniform(20.0, 42.0), 2) for _ in range(count)]


def save_readings_to_csv(readings, filename):
    """Save simulated readings in CSV format."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Reading_Number", "Temperature_C"])
        for number, temperature in enumerate(readings, start=1):
            writer.writerow([number, temperature])


def read_and_validate_csv(filename):
    """Read CSV data and skip missing, invalid, or out-of-range values."""
    valid_readings = []
    invalid_count = 0
    with open(filename, "r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            value = (row.get("Temperature_C") or "").strip()
            number = row.get("Reading_Number", "?")
            if not value:
                print(f"Missing temperature at reading {number}; skipped.")
                invalid_count += 1
                continue
            try:
                temperature = float(value)
            except ValueError:
                print(f"Invalid temperature '{value}' at reading {number}; skipped.")
                invalid_count += 1
                continue
            if not 0 <= temperature <= 100:
                print(f"Out-of-range temperature '{value}' at reading {number}; skipped.")
                invalid_count += 1
                continue
            valid_readings.append((int(number), temperature))
    return valid_readings, invalid_count


def display_average_and_warnings(valid_readings):
    """Calculate average and warn when a reading exceeds 35 degrees C."""
    if not valid_readings:
        print("No valid temperature readings are available.")
        return
    temperatures = [temperature for _, temperature in valid_readings]
    average = sum(temperatures) / len(temperatures)
    print(f"Valid readings: {len(temperatures)}")
    print(f"Average temperature: {average:.2f}°C")
    alerts = [(number, value) for number, value in valid_readings
              if value > WARNING_LIMIT]
    if alerts:
        for number, value in alerts:
            print(f"WARNING: Reading {number} is {value:.2f}°C "
                  f"(above {WARNING_LIMIT:.1f}°C).")
    else:
        print("No temperature exceeded 35°C.")


def create_temperature_graph(valid_readings, filename):
    """Create and save a graph of valid readings."""
    if not valid_readings:
        print("Graph not created because there are no valid readings.")
        return
    numbers = [number for number, _ in valid_readings]
    temperatures = [value for _, value in valid_readings]
    plt.figure(figsize=(10, 5))
    plt.plot(numbers, temperatures, marker="o", label="Temperature")
    plt.axhline(WARNING_LIMIT, linestyle="--", label="Warning limit (35°C)")
    plt.title("IoT Temperature Monitoring System")
    plt.xlabel("Reading Number")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    print(f"Temperature graph saved as {filename}")
    plt.show()


def main():
    print("=== IoT Temperature Monitoring System ===")
    readings = simulate_temperature_readings(NUMBER_OF_READINGS)
    save_readings_to_csv(readings, DATA_FILE)
    print(f"{len(readings)} simulated readings saved to {DATA_FILE}.")
    valid_readings, invalid_count = read_and_validate_csv(DATA_FILE)
    print(f"Missing/invalid rows skipped: {invalid_count}")
    display_average_and_warnings(valid_readings)
    create_temperature_graph(valid_readings, GRAPH_FILE)


if __name__ == "__main__":
    main()

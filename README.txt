# LENS-COS 324 – IoT Practical Assignment
## Python-Based IoT Temperature Monitoring System

### Project description
This project simulates an Internet of Things (IoT) temperature monitoring system using Python. It generates temperature readings as if they were coming from a temperature sensor. No physical IoT device is required.

### Files in this repository
- `temperature_monitor.py` – Python source code.
- `temperature_readings.csv` – Sample CSV dataset containing 60 valid simulated readings plus one missing and one invalid example row.
- `temperature_graph.png` – Graph of the 60 valid sample readings.
- `README.md` – Project explanation and instructions.

### Requirements
- Python 3
- Matplotlib

Install Matplotlib with:
```bash
python -m pip install matplotlib
```

### How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:
```bash
python temperature_monitor.py
```

The program generates 60 new simulated readings, saves them to `temperature_readings.csv`, reads the CSV file, skips missing or invalid values, calculates the average, reports every reading above 35°C, and saves/displays `temperature_graph.png`.

### Sample result from the included CSV
- Valid sample readings: 60
- Average temperature: 30.81°C
- Readings above 35°C: 21
- Missing/invalid demonstration rows: 2 (one blank and one non-numeric value)

The sample CSV includes malformed rows to demonstrate validation. The program itself generates 60 fresh numeric readings whenever it is run.

### How the program works
1. `simulate_temperature_readings()` creates random temperatures between 20°C and 42°C.
2. `save_readings_to_csv()` stores the readings in a CSV file.
3. `read_and_validate_csv()` reads the file and skips blank, non-numeric, or out-of-range values.
4. `display_average_and_warnings()` calculates the mean and prints a warning for each temperature above 35°C.
5. `create_temperature_graph()` plots the valid readings with a horizontal 35°C warning-limit line.

### Relationship to a real IoT temperature sensor
In a real IoT system, a physical temperature sensor measures the surrounding temperature and sends the readings to a computer or microcontroller. In this practical, Python's random-number generator replaces the physical sensor by producing simulated readings. The CSV file represents stored sensor data, while the average, warnings, and graph represent monitoring and analysis. A real deployment could replace the simulation function with code that reads data from a sensor connected to a device such as a microcontroller.

### GitHub submission
1. Sign in to GitHub and create a **public** repository, for example `LENS-COS-324-IoT-Temperature-Monitor`.
2. Upload all four files listed above.
3. Open the repository page and confirm that the files are visible.
4. Copy the repository URL and submit it through the Google Form specified in the assignment.
5. Use your correct matriculation number and submit only once.

**Important:** Replace any sample/personal details if required by your lecturer. Make sure the repository link is accessible to the lecturer.

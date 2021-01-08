# FSTelemetry
Python library collecting Flight Simulator 2020 telemetry into a local csv file using SimConnect.
Variables for collection are simply defined in a `config.yaml` file. 

A
list of available data points can be found here https://github.com/odwdinc/Python-SimConnect/blob/master/SimConnect/RequestList.py#L234. 

Data is collected every second by default.

## Getting Started
Install FSTelemetry

```bash
pip install fstelemetry
```

Create a `config.yaml` file in a new folder containing a list of metrics
you would like to track:

```yaml
keys:
  - PLANE_ALTITUDE
  - GROUND_VELOCITY
  - AIRSPEED_INDICATED
  - AIRSPEED_MACH
  - AMBIENT_TEMPERATURE
  - AMBIENT_PRESSURE
  - TOTAL_WEIGHT
  - FUEL_TOTAL_QUANTITY
  - ENG_FUEL_FLOW_GPH:1
  - ENG_FUEL_FLOW_GPH:2
  - TURB_ENG_CORRECTED_N1:1
  - TURB_ENG_CORRECTED_N2:1
  - VERTICAL_SPEED
  - AIRCRAFT_WIND_X
  - AIRCRAFT_WIND_Y
```

In the same directory, simply launch the tool (Note: ensure you are in an
active flight)

```bash
fstelemetry
```

This will produce a log file named `log.csv` by default. You can change
settings such as the config & log file location if needed. You can also
adjust the delay in logging (default 1.0 seconds). See:
```bash
fstelemetry --help
usage: fstelemetry [-h] [--config CONFIG] [--log LOG] [--interval INTERVAL]

optional arguments:
  -h, --help           show this help message and exit
  --config CONFIG      Relative path to the config file
  --log LOG            Relative path for the output log file
  --interval INTERVAL  Polling interval in seconds
```

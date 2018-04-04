# OSRM distance and duration matrices service

Returns an object containing numpy matrices for distance and duration from an OSRM server giving an input list of OSRM coordinates.

### Installation
Simply run:
```bash
pip install osrm_plus
```

### Usage
```python
import clique_tour, requests, json
import numpy as np
test_coordinates = [
    "60.70278,31.6386",
    "60.92565,33.94732",
    "61.28789,32.23765",
    "65.90314,37.6431",
    "66.9574,34.18027",
    "67.5304,31.95617",
    "67.63406,33.14132"
]
route_info = osrm_plus.distances_and_durations(test_coordinates)
distances = route_info['distances']
durations = route_info['durations']

print("Distance matrix: \n\t{}".format(distances))
print("Duration matrix: \n\t{}".format(durations))
print("Speed matrix (m/s): \n\t{}".format(distances/(durations+np.finfo(np.float32).eps)))
print("Speed matrix (km/h): \n\t{}".format(distances/(durations+np.finfo(np.float32).eps)*((60*60)/1000)))
```

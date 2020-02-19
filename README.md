# OSRM distance and duration matrices service

Returns an object containing numpy matrices for distance and duration from an OSRM server giving an input list of OSRM coordinates. This was made after [this discussion](https://github.com/Project-OSRM/osrm-backend/issues/1353#issuecomment-378575752)

### Installation
```bash
pip install osrm_plus
```

### Usage
```python
import osrm_plus

test_coordinates = [
     "60.70278,31.6386",
     "60.92565,33.94732",
     "61.28789,32.23765",
     "65.90314,37.6431",
     "66.9574,34.18027",
     "67.5304,31.95617",
     "67.63406,33.14132"
]
route_info = osrm_plus.distances_and_durations(test_coordinates, include_speed=True)
distances = route_info['distances']
durations = route_info['durations']
speeds = route_info['speeds']

print("Distance matrix: \n\t{}".format(distances))
print("Duration matrix: \n\t{}".format(durations))
print("Speed matrix (m/s): \n\t{}".format(speeds))
print("Speed matrix (km/h): \n\t{}".format(speeds*((60*60)/1000)))
```

Which outputs:
```bash
Distance matrix:
	[[      0.   597848.5  111905.3 1424042.5 1327335.6  908101.5  981078.8]
 [ 597848.5       0.   579581.6  938840.5 1397277.6  883615.5 1051166.7]
 [ 111905.3  579581.6       0.  1374843.5 1432621.7  916834.9 1084560.8]
 [1424042.5  938840.5 1374843.5       0.   902239.6  983268.3  905651.4]
 [1327335.6 1397277.6 1432621.7  902239.6       0.   515612.   438002.3]
 [ 908101.5  883615.5  916834.9  983268.3  515612.        0.   197313.8]
 [ 981078.8 1051166.7 1084560.8  905651.4  438002.3  197313.8       0. ]]
Duration matrix:
	[[     0.   74002.1  14669.4 144092.3 120643.   80559.3  96219.7]
 [ 74002.1      0.   71016.5  82867.2 108230.5  63790.4  83739.4]
 [ 14669.4  71016.5      0.  132550.5 136620.   87058.8 109406.6]
 [144092.3  82867.2 132550.5      0.   85250.8  75562.9  79776. ]
 [120643.  108230.5 136620.   85250.8      0.   47162.4  46454.5]
 [ 80559.3  63790.4  87058.8  75562.9  47162.4      0.   18105.8]
 [ 96219.7  83739.4 109406.6  79776.   46454.5  18105.8      0. ]]
Speed matrix (m/s):
	[[ 0.          8.07880452  7.62848515  9.8828494  11.00217667 11.27246016
  10.19623632]
 [ 8.07880452  0.          8.1612245  11.32945846 12.91020184 13.85185702
  12.55283296]
 [ 7.62848515  8.1612245   0.         10.37222417 10.48617845 10.53121454
   9.91312042]
 [ 9.8828494  11.32945846 10.37222417  0.         10.5833564  13.01258025
  11.3524293 ]
 [11.00217667 12.91020184 10.48617845 10.5833564   0.         10.93269214
   9.42863016]
 [11.27246016 13.85185702 10.53121454 13.01258025 10.93269214  0.
  10.8978228 ]
 [10.19623632 12.55283296  9.91312042 11.3524293   9.42863016 10.8978228
   0.        ]]
Speed matrix (km/h):
	[[ 0.         29.08369627 27.46254653 35.57825782 39.60783601 40.58085659
  36.70645076]
 [29.08369627  0.         29.38040821 40.78605045 46.47672662 49.86668527
  45.19019864]
 [27.46254653 29.38040821  0.         37.34000702 37.75024242 37.91237233
  35.68723349]
 [35.57825782 40.78605045 37.34000702  0.         38.10008305 46.84528889
  40.86874549]
 [39.60783601 46.47672662 37.75024242 38.10008305  0.         39.35769172
  33.94306859]
 [40.58085659 49.86668527 37.91237233 46.84528889 39.35769172  0.
  39.23216207]
 [36.70645076 45.19019864 35.68723349 40.86874549 33.94306859 39.23216207
   0.        ]]
```

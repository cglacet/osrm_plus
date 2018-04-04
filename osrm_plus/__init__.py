import clique_tour, requests, json
import numpy as np

__osrm_route_service = "http://router.project-osrm.org/route/v1/driving/"

def main():
    test_coordinates = [
        "60.70278,31.6386",
        "60.92565,33.94732",
        "61.28789,32.23765",
        "65.90314,37.6431",
        "66.9574,34.18027",
        "67.5304,31.95617",
        "67.63406,33.14132"
    ]
    route_info = distances_and_durations(test_coordinates, include_speed=True)
    distances = route_info['distances']
    durations = route_info['durations']
    speeds = route_info['speeds']

    print("Distance matrix: \n\t{}".format(distances))
    print("Duration matrix: \n\t{}".format(durations))
    print("Speed matrix (m/s): \n\t{}".format(speeds))
    print("Speed matrix (km/h): \n\t{}".format(speeds*((60*60)/1000)))

def distances_and_durations(coordinates, osrm_route_service=None, include_speed=False):
    if len(coordinates) > 15:
        raise ValueError("The service currently support 15 coordinates at most.")
    if osrm_route_service is None:
        osrm_route_service = __osrm_route_service

    sample_size = len(coordinates)
    eulerian_tour = clique_tour.build(sample_size)
    fake_route = ";".join([ coordinates[i] for i in eulerian_tour ])
    address = osrm_route_service + fake_route

    r = requests.get(address, params={}, timeout=None)
    data = json.loads(r.text)
    if data['code'] == "Ok":
        route = data["routes"][0]
        legs = route["legs"]
        eulerian_tour_distances = [ leg["distance"] for leg in legs]
        eulerian_tour_durations = [ leg["duration"] for leg in legs]

        distances = np.zeros((sample_size,sample_size))
        durations = np.zeros((sample_size,sample_size))
        for i in range(len(eulerian_tour)-1):
            u = eulerian_tour[i+1]
            v = eulerian_tour[i]
            # get distances/durations for all edges and fill the matrix
            distances[u,v] =  eulerian_tour_distances[i]
            distances[v,u] =  eulerian_tour_distances[i]
            durations[u,v] =  eulerian_tour_durations[i]
            durations[v,u] =  eulerian_tour_durations[i]

    response = { 'durations':durations, 'distances':distances }
    if include_speed:
        response['speeds'] = distances/(durations+np.finfo(np.float32).eps)

    return response

if __name__ == "__main__":
    main()

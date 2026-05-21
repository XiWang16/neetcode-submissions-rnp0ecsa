class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by from pos
        trips_sorted_by_start_pos = sorted(trips, key=lambda x: x[1])

        loc_to_num_passengers = defaultdict(int)

        for trip in trips:
            for i in range(trip[1], trip[2]):
                loc_to_num_passengers[i] += trip[0]
                if loc_to_num_passengers[i] > capacity:
                    return False

        return True
        
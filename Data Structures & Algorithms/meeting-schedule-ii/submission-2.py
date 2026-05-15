class Solution:
    def minMeetingRooms(self, intervals):

        if not intervals:
            return 0

        starts = []
        ends = []

        # separate starts and ends
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        s = 0
        e = 0

        rooms = 0
        max_rooms = 0

        while s < len(intervals):

            # need new room
            if starts[s] < ends[e]:
                rooms += 1
                s += 1

            # room freed
            else:
                rooms -= 1
                e += 1

            max_rooms = max(max_rooms, rooms)

        return max_rooms
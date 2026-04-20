class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = [(0,0)]
        for d in path:
            new_x = locations[-1][0]
            new_y = locations[-1][1]
            if d == 'N':
                new_y += 1
            elif d == 'S':
                new_y -= 1
            elif d == 'W':
                new_x -= 1
            else:
                new_x += 1
                
            if (new_x, new_y) in locations:
                return True
            locations.append((new_x, new_y))
        return False
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = set((0,0))
        new_x, new_y = 0,0
        for d in path:
            locations.add((new_x, new_y))
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
            
        return False
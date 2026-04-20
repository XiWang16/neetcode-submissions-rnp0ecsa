class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if stack == [] or asteroid > 0:
                stack.append(asteroid)
            else:
                add = True
                while stack != [] and stack[-1] > 0:
                    if stack[-1] + asteroid > 0: # new asteriod destroyed
                        add = False
                        break
                    elif stack[-1] + asteroid == 0:
                        add = False
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if add:
                    stack.append(asteroid)
        return stack

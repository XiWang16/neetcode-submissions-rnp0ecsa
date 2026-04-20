class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []

        while True:
            t = n // 1000
            h = (n - 1000 * t) // 100
            tenth = (n - 1000 * t - 100 * h) // 10
            one = n - 1000 * t - 100 * h - 10 * tenth
            running = t ** 2 + h ** 2 + tenth ** 2 + one ** 2
            if running == 1: 
                return True
            if running in seen:
                return False
            seen.append(running)
            n = running


        
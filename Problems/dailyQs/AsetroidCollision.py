# 735. Asteroid Collision
'''
i=0 .. n
    if arr[i] > 0 or arr == []
        out.push(arr[i])
    else
        while (out != [] and out.top > 0 and out.top < abs(arr[i]))
            out.pop
        if out != [] and out.top == abs(arr[i])
            out.pop
        elif out == [] or out.top < 0
            out.push(arr[i])
'''

asteroids = [10, 2, -5]
out = []

# while (len(asteroids) > 0):
#     pass
for i in range(len(asteroids)):
    if asteroids == [] or asteroids[i] > 0:
        out.append(asteroids[i])
    else:
        while (out != [] and out[len(out)-1] > 0 and out[len(out)-1] < abs(asteroids[i])):
            out.pop()
        if out != [] and out[len(out)-1] == abs(asteroids[i]):
            out.pop()
        elif out == [] or out[len(out)-1] < 0:
            out.append(asteroids[i])

print(out)

'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        for i in range(len(asteroids)):
            if asteroids == [] or asteroids[i] > 0:
                out.append(asteroids[i])
            else:
                while (out != [] and out[len(out)-1] > 0 and out[len(out)-1] < abs(asteroids[i])):
                    out.pop()
                if out != [] and out[len(out)-1] == abs(asteroids[i]):
                    out.pop()
                elif out == [] or out[len(out)-1] < 0:
                    out.append(asteroids[i])
        return out
'''

# input = 'target area: x=20..30, y=-10..-5'
input = 'target area: x=137..171, y=-98..-73'
# parse input 
xT_min, xT_max = int(input.split(": ")[-1].split(", ")[0].split("..")[0].split('=')[-1]), int(input.split(": ")[-1].split(", ")[0].split("..")[-1])
yT_min, yT_max = int(input.split(": ")[-1].split(", ")[-1].split("..")[0].split('=')[-1]), int(input.split(": ")[-1].split(", ")[-1].split("..")[-1])
T = (xT_min, xT_max, yT_min, yT_max)

def flight(vx, vy, x=0, y=0):
    global T
    if (T[0] <= x <= T[1]) and (T[-1] >= y >= T[2]): # hit target 
        return x, y, 
    if (x > T[1]) | (y < T[2]):  # past target
        return False
    # update motion coords 
    x+=vx
    y+=vy
    if vx > 0:
        vx -= 1
    if vx < 0:
        vx += 1
    vy-=1
    return flight(vx, vy, x, y)

def h(n):
    if n%2==0:
        diff = ((n/2) * n) + n/2
    else:
        diff = (n+1)/2 * n
    return diff

flights = [[h(vy), flight(vx, vy)] for vx in range(0, 1+xT_max) for vy in range(yT_min, -1*yT_min) if flight(vx, vy) != False]

# part 1
print(f'part 1: {int(max([f[0] for f in flights]))}')
# part 2
print(f'part 2: {len(flights)}')
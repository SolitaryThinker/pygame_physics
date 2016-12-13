import circle, math

def collide_circle(circle_a, circle_b):
    if (dist((circle_a.x, circle_a.y), (circle_b.x, circle_b.y)) <=
            circle_a.radius + circle_b.radius):
        print("collision")

def dist(a, b):
    return math.hypot(b[0] - a[0], b[1] - a[1])
    

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

# Calculate delay for 5-second animation
# 400 iterations, each with 2 forward movements
total_iterations = 400
total_movements = total_iterations * 2  # 2 forward() calls per iteration
delay_ms = (5000 / total_movements)  # 5 seconds = 5000ms

t.speed(0)  # Use fastest speed
turtle.tracer(1, delay_ms)  # delay in milliseconds

t.color("#D7CCC8")

for i in range(400):
    t.forward(i)
    t.left(125)
    t.forward(i)
    t.left(45)

turtle.done()
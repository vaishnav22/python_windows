import turtle as tu
bob = tu.Turtle()
bob.left(90)
bob.speed(10)

#recursion

def draw(l):
    if(l<1):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*1/4)
        bob.right(60)
        draw(3*1/4)
        bob.left(30)
        bob.backward(l)


draw(100)



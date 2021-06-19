'''
This Program uses  Python Turtle Graphics interface and designs a green tree with branches

'''
import turtle as t
# main screen specs
t.speed("fastest")
t.bgcolor("black")
t.pensize(4)

# function to the structure of the tree
def tree(branchLen,t):
    if branchLen>4:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-15,t)
        t.left(60)
        tree(branchLen-15,t)
        t.right(30)
        tree(branchLen-15,t)
        t.backward(branchLen)

def main():
    myWin=t.Screen()
    t.left(90)                  
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(105,t)
    myWin.exitonclick()

main()
        

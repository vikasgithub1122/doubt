class A:
    def show(self):
        print("class A")
    def show(self):
        print("play class A")
class B(A):
    def start(s):
        print("class B start")
        
class C(B):
    def message(s):
        print("class C")
class D(A, B):
    def message(s):
        print("class D")
        

c=C()
c.message()
c.start()
c.show()



b=B()
b.start()
b.play()
from threading import Lock

class Foo:
    '''
    Suppose we have a class:
        public class Foo {
        public void first() { print("first"); }
        public void second() { print("second"); }
        public void third() { print("third"); }
        }
    The same instance of Foo will be passed to three different threads. 
    Thread A will call first(), thread B will call second(), and thread C will call third(). 
    Design a mechanism and modify the program to ensure that second() is executed after first(), 
    and third() is executed after second().

    Note:

    We do not know how the threads will be scheduled in the operating system, 
    even though the numbers in the input seem to imply the ordering. 
    The input format you see is mainly to ensure our tests' comprehensiveness.
    
    '''
    def __init__(self):
        self.l1 = Lock()
        self.l2 = Lock()
        self.l1.acquire()
        self.l2.acquire()

    def first(self, printFirst) -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l1.release()

    def second(self, printSecond) -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.l1:
            printSecond()
            self.l2.release()

    def third(self, printThird) -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.l2:
            printThird()
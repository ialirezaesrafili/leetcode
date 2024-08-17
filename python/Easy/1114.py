import threading

class Foo(object):
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        # printFirst() outputs "first".
        printFirst()
        # Signal that first() is done
        self.first_done.set()

    def second(self, printSecond):
        # Wait until first() is done
        self.first_done.wait()
        # printSecond() outputs "second".
        printSecond()
        # Signal that second() is done
        self.second_done.set()

    def third(self, printThird):
        # Wait until second() is done
        self.second_done.wait()
        # printThird() outputs "third".
        printThird()

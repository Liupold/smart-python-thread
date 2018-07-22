from threading import Thread, _start_new_thread, Lock, active_count
from queue import Queue
from time import time, sleep

###############################################################################
#
#	File info : Main file for yamata ochini
#	Initiator : Liupold
#
################################################################################
# Effiecent_Theads

class E_Thread(object):
    def __init__(self, G_THREAD, timeout=100000, Max_thread=200):
        self.G_TH = G_THREAD
        self.timeout = timeout  # will prevent from waiting for the thread
        self.TH_Q = Queue(Max_thread)     # the Queue containg threads
        self.limit = Max_thread  # maximum no. of thread that can run at once
        self.done = 0
        self.thread_no = 0
        self.run = True

        for _ in range(self.limit):
            self.TH_Q.put(Thread(target=self.G_TH, daemon=True))

    def Worker(self, X_thread, *args):  # Worker which actuall does the work
        X_thread._args = args[0]
        X_thread.start()
        X_time_limit = time() + self.timeout
        while X_thread.isAlive():
            sleep(0.0167)
            if time() > X_time_limit:
                print(active_count())
                break
        with Lock():
            self.done += 1
            self.TH_Q.put(Thread(target=self.G_TH, daemon=True))

    def start(self, *args):  # manage the work
        """ The func to be called multiple times """
        X_thread = self.TH_Q.get()
        _start_new_thread(self.Worker, (X_thread, args))
        self.thread_no += 1

    def join(self):
        while self.done != self.thread_no:
            sleep(0.0167)
        else:
            pass  # this will hall till all thread are completed

    def close(self):
        # will prevent further thread allocation but will not stop the ongoing
        self.done = self.thread_no

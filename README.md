# Yamata oroch
<https://github.com/Liupold/yamata-orochi/>
![Yamata-no-orochi](Orochi.jpg)
Yamata orchini is a module for smart thread managment in python. It's small compact and get's the job done.

  - Run Unlimited thread
  - No more messy threading do it the efficient way
  - Unblock I/O style to give the threads what they need!

# Features!

  - Assign Unlimited thread on the go
  - let the workers handel the JOB for you
  - Thread start instantly as worker finish the job



You can also:
  - Wait for all the thread to complete
  - Set a Timeout 
  (Timeout will prevent the running thread from blocking other but will not terminate the Thread)

### Requirements

What is needs:

* Time module.
* Thread from threading module.
* queue from Queue module.

You probably have all of the as you have if you have a standard version of python3 on Liux/MAC/Windows

### Installation

- Copy the ``main.py`` file to your projet folder and You are done!!
- You can also copy  ``main.py`` to any forlder and import it to your project.


### Description
Think of this like a snake with multiple head. Yeah!

You initiate the class with the function which you want to run in parallel.
You call a function in the class which take the perticular args for your fuction.
They all start as soon as you call, but not all you can specify how many (default is 200)  you want to run at once, other wait for the completion.


### Development

Want to contribute? Great!

Start a pull request!
or
Report some bugs!


### Useage Example
Download ``main.py`` to your project folder.
rename ``main.py`` to ``yamata.py`` or ``WhatEverYouWant.py``
```
import yamata.py
```

Let's create a sample fuction
For ``print`` and shared variable it's recomended to use ``Lock()``
```
import time
from threading import Lock

def sleep_for(self):
    with Lock():
        print('sleep_for({}) Started.'.format(self))
    time.sleep(self)
    with Lock():
        print('sleep_for({}) Done!'.format(self))
```
create a instance with the function

```
thread_maneger = yamata.E_thread(sleep_for)
```

Now let's run the function for 100000 (OMG) times

```
for i in range(100000):
    thread_maneger.start(i)
```

But wait i want all to be finished before i execute the next line.
No Prob!

use the join() methord.
```
thread_maneger.join()
```
### Todos

 - Intregate with process module for multicore enhancement
 - Remove bugs / issues
 - Improve ``README.md`` file

License
----

GPL 3.0


**It Work's, Hell Yeah!**
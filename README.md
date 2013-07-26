python-mocking-tutorial
=======================

Demo of some Python mocking concepts

Start with man.py, watch.py and test_man_skeleton.py. These will give you the basic context of the code you are running.

test_man.py gives you a jumpstart on how to use Python's `patch` to mock out the creation of datetime objects. Get comfortable with what the test is doing.

From there, attempt to upgrade man.py to Version 2 of the watch api (`from watch_v2 import Watch`).

Do the tests still pass? `python test_man.py`

Should they? `python -c 'from man import Man; print Man().tell_time()'`

You can check out test_man_v*.py.answers To see how you can fix your tests. The number of the test file corresponds to the version of the watch library you are trying to use.

The other files are for reference, mostly so when presenting live, you have a place to copy-and-paste from if the demo goes south :)

### Hours Minutes and Seconds - `hms_string`

This helper function `hms_string` helps us to calculate the difference between time and return a string representation of hours, minutes and seconds. For example this function can be used to tell how long does a loop run in hours, minutes and seconds. This function is very handy when working with custom loops training of neural nets. The function is as follows:

```py
import time
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)
```

The function takes number of seconds as it's argument and do the computation of finding how many hours, minutes and seconds are there in those seconds.

### How to use it.

The following code shows how we can use this function to determine how long the loop took to execute a code:

```py
import time

def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)

start = time.time()
for i in range(10000000000):
    pass
end = time.time()

print(hms_string(end-start))
```

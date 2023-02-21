# -*- coding: utf-8 -*-
import numpy as np
import time

start_time = time.time()

numbers = np.array(list(range(100000)))
np.random.shuffle(numbers)

end_time = time.time()

print(end_time - start_time)



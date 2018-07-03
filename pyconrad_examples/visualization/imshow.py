import pyconrad.autoinit
import time
import numpy as np


print('Enjoy white noise!')
for i in range(300):
    noise = np.random.rand(200, 200)
    pyconrad.imshow(noise, 'White noise')
    time.sleep(0.01)

pyconrad.close_all_windows()

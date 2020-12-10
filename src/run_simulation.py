from time import time
from env_config import PICKLE_PATH

print("Preparing simulation")
from sim.run import run
import cloudpickle
print("Run simuation")
result = run()

print(f"Simulation executed! Pickling result to {PICKLE_PATH}")
t1 = time()
with open(PICKLE_PATH, 'wb') as fid:
    cloudpickle.dump(result, fid)
t2 = time()
print(f"Results pickled sucessfuly in {t2 - t1:.2f}s")

# simpy fabsim simple_1
# Paul Connelly
# 2022-March-11

import simpy
import random

# Global Variables
lots_init_start = 250
lots_wip_container_cap = lots_init_start
lots_container_cap = 1000
clean_wip_cap = 25
lots_out = 0
lots_complete = False

# Resource
# Clean process statistics
num_clean = 25
mean_clean = 15
std_clean = 0.1

# Class definitions
class Fab:   # attribute lots_out missing
    def __init__(self, env):
        self.lot_in = simpy.Container(env, capacity=lots_container_cap, init=lots_init_start)
        self.lot_wip = simpy.Container(env, capacity=lots_wip_container_cap, init=lots_wip_container_cap)
        self.lot_out = simpy.Container(env, capacity=lots_container_cap, init=lots_out)
        self.lot_clean_wip = simpy.Container(env, capacity=clean_wip_cap, init=0)


# Resource definitions
def clean(env, fab1):
    while True:
        yield fab1.lot_in.get(num_clean)
        print("<<<............Clean process - Lot start: [", int(env.now), "]")
        clean_time = random.gauss(mean_clean, std_clean)
        yield env.timeout(clean_time)
        print("<<<............Clean process - Lot complete: [", int(env.now), "]")
        yield fab1.lot_out.put(num_clean)
        lots_out=lots_out+1
        if lots_out == lots_init_start:
            lots_complete = True
        else:
            lots_complete = False
        print("<<<............Clean process  - Lot out: [", int(env.now), "]")

# process tool generator
def clean_tool_gen(env, fab1):
    for i in range(num_clean):
        env.process(clean(env, fab1))
        yield env.timeout(0)

# simulation run
def main():
    env = simpy.Environment()
    fab1 = Fab(env)
    clean_gen = env.process(clean_tool_gen(env, fab1)) # error here + 1
    start_time = env.now
    print(" time start ", start_time)
    env.run()
    finish_time = env.now
    total_time = finish_time - start_time
    print(" finish time is : ", int(finish_time), " Total time is : ", int(total_time))

if __name__ == '__main__':
    main()
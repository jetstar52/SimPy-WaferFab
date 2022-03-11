# Fab 1: version 1 release 3
"""
Semiconductor manufacturing facility simulation using SimPy.
"""

# imports
import simpy
import random

# Global Variables
lots_init_start = 250
lots_wip_container_cap = lots_init_start
lots_container_cap = 1000
clean_wip_cap = 20
dep_wip_cap = 20
litho_wip_cap = 20
etch_wip_cap = 20

# Resource, Container initial variables
# Stocker process statistics
#num_stocker = 1
#mean_stocker = 1
#std_stocker = 0.1


# Clean process statistics
num_clean = 25
mean_clean = 15
std_clean = 0.1

# Deposition process statistics
num_dep = 5
mean_dep = 2
std_dep = 0.1

# Lithography process statistics
num_litho = 1
mean_litho = 1
std_litho = 0.1

# Etch process statistics
num_etch = 3
mean_etch = 2
std_etch = 0.1

# Class definitions
class Fab:
    def __init__(self, env):
        self.lot_in = simpy.Container(env, capacity=lots_container_cap, init=lots_init_start)
        #self.lot_wip = simpy.Container(env, capacity=lots_wip_container_cap, init=0)
        self.lot_out = simpy.Container(env, capacity=lots_container_cap, init=0)
        self.lot_clean_wip = simpy.Container(env,capacity=clean_wip_cap,init=0)
        self.lot_dep_wip = simpy.Container(env,capacity=dep_wip_cap,init=0)
        self.lot_litho_wip = simpy.Container(env,capacity=litho_wip_cap,init=0) 
        self.lot_etch_wip = simpy.Container(env,capacity=etch_wip_cap,init=0) 

# Resource, process and container definitions

# next phase will create tools from a class..
# or to just plane define x number of processes utilising 'y' tools
# where tools and or processes are reused so as to create a que.
# I may need to create some storage pools lets think on this ******************** 


#def stocker(env, fab1):
 #   while True:
  #      yield fab1.lot_in.get(num_clean)
   #     print("<<<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Stocker process - Lot start: [", int(env.now), "]")
    #    yield env.timeout(stocker_time)
     #    stocker_time= random.gauss(mean_stocker, std_stocker)
      #  print("<<<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Stocker process - Lot complete: [", int(env.now), "]")
       # yield fab1.lot_clean_wip.put(num_clean)
        #print("<<<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Stocker process - Lot out: [", int(env.now), "]")

def clean(env, fab1):
    while True:
        yield fab1.lot_in.get(num_clean)
        print("<<<............Clean process - Lot start: [", int(env.now), "]")
        clean_time = random.gauss(mean_clean, std_clean)
        yield env.timeout(clean_time)
        print("<<<............Clean process - Lot complete: [", int(env.now), "]")
        yield fab1.lot_dep_wip.put(num_clean)
        print("<<<............Clean process  - Lot out: [", int(env.now), "]")


def deposition(env, fab1):
    while True:
        yield fab1.lot_dep_wip.get(num_dep)
        print("<<<..........................deposition process - Lot start: [", int(env.now), "]")
        dep_time = random.gauss(mean_dep, std_dep)
        yield env.timeout(dep_time)
        print("<<<..........................deposition process - Lot complete: [", int(env.now), "]")
        yield fab1.lot_litho_wip.put(num_dep)
        print("<<<..........................deposition process - Lot out: [", int(env.now), "]")


def litho(env, fab1):
    while True:
        yield fab1.lot_litho_wip.get(num_litho)
        print("<<<.............................................litho process - Lot start: [", int(env.now), "]")
        litho_time = random.gauss(mean_litho, std_litho)
        yield env.timeout(litho_time)
        print("<<<.............................................litho process - Lot complete: [", int(env.now), "]")
        yield fab1.lot_etch_wip.put(num_litho)
        print("<<<.............................................litho process - Lot out: [", int(env.now), "]")


def etch(env, fab1):
    while True:
        yield fab1.lot_etch_wip.get(num_etch)
        print("<<<..........................................................etch process - Lot start: [", int(env.now), "]")
        etch_time = random.gauss(mean_etch, std_etch)
        yield env.timeout(etch_time)
        print("<<<..........................................................etch process - Lot complete: [", int(env.now), "]")
        yield fab1.lot_out.put(num_etch)
        print("<<<..........................................................etch process - Lot out: [", int(env.now), "]")



# process tool generator
#def stocker_tool_gen(env, fab1):
 #   for i in range(lots_init_start):
  #      env.process(stocker(env, fab1))
   #     yield env.timeout(0)


def clean_tool_gen(env, fab1):
    for i in range(num_clean):
        env.process(clean(env, fab1))
        yield env.timeout(0)

def dep_tool_gen(env, fab1):
    for i in range(num_dep):
        env.process(deposition(env, fab1))
        yield env.timeout(0)

def litho_tool_gen(env, fab1):
    for i in range(num_litho):
        env.process(litho(env, fab1))
        yield env.timeout(0)

def etch_tool_gen(env, fab1):
    for i in range(num_etch):
        env.process(etch(env, fab1))
        yield env.timeout(0)

# simulation run
# I need to simulate a process_runner sheet where by tools and therefore processes are reused
# lor_runner defines the flow through mask sets. lets think on this*************
def main():
    env = simpy.Environment()
    fab1 = Fab(env)

    # stocker_gen = env.process(stocker_tool_gen(env,fab1))
    clean_gen = env.process(clean_tool_gen(env, fab1))
    deposition_gen = env.process(dep_tool_gen(env, fab1))
    litho_gen = env.process(litho_tool_gen(env, fab1))
    etch_gen = env.process(etch_tool_gen(env, fab1))

    print(" Lots to process ", int(fab1.lot_in.level))
    start_time = env.now
    print(" time start ", start_time)
    fab_run_time = (input("Enter an integer > 10 and < 5000 for the model tun time : "))
    env.run(until=fab_run_time)

    # Useful output
    print("Lots processed with 5 processes ", int(fab1.lot_out.level))
    finish_time = env.now
    total_time = finish_time - start_time
    print(" finsih time is : ", int(finish_time), " Total time is : ", int(total_time))

# call the main function

main()

# The following text is from my initial thoughts document.
# The main running script for this semiconductor fabrication plant model.

# Basic steps to grow the model
# Model 1: Single process
#
# A1 -> P1 in T1 -> B1 - [ single substrate single process ]
# A(1,2,3) -> P1 in T1 -> B(1,2,3) - [ Multiple substrates single process]
#
# Model 2: Two process steps
# A(1..3) -> P1 in T1 -> B(1..3) ->......P2 in T2 -> c(1..3)
#
# Model 3: Multiple process steps
# A(1..n) -> P1 in T1 -> B(1..n) ->......Pm in Tm -> M(1..n)
#
# This will suit trying a NON-CLASS based program -> hard coded


# Process(n)[(wafer_load = 1, process_time = t(n), process_type = textual description)]
#
# Assume Each tool is a single wafer tool.
# Note: Wafer load could be as high as 400 in a batch dependant on tool.
# This variable will be used in a later revision.
#
# Differing processes using Process(n) as a super class:
#
# Photo = Process(n+a) + mask_number
# Clean = Process(n+b) + clean_method
# Dep = Process(n+c) + deposition_method
# Etch = Process(n+d) +etch_method
# Metrology = Process(n+e) + metrology_type
# Implant = Process(n+f) + implant_type
# CMP = Process(n+g) + cmp_type
# Box = Process(n+h) + in_or_out
# Store = Process(n+i) + location
#
# Process List
# The process list is a sequence of the different process types, Governed by mask stage.
# Each process is initially hard coded but ideally would be dragged in from a text or XML file. 
#
# Example:
# Box(1)[(wafer_load = 1, process_time = t(1), process_type = unboxing) + in]
# Clean(2)[[(wafer_load = 1, process_time = t(2), process_type = piranha) + (SAT_wet_clean)]
# Dep(3)[[(wafer_load = 1, process_time = t(3), process_type = initial_oxide) + (thermal_oxide)]
# Clean(4)[(wafer_load = 1, process_time = t(2), process_type = piranha) + (SAT_wet_clean)]
# Photo(5)[(wafer_load = 1, process_time = t(4), process_type = TRACKS,DEV) + (Resit and pattern processing)]
# Etch(6)[(wafer_load = 1, process_time = t(5), process_type = dry_etch_ox) + plasma_etch


# One lot one wafer one process (L1,W1,P1)

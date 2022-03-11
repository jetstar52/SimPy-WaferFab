# SimPy-WaferFab
Using SimPy to model a wafer fab
 - https://simpy.readthedocs.io/en/latest/index.html

Definition: fab is a semiconductor fabrication plant..makes computer chips...

The need for this model arose through a requirement to fearcast the tool requirements when upgrading or building a fab from new.

My goal here is initially to use the constructs of SimPy and my pathetic programming skills to build simple models that allow me to build a more complex model. 
This will be achieved with Python and an Obect Oriented style of programing. 
I do not care about Gui, or speed of the calculation at this time as my models will never be that intensive to begin with.

I am attaching the links to the SimPy tutorials that I am basing my work on.
  https://simpy.readthedocs.io/en/latest/simpy_intro/index.html
  [tutorial_simpy_2car.txt](https://github.com/jetstar52/SimPy-WaferFab/files/8234253/tutorial_simpy_2car.txt)  
  [simpy_tutorial1.txt](https://github.com/jetstar52/SimPy-WaferFab/files/8234261/simpy_tutorial1.txt) 
  [Guitar Factory - DISCRETE EVENT SIMULATION.docx](https://github.com/jetstar52/SimPy-WaferFab/files/8234263/Guitar.Factory.-.DISCRETE.EVENT.SIMULATION.docx)


Description of a fab:
A fabs task is to manufacture wafers that contain semiconducting devices. The basic process uses 8 steps.

-> Wafer has a deposition on it.
-> A photoresist mask is put on the wafer surface
-> The wafer is etched to remove the exposed material
-> the resist mask is removed
-> Ions are implanted in selected areas to create the semiconducting component
-> Metal is deposited and patterned to create conductors
-> The wafers are cleaned
-> The wafers are inspected
the steps are basic and will be combined in many ways and as an example a single metal layer requires about 12 masks and 400 steps.

There are typically steps before these oft-repeated steps as an example each new wafer:
- Wafer is cleaned
- Wafer is inspected
- Wafer is marked with an unique ID
- Wafer is cleaned

The simplest fab:
Wafer in -> Process -> semiconductor wafer out.

Second simplest fab:
> Wafer in -> Clean -> Process -> Metrology -> wafer out


The ideal model needs to expand to be able to allow a similar construction and process flow as the wafer fab.
Staring to process means that the wafer(s) will go through to the process bays:
- Start Bay
- Lithography Bay
- Wet Bay
- Dry Bay
- Furnace Bay
- Implant Bay
- Metrology Bay
- Metal Bay

The goal of going into a bay is to be processed by a tool. There are 8 bays. So we could have a Bay class. Would I then have each bay as a sub class. But my goal here I believe is to have the tools as classes with the processes on that tool as methods.

NOTE: Wafers are processed in LOTS of 25 wafers. Some systems process a single wafer at a time others process a multiple number of wafers ~ 400 wafers.
Single wafer processes can be a few seconds to some minutes, batch process es tend to take a VERY long time 5-10 hours. There is also a lovely spread of combinations imbetween. I am going to stick with single wafer = 1 min and 200 wafer Batch = 5 hours.

To calculate the number of tools in each bay/factory we would assign an output of x wafers per month and work backwards assuming NO LOSSES NO ERROR etc.such that we had continuous 24hrs processing.

I ignore maintenance and consumable needs for the moment.

# FlyUC battery opimization software

 - CLI(command line interface) tool for simple drone battery optimization
 - Picks optimal cell from a list of cells
 - Opimizes for **lightest weight**
 - Calculations based on **U7 420 KV** motor
 - Accounts for basic thermal losses(Joule heating)
 - **Does not account for voltage drop**
	 - To get a rough idea of accounting for voltage drop, multiply cells in parallel by 1.3	
		 - Find new pack dimentions by multiplying cells in series by new cells in parallel
 - Probably has a lot of bugs
 
## Outputs:
 - Pack voltage
 - Pack max continous current
 - Cells in series
 - Cells in parallel
 - Total cells
 - Total capacity(Ah)
 - Weight(kg)

## Other info:
 1. There is only one file to run, main.py
 2. Main function is at the very bottom of the file
 3. Inputs are at the top of main.py
 4. Contains 3 classes, motor, cell, and pack
 5. You can disable warning flags, but I don't recommend it, to disable, set FLAGS_ENABLED = 0
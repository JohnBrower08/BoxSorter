# BoxSorter
Scenario

As an engineer, you are tasked with designing a box sorting system where numerous boxes have been properly singulated (items have been separated out into a single line) ride on a conveyor until a sensor is blocked, at which time the conveyor will stop until the sensor is cleared.  Once the sensor is cleared, the conveyor will start back up until the next package blocks the sensor.  

All “valid” boxes will fall within the following parameters:

Parameter

Min              Max
 
Weight	0.5 Lbs.	1.0 Lbs.
Length	6.0 inches	9.0 inches
Width	6.0 inches	9.0 inches
Height	6.0 inches	9.0 inches

 

Facing upward on the top side of each of the boxes is a linear (Code128) barcode.  Inside of that barcode contains the following information:

    The package ID (an alphanumeric value 8 characters in length)
    A sort location code (a value of “1”, “2”, or “3”).  

Based on the sort location information contained in the barcode, the package needs to be sorted into one (1) of three (3) large bin locations (the packages do not need to be neatly stacked within the bin location).  

There is a fourth (4th) location where packages that are not assigned to one of the three (3) other bins are placed, which can be designated as a “Reject Bin”.  

No type of safety caging is desired around the location where the sorting is to take place.  
Deliverables

    Create a simple conceptual design illustrating the system.  
    Create a flow chart detailing the operation of the system (stopping the conveyors, determining how to sort the boxes, etc.)
        The flow chart should also describe how packages that cannot be sorted are handled.   
    Create a list of basic components required to implement the system (barcode readers, conveyors, sensors, etc.)

Bonus Points

    Update the flow chart to encompass capturing the mail piece ID and associating it with the final sort location.  
    Provide cost considerations for the solution that was developed.
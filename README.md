# Seat Map Generator
This workflow is comprised of 3 parts: 
1. A process for specifying/exporting seat locations in/from Adobe Illustrator  
2. A csv file for updating user seating assignments
3. A python script used to generate a labeled floor plan

## 1. Prepare Seat Map
You shouldn't have to do this very often!  
When you open reference_floorplan.pdf in Illustrator, you'll see the floorplan with numbered markers overlaid. These markers indicate the position of the labeled seat. If the floorplan is updated, the markers can be moved to indicated the new seat positions. To export the indicated seat positions for the Seat Map Generator, navigate to File > Scripts > Other Scripts, and then load get_seatPositions.jsx. The export location can be modified from the .jsx script, but the file name should be seatPositions.csv.  
Each marker is a group named with it's seat number in the layer "Desk_Labels". To add additional seats, duplicate an existing marker and update it's name to a new seat number. Update seatUsers.csv with a new row for the seat.

## 2. Update Seat Assignments
seatUsers.csv maps a seat number to a user. Move the user names around to update their seat assignment. Refer to reference_floorplan.pdf for seat locations!

## 3. Generate Labeled Floorplan
app.py takes base_floorplan.png, seatPositions.csv and seatUsers.csv and writes a pdf floorplan.pdf with the assigned seats labeled.
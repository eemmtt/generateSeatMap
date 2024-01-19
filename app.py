from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait, ELEVENSEVENTEEN
import csv

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

ORIGIN = Point2D(0,0)
OFFSET_X = -10
OFFSET_Y = -5
DOC_HEIGHT = 17 * 72
DOC_WIDTH = 11 * 72
IMAGE_PATH = "base_floorplan.png"
OUTPUT_FILE = "floorplan.pdf"

with open('seatUsers.csv', 'r') as file:
    reader = csv.DictReader(file)
    map_seatToUser = {}
    for row in reader:
        #Add user to seating dict, with seat number as key, and first name + last initial as value
        name_split = row['User'].split(" ", 1)
        first_last = name_split[0]
        if len(name_split) > 1:
            first_last += " " + name_split[1][0]
        map_seatToUser[int(row['Seat'])] = first_last
file.close()

with open('seatPositions.csv', 'r') as file:
    reader = csv.DictReader(file)
    map_seatToPos = {}
    for row in reader:
        map_seatToPos[int(row['Name'])] = Point2D(float(row['X']), float(row['Y']))
file.close()

c = canvas.Canvas(
    filename=OUTPUT_FILE,
    pagesize=portrait(ELEVENSEVENTEEN)
    )

c.setFont("Helvetica", 6)
c.drawImage(image=IMAGE_PATH, x=ORIGIN.x, y=ORIGIN.y, width=DOC_WIDTH, height=DOC_HEIGHT)
for seat in map_seatToPos.keys():
    #print(f"{i}: {seat.pos_desk.x}, {seat.pos_desk.y}, {map_seatToUser[i]}")
    try:
        c.drawString(x=map_seatToPos[seat].x + ORIGIN.x + OFFSET_X, 
                    y=map_seatToPos[seat].y + ORIGIN.y + OFFSET_Y, 
                    text=map_seatToUser[seat])
    except KeyError:
        print(f"Seat {seat} not found in seating chart.")

c.save()



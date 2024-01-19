//Script for Adobe Illustrator, get the positions of each group in a specified layer

var doc = app.activeDocument;
var layer = doc.layers["Desk_Labels"]; // Replace with your actual layer name
var group_list = [];

for (var i = 0; i < layer.groupItems.length; i++) {
    var group = layer.groupItems[i];
    var position = group.position; // This gives you the [x, y] position of the top-left corner of the group
    group_list.push({name: group.name, position: position});
};


var filePath = ""; // Replace with output file path
var file = new File(filePath);
file.open('w');
file.writeln("Name,X,Y");
for (var i = 0; i < group_list.length; i++) {
    file.writeln(group_list[i].name.concat(",",group_list[i].position)); // Writes the item and adds a new line
}

file.close();
alert("File written to " + filePath);

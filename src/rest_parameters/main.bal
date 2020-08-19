import ballerina/io;
function printDetails(string name,
                      int age = 18,
                      string... modules) {
    string detailString = "Name: " + name + ", Age: " + age.toString();    if (modules.length() == 0) {
        io:println(detailString);
        return;
    }    int index = 0;
    string moduleString = "Module(s): ";    foreach string module in modules {
        if (index == 0) {
            moduleString += module;
        } else {
            moduleString += ", " + module;
        }
        index += 1;
    }    io:println(detailString, ", ", moduleString);
}public function main() {
    printDetails("Alice");
    printDetails("Bob", 20);
    printDetails("Corey", 19, "Math");
    printDetails("Diana", 20, "Math", "Physics");
    string[] modules = ["Math", "Physics"];
    printDetails("Diana", 20, ...modules);
}

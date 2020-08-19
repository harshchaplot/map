import ballerina/io;
function 'function(int val) returns int {
    return val + 1;
}public function main() {
    int 'int = 1;
    int i = 'function('int);
    io:println(i);
    int '1PlusI = 1 + i;
    io:println('1PlusI);
}

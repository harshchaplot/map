import ballerina/io;
function calculate(int a, int b, int c) returns int {
    return a + 2 * b + 3 * c;
}public function main() {
    int result = calculate(5, 6, 7);
    io:println(result);
    result = calculate(5, c = 7, b = 6);
    io:println(result);
}

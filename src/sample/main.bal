import ballerina/http;
import ballerina/io;
import ballerina/log;

public function main() {
    io:println("Hello, World!");
}

service harsh on new http:Listener(9090) {
    resource function helloMe (http:Caller caller, http:Request req) {
        http:Response res = new;
        res.setPayload("Hello, World!");
        log:printDebug("debug log");
        var respondResult = caller->respond(res);
        if (respondResult is error) {
            log:printError("Error sending response", err = respondResult);
        }
    }
}
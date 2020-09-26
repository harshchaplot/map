import ballerina/io;
import ballerina/rabbitmq;

public function main() {

    rabbitmq:Connection connection = new ({host: "localhost", port: 5672});

    rabbitmq:Channel newChannel1 = new (connection);
    rabbitmq:Channel newChannel2 = new (connection);

    var queueResult1 = newChannel1->queueDeclare({queueName: "MyQueue"});
    if (queueResult1 is error) {
        io:println("An error occurred while creating the MyQueue queue.");
    }

    var queueResult2 = newChannel2->queueDeclare({queueName: "MyQueue2"});
    if (queueResult2 is error) {
        io:println("An error occurred while creating the MyQueue2 queue.");
    }

    worker w1 {
        var sendResult = newChannel1->basicPublish("Hello from Ballerina",
                                        "MyQueue");
        if (sendResult is error) {
            io:println("An error occurred while sending the message to " +
                     "MyQueue using newChannel1.");
        }
    }

    worker w2 {
        var sendResult = newChannel2->basicPublish("Hello from Ballerina",
                                        "MyQueue");
        if (sendResult is error) {
            io:println("An error occurred while sending the message to " +
                    "MyQueue using newChannel2.");
        }
    }

    worker w3 {
        var sendResult = newChannel1->basicPublish("Hello from Ballerina",
                                        "MyQueue2");
        if (sendResult is error) {
            io:println("An error occurred while sending the message to " +
                    "MyQueue2 using newChannel1.");
        }
    }
    _ = wait {w1, w2, w3};
}
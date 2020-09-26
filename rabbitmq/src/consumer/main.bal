import ballerina/log;
import ballerina/rabbitmq;

rabbitmq:Connection connection = new ({host: "localhost", port: 5672});

listener rabbitmq:Listener channelListener = new (connection);

@rabbitmq:ServiceConfig {
    queueConfig: {
        queueName: "MyQueue"
    }
}

service rabbitmqConsumer on channelListener {

    resource function onMessage(rabbitmq:Message message) {

        var messageContent = message.getTextContent();
        if (messageContent is string) {
            log:printInfo("The message received: " + messageContent);
        } else {
            log:printError("Error occurred while retrieving the message content.");
        }
    }
}
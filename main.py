import paho.mqtt.client as mqtt  # import the client1
import time
import random
broker_address = "localhost"
# broker_address="iot.eclipse.org"


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def on_log(client, userdata, level, buf):
    print('log: ', buf)


def on_disconnect(client, userdata, rc=0):
    print("Disconnect: ", str(rc))
    logging.debug("Disconnected: " + str(rc))
    # client.reconnect()
    client.loop_stop()


def on_publish(client, userdata, mid):
    print("mid: ", str(mid))


def send_data_to_broker(message, topic):
    print("creating new instance")

    client = mqtt.Client("P1", protocol=mqtt.MQTTv311)  # create new instance

    client.on_message = on_message

    client.on_publish = on_publish

    # client.on_log = on_log

    client.on_disconnect = on_disconnect

    print("connecting to broker located in: ", broker_address)
    # connect to broker
    client.connect(broker_address, keepalive=100)
    print("Subscribing to topic: ", topic)
    client.subscribe(topic=topic)
    print("Publishing message to: ", topic)
    client.publish(topic, message)
    time.sleep(4)


while True:
    print("\n\n\n\n\n\n[1]: Manual Data Entry \n[2]: Temperature Simulation\n\tSends Message if T > 40 °C\n[3]: Distance Simulation\n\tSends Message if you go further than 300 cm\n")
    Scenario = input(
        "What kind of scenario would like to simulated?(input number)")
    if Scenario == '1':
        topic = input("What topic would you like to store your data under: ")
        message = input("what do you want do you want to send: ")
        send_data_to_broker(message, topic)
    elif Scenario == '2':
        T = random.triangular(20, 47)
        if T >= 40:
            send_data_to_broker(T, "Temperature")
        else:
            print("Temperature turned out less than 40: ", T)
            time.sleep(2)
    elif Scenario == '3':
        print("Simulating distance values...")
        time.sleep(2)
        D = random.randint(0, 300)
        if D >= 300:
            send_data_to_broker(D, "Distance")
        else:
            print("You're still close!! ( "+str(D * 0.01) +" Meters)")
            time.sleep(2)
    else:
        pass

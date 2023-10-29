# Implement Stop and Wait Protocol and execute the same and display 
# the result.
import time
import random

# sender_message = [1, 2, 3, 4, 5]
sender_message = list(map(str,input("Enter the data : ").split(",")))
print(f"Sender Frame : {sender_message}")
receiver_message = []

sn = 0
while sn < len(sender_message):
    frame = sender_message[sn]

    def sender():
        print(f"SENDER: Sending frame '{frame}'")
        if random.random() < 0.2:
            print("SENDER: Frame Corrupted!")
        else:
            time.sleep(1)
            print(f"SENDER: Frame '{frame}' is Sent Successfully!")
            receiver()

    def receiver():
        global sn
        receiver_frame = frame
        print(f"RECEIVER: received Frame '{receiver_frame}'")

        receiver_ack = random.choice([True,False])
        if receiver_ack:
            receiver_message.append(receiver_frame)
            print("RECEIVER: Sending ACK")
            sn = sn + 1
        else:
            print("RECEIVER : ACK failed")
            sender()

    sender()

print(f"Receiver Frame : {receiver_message}")

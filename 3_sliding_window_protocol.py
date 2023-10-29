# Implement Sliding Window Protocol in python program and execute 
# the same and display the resultimport time
import time

RTT = 5

window_size = int(input("Enter window size: "))
f = int(input("\nEnter number of frames to transmit: "))
frames = []

print("\nEnter", f, "frames:")
for i in range(f):
    frame = int(input())
    frames.append(frame)

print("\nAfter sending", window_size, "frames at each stage sender waits for ACK")
print("Sending frames in the following manner...\n")

for i in range(f):
    if i % window_size != 0:
        print(frames[i], end=" ")
    else:
        print(frames[i])
        print("SENDER: waiting for ACK...\n")
        time.sleep(RTT/2)
        print("RECEIVER: Frames Received, ACK Sent")
        print("-------------------------------------------")
        time.sleep(RTT/2)
        print("SENDER: ACK received, sending next frames")

if f % window_size != 0:
    print("\nSENDER: waiting for ACK...")
    time.sleep(RTT/2)
    print("RECEIVER: Frames Received, ACK Sent")
    print("-------------------------------------------------")
    time.sleep(RTT/2)
    print("SENDER: ACK received.")

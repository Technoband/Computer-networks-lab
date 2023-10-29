# Write a program for congestion using the leaky bucket algorithm in  
# Python and execute the same and display the result
import time 

bucket_data = []
loss_data = []

print("...Leaky Bucket...")
print()
print("The Capacity of bucket is 10 packets only!")
print()

n = int(input("Enter the data packets : "))
for i in range(1,n+1):
    if len(bucket_data)<10:
        bucket_data.append(i)
    else:
        loss_data.append(i) 
        print(f"{i} is loss! Congestion Occurs!")    
print(f"Bucket Contain the Following Packets : {bucket_data}")    
print(f"Loss data are : {loss_data}")    

print()

print("Transmiting the packets..")
print("Packets are transmitted with Constant rate (2 sec)")

for i in range(1,n+1):
    time.sleep(2)
    bucket_data.pop(0)
    print(bucket_data)
if bucket_data == []:
    print("Bucket is empty!")    

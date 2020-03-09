# init vcan

```
sudo ip link set can0 type can bitrate 500000
sudo modprobe vcan  
sudo ip link add dev vcan0 type vcan  
sudo ip link set up vcan0
```

# to see the data on the bus

```
candump vcan0
```

# send some data 

```
cansend can0n123#1122334455667788
```

# setup scoketcand

```
socketcand -v -n -i vcan0 -l lo -p 29536
```



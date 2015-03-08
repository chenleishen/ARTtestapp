from bluetooth import *


print "performing inquiry..."

nearby_devices = discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)

for name, addr in nearby_devices:
     print " %s - %s" % (addr, name)
'''
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("10:40:F3:AB:DB:17", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
'''
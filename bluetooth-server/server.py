#from bluetooth import *
import bluetooth as bluetooth

# Tutorial:
# http://homepages.ius.edu/RWISMAN/C490/html/PythonandBluetooth.htm
#http://stackoverflow.com/questions/21866100/android-bluetooth-client-and-server-wont-connect
'''
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "1aefbf9b-ea60-47de-b5a0-ed0e3a36d9a5"
testUuid = "00001101-0000-1000-8000-00805F9B34FB"

advertise_service( server_sock, "GlassServer",
                   service_id = testUuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")

'''


server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
client_sockets = []

server_socket.bind(("",bluetooth.PORT_ANY))
port = server_socket.getsockname()[1]
uuid = "00001101-0000-1000-8000-00805F9B34FB"

print "Listening for devices..."

# advertise service
server_socket.listen(1)
bluetooth.advertise_service( server_socket, "Validation Host",
    service_id = uuid,
    service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
    profiles = [ bluetooth.SERIAL_PORT_PROFILE ],
)

# accept incoming connections
client_sock, client_info = server_socket.accept()
client_sockets.append(client_sock)
print "Accepted Connection from ", client_info
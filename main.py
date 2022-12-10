import json
import psutil
import time
from socketserver import TCPServer, BaseRequestHandler

# Define a handler class that will be used to process the incoming data
class DataHandler(BaseRequestHandler):
    def handle(self):
        # Retrieve information about the CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        data = {'cpu': cpu_percent}

        # Retrieve information about the memory usage
        memory = psutil.virtual_memory()
        data['memory'] = {
            'total': memory.total,
            'available': memory.available,
            'used': memory.used,
            'percent': memory.percent
        }

        # Convert the data to a JSON string
        json_str = json.dumps(data)

        # Send the JSON string to the client
        self.request.sendall(json_str.encode())

# Create a new server and start listening for incoming connections
server = TCPServer(('localhost', 8080), DataHandler)
server.serve_forever()

This repository contains the deployment files and image creation for the robotic demo.


Use the following command to deploy on the kubernets cluster:

''' 
kubectl apply -k k8s_deployment -n <namespace>
'''

You will deploy:

- Foxglove studio container with a default layout
- Foxglove bridge and zenoh bridge container colocated with Foxglove studio for easier communication
- Zenoh Router
- MQTT broker

After deployment you can reach the Foxglove Studio (using Chrome webbrowser) at https://foxglove-demo.robopaas.dev/ and open a websocket connection to the bridge to reach the ROS world towards this ingress wss://bridges.robopaas.dev


Any ROS topic published to the same Zenoh Router can be shown in the Foxglove dashboard.

N.B. You might need to change the NodePorts used!

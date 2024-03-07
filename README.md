This repository contains the deployment files and container image creation files for the robotic demo.


Use the following command to deploy on the kubernetes cluster:

``
kubectl apply -k k8s_deployment -n <namespace>
``

You will deploy:

- Foxglove studio container with a default layout (using a configmap)
- Foxglove bridge and Zenoh bridge container colocated with Foxglove studio container for easier communication
- Zenoh Router
- MQTT broker

After the deployment you can reach the Foxglove Studio (using Chrome webbrowser) at https://foxglove-demo.robopaas.dev/ and open a websocket connection to the bridge to reach the ROS world towards this ingress wss://bridges.robopaas.dev 
Any ROS topic published to the same Zenoh Router can be shown in the Foxglove dashboard.

The MQTT broker is going to used to expose data from ROS to the outer world using this client https://github.com/ika-rwth-aachen/mqtt_client  

N.B. You might need to change the NodePorts used!

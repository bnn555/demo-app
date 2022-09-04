# demo-app

This is a demo app that is deployed on Azure cloud using kubernetes created by Nicolae Bodislav.  
In this example we are going to create a new virtual server deployed on cloude that we are going to call **clientVM**. On this server we are going to install [AKS-Engine](https://github.com/Azure/aks-engine). This would help us to deploy a Kubernetes cluster and on that cluster we are going to deploy 2 simple services.  
In order to follow the example you must go to **deployment-how-to** folder and follow the 5 steps:  
1. [Setup initial clientVM](deployment-how-to/1.Setup_initial_VM.md)
2. [Deploy kubernetes cluster](deployment-how-to/2.Deploy_kubernetes_cluster.md)
3. [Deploy app with services](deployment-how-to/3.Deploy_app_and_services.md)
4. [Nginx ingress controller setup](deployment-how-to/4.nginx-ingress-controller-setup.md)
5. [Network policies](deployment-how-to/5.Network-policies.md)

The 2 services that are going to be deployed can be found in the folders **service-a** and **service-b** each with his own readme file.

Thanks,
Nicolae.
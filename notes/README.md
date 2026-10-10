# Notes

## Introduction of Docker and Containers 
#### What are Containers?
- Containers are light weight, portable  units for running applications. 
- They bundle one applications with all of its dependancies ensuring that it runs consistently across different environments. 
- Example: You have an application and you want to run every part of the application. Containers will include the code, the run time, the libraries and anything I need, including all dependancies that the application needs to run. As containers are isolated it runs the same on any environment. 

![Containers](images/containers.png) 

- What is it showing in the above image?
1. You have 3 containers that sit above a Docker Engine 
2. Each container has its 'App' and its 'Binaries/Libraries' -> The app requires this to run
3. The Docker Engine sits on the Host Operating System. 
4. The Host Operating System sits above the Infrastructure 
- Infrastructure -> represents the physical, virtual hardware, where everything runs
- Host Operating System -> this is the OS that runs directly in the Infrastructure. It is the foundation for everything above it. e.g. MacOS HOS is MacOS. 
- Docker Engine -> is what makes containerisation possible. Provides the environment to build, run and manage containers. 
- Docker containers -> This isolation of each container, ensures each application runs consistently regardless of the environment. This is why App A doesnt affects App B, App B doesn't affect App C etc. 

#### Benefits of Containers 
1. Isolation -> containers isolate applications for each other and the underlying system -> prevents conflicts ensuring applications runs smoothly 
2. Consistent environment -> makes development and deployment more predictable and relibale. 
3. Efficient -> containers are more resource efficent than traditional virtual machines. They share the host OSkernal. This reducing overhead and allows more containers to run on the same hardware. 


#### What is Docker?  
- Docker is the most popular platform for managing containers 
- Docker is an open platfrom for developing, shipping and running applications in containers 
- Simplifies the process of managing containers, making it easier to build, deploy and run applications

##### Key components of Docker 
1. Docker Engine -> This the core service that runs and manages containers. Controls the whole thing. A portable, lightweight application runtime and packaging tool. 
2. Docker Hub -> is a repo, where you can find and share container images. Its like the App Store for Docker images. It is a cloud service for sharing applications and automating workflows. 

#### Images and Containers 

1. Images 
- Images are templates for creating containers.
- Images are snapshot of an application at a certain point in time.
- Images are immutable -> do not change once they are created
- - The immutabillity characteristic ensures that the applications runs consistently no matter where it is deployed. 

2. Containers 
- Containers are running instances of images 
- If an image is a recipe, a container is the dish you create from it. 
- Containers are what you interact with -> can start, stop, modify them as needed

- Docker file is used to create these images. Contains a series of instructions that docker uses to assemble an image 

#### Importance in Modern Development

1. Simplified deployment -> the biggest challenge with software development is ensuring that applications work consistently across different environments. This problem is solved by docker by creating an consistent environment from development to production. 
2. Improved efficiency -> Traditional virtual machines can be resource heavy and slow to start. Docker containers are lightweight and shares the Host System's Kernal which allows it to start up almost instantly. 
3. Enhanced collaboration -> docker allows collaboration with team members. You can just share the docker image with team and everyone is working in the same environment. Onboarding new developers becomes faster and less error prone. 
- - Docker integrates smoothly with CI/CD pipelines -> allows for automating testing, and deployment of containers. 

#### VMs vs Containers 

1. Virtual Machine 
- Allows multiple operating systems to run on a single physical machine. 
- At the base is the infrastucture. On top of that sits the host operating system. Above that is the hypervisor -> which is reponsible for creating and managing virtual machines by allocating resources like CPU, Memory and Storage. 
- Each virtual machine runs a full guest OS, which is completley isolated from others. 
- Within the setup of Applications, bin/libr, there is a strong isolationg 
- This means VM is resource heavy, taking up significant CPU, memory and storage. 

2. Containers 
- Containers are more lightweight and efficent way to isolate applications. 
- They share the whole Host operating system, but instead of using a Hypervisor, they run on the Docker engine. 
- Containers are isolated from each other at the process level but they share the same OS Kernal - making them much lighter than VMs 
- Containers can start up quickly and can use far lesser resources than VMs 

##### Key differences 

1. Virtual Machine 
- Startup -> Needs to boot up a full Guest OS -> can take minutes 
- Resource Usage -> Consume more resources 
- Isolation -> Strong isolation
- Portabillity -> Less portable due to size and dependencies on specific Hypervisor

2. Containers 
- Startup -> share the Host Operating System -> starts within seconds 
- Resource Usage -> Resource efficent 
- Isolation -> Process level isolation - is efficent but not robust like VM 
- Portabillity -> highly portable and can run consistently across environments 








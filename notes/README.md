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


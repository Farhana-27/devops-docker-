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

## Docker Setup and Fundementals 
- docker --version -> see if installed 
- docker info -> information on the docker 
- docker run hello-world -> docker will search for this on your own terminal and if not found will take this out from its own library 
- docker ps -> shows any existing containers and info related to it 

#### What is a dockerfile?
- It is a series of instructions on how to build a docker image 
- Each instruction is in the docker file creates a layer in the image 
- Think of it as a recipe for creating your containerisation
- You are do repeatable builds - meaning you can create the exact same environment every single time 

#### Key comands of docker 
1. FROM -> specifies the base image to use for the Docker image 
2. RUN -> executes commands in the container. 
3. COPY -> copies files from the host machine into the container 
4. WORKDIR -> sets the working direcotry for subsequent instructions 
5. CMD -> specifies the command to run when the container starts 

##### Example 
- Use the official Node.js image as the base image FROM node:14
- Set the working directory in the container WORKDIR /app 
- Copy the package.json and package-lock.json files COPY package*.json ./
- Install dependencies RUN npm install 
- Copy the rest of the application code COPY ..
- Expose the application port EXPOSE 3000 
- Specify the command to run the application CMD ["node", "index.js"]

## Docker Networking 
#### Basic Networking concepts in Docker 
- Bridge network -> is the default network mode for containers on the same machine. Containers connected to the bridge network can communicate with each other using their own IP addresses. Isolated from your host machine network, proividing an extra level of security 
- Host Network -> In host mode, a container uses the host machines network directly without any isolation. Its as if the container is plugged directly into your home network, with no distincton between the container and the host. This mode is useful for applications that need to closley interact with the host system 
- None Network -> this option gives the container no network interface at all which makes it completley isolated. Its like a room with no doors or windows. 

- Think of containers as small portable apps and networks allow these apps to talk to each other, share data and function as a cohesive system. 

#### Docker Compose 
- Docker Compose helps you run multiple Docker containers together 
- Key features 
- - Docker-compose.yml file 
- - Commands 
- - Networking 

##### Importance in DevOps 
- Makes development and testing easier 
- Ensures consistency 
- Enhances Teamwork 

#### Docker Registries
- Docker Registry is a system for storing and sharing Docker images 
- Key features 
-  - Private registries 
-  - Public registries 

##### Importance of Docker Registries in DevOps 
- Steamline Deployment -> once your docker images is stored in a registry it cna be easily accessed and deployed across multiple environments, fro development all the way to production. Makes it faster and more reliable to roll out new features or updates 
- Enhances Collaboration -> when your images are stored, everyone on your team has access to the same resources making it easier to share and manage images. 
- Ensures conistency -> you can make sure that the exact same image is being used in development, testing and production. Means what you have tested locally is exactly what runs in production. 

##### DockerHub: A popular Docker Registry 
- A public registry where you can store, share and access docker image. 
- Its like the app store for docker images 
1. Accessibilty -> you can easily pull images to start your projects 
2. Hosts a large collection of community contributed images 
3. Free tier -> you can use it for free 

##### Amazon ECR (elastic container registry)
- Is a fully managed docker registry service that is great for storing and managing private docker images 

##### Important Docker Commands 
- To get a quick overview of the images stored locally -> docker images 
- More detailed information about an image -> docker inspect (docker ID) 
- Cleaning up your docker environment. Note if the container is still running, docker will not remove it and you need to stop it and then remove it -> docker rmi (docker ID)
- Remove all unused docker obejects -> docker system prune -> this removes all stopped containers, all networks is not used by a container, all dangling images and all dangling build cache 
- To stop a container from running -> docker run (container ID)
- To remove it completley -> docker run (container ID)
##### Making out image lighter: Multistage builds!
- The Docker image created is quite large - large images can slow down your deployments - consumes more bandwidth and uses up your storage 
- Optimise the docker file using multistage builds -> this allows you to use multiple FROM statements in the docker file. 
- aim is to use one stage to build your application and the other, much lighter stage to create the final image that you deploy -> allows you to discard unnessecary dependencies. 
- smaller images quicker to pull from a registry, faster to deploy and take up less disk space. 

##### Orchestration Tools 
- What we’ve learned so far: We’ve covered the Docker basics, which means building apps into containers, making the images smaller and getting them running.
- The next problem: Big real-world apps can have hundreds or even thousands of containers. Starting and looking after each one by hand gets too hard, and even Docker Compose can’t keep up at that size.
- The answer is “container orchestration”: Special tools manage lots of containers for you automatically. They start containers, add more when the app gets busy and replace ones that break.
- The two tools covered:
- - Kubernetes: the most popular orchestration tool. It gets its own full module later.
- - Docker Swarm: Docker’s own, simpler tool, which this section compares with Kubernetes.
- When you need it: The section also explains how to tell when these tools stop being nice to have and become a must.
- Why it matters for your career: Orchestration is a core skill for jobs like DevOps engineer, site reliability engineer (SRE) and cloud engineer.
- In one line: Docker runs containers, and orchestration tools like Kubernetes manage huge numbers of them for you.

##### Kubernetes 

- The problem: Docker works well for a few containers on one computer. But real companies may need to run hundreds or thousands of containers spread across many computers. Doing that by hand is slow and easy to get wrong.
- What Kubernetes is: A free, open-source tool that runs and manages containers for you automatically. People often shorten it to K8s, with the 8 standing for the eight letters between the “K” and the “s”.

Think of it as a manager for your containers. It:
- Deploys them, making sure each container starts up correctly.
- Scales them, adding more containers when the app gets busy and removing them when it’s quiet.
- Self-heals, so if a container crashes, it replaces it on its own.
- It hides the messy details. You don’t have to think about which computer each container runs on. You just focus on your app.
- The big cloud companies offer it too. AWS, Google Cloud and Azure each have their own ready-made Kubernetes service, so developers can spend their time writing code instead of managing containers.

Why learn it:
- Most modern companies build apps as lots of small pieces (called microservices) that run in the cloud, and Kubernetes is the standard way to run them.
- Kubernetes takes some effort to learn, so people who know it well are in demand. That’s where DevOps engineers come in.

- In one line: Kubernetes is an automatic manager that runs, scales and fixes huge numbers of containers across many computers, so you can focus on your app.

##### Docker Swarm vs K8s
Docker Swarm:

- Built into Docker, so it’s easy to set up, especially if you already know Docker commands.
- Easy to start a cluster. A cluster is just a group of computers working together.
- No automatic scaling. You add or remove containers yourself, or use extra tools.
- Has a solid community, but a smaller one than Kubernetes.
- Can only do what Docker itself supports.
- - Best for: smaller, simpler projects.

Kubernetes (K8s):

- Originally made by Google, and now the industry standard.
- Automatic scaling adds or removes containers on its own as the app gets busier or quieter.
- Has a huge, active community, which means more help, more guides and constant improvements.
- Harder to set up because you need to understand more of how it works. Ready-made cloud services from AWS, Azure and Google Cloud make this much easier.
- Isn’t limited to Docker. It works with other container tools too and has more advanced features.
- Best for: large, complex company apps.

## Docker Swarm vs Kubernetes

| Feature              | Docker Swarm           | Kubernetes           |
|----------------------|------------------------|----------------------|
| Ease of setup        | Easy                   | Harder               |
| Automatic scaling    | No                     | Yes                  |
| Community            | Good                   | Very large           |
| Works beyond Docker  | No                     | Yes                  |
| Best for             | Small, simple projects | Big, complex projects |

##### Why Orchestration tools?

- Why use orchestration tools: Once an app grows to lots of containers on lots of computers, managing them by hand gets too hard. Tools like Kubernetes and Docker Swarm do that work for you automatically.
- They keep your app running (high availability): They watch your containers all the time. If one breaks, they restart it or move it to another computer, with no human needed. This is also called self-healing.
- They scale automatically: They add containers when lots of people use the app and remove them when it’s quiet. That keeps the app fast and saves money.
- They save you effort: Lots of manual jobs get automated, so developers can spend their time improving the app instead of managing computers.
- Your role as a DevOps engineer: You’ll be the Kubernetes expert, comfortable running its commands. The upcoming Kubernetes section teaches this in detail.
- In one line: Orchestration tools keep big apps running, growing and fixing themselves automatically, and automation is a big part of what DevOps is about.



## ADVANCED SECTION 
#### Containers for scratch 
- DevOps engineer job is to host applications on AWS, Cloud or any infrastructure 
- Docker, ECS, EKS are heavy in the industry 
#### Containers from First Principles
1. Basics: Where does it start from?
- You are a DevOps engineer and you are handed a file/zip/repo and you are asked "Hey can you containerise this and deploy it on ECS or Kubernetes?"
- This is real and happens everyday 

2. First question: How do I run this app normally?
- Before docker, before containers, before cloud, before base image 
- We MUST know how the app runs on a normal computer 

The rule:
- If you don't know how to run it normally 
- You will never know how to run it inside a container 
- GOAL -> find the app's entrypoint command 

Examples 
1. Python -> python app.py 
2. Node -> node index.js 
3. Go -> go run app.go 
4. Jave 
- - mvn package 
- - java -jar target/app.jar 
5. c# -> dotnet run 
6. PHP -> php -S localhost:8000

- Go, Jave etc. are compound languages. That means when you run that command, that language will create a binary. That binary is litreally your application. If you have that binary, and you put it in the container, it will RUN 
- Python and Node are NOT compound. It is in pure english but when you run it, it is a heavy applicaton on your laptop, container -> this is because it requires alot of dependencies to run

- Static site: Just open in a browser 
- Key insight: Every app already has an 'entrypoint' command 
- Docker does not invent anything - it just runs the same command inside the container 











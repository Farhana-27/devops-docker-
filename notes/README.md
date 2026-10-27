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

## Containers from First Principles (ECS Accelerator, Session 1)
- **What the series is for**
  - It's a run of about 8–10 weekly sessions to help with the **ECS project**. It covers the steps in order: get the app → Dockerise it → Terraform → ECS/EKS.
  - **Why Docker, ECS and EKS:** containers on ECS and on Kubernetes (EKS) are the most in-demand skills in industry right now. EC2s (virtual machines in AWS) and on-prem servers (a company's own machines) are still used, and serverless is a possible future roadmap.
  - **The DevOps / platform engineer's job:** host applications on the cloud (AWS) and look after the infrastructure. Docker is just one tool for that.

- **The real-world scenario**
  - At work, a developer hands you a folder, a zip or a repository and says: **"Containerise this so I can deploy it to the cloud"** (ECS, Kubernetes and so on). This happens all the time.
  - **The first question to ask, before writing any Dockerfile:** *"How do I run this app normally, without Docker?"*

- **The golden rule: find the app's entry point**
  - **If you can't run an app on your own computer, you can't run it in a container.**
  - The **entry point** is the command that starts the app. An app may have many APIs, but none of them work until the app is started.
  - **Where to find it:** the project's **README** usually lists the run commands. If it doesn't, check which language the app uses (GitHub shows this on the repo page) and look up how apps in that language are started.
  - **Common entry point commands:**

    | Language | Command to run the app |
    |---|---|
    | Python | `python app.py` or `python3 app.py` |
    | Node (JavaScript) | `node index.js` |
    | Go | `go run` |

- **Compiled vs. non-compiled languages** (useful later for writing Dockerfiles)
  - **Compiled (Go, Java, C#):** building the app turns it into a single **binary** file, and that binary *is* the app. You can put just the binary into a container, which makes the container **lighter**. The code is harder for people to read.
  - **Not compiled (Python, Node):** the code is easy to read, almost like English. But running it needs **lots of hidden dependencies**, so the app and its container are **heavier**.

- **How the entry point links to Docker**
  - A Dockerfile uses the same idea, with the instructions **`CMD`** or **`ENTRYPOINT`**. The differences between them come in a later session.
  - You use **the same command you'd run on your computer**, but it runs inside the container. For example, `CMD ["python", "app.py"]`.

- **What a container is (a common interview question: containers vs. VMs)**
  - A **VM (virtual machine)** is a whole, heavy computer with its own full operating system. Using a whole VM for one app wastes a lot of resources.
  - A **container** is a **small, lightweight box inside a computer**. One VM, or your laptop, can run **many containers**, but a container can't hold VMs.
  - **House analogy:** the VM is the **house** and each container is a **room**. Every room has its own files, network and app, separate (**isolated**) from the other rooms.
  - **Why it's useful:** once a container works and you've tested it, it will usually run the same on **any other computer**, ECS machine or EKS cluster.
  - **Why containers exist:** to keep things **light, with no wasted space**. They're built on an older Linux feature called **namespaces**, which keeps processes isolated from each other.

- **How containers are made (the chain to remember)**

  ```
  Dockerfile  →  builds an  →  Image  →  runs as a  →  Container
  ```

  - To get a **container**, you need an **image**.
  - To get an **image**, you need a **Dockerfile**.

  ## Base Images, Image Types & Dockerfile Instructions (ECS Accelerator, Session 1, part 2)

- **The 4 things every container needs to work**
  - If a Dockerfile has these 4 things, the container will almost always work. Everything else is an extra that improves things, like security settings or adding a user.
    1. **A base image** (`FROM`): the environment the app needs, such as Python, Node or Go.
    2. **The dependencies** (`COPY` the dependency file + `RUN` the install): the libraries the app needs.
    3. **The application code** (`COPY`): the app itself.
    4. **The start command** (`CMD` / `ENTRYPOINT`): how the container runs the app.
  - **Think backwards:** first work out what language the app uses and how it runs locally. That tells you which base image to choose.

- **Choosing a base image**
  - Use a **language-specific image** that matches the app, for example `python:3.12-slim`, `node:20` or `golang`. Seeing `FROM golang` usually means it's a Go app.
  - **Avoid full operating-system images** like `ubuntu` or `centos`. They contain a whole OS, which makes the image heavy and is rarely needed.
  - Base images are built by other people, often open source, from their own Dockerfiles. Many are a lighter version of Ubuntu or Debian with the language added on top.
  - **How an image name is read:** `name:version-type`. For example, `python:3.12-slim` means Python, version 3.12, slim type.

- **Image types, from biggest to smallest**

  | Type | Example | What's inside | Good | Bad |
  |---|---|---|---|---|
  | **Full** | `python:3.12` | A full system with all tools and compilers | Easy, everything usually works | Heavy, slow, less secure, lots of bloat |
  | **Slim** | `python:3.12-slim` | A minimal OS, just enough to run the app | Much smaller, and the usual choice for Python | Sometimes too minimal, so the app may be missing a system library it needs |
  | **Alpine** | `node:20-alpine` | A tiny Linux with basic tools | Very small, and works well for Go and Node | Uses a different core library (**musl** instead of **glibc**), which can break Python packages |
  | **Distroless** | Google's distroless images | Only the app and what it needs. **No shell, no package manager** | Very secure | Hard to debug, because you can't `docker exec` into it |
  | **Scratch** | `scratch` | **Completely empty**: no shell, no files | Tiny. A Go app can be about 5–10 MB | Only works for **compiled** languages (Go, Rust, C). **Not** for Python or Node |

  - **Why scratch works for compiled languages:** Go, Rust and C build the app into one **binary** file. The container only has to run that file, for example `./server`, so it needs nothing else.
  - **There's a limit to shrinking:** Python and Node are heavy languages by nature, so their images can only get so small.
  - **Everything is a trade-off:** big companies often choose light languages like Go and Rust to save money, but those are harder to learn. Python is easy to read but heavier.

- **The Python example Dockerfile, step by step**
  - **Locally,** you'd install the requirements (`pip install -r requirements.txt`) and then run `python app.py`. **The Dockerfile repeats exactly those steps.**
  - `requirements.txt` lists the app's libraries, such as `Flask`. Every language has its own dependency file.
  - **`WORKDIR /app`:** sets the folder inside the container where the app lives. It's **optional**, because without it everything goes in the root folder `/`, which works but is messy. It's good practice to set it.
  - **`COPY requirements.txt .` → `RUN pip install --no-cache-dir -r requirements.txt` → `COPY . .`**
    - Without copying `requirements.txt`, the dependencies can't be installed.
    - `--no-cache-dir` stops pip from keeping downloaded files, which makes the image smaller.
    - **Copy the dependency file first, then the code.** This is for **layer caching**: if only the code changes, Docker reuses the saved install step, so rebuilds are much faster.
  - **`COPY . .` copies everything,** which isn't ideal. Use a **`.dockerignore`** file to leave out things you don't need, like the `venv` folder.

- **`EXPOSE`**
  - It's **for documentation only.** The app still works if you remove it.
  - It tells other people which port the app uses. For example, on ECS you need to know which port to open.
  - The port is actually opened when you **run** the container, for example `docker run -p 5000:5000`, not in the Dockerfile.

- **The start command depends on the language**
  - Python: `CMD ["python", "app.py"]`. Node: `CMD ["node", "index.js"]`.
  - Go and other compiled languages: build the binary, then run it with `./server`. The Go example uses a **multistage build**: stage 1 builds the binary, and stage 2 copies only the binary and runs it.
  - **It's the same command you'd run on your own computer. There's nothing magic about it.**

- **Similar instructions and how they differ (common interview question)**

  | Instruction | When it runs | Key point |
  |---|---|---|
  | **`RUN`** | While **building** the image | Installs things, changes permissions and so on |
  | **`CMD`** | When the **container starts** | The **default** command. **It can be overridden** on the command line |
  | **`ENTRYPOINT`** | When the **container starts** | **Always runs**, so it's "set in stone". Choose it carefully |
  | **`COPY`** | While building | Copies files from your project into the image. **Predictable**, so it's preferred |
  | **`ADD`** | While building | Like `COPY`, but it can also **download from URLs** and **unpack archives** like zip or tar files. It's rarely used, because a URL can change, which makes builds unpredictable |

  - **Goal:** containers should be **deterministic**, meaning they build the same way every time. That's why `COPY` is preferred over `ADD`.

- **The rough Dockerfile template**

  ```dockerfile
  FROM <language>:<version>-<type>    # 1. Base image (slim, alpine, distroless, scratch)
  WORKDIR /app                        #    Optional but good practice
  COPY <dependency file> .            # 2. Dependencies (these two lines go together)
  RUN <install command>
  COPY . .                            # 3. The application code
  EXPOSE <port>                       #    Optional, for documentation
  CMD ["<runtime>", "<file>"]         # 4. Start command (CMD or ENTRYPOINT)
  ```

- **Layers**
  - **Every instruction (line) in a Dockerfile creates a layer**, and layers add to the image size.
  - **Keep the number of layers small.** For example, combine several Linux commands into **one `RUN`** using `&&` instead of writing five separate `RUN` lines.
  - Run `docker history <image>` to see each layer and how big it is.

  # Docker Session Notes: Examples, Debugging & Q&A



## 1. Image sizes: base image choice matters

| Image | Size (approx.) | Why |
|---|---|---|
| Python basic (`python:3.12`, full) | ~1.65 GB | Full OS + build tools |
| Python slim (`python:3.12-slim`) | ~630 MB | Stripped-down Debian |
| Python distroless + multistage | ~103 MB | Only the runtime + the app |
| Java (full JDK image) | ~300 MB | Not using a slim/JRE-only base |
| C# | ~350 MB | |
| Go multistage (distroless) | ~60 MB | Builder stage thrown away |
| Go `scratch` | ~10 MB | Empty image + compiled binary only |

**Why Go can use `scratch` but Python can't:** Go compiles to a single static binary that needs nothing else.
Python needs an interpreter and libraries at runtime, so it needs a base image that has Python in it.

**Image types, biggest to smallest:**
- **Full** (`python:3.12`): everything included. Easiest, but huge.
- **Slim** (`python:3.12-slim`): a minimal Debian. A good default starting point.
- **Alpine** (`python:3.12-alpine`): very small, but uses `musl` instead of `glibc`, so some packages break or need compiling.
- **Distroless**: only the language runtime. No shell, no package manager.
- **Scratch**: completely empty. Only works for static binaries (Go, Rust).

---

## 2. Multistage builds

- **Stage 1 (`AS builder`)** is a temporary helper container that installs dependencies and compiles/builds the app.
- **Stage 2 (final)** uses `COPY --from=builder` to bring in **only** what's needed to run. Everything else is thrown away.
- You can have 3–4 stages if needed. **Only the last stage ships.**

```dockerfile
# ---- Stage 1: build ----
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --target=/app/deps -r requirements.txt
COPY . .

# ---- Stage 2: run ----
FROM gcr.io/distroless/python3
WORKDIR /app
COPY --from=builder /app /app
ENV PYTHONPATH=/app/deps
CMD ["app.py"]
```

**"How do I know what to copy out of the builder?"**
You know the `WORKDIR` (e.g. `/app`) and what you copied into it, so you copy that path.
Some details, like setting `PYTHONPATH` so Python finds the installed packages, you only discover by debugging.

**Frontend pattern (React/Vue):**
- Stage 1: Node builds the app, producing `index.html` plus JS/CSS in `dist/` or `build/`.
- Stage 2: **nginx** serves those static files. Much lighter than shipping Node.

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
```

**Simple scripts:** a container can run anything. One example was just `alpine` running a bash script that prints hello.

---

## 3. Layer caching (order matters)

- Each instruction adds a layer. If a layer hasn't changed, Docker **reuses it from cache**.
- Once one layer changes, **every layer after it is rebuilt.**
- **Trick:** copy the dependency file first, install, *then* copy the source code:

```dockerfile
COPY requirements.txt .              # or package.json / yarn.lock
RUN pip install -r requirements.txt  # cached unless requirements.txt changes
COPY . .                             # code changes don't re-trigger the install
```

- Put things that rarely change at the top and things that change often at the bottom.
- `COPY . .` early in the file defeats caching, because any code change forces dependencies to reinstall.

> **Correction:** not *every* line creates a filesystem layer. Only `RUN`, `COPY` and `ADD` do.
> `ENV`, `EXPOSE`, `CMD`, `WORKDIR` etc. only add metadata.

---

## 4. Build then run

```bash
docker build -t python-slim .     # 1. build the image (-t = name/tag, . = folder with the Dockerfile)
docker run -p 5001:5000 python-slim   # 2. run a container from it
```

You can't run without building first. No image, no container.

### Ports: `-p HOST:CONTAINER`

```
docker run -p 5001:5000 my-app
              │    │
              │    └── CONTAINER port: must match the port the app listens on
              └─────── HOST port: any free port on your machine → http://localhost:5001
```

- **Right number (container)** must match what the app opens (e.g. Flask on 5000, the demo app on 9000).
- **Left number (host)** can be anything free. That's why the same app ran on 5001 and 5002 side by side.
- The app must listen on `0.0.0.0` inside the container, not `127.0.0.1`, or the port mapping can't reach it.

### `EXPOSE`
- `EXPOSE` documents the **container (right-hand) port**.
- It's **documentation only.** The demo proved the app still works with `EXPOSE` commented out.
- It's still worth having: it tells teammates and ECS task definitions which port to map, without digging through the code.



---

## 5. Experiments from the session

| Experiment | Result | Why |
|---|---|---|
| Comment out `EXPOSE` | App still works | `EXPOSE` is documentation only |
| Rebuild with no changes | Finished in ~0s | Every layer came from cache |
| Comment out `CMD` | Builds fine, container **exits immediately** | No proper start command, see below |

**Why the container exited without `CMD`:** it fell back to the base image's default command (`python3`, an interactive shell).
With no terminal attached, that shell exits straight away. **A container only lives as long as its main process.**

### `RUN` vs `CMD` vs `ENTRYPOINT`

| | When it runs | Overridable? |
|---|---|---|
| `RUN` | **Build** time (installs things into the image) | n/a |
| `CMD` | **Container start**, the default command | Yes: `docker run my-app <other command>` |
| `ENTRYPOINT` | **Container start**, always runs | Only with `docker run --entrypoint ...` |


## 6. The Dockerfile checklist (for any new app)

1. **How do I run this locally?** Forget Docker. Get it running first. That command becomes your `CMD`.
2. **What language is it?** That's your base image (Python → `python`, Node → `node`, Go → `golang`).
3. **What are the dependencies?** `requirements.txt`, `package.json`, `go.mod`, `pom.xml`...
4. **Where does it live?** `WORKDIR` (optional, but good practice).

**The four Lego blocks:** base image → copy dependencies → install them → start command.
Everything else (multistage, caching, `.dockerignore`, security) is added on top.

**Order of work:** ① make it work → ② optimise size → ③ harden security.

---

## 7. Q&A takeaways

### "Given a big unfamiliar repo, how do I figure out what it needs?"
- **Look at file extensions** to find the language: `.vue`/`.js`/`.jsx` → JavaScript, `.py` → Python, `.go` → Go.
- **Find the dependency file:** `package.json`, `requirements.txt`, `go.mod`.
- **Find the entry point:** `main.py`, `app.py`, `index.js`, or the `"scripts"` section in `package.json`.
- **Read the README.** It usually says how to run the app.
- **Check for an existing Dockerfile.** If there is one, read it and understand it.
- Use **`.dockerignore`** to exclude what you don't need (`node_modules`, `.git`, `.venv`, tests).

Language reference:

| Language | Dependency file | Typical entry point / run command |
|---|---|---|
| Python | `requirements.txt` | `python main.py` / `python app.py` |
| Node (backend) | `package.json` | `node index.js` / `npm start` |
| Node (frontend) | `package.json` | `npm run build` → serve `build/` or `dist/` with nginx |
| Go | `go.mod` | `go build` → run the binary |
| Static site | none | `index.html` served by nginx |

### "npm vs yarn vs serve?"
- **npm** and **yarn** are both Node package managers. They do the same job.
- **Check the lockfile:** `yarn.lock` → use yarn, `package-lock.json` → use npm.
- **`serve`** is a tiny static file server for built frontend files. nginx does the same job in production.
- **Threat Composer** uses **yarn** for install, build and run.

### ECS project advice
- **Threat Composer** is the easier route. Others have done it, so there's help available.
- Pick a different app if you want the challenge.
- If your own app uses a similar stack to Threat Composer (React/Node), stick with it.
- Try to figure problems out yourself first (docs, GPT), then ask.

### "Slim, full or distroless? How do I choose?"
- Look at what the app actually needs. Flask alone doesn't need a 1.6 GB image.
- **Start with slim.**
  - Breaks because something is missing? Go **one size up**.
  - Works? Try **one size smaller** (distroless).
- Experiment locally and compare sizes with `docker images`.
- Python has a floor (it always needs the interpreter). Go can go all the way down to `scratch`.

### "App works locally but shows no data on ECS Fargate (Mac user)"
Apple Silicon Macs build **ARM64** images by default. Fargate defaults to **x86_64 / AMD64**.

Fix, option 1: build for AMD64:
```bash
docker build --platform linux/amd64 -t myapp .
```

Fix, option 2: tell ECS to use ARM in the task definition:
```json
"runtimePlatform": { "cpuArchitecture": "ARM64", "operatingSystemFamily": "LINUX" }
```

Also check:
- **Environment variables** are set in the task definition.
- **API URL:** frontends often have the API URL **baked in at build time**, so `localhost` won't work in the cloud.
- **Security groups** allow traffic between the services.
- **CloudWatch logs** for the task.

### "Why are Go, Rust or Java 'faster' than Python?"
- **Compiled languages** (C, Rust, Go, C#) are turned into machine code ahead of time. They're closer to the hardware: faster, and they use less memory and energy, but they're harder to write.
- **Interpreted languages** (Python, JavaScript) are translated while running. That's more overhead, but they're easier to write.
- At large scale (AWS-size), that difference costs real money and electricity.
- The chart shown was from a "programming language energy efficiency" study.

---

## Quick command reference

```bash
docker build -t <name> .                     # build an image from the Dockerfile in this folder
docker build --platform linux/amd64 -t <name> .   # build for ECS/x86 from an Apple Silicon Mac
docker images                                # list images and their sizes
docker run -p <host>:<container> <name>      # run a container with port mapping
docker run -d -p 5001:5000 <name>            # same, in the background (detached)
docker ps                                    # list running containers
docker ps -a                                 # list all containers, including exited ones
docker logs <container>                      # see a container's output (works on exited ones too)
docker stop <container>                      # stop a running container
```









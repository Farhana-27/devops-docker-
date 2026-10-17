# Docker Learning 
- Flask - simple and lightweight framework for creating web applications in Python - perfect for web framework
- pip3 install flask -> to install flask and its dependencies 
- mkdir hello_flask -> create another directory 
- touch app.py -> create application in this directory 
- Ran a code inside the application to display Hello World! -> python3 app.py 

#### Containerise our Web Application 
- The same application made in app.py -> we will containerise it using docker 
- Will by the end have a docker container running the python app allowing you to easily deploy it anywhere 
- To containerise, first write the Dockerfile -> This is a text file that contains a series of instructions on how to build a container image for our application 
1. inside devops-docker directory create the file -> touch Dockerfile
2. Inside the Dockerfile will write the instructions
- 1. FROM python:3.8-slim -> The first command is always the FROM command. This is followed with the image we are going to use. Will use the official python image, then the version - this is a minimal python environment that uses only essential commands - makes the image lighter 
- 2. WORKDIR /app ->  We set the WORKDIR so that any commands ran after will be in this directory
- 3. COPY .. -> We will copy all the files from our current directory (app.py) and put it into the container. The . means everything in the current directory - then set it to the WORKDIR but since its already been said you just say .
- 4. RUN pip install flask -> will install flask in our container 
- 5. EXPOSE 5002 -> to EXPOSE port 5002 and making this port available to access the container from our local host. This makes the application accessible from outside the container 
- 6. CMD ["python" , "app.py"] -> tells the docker to run out python application. 

- The next step is building the docker image 
- - In the command line you -> docker build -t hello-flask . 
- - 1. docker build -> this command initiates the build 
- - 2. -t -> tage the image with the name 
- - 3. hello-flask -> is the name of the image 
- - 4. . -> represents the current directory and tells docker to look for the docker file there 

#### Docker file(recipe) -> docker image (snapshot) -> run it 
- docker run -d -p 5002:5002 hello-flask 
- - 1. -d -> runs the container in detatched mode -> means running it in the background 
- - 2. -p 5002:5002 -> mapping port 5002 on my machine to the port 5002 in the container 
- - 3. hello-flask -> name of the image we are using
- You will get the container ID 
- Verify that the container is running with -> docker ps 

#### Stop the container 
- Docker stop container ID
#### To restart the container 
- Find the container ID -> docker ps -a (the -a includes stopped containers)
- Then start it again -> docker start (container ID)

#### Linking Containers together 
- I had some issues when I tried to link the containers but for looking back on my notes 
1. Checked if I had python installed with python3 --version 
2. Installed ~ pip3 install flask 
3. Created file ~ touch app.py (did py because I am using python)
4. Inside the app.py, pasted in code for flask because I am using a web and wanted it to say "Hello World MYSql version 5.7" 
5. Did ~ python3 app.py -> this is to start the flask app directly on my mac without docker 
6. Created dockerfile ~ touch Dockerfile 
7. Docker build turns your project folder into an image. An image is a packaged snapshot of your app containing python. Containers are started from images, so you need to build before you can run
- - ~ docker buildd -t hello-flask 
- - ~ docker build -> follows the instructions in your Dockerfile 
- - ~  -t hello-flask -> gives the image a name (tag) -> without it you would be given a random ID 
- - ~ . -> means to use the current folder - docker looks for the Dockerfile and the files to copy in 
8. Created a personal network -> ~ docker network create my-custom-network. You want to see the list of networks -> ~ docker network ls 
9. To check what the docker is actually reading from the app.py you do -> ~ docker exec myapp cat app.py 
10. Then I had to rm the container, save the changes and then build the docker again adn then run it again 
- - docker rm myapp 
- - docker build -t hello-flask-mysql
- - docker run docker run -d --name myapp --network my-custom-network -p 5002:5002 hello-flask-mysql

Key notes: When to run a docker build 

-> Every time you change app.py, the Dockerfile or your package list. The image is a snapshot, so changes to your files don't reach a container until you rebuild. 


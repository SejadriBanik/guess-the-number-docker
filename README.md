

## 1.	Application Description

The "Guess the Number" game is a fun and interactive console game where the application generates a random number and the player needs to guess the number between a predefined range. The game gives the player hints after each guess (too high, too low) and ends when the player guesses the correct number or runs out of attempts.


## 2.	How to build the Docker image

To build a docker image follow:

o	Navigate to the directory where the ‘Dockerfile’ is located.\
o	Run the following command to build the Docker image: 



```bash
  docker build -t username/appname:v1 .  
```

Verify your image was created successfully:
```bash
  docker images
```

•	docker build : command to build the image.\
•	-t : stands for tag (to name the image properly).\
•	v1 : version 1 of app.\
•	. : means "current directory" (where Dockerfile exists).

## 3.	How to run the container

Once image is created, run the following command:
```bash
  docker run -d -p [HOST-PORT]:[CONTAINER-PORT] --name myapp username/appname:v1 
```


•	When we execute docker run, the container process that runs is isolated in that it has its own file system, its own networking, and its own isolated process tree separate from the host.\
•	-d: Run in detached mode (in the background).\
•	-p: used to map a port on your host machine to a port on the container.\
•	HOST_PORT: The port number on your host machine where you want to receive traffic\
•	CONTAINER_PORT: The port number within the container that's listening for connections\
•	--name : Assign a name to the container.


Verify your application is working correctly:
```bash
  curl http://localhost:HOST-PORT/
```
## 4.	Available configuration options 

Exposed Port:\
•	`Host Port: 8080` — The port on your local machine that you’ll use to access the web application.\
•	`Container Port: 5000` — The port inside the container where the application is running.

## 5.	Basic usage instructions
**1. Run the Docker Container** 

Ensure that you have Docker installed and running on your machine. Then, start the Docker container using the following command:\
`docker run -d -p 8080:5000 --name guess-the-number sejadri/guess-the-number:v1`\
This will:\
•	Start the application in the background (-d for detached mode).\
•	Expose port 5000 inside the container and map it to port 8080 on your local machine (-p 8080:5000).\
•	Name the container guess-the-number for easy management.

**2. Access the Game in Your Web Browser**

Open your web browser and navigate to:\
`http://localhost:8080`\
This URL will load the game interface running inside the container on port 5000, but you'll access it through port 8080 on your host machine.

 **3. Play the Game**

Once you are on the game’s webpage:\
•	The game will randomly select a number within a predefined range (e.g., between 1 and 100).\
•	You will be prompted to enter your guess.\
•	After each guess, the game will tell you if your guess is "too high" or "too low."\
•	Keep guessing until you either guess the correct number or exhaust your attempts (the number of guesses allowed may vary depending on the configuration).

**4. End of the Game**

Once you guess the number correctly, or if you run out of attempts:\
•	The game will display the correct number.\
•	If allowed, you may get an option to restart the game.

   If you want to exit the game or stop the container, you can use the following Docker commands:\
•	Stop the container:\
`docker stop guess-the-number`\
• Remove the container (optional after stopping it):\
`docker rm guess-the-number`


## 6. Troubleshooting Tips
•	**Cannot access the game in the browser:**\
o	Ensure Docker is running and that the container started successfully.\
o	Make sure port 8080 on your local machine is not already in use by another application.\
o	Verify that the container is running with docker ps and check the logs with docker logs guess-the-number.

•	**Port Mapping Issues:**\
o	If you encounter a conflict on port 8080, you can change the host port to another one (e.g., -p 9090:5000 to use port 9090 on the host).

•	**Game freezes or does not respond:**\
o	Check if the container is still running with `docker ps`.\
o	If the game stops working unexpectedly, you can stop and restart the container:\
`docker restart guess-the-number`

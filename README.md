### QA-Practical-Project


We have been tasked to create a simple web app individually, this web app must make use of a range of technologies in a CD/CI pipeline to trigger a rolling update. The pipeline had 4 services in it listed below.

* Service 1: Front-end of the program, makes use of api calls to display the program by calling the other 3 services
* Service 2/3: Generates random number and a random choice from a dictionary
* Service 4: called by a POST request in service 1

The functionality of the app is simple from a user point of view. However the tools used to build and deploy this app are more complex.

* Docker and Docker-Compose used to containerise the images and builds
* Docker Swarm will spread the program across worker nodes/managers, using multiple replicas
* Nginx will load balance the project so the server is not overloaded
* Jenkins was used, both to build and test automatically. A web hook could be used to create an automatic update via Github but I did not have the time to achieve this goal


### Workout Generator

A simple app that will generate for you an exercise to do and how many reps of that exercise to do.

## Software design


### Jira

Used a KanBan board on Jira to set tasks and track the progress of the project.

### Database

A single database connected to the web app, the only real purpose of this is to track the user generated workouts and then list them via the last 5 generated. A relatively useless function but it does show case the database connection established.


* ID: unique identifier
* Exercise: String value containing the variable in question. “Press ups” for example
* pick: Integer value that stores the overall pick value of the drafted player


### Risk Assessment

A risk assessment was completed initially and then added to as things became more apparent.

### Continuous Deployemnt and Integration

Jenkins was used as an automated process of the Contiuous Deployment and Integration devops mindset.
Below is the completed Jenkins pipeline for the project.
Insert Jenkins image here
There are 7 Stages:

* Checkout SCM: Simply checks out the code version which will be trigged to run via the linked github repo.
* Install Requirents: Installs all the requirements for the app and Jenkins from the file given. Insuring everything is updated such as pip modules.
* Testing: Performs the unit tests for the project
* Build: This builds the services into seperate images onto the local jenkins machine
* Push: Pushes the images generated onto Dockerhub
* Ansible: Running the ansible scripts. Allowing Jenkins to separate the nodes into separate roles such as a worker or the nginx machine. Done via Docker swarm
* Deploy: Using a deploy script, jenkins is able to ssh into the manager node, copy over the ansible playbook (due to set up form the previous build) and allows the swarm to be fully created and made availble to the public. Using a stack also paired with nginx means that there is no downtime for the user from when the devs push the code to git hub to when the stack is deployed.


### Services

The project uses 4 services to run the application.

Services:
* Front-End, shows the user which player has been drafted. acts as a base for the API calls
* Generates a random exercise from a given list
* Generates a random number
* Using a post request, the random number and exercise are inputted to the service. There is a Joke exercise which when found would generate a message saying you cheated. 

Otherwise the app will commend you on burning over 100 calories


### Testing

Automated testing was done via Jenkins. Requests_mock was also used to mock the unit test of service 1. Request mock was used to perform a dummy live test instead of needing the containers in place to actually run the app.

85% coverage was achieved overall. This is mostly a failure in service_4. Which is to be expected given the rushed finish I made on the app.



### Front End

Front end is simply a little message and a submit button. Upon clicking this you will be given your exercise and the number of reps to do for it. I however had some issues with the URL request when using the other services so the app does not go further beyond the home page

### Improvements

* Fix the url requests – I believe this is because docker is naming the image to something else
* Instead of a generic calories, use the number of reps and the exercise to calculate a calories burned base on that.
* Streamline everything
* Testing can also be improved. This could also be because of the url requests failing but 100% should be the goal

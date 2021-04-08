# QA-Project-1

# Little Help

### Resources:
GitHub repository: <br />
Trello board: https://trello.com/b/W2cvarha/littlehelp

### Content
1.[Brief](#brief)<br />
2.[Software Design](#software-design)<br />
3.[Programming and Software Development](#programming-and-software-development)<br />
4.[Testing](#testing)<br />
5.[System Integration and Build](#system-integration-and-build)<br />
6.[Risk Assessment](#risk-assessment)<br />
7.[Future Improvements](#future-improvements)<br />
***

## Brief
Requirement for this project was to create a CRUD web application in Python, following best practices and design principles. The part of requirements was to utilize following tools: Python, Pytest, SQL server (GCP), Flask (HTML), Version Control (Git), CI Server (Jenkins), Cloud server (GCP). 

Additional specification of the project: 

* Full ERD and documentation of the design and development of the application.
* Utilisation of Cloud Hosted managed Relational Database modelling two tables.
* Unit testing using Pytest.
* The project must follow the Service-oriented architecture that has been asked for.
* A fully functional front end web application via Flask.
* Continuous Integration via Jenkins and version control system Git.

***
## Software Design

### Approach of the project

Inspiration for this project was the problem for many people during Covid 19 outbreak - if I'm on quarantine, who is going to do my grocieres. I came up with idea of web application featuring posts about help that someone needs and help that the other person is willing to give. Users can create profiles filled with basic informations and create posts.

![](https://github.com/SuraKarolina/QA-Project-1/blob/main/Documentation/About.png)

### ER table

Below is an entity relationship diagram (ERD) showing the tables used in a project and how they relate with each other. The database was created on GCP MySQL server. 

![](https://github.com/SuraKarolina/images/blob/main/images/ER1.png)

### Minimum Viable Product 

The Minimum Viable Prodact is presented in MosCow prioritization diagram: 

<img width="420" alt="Moscow" src="https://github.com/SuraKarolina/images/blob/main/images/moscow1.png">

User can create and update the profile. User can create, update and delete and browse posts (home page). 

![](https://github.com/SuraKarolina/QA-Project-1/blob/main/Documentation/Create.png)
![](https://github.com/SuraKarolina/QA-Project-1/blob/main/Documentation/Update.png)
![](https://github.com/SuraKarolina/QA-Project-1/blob/main/Documentation/Read.png)

### Project tracking

For project tracking and management Trello board was used. 

<img width="700" alt="trello" src="https://github.com/SuraKarolina/images/blob/main/images/trello.png">



***
## System Integration and Build

### Test coverage 

Unit test results for application:

![](https://github.com/SuraKarolina/QA-Project-1/blob/main/Documentation/Test.png)



### CI pipline

<img width="500" alt="CI" src="https://github.com/SuraKarolina/images/blob/main/images/CI1.png">




***
## Risk Assessment

![](https://github.com/SuraKarolina/QA-Project-1/blob/main/Documentation/Risk.png)

***
## Future Improvements

- Improve overall test coverage.
- Improve user interface.
- Create a messages functionality to enable user's direct contact.


***


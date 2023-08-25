# CapSuit Python Backend

This python code for **Interview Test**. The main function is to provide the ability to crud operation of local docker-based mysql database.

# Detail

I have never really worked with mysql before and this project involves a lot of database related frameworks such as **SQLAlchemy**, so I need to learn as I go along and need to maintain code quality.
Luckily I was able to complete the project and fulfill some of the requirements I had for myself.
Meanwhile I encountered quite a few problems and learned a lot during this development experience, which I will explain step by step below.

## How to run
1. Download the database.zip and install the docker software
2. Unzip database.zip to you want, and run it by cmd or powershell in this directory
```bash
docker-compose up --build --force-recreate --renew-anon-volumes db
```
3. The docker container will use port 3306 and automatically maps the docker container's port to the host's port 3306, make sure that your port 3306 is not occupied, otherwise you can't start it.

4. Run the python server
```bash
uvicorn main:app --reload
```


- Main Frameworks
	> FastAPI (Easy to learn)
    
    > SQLAlchemy 
    (I have previous experience with MongoDB, and SQLAlchemy feels to me more like using code as a query than using SQL statements (but at the same time you have to learn SQL statements to know how to turn them into code form).)

- Main difficulties
    > Difficulty to get started is moderate, and requires some Python skills, and SQL skills

    > Program errors are difficult to understand and take a long time to debug

- Learned
    > Very small amount of Docker information, because the my first contact the database is Cloud MongoDB, so the first difficulty is **How do I connect to the database**, so my first idea instead of installing MySql first software first, and then the installation process also encountered quite a lot of problems, for example, port occupation.
    
    > More in-depth knowledge of FastAPI, my previous FYP also use FastAPI as the back-end framework, this development experience allows me to know more about it!

- Usage time
    > About 9 hours.
    (Learn, Develop, Debug, etc)

- ScreenShot
<img alt="Train loss" src=".\gitImage\1.png" >

# All Source code repo
<a href="https://github.com/kjjkjjzyayufqza/CapSuit_Python_BackEnd">BackEnd</a><br/>
<a href="https://github.com/kjjkjjzyayufqza/CapSuit_NextJs_FrontEnd">FrontEnd</a>
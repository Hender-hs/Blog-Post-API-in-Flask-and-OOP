# Blog Post DB in Flask and with MongoDB and made with OOP
> It's a Image data base made in Flask.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Ideas for Improvements](#ideas-for-improvements)
* [Contact](#contact)


## General Information
- It is a NoSQL API that was created with Object Oriented Programming, Flask, MongoDB and it's able to store blog posts contents.
- This API was made to easy storing blogs posts using NoSQL database!
- The mainly reason that it was created was to putt my knoledge and what I've learned with flask and OOP in pratice.



## Technologies Used
- Python - version 3
- Flask - version 2.0
- NoSQL MongoDB
- Object Oriented Programming


## Features
Features:
- Store content releated to blogs posts with data time.
- Many advices for who's doing a bad request to API.
- A secure API.


## Setup
If you want to change something to your necessties, feel free to fork or clone the project and use the requirements.txt file to install required dependencies.

These dependencies are mainly:

pip
environs
Jinja2
pytest (to test the code)
werkzeug

## Usage

### End-Points

#### GET

> `/posts`
> - You're gonna receive all posts on API. Such as:
```
[
  {
	  "title": <string>,
	  "author": <string>,
	  "tags": <string>,
	  "content": <string>
  }
]
```

> - If some of these keys are missed or incorrect, you're gonna receive a advice.


#### POST

> `/posts`

```
{
	"title": <string>,
	"author": <string>,
	"tags": <string>,
	"content": <string>
}
```

> - If some of these keys are missed or incorrect, you're gonna receive a advice.

#### PATCH

> `/posts/<id>`

> In this end-point you'll need to especify the post ID

```
{
	"title": <string>,
	"author": <string>,
	"tags": <string>,
	"content": <string>
}
```

> - If some of these keys are missed or incorrect, you're gonna receive a advice.


#### DELETE

> `/posts/<id>`

> In this end-point you'll kust need to especify the post ID. If you give a ID that doesn't exists, you will receive a advice


## Project Status
Project is: _in progress_


## Ideas for Improvements
In the future extend the project, to be a largest API to stores a large amount of information.


## Contact
Created by [@Hender-hs](https://github.com/Hender-hs). My own Portifolio Web Site [here](https://portifolio-p.vercel.app/)  - feel free to contact me!

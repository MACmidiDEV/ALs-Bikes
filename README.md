# Miguel Camacho Stream Four Project: 
# Fullstack Development Milestone Project - Code Institute 

MileStone 4 Full Stack Software Development Course at Code Institute. Visit [GitHub](https://github.com/MACmidiDEV/ALs-Bikes) for entire build information. The main focus of this project was to create, develop and deploy a mongoDB database connected web application hosted on [HEROKU](https://github.com/MACmidiDEV/ALs-Bikes)

## Purpose of This Project
build a full-stack site based around business logic used to control a bike-shop and the owners dataset. The site has an authentication mechanism and provides were users have to create an account to be able to purchase a product. The site owner is able to make money by providing this a of services to and bikes for sale to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.


### Strategy
My goal in the design was to make it as easy as possible for customers to access the site and purchase a bike.

### Scope
Ecommerence bikeshop written in django 

## Demo | Deploy
This site is hosted using GitHub, deployed directly from the master branch to Heroku.
The current site in production is hosted via [HEROKU](https://github.com/MACmidiDEV/ALs-Bikes)
The GitRepo can be found on [GitHub](https://github.com/MACmidiDEV/e-comm)

## Wireframes
- ![LittleLinks-DRAFT](https://raw.githubusercontent.com/MACmidiDEV/CInst-M3-Data-Centric-Development/master/LittleLinks/static/images/aDRAFT.jpg "Wireframe")

## Utilized Technologies
### Languages
- HTML5
- CSS3 
- JavaScript
- Jquery
- Python3

### Frameworks & Technologies
- Bootstrap: For responsive web designing 
- Flask: HTML templating & routing
- Git: version control
- VSCode: code editor
- Github: hosts the website

### Database
- Aws Bukets: To store information into a database

## Environment and Configuration Variables
#### Local Variables
local env.py holds config vars 'SECRET_KEY', 'MONGO_URI' and 'DEVELOPMENT', which have the values that are required in the app.py file for the mongo URI password, the secret key password and the debug value.

#### Heroku Configuration Variables
heroku config vars 'IP', 'PORT', 'SECRET_KEY', 'MONGO_URI' and 'DEVELOPMENT' variables. The 'SECRET_KEY' and 'MONGO_URI' contain the same passwords on Heroku as they do locally in the env.py file. The 'DEVELOPMENT' variable is set to 1 during build and 0 in production

## Deployments and Installations
### Start A Virtual Environment & Install
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
for security purposes you will need your own database connection string to [mongoDB](https://docs.mongodb.com/manual/reference/connection-string/)

## Defensive Design
Throughout the build of this site various defensive features were added to protect against malicious activity, and also to stop things from breaking.
	•	 Prevention of  Cross Site Request Forgeries by adding {% csrf_token %}  to each form .
	•	User  authentication checks are employed to avoid an already logged in user from logging in again. Non registered users cannot make purchases and registered users are allowed purchasing capability. 
	•	Several checks were put in place within the forms and the models to ensure all requests were receiving all the expected data. Adding 'required' to certain field helped ensure this was achieved and fields were not left blank.
	•	Reset password sent to email available to registered users if user is locked out of account.

## UX
### User stories
As a customer I want to acees the site and if I see a bike I am able to purchase it

### Surface
Color schemes were selected by the owner of the bike store.

## Features 
	•	Landing page - A page that that showcases the owner skill set on bikes.
	•	Online store - featuring all available options of bikes for sale by owner . Users can browse available bikes with the option to purchase a repair package.
	•	Check out page - giving user the ability to review and remove unwanted items . 
	•	User Accounts - Users are able to register an account , login with a unique username and password. 
	•	Owner Contact - Gives the user and owner the ability to communicate. This allows question about purchases , returns , and repairs between owner and user. 

### Features Left to Implement
As the site progresses I want to implement a bidding p[age where customes can join an auctions for the site.]

## Testing
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness via [responsinator](https://www.responsinator.com/)

All of my testing was done manually for this project. I did however use automatic validators to check my code. I used PEP8 for my Python code, and the W3C validator for my HTML and CSS code. I used all of these periodically throughout development to ensure I was always adhering to standards.
My choice of browser for this project was firefox developer edition. This is my go to browser due to the really good dev tools. The dev tools play a huge part in how I developed my website. When working on bug fixes or new styles I always use the dev tools first to see what they look like or if I can find whats causing the bug before implementing into my own code. The dev tools also play a major part in me using the mobile-first approach to designing and developing my website.
Although I primarily used firefox for development, i periodically checked how my site look in other modern browsers. Firefox, Chrome, Safari, Opera and Edge were all used to ensure all functionality was working across them all. In addition to testing on various browsers, I also ensure the site was responsive by testing on various mobile devices. Primarily, on iPhone and iPad.
Additionally, after realising the dev tools aren't always 100% accurate with certain things (see footer bug below), I got the help of my peer Anthony to help test my site on non iOS mobile devices.

### Media
All photos were taken from [unsplash](https://www.unsplash.com/), open source image library.

### Acknowledgements
All skills acquired from [codeInstitute](https://codeinstitute.net/), training source.
- [W3Schools](https://www.w3schools.com/python/python.asp)
- [Stackoverflow](https://stackoverflow.com/)
- [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/)

**This is for educational use.**

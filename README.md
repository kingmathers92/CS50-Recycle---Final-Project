# *CS50 Recycle*

>This was my final project for conclude the CS50 Introduction to Computer Sciense course.

>Python, Flask, Google API, Jinja2, JavaScript, HTML5, CSS, SQL, Bootstrap, CS50

## Features
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Sqlite](https://www.sqlite.org/index.html)
- [Bootstrap](https://getbootstrap.com/)

## Usage
Register and login, easy map to use that includes markers with info

## for mac and linux
cd [path to app.py] <br/>
export FLASK_APP=app.py <br/>
flask run <br/>
### optional
export FLASK_ENV=development <br/>
export FLASK_DEBUG=1 <br/>

## for Windows
cd [path to app.py] <br/>
set FLASK_APP=app <br/>
flask run
### optional
set FLASK_ENV=development <br/>
set FLASK_DEBUG=1
<br/>
for more info visit: https://flask.palletsprojects.com/en/1.0.x/cli/

## Description
With my recycling website the user can register, the registration includes name, email and a unique password.
After they log in, the main entry point takes you straight away to a map which I implented using Google maps javascript api.
It hightlights 10 markers at the same time with a customed pin icons. Those 10 markers are of the top 10 countries in the world that are successful at recycling, basically their way of life. When you hover over a certain pin you see the title which would be, the number of the country on the top 10 list, country's name and their percentage of recycling. You can also click on the pin and it will appear an window info containing more information.

My overall strategy was to break down the project into smaller pieces and making sure that functionality was working before moving on to the next piece. That strategy had for me proven beneficial when working with the psets and labs of CS50 and I'm convinced that was what got me through this final project. For me Flask was a fun and easy. It is unlike anything I have seen with C, Python and SQL which th elearning curve was steep.

I started out with laying out the design first so I can see what I'm working with, it helps visually. The colors are all insipired from [WhatsApp](https://www.whatsapp.com/), it seemed convenient. Right after that I created the /awareness route and added some content to it and I made sure I styled it really good. Then jumped to the /contact route, made with HTML and CSS, colors goes with the website theme. And I used [formspree](https://formspree.io/)'s API to generate a unique and secure endpoint for my form and stores all of the entries in my account. Totally free for the first 50 requests.

After I finished all that, I got to the juicy part. I've never worked with API's or studying anything about them but I wanted to do something with [Google Maps API](https://developers.google.com/maps) so bad in my final project so I basiacaly spent most of my time doing this project reading and watching tutorials to learn and understand API's and I think it turned out decent even though I always think that I could do better.

I have learned a lot during this final project and the courage and strength to engage and complete a project in Flask was build up during the lectures and problem sets of CS50 leading up to the final project.

# THIS WAS CS50








# News-Web-App

![NewsApp Banner](https://i.imgur.com/ho9IUf1.gif)

[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://newswebapp.herokuapp.com/)
[![travis-ci](https://api.travis-ci.com/Akash1362000/Django_Student_Management_System.svg?token=nv6BYq1BY3w4kf8uZuGj&branch=main)](https://travis-ci.com/github/Akash1362000/Django_Student_Management_System/)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAkash1362000%2FNews-Web-App%2F&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Akash1362000/News-Web-App/graphs/commit-activity)

News Web App 📰 built using Python Django 🌐 and NewsAPI 🚀 Fetches latest news. 😍 It is a Progressive Web App (PWA) which enables users 👨‍👩‍👦 to install it on their mobile phones 📱 (Android & iOS) as well as Desktop 💻 (Windows, Linux, etc.) 🔥

Checkout the live Website [here](https://news-web-app-8pf8.onrender.com/)!

Find the detailed project report [here](https://drive.google.com/file/d/1CotBwalG53YZ9wDjjDHIA-nrLDLWkJHn/view?usp=sharing)! 📜

### Demo 🎥

![NewsApp Demo](https://github.com/Akash1362000/News-Web-App/blob/master/static/newsapp/NewsApp.gif)

### Meet the Developers ✨🌟

<table>
		<tr>
			<td align="center"><img src="https://i.imgur.com/ZwcK1xV.jpg"  width=100px;"><br /><sub><b>Akash Shrivastava</b></sub><br/><a href="https://github.com/Akash1362000">👨‍💻🚴‍♂️📸</a></td>
		   <td align="center"><img src="https://i.imgur.com/zvN556m.jpg"  width=100px;"><br /><sub><b>Akanksha Tamboli</b></sub><br/><a href="https://github.com/akankshast">💻🎨</a></td>
			<td align="center"><img src="https://i.imgur.com/fVE1MSw.jpg"  width=100px;"><br /><sub><b>Shreejit Nair</b></sub><br/><a href="https://github.com/ShreejitNair">🎓🏏📱</a></td>			<td align="center"><img src="https://i.imgur.com/oKHebZM.jpg"  width=100px;"><br /><sub><b>Samiksha Naik</b></sub><br/><a href="https://github.com/samiksha8888989">💃📸</a></td>
		</tr>

</table>

## Development 🛠
Note : Make sure you have Python version 3.8+ and Postgres 14 or above

Environment Setup

`$ git clone https://github.com/Akash1362000/News-Web-App.git`

`$ cd News-Web-App/`

Create `.env` file (refer `.env.example` file)

Generate `SECRET_KEY` from [here](https://djecrety.ir/)

Get your `NEWS_API_KEY` from [here](https://newsapi.org/)

## Database Setup

Install Postgres Latest version from [here](https://www.postgresql.org/download/)

Install pgAdmin from [here](https://www.pgadmin.org/download/)

Create a Database using pgAdmin by following the steps mentioned [here](https://www.tutorialsteacher.com/postgresql/create-database)

Update your `DATABASE_URL` in `.env` with your DB details like `USER`, `PASSWORD` and `DB_NAME`

---

If virtualenv is not installed [(What is virtualenv?)](https://www.youtube.com/watch?v=N5vscPTWKOk&t=313s):

`$ pip install virtualenv`

Create a virtual environment

`$ virtualenv venv`

Activate the environment everytime you open the project

`$ source venv/Scripts/activate`

Install requirements

`$ pip install -r requirements.txt`

`$ pre-commit install`

`$ python manage.py migrate`

---

Create superuser

`$ python manage.py createsuperuser`

---

That's it. You're all Set!

To run the server:

`$ python manage.py runserver`

Open your desired browser and head over to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

To exit the environment

`$ deactivate `

---
## Docker Setup (Optional) ![](https://skillicons.dev/icons?i=docker)

If you want to use Docker to run this project, you need to do the following steps:
- Install Docker for your OS from [here](https://www.docker.com/products/docker-desktop/)
- Run `docker --version` and `docker compose --version` [In Windows, you need to run `docker-compose --version` to check the version]
- If you see both the versions, then Docker is successfully installed on your system and you can follow along
- If you don't see the version, check with your Docker installation
- Open `docker-compose.yml` file and update the value of `NEWS_API_KEY` with your generated key. You can generate it from [here](https://newsapi.org/) 
- Run `docker compose up -d`
- Run `docker exec -it news_web_app sh -c "python manage.py createsuperuser"` to create a new superuser
- Access the app at [http://localhost:8000](http://localhost:8000)
- To stop the container, run `docker compose stop` from the project root
- To restart the container, run `docker compose start` from the project root
- To delete the container, run `docker compose down` from the project root

---


### License ✍

```
MIT License

Copyright (c) 2020 Akash Shrivastava

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Leave a ⭐ from [here](https://github.com/Akash1362000/News-Web-App) if you like 😁

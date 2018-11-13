# store setting of the application

from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://///mnt/r/==MyRepos==/Flask/Books/database.db"
#"/mnt/r/==MyRepos==/Flask/Books/database.db"
##"/mnt/r/==MyRepos==/Flask/Books/database.db" #"R:\==MyRepos==\Flask\Books\database.db"
#sqlite:////Users/sanjayrai/Documents/Rest-Api-With-Python-And-Flask/Module_7/database.dbt
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

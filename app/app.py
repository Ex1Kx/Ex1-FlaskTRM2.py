from flask import Flask
from routes import *


app = Flask(__name__)

#user
app.add_url_rule(user["register_user"], view_func=user["register_user_controllers"])
app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
#app.add_url_rule(routes["json"], view_func=routes["json_controllers"])

#line
app.add_url_rule(line["register_line"], view_func=line["register_line_controllers"])
app.add_url_rule(line["update_line"], view_func=line["update_line_controllers"])
app.add_url_rule(line["delete_line"], view_func=line["delete_line_controllers"])
app.add_url_rule(line["get_line"], view_func=line["get_line_controllers"])

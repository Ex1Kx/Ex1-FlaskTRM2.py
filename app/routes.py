from controllers import RegisterUserControllers, LoginUserControllers, JsonControllers, LineControllers

#rutas del user
user = {
    "register_user": "/api/v01/user/register", "register_user_controllers": RegisterUserControllers.as_view("register_api"),
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    #"json": "/api/json", "json_controllers": JsonControllers.as_view("json_api")
}

#rutas de line
line = {
    "register_line": "/api/v01/line/create", "register_line_controllers": LineControllers.as_view("register_line_api"),
    "update_line": "/api/v01/line/update", "update_line_controllers": LineControllers.as_view("update_line_api"),
    "delete_line": "/api/v01/line/delete", "delete_line_controllers": LineControllers.as_view("delete_line_api"),
    "get_line": "/api/v01/line/get", "get_line_controllers": LineControllers.as_view("get_line_api"),
}

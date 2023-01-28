from app.controllers.cnab_controllers import cnab_get_controller,cnab_post_controller

def cnab_route(app):
    app.route("/",methods=["get"])(cnab_get_controller)
    app.route("/",methods=["post"])(cnab_post_controller)
   
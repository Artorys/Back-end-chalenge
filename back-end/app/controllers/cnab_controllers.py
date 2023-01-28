from app.services.cnab_services import cnab_get_service,cnab_post_service
def cnab_post_controller():
    cnab = cnab_post_service()
    ...
def cnab_get_controller():
    cnab = cnab_get_service()
    ...
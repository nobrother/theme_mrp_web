from openerp import http
from openerp.addons.web.controllers import main

class controller(main.Home):
    @http.route('/services', type='http', auth="public", website=True)
    def service_page(self):
        return http.request.render('theme_mrp_web.page_services')
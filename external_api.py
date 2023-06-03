url = 'http://localhost:8069'
db = "odoo_db"
username = "trinh.mai@ecotruck.vn"
password = "Tin24120"

import xmlrpc.client

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
version = common.version()

# authenticate
uid = common.authenticate(db, username, password, {})
if uid:
    print(f"uid: {uid}")


    # search method
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # result = models.execute_kw(db, uid, password, 'crm.lead', 'search', [[['email', '=', '']]])
    partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
    print(f"Result: {partners}")

    record = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners], {'fields': ['display_name', 'phone', 'email', 'function', ]})
    print(f"Result: {record}")


else:
    print('Authentication Falied')
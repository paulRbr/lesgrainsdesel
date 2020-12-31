from odoo import Odoo

odoo = Odoo()

odoo.connect()

# exemple : on cherche l'evenement avec un id de 2
#           et on affiche que la propriete name et
#           l organisateur de l evenement

# Ne pas oublier de rajouter au moins 2 evenements
print(odoo.searchRead("event.event", [], ["name", "organizer_id"]))
# exemple : sans filtre, on affiche tous les evenements
# verifier bien que l'id de la personne existe sinon
# changez l id
# print(odoo.searchRead("res.partner", [['id', '=', 7]],
#                    ["name", "age", "contact_address", "phone"]))

#odoo.createEvent("event_test5", "2020-12-28 20:18:18",
#                 "2020-12-29 20:18:18", 6)
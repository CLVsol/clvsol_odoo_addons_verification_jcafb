# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonAuxFamilyUpdt(models.TransientModel):
    _description = 'Person (Aux) Family Update'
    _name = 'clv.person_aux.family_updt'

    person_aux_ids = fields.Many2many(
        comodel_name='clv.person_aux',
        relation='clv_person_aux_family_updt_rel',
        string='Persons (Aux)'
    )

    update_contact_info_data = fields.Boolean(
        string='Update Contact Information Data',
        default=True,
        readonly=False
    )

    update_ref_address_data = fields.Boolean(
        string='Update Address Data',
        default=False,
        readonly=False
    )

    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.model
    def default_get(self, field_names):

        defaults = super().default_get(field_names)

        defaults['person_aux_ids'] = self.env.context['active_ids']

        return defaults

    def do_person_aux_family_updt(self):
        self.ensure_one()

        for person_aux in self.person_aux_ids:

            _logger.info(u'%s %s', '>>>>>', person_aux.name)

            if not person_aux.family_is_unavailable:

                family = person_aux.family_id
                vals = {}

                if (person_aux.phase_id != family.phase_id):

                    vals['phase_id'] = person_aux.phase_id.id

                # if (person_aux.state != family.state):
                if (person_aux.ref_address_id.state != family.state):

                    # vals['state'] = person_aux.state
                    vals['state'] = person_aux.ref_address_id.state

                if self.update_contact_info_data:

                    if (person_aux.contact_info_is_unavailable != family.contact_info_is_unavailable):

                        vals['contact_info_is_unavailable'] = person_aux.contact_info_is_unavailable

                    if (person_aux.zip != family.zip):

                        vals['zip'] = person_aux.zip

                    if (person_aux.street_name != family.street_name):

                        vals['street_name'] = person_aux.street_name

                    if (person_aux.street_number != family.street_number):

                        vals['street_number'] = person_aux.street_number

                    if (person_aux.street2 != family.street2):

                        vals['street2'] = person_aux.street2

                    if (person_aux.district != family.district):

                        vals['district'] = person_aux.district

                    if (person_aux.country_id != family.country_id):

                        vals['country_id'] = person_aux.country_id.id

                    if (person_aux.state_id != family.state_id):

                        vals['state_id'] = person_aux.state_id.id

                    if (person_aux.city_id != family.city_id):

                        vals['city_id'] = person_aux.city_id.id

                    # if (person_aux.phone is not False) and (person_aux.phone != family.phone):

                    #     vals['phone'] = person_aux.phone

                    # if (person_aux.mobile is not False) and (person_aux.mobile != family.mobile):

                    #     vals['mobile'] = person_aux.mobile

                if self.update_ref_address_data:

                    if (person_aux.ref_address_is_unavailable != family.ref_address_is_unavailable):

                        vals['ref_address_is_unavailable'] = person_aux.ref_address_is_unavailable

                    if (person_aux.ref_address_id != family.ref_address_id):

                        vals['ref_address_id'] = person_aux.ref_address_id.id

                if vals != {}:

                    vals['reg_state'] = 'revised'

                _logger.info(u'%s %s', '>>>>>>>>>>', vals)
                family.write(vals)

        return True
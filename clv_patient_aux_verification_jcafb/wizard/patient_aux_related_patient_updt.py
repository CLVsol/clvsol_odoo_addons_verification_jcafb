# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientAuxRelatePatientUpdt(models.TransientModel):
    _description = 'Patient (Aux) Related Patient Update'
    _name = 'clv.patient_aux.related_patient_updt'

    def _default_patient_aux_ids(self):
        return self._context.get('active_ids')
    patient_aux_ids = fields.Many2many(
        comodel_name='clv.patient_aux',
        relation='clv_patient_aux_related_patient_updt_rel',
        string='Patients (Aux)',
        default=_default_patient_aux_ids
    )

    update_contact_info_data = fields.Boolean(
        string='Update Contact Information Data',
        default=True,
        readonly=False
    )

    related_patient_verification_exec = fields.Boolean(
        string='Related Patient Verification Execute',
        default=True,
    )

    patient_aux_verification_exec = fields.Boolean(
        string='Patient (Aux) Verification Execute',
        default=True,
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

    def do_patient_aux_related_patient_updt(self):
        self.ensure_one()

        for patient_aux in self.patient_aux_ids:

            _logger.info(u'%s %s', '>>>>>', patient_aux.name)

            if not patient_aux.related_patient_is_unavailable:

                related_patient = patient_aux.related_patient_id
                vals = {}

                if (patient_aux.phase_id != related_patient.phase_id):

                    vals['phase_id'] = patient_aux.phase_id.id

                if (patient_aux.state != related_patient.state):

                    vals['state'] = patient_aux.state

                if (patient_aux.global_tag_ids.id is not False):

                    m2m_list = []
                    count = 0
                    for global_tag_id in patient_aux.global_tag_ids:
                        m2m_list.append((4, global_tag_id.id))
                        count += 1

                    if count > 0:
                        vals['global_tag_ids'] = m2m_list

                if (patient_aux.category_ids.id is not False):

                    m2m_list = []
                    count = 0
                    for global_tag_id in patient_aux.category_ids:
                        m2m_list.append((4, global_tag_id.id))
                        count += 1

                    if count > 0:
                        vals['category_ids'] = m2m_list

                if (patient_aux.marker_ids.id is not False):

                    m2m_list = []
                    count = 0
                    for global_tag_id in patient_aux.marker_ids:
                        m2m_list.append((4, global_tag_id.id))
                        count += 1

                    if count > 0:
                        vals['marker_ids'] = m2m_list

                if (patient_aux.name != related_patient.name):

                    vals['name'] = patient_aux.name

                if (patient_aux.code != related_patient.code):

                    vals['code'] = patient_aux.code

                if (patient_aux.is_absent != related_patient.is_absent):

                    vals['is_absent'] = patient_aux.is_absent

                if (patient_aux.gender != related_patient.gender):

                    vals['gender'] = patient_aux.gender

                if (patient_aux.birthday != related_patient.birthday):

                    vals['birthday'] = patient_aux.birthday

                if (patient_aux.date_death != related_patient.date_death):

                    vals['date_death'] = patient_aux.date_death

                if (patient_aux.force_is_deceased != related_patient.force_is_deceased):

                    vals['force_is_deceased'] = patient_aux.force_is_deceased

                if self.update_contact_info_data:

                    if (patient_aux.contact_info_is_unavailable != related_patient.contact_info_is_unavailable):

                        vals['contact_info_is_unavailable'] = patient_aux.contact_info_is_unavailable

                    if (patient_aux.zip != related_patient.zip):

                        vals['zip'] = patient_aux.zip

                    if (patient_aux.street_name != related_patient.street_name):

                        vals['street_name'] = patient_aux.street_name

                    if (patient_aux.street_number != related_patient.street_number):

                        vals['street_number'] = patient_aux.street_number

                    if (patient_aux.street_number2 != related_patient.street_number2):

                        vals['street_number2'] = patient_aux.street_number2

                    if (patient_aux.street2 != related_patient.street2):

                        vals['street2'] = patient_aux.street2

                    if (patient_aux.country_id != related_patient.country_id):

                        vals['country_id'] = patient_aux.country_id.id

                    if (patient_aux.state_id != related_patient.state_id):

                        vals['state_id'] = patient_aux.state_id.id

                    if (patient_aux.city_id != related_patient.city_id):

                        vals['city_id'] = patient_aux.city_id.id

                    if (patient_aux.phone is not False) and (patient_aux.phone != related_patient.phone):

                        vals['phone'] = patient_aux.phone

                    if (patient_aux.mobile is not False) and (patient_aux.mobile != related_patient.mobile):

                        vals['mobile'] = patient_aux.mobile

                if vals != {}:

                    vals['reg_state'] = 'revised'

                _logger.info(u'%s %s', '>>>>>>>>>>', vals)
                related_patient.write(vals)

            if self.related_patient_verification_exec:
                if patient_aux.related_patient_id.id is not False:
                    patient_aux.related_patient_id._patient_verification_exec()

            if self.patient_aux_verification_exec:
                patient_aux._patient_aux_verification_exec()

        return True

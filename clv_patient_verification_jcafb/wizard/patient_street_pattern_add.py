# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from functools import reduce

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


class PatientStreetPatternAdd(models.TransientModel):
    _description = 'Patient Street Pattern Add'
    _name = 'clv.patient.street_pattern_add'

    def _default_patient_ids(self):
        return self._context.get('active_ids')
    patient_ids = fields.Many2many(
        comodel_name='clv.patient',
        relation='clv_patient_street_pattern_add_rel',
        string='Patients',
        default=_default_patient_ids)
    count_patients = fields.Integer(
        string='Number of Patients',
        compute='_compute_count_patients',
        store=False
    )

    patient_verification_exec = fields.Boolean(
        string='Patient Verification Execute',
        default=True,
    )

    @api.depends('patient_ids')
    def _compute_count_patients(self):
        for r in self:
            r.count_patients = len(r.patient_ids)

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

    def do_patient_street_pattern_add(self):
        self.ensure_one()

        PartnerEntityStreetPattern = self.env['clv.partner_entity.street_pattern']

        for patient in self.patient_ids:

            _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (patient):', patient.name)

            street_patern = PartnerEntityStreetPattern.search([
                ('street', '=', patient.street_name),
                ('street2', '=', patient.street2),
            ])

            if street_patern.street is False:

                values = {}
                values['street'] = patient.street_name
                values['street2'] = patient.street2
                values['active'] = True
                PartnerEntityStreetPattern.create(values)

            if self.patient_verification_exec:
                patient._patient_verification_exec()

        return True

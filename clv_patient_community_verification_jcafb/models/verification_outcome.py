# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import models, _

_logger = logging.getLogger(__name__)


class VerificationOutcome(models.Model):
    _inherit = 'clv.verification.outcome'

    def _person_verification_patient(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        state = 'Ok'
        outcome_info = ''

        patient_ids = model_object.patient_ids

        if model_object.is_patient:

            if len(patient_ids) == 0:
                outcome_info = _('Missing related "Patient" register.')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

            if len(patient_ids) > 1:
                outcome_info = _('There are more than one related "Patient" register.')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

        else:

            if len(patient_ids) != 0:

                outcome_info = _('"Related Patient" should not be set.\n')
                state = self._get_verification_outcome_state(state, 'Error (L1)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

        verification_values = {}
        verification_values['date_verification'] = date_verification
        verification_values['outcome_info'] = outcome_info
        verification_values['state'] = state
        verification_outcome.write(verification_values)


class VerificationOutcome_2(models.Model):
    _inherit = 'clv.verification.outcome'

    def _patient_verification_related_person(self, verification_outcome, model_object):

        # _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)
        _logger.warning(u'%s %s',
                        '>>>>>>>>>>>>>>> "_patient_verification_related_person" was not processed for', model_object.name)

        date_verification = datetime.now()

        # related_person = model_object.related_person_id

        state = 'Ok'
        outcome_info = ''

        # if model_object.related_person_is_unavailable:

        #     if related_person.id is not False:

        #         outcome_info = _('"Related Person is Unavailable" should not be set.\n')
        #         state = self._get_verification_outcome_state(state, 'Error (L0)')

        # else:

        #     if related_person.id is not False:

        #         if (model_object.name != related_person.name):

        #             outcome_info += _('"Name" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.code != related_person.code):

        #             outcome_info += _('"Person Code" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.is_absent != related_person.is_absent):

        #             outcome_info += _('"Is Absent" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.gender != related_person.gender):

        #             outcome_info += _('"Gender" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.birthday != related_person.birthday):

        #             outcome_info += _('"Date of Birth" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.force_is_deceased != related_person.force_is_deceased):

        #             outcome_info += _('"Force Is Deceased" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.date_death != related_person.date_death):

        #             outcome_info += _('"Deceased Date" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.phase_id != related_person.phase_id):

        #             outcome_info += _('"Phase" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.state != related_person.state):

        #             outcome_info += _('"State" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.zip != related_person.zip) or \
        #            (model_object.street_name != related_person.street_name) or \
        #            (model_object.street_number != related_person.street_number) or \
        #            (model_object.street_number2 != related_person.street_number2) or \
        #            (model_object.street2 != related_person.street2) or \
        #            (model_object.country_id != related_person.country_id) or \
        #            (model_object.state_id != related_person.state_id) or \
        #            (model_object.city_id != related_person.city_id):

        #             outcome_info += _('"Contact Information (Address)" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if ((model_object.phone is not False) and (model_object.phone != related_person.phone)) or \
        #            ((model_object.mobile is not False) and (model_object.mobile != related_person.mobile)) or \
        #            ((model_object.email is not False) and (model_object.email != related_person.email)):

        #             outcome_info += _('"Contact Information (Phones)" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         # if (model_object.global_tag_ids.id is not False):

        #         #     related_person_global_tag_ids = []
        #         #     for global_tag_id in related_person.global_tag_ids:
        #         #         related_person_global_tag_ids.append(global_tag_id.id)

        #         #     count_new_global_tag_ids = 0
        #         #     for global_tag_id in model_object.global_tag_ids:
        #         #         if global_tag_id.id not in related_person_global_tag_ids:
        #         #             count_new_global_tag_ids += 1

        #         #     if count_new_global_tag_ids > 0:
        #         #         outcome_info += _('Added "Global Tag(s)".\n')
        #         #         state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.category_ids.id is not False):

        #             related_person_category_ids = []
        #             for category_id in related_person.category_ids:
        #                 related_person_category_ids.append(category_id.id)

        #             count_new_category_ids = 0
        #             for category_id in model_object.global_tag_ids:
        #                 if category_id.id not in related_person_category_ids:
        #                     count_new_category_ids += 1

        #             if count_new_category_ids > 0:
        #                 outcome_info += _('Added "Person Category(ies)".\n')
        #                 state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         # if (model_object.marker_ids.id is not False):

        #         #     related_person_marker_ids = []
        #         #     for marker_id in related_person.marker_ids:
        #         #         related_person_marker_ids.append(marker_id.id)

        #         #     count_new_marker_ids = 0
        #         #     for marker_id in model_object.marker_ids:
        #         #         if marker_id.id not in related_person_marker_ids:
        #         #             count_new_marker_ids += 1

        #         #     if count_new_marker_ids > 0:
        #         #         outcome_info += _('Added "Person Marker(s)".\n')
        #         #         state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if model_object.related_person_id.verification_state != 'Ok':

        #             outcome_info += _('Related Person "Verification State" is "') + \
        #                 model_object.related_person_id.verification_state + '".\n'
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #     else:

        #         outcome_info = _('Missing "Related Person".\n')
        #         state = self._get_verification_outcome_state(state, 'Error (L0)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

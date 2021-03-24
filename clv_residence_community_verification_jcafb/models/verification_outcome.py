# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from datetime import datetime

from odoo import models, _

_logger = logging.getLogger(__name__)


class VerificationOutcome(models.Model):
    _inherit = 'clv.verification.outcome'

    def _address_verification_residence(self, verification_outcome, model_object):

        _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)

        date_verification = datetime.now()

        state = 'Ok'
        outcome_info = ''

        residence_ids = model_object.residence_ids

        if model_object.is_residence:

            if len(residence_ids) == 0:
                outcome_info = _('Missing related "Residence" register.')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

            if len(residence_ids) > 1:
                outcome_info = _('There are more than one related "Residence" register.')
                state = self._get_verification_outcome_state(state, 'Error (L0)')

        else:

            if len(residence_ids) != 0:

                outcome_info = _('"Related Residence" should not be set.\n')
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

    def _residence_verification_related_address(self, verification_outcome, model_object):

        # _logger.info(u'%s %s', '>>>>>>>>>>>>>>> (model_object):', model_object.name)
        _logger.warning(u'%s %s',
                        '>>>>>>>>>>>>>>> "_residence_verification_related_address" was not processed for', model_object.name)

        date_verification = datetime.now()

        # related_address = model_object.related_address_id

        state = 'Ok'
        outcome_info = ''

        # if model_object.related_address_is_unavailable:

        #     if related_address.id is not False:

        #         outcome_info = _('"Related Address is Unavailable" should not be set.\n')
        #         state = self._get_verification_outcome_state(state, 'Error (L0)')

        # else:

        #     if related_address.id is not False:

        #         if (model_object.name != related_address.name):

        #             outcome_info += _('"Name" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L0)')

        #         if (model_object.code != related_address.code):

        #             outcome_info += _('"Address Code" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.phase_id != related_address.phase_id):

        #             outcome_info += _('"Phase" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         # if (model_object.reg_state != related_address.reg_state):

        #         #     outcome_info += _('"Register State" has changed.\n')
        #         #     state = self._get_verification_outcome_state(state, 'Warning (L0)')

        #         if (model_object.state != related_address.state):

        #             outcome_info += _('"State" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.zip != related_address.zip) or \
        #            (model_object.street_name != related_address.street_name) or \
        #            (model_object.street_number != related_address.street_number) or \
        #            (model_object.street_number2 != related_address.street_number2) or \
        #            (model_object.street2 != related_address.street2) or \
        #            (model_object.country_id != related_address.country_id) or \
        #            (model_object.state_id != related_address.state_id) or \
        #            (model_object.city_id != related_address.city_id):

        #             outcome_info += _('"Contact Information (Address)" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L0)')

        #         if (model_object.phone != related_address.phone) or \
        #            (model_object.mobile != related_address.mobile) or \
        #            (model_object.email != related_address.email):

        #             outcome_info += _('"Contact Information (Phone)" has changed.\n')
        #             state = self._get_verification_outcome_state(state, 'Warning (L0)')

        #         if model_object.related_address_id.verification_state != 'Ok':

        #             outcome_info += _('Related Address "Verification State" is "') + \
        #                 model_object.related_address_id.verification_state + '".\n'
        #             state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         # if (model_object.global_tag_ids.id is not False):

        #         #     related_address_global_tag_ids = []
        #         #     for global_tag_id in related_address.global_tag_ids:
        #         #         related_address_global_tag_ids.append(global_tag_id.id)

        #         #     count_new_global_tag_ids = 0
        #         #     for global_tag_id in model_object.global_tag_ids:
        #         #         if global_tag_id.id not in related_address_global_tag_ids:
        #         #             count_new_global_tag_ids += 1

        #         #     if count_new_global_tag_ids > 0:
        #         #         outcome_info += _('Added "Global Tag(s)".\n')
        #         #         state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         if (model_object.category_ids.id is not False):

        #             related_address_category_ids = []
        #             for category_id in related_address.category_ids:
        #                 related_address_category_ids.append(category_id.id)

        #             count_new_category_ids = 0
        #             for category_id in model_object.category_ids:
        #                 if category_id.id not in related_address_category_ids:
        #                     count_new_category_ids += 1

        #             if count_new_category_ids > 0:
        #                 outcome_info += _('Added "Person Category(ies)".\n')
        #                 state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #         # if (model_object.marker_ids.id is not False):

        #         #     related_address_marker_ids = []
        #         #     for marker_id in related_address.marker_ids:
        #         #         related_address_marker_ids.append(marker_id.id)

        #         #     count_new_marker_ids = 0
        #         #     for marker_id in model_object.marker_ids:
        #         #         if marker_id.id not in related_address_marker_ids:
        #         #             count_new_marker_ids += 1

        #         #     if count_new_marker_ids > 0:
        #         #         outcome_info += _('Added "Person Marker(s)".\n')
        #         #         state = self._get_verification_outcome_state(state, 'Warning (L1)')

        #     else:

        #         outcome_info = _('Missing "Related Address".\n')
        #         state = self._get_verification_outcome_state(state, 'Error (L0)')

        if outcome_info == '':
            outcome_info = False

        self._object_verification_outcome_updt(
            verification_outcome, state, outcome_info, date_verification, model_object
        )

        # verification_values = {}
        # verification_values['date_verification'] = date_verification
        # verification_values['outcome_info'] = outcome_info
        # verification_values['state'] = state
        # verification_outcome.write(verification_values)

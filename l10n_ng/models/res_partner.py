# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one(
        'res.city', string='Local Area', domain="[('state_id', '=', state_id)]")

    @api.onchange('state_id')
    def _onchange_state(self):
        super(Partner, self)._onchange_state()
        if not(self.state_id) or (self.state_id and self.state_id != self.city_id.state_id):
            self.city_id = False

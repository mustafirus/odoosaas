# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Database(models.Model):
    _name = 'odoosaas.database'

    name = fields.Char('Name', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    date_time = fields.Datetime('Database creation date', default=datetime.now())
    domain = fields.Char('Domain')

# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Database(models.Model):
    _name = 'odoosaas.database'

    name = fields.Char('Name', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    date_time = fields.Datetime('Creation date', default=datetime.now())
    domain = fields.Char('Domain')
    version = fields.Selection([
        ('v8', 'v8'),
        ('v9', 'v9'),
        ('v10', 'v10'),
        ('v11', 'v11'),
        ('v12', 'v12')],
        default='v12', string='Version', required=True, help='Version of the Odoo')
    trial = fields.Selection([
        ('trial', 'Trial version'),
        ('full', 'Full version')],
        string='Subscription version')
    active = fields.Boolean(default=True)
    tariff_id = fields.Many2one('odoosaas.tariff', string='Tariff')
    backupplan_id = fields.Many2one('odoosaas.backupplan', string='Backup plan')

    _sql_constraints = [('name_unique', 'unique (name)', 'Name must be unique !')]


class BackupPlan(models.Model):
    _name = 'odoosaas.backupplan'

    items_id = fields.Many2one('odoosaas.items')


class BackupPlanItems(models.Model):
    _name = 'odoosaas.backupplanitems'

    type = fields.Selection([('hourly', 'hourly'), ('daily', 'daily'), ('weekly', 'weekly')])
    cnt = fields.Integer('Number of backups')

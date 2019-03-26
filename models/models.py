# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Database(models.Model):
    _name = 'odoosaas.database'

    name = fields.Char('Name', required=True)
    # make name unique
    partner_id = fields.Many2one('res.partner', required=True)
    # there is standard field creation_date
    # date_time = fields.Datetime('Database creation date', default=datetime.now())
    domain = fields.Char('Domain')
    version = fields.Selection({
        'v8': "v8"
        #................. until 12
    }, default='v12')
    trial = fields.Boolean()
    active = fields.Boolean() # special field - u must implement all funtions of this field
    tariff = fields.Many2one('asdasdd.tariff')
    backupplan

class BackupPlan(models.Model):
    items = fields.Many2one('asdasdd.items')
    pass

class BackupPlanItems(models.Model):
    type = selection# hourly, daily weekly
    cnt = integer # number of backups
    pass

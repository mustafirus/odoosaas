# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tariff(models.Model):
    _name = 'odoosaas.tariff'

    name = fields.Char()


class Items(models.Model):
    _name = 'odoosaas.items'

    name = fields.Char()

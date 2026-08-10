# -*- coding: utf-8 -*-
from odoo import models

class VasEinvoiceTaxMap(models.Model):
    _name = 'vas.einvoice.tax.map'
    _description = 'Ánh xạ thuế suất CQT → thuế trong Odoo'
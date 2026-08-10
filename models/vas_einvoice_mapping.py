# -*- coding: utf-8 -*-
from odoo import models

class VasEinvoiceMapping(models.Model):
    _name = 'vas.einvoice.mapping'
    _description = 'Bảng ánh xạ hóa đơn CQT → Odoo (Cấp 3 – không có PO)'
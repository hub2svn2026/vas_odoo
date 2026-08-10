# -*- coding: utf-8 -*-
from odoo import models

class VasEinvoiceFetchWizard(models.TransientModel):
    _name = 'vas.einvoice.fetch.wizard'
    _description = 'Lấy hóa đơn điện tử từ CQT'
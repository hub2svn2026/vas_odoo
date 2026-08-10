# -*- coding: utf-8 -*-
from odoo import models

class VasPaymentEinvoiceViewer(models.TransientModel):
    _name = 'vas.payment.einvoice.viewer'
    _description = 'Xem Hóa đơn CQT liên kết với Thanh toán'
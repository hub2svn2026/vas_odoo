# -*- coding: utf-8 -*-
from odoo import models

class VasEinvoiceImportJournalWizard(models.TransientModel):
    _name = 'vas.einvoice.import.journal.wizard'
    _description = 'Chọn nhật ký để nhập hóa đơn CQT không tìm được sản phẩm'
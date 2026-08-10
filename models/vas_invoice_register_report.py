# -*- coding: utf-8 -*-
from odoo import models

class VasInvoiceRegisterXlsx(models.AbstractModel):
    _name = 'report.vas_accounting.vas_invoice_register_xlsx'
    _description = 'Bảng kê hóa đơn mua vào - bán ra XLSX'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
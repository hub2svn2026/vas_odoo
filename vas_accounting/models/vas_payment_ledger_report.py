# -*- coding: utf-8 -*-
from odoo import models

class VasPaymentLedgerReport(models.AbstractModel):
    _name = 'report.vas_accounting.vas_payment_ledger_pdf'
    _description = 'Sổ Chi Tiết Thanh Toán S32-DN'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
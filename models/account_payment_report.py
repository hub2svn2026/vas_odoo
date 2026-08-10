# -*- coding: utf-8 -*-
from odoo import models

class AccountPaymentVoucherReport(models.AbstractModel):
    _name = 'report.vas_accounting.account_payment_voucher_pdf'
    _description = 'In Phiếu Thu / Phiếu Chi'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
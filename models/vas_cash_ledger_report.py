# -*- coding: utf-8 -*-
from odoo import models

class VasCashLedgerReport(models.AbstractModel):
    _name = 'report.vas_accounting.vas_cash_ledger_pdf'
    _description = 'Sổ kế toán chi tiết quỹ tiền mặt / tiền gửi ngân hàng'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
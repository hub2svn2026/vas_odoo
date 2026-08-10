# -*- coding: utf-8 -*-
from odoo import models

class AccountDebtClearingReport(models.AbstractModel):
    _name = 'report.vas_accounting.account_debt_clearing_pdf'
    _description = 'Báo cáo Biên bản bù trừ công nợ'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
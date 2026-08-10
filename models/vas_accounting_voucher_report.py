# -*- coding: utf-8 -*-
from odoo import models

class VasAccountingVoucherReport(models.AbstractModel):
    _name = 'report.vas_accounting.vas_accounting_voucher_pdf'
    _description = 'Báo cáo Phiếu Kế Toán PDF'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
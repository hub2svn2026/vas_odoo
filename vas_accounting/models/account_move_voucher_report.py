# -*- coding: utf-8 -*-
from odoo import models

class AccountMoveVoucherReport(models.AbstractModel):
    _name = 'report.vas_accounting.account_move_voucher_pdf'
    _description = 'In Phiếu Kế Toán từ Bút Toán'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
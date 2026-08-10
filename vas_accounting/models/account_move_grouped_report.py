# -*- coding: utf-8 -*-
from odoo import models

class AccountMoveGroupedVoucherReport(models.AbstractModel):
    _name = 'report.vas_accounting.account_move_grouped_voucher_pdf'
    _description = 'In Phiếu Kế Toán – nhóm Miscellaneous theo Sequence Prefix'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
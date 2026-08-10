# -*- coding: utf-8 -*-
from odoo import models

class StockPickingVoucherReport(models.AbstractModel):
    _name = 'report.vas_accounting.stock_picking_voucher_pdf'
    _description = 'In Phiếu Nhập/Xuất Kho'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
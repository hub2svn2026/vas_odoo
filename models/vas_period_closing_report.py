# -*- coding: utf-8 -*-
from odoo import models

class VasPeriodClosingReport(models.AbstractModel):
    _name = 'report.vas_accounting.report_vas_period_closing'
    _description = 'Report: Bảng kết chuyển cuối kỳ'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
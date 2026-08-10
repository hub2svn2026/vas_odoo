# -*- coding: utf-8 -*-
from odoo import models

class VasGeneralLedgerReport(models.AbstractModel):
    _name = 'report.vas_accounting.vas_general_ledger_pdf'
    _description = 'Sổ Cái S03b-DN Report'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}
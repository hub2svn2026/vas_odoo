# -*- coding: utf-8 -*-
from odoo import models

class StockInventoryReportWizard(models.TransientModel):
    _name = 'stock.inventory.report.wizard'
    _description = 'Wizard báo cáo nhập xuất tồn kho theo kỳ'
# -*- coding: utf-8 -*-
#Inventory Report
from . import goods_receipts_report
from . import goods_delivery_report
from . import stock_inventory_report_month
from . import stock_inventory_report_mapped
from . import stock_inventory_report_line
#VAS Accounting
from . import vas_correspondence_rule
from . import vas_account_ledger
from . import account_move
from . import account_move_voucher_report
from . import account_move_grouped_report
from . import account_payment
from . import account_payment_report
from . import stock_picking
from . import stock_picking_report
#VAS Accounting General Ledger Report
from . import vas_general_ledger_report
from . import vas_general_ledger_xlsx
#VAS Accounting Payment Ledger S32-DN
from . import vas_payment_ledger_report
#VAS EInvoice CQT
from . import vas_payment_einvoice_wizard
from . import vas_payment_einvoice_viewer
from . import vas_einvoice_config
from . import vas_einvoice_tax_map
from . import vas_einvoice_mapping
from . import vas_einvoice_invoice
from . import vas_einvoice_import_wizard
#VAS Invoice Register
from . import vas_invoice_register_report
#VAS Cash Ledger S07a/S08
from . import vas_cash_ledger_report
#VAS Accounting Voucher – Phiếu Kế Toán
from . import vas_voucher_type
from . import vas_accounting_voucher
from . import vas_accounting_voucher_report
#VAS Debt Clearing – Cấn trừ công nợ 131/331
from . import account_debt_clearing
from . import account_debt_clearing_report
#VAS Period Closing – Kết chuyển cuối kỳ
from . import vas_closing_rule
from . import vas_period_closing
from . import vas_period_closing_report

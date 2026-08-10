/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

class VasPaymentRequired extends Component {
    static template = xml`
<div style="display:flex;align-items:center;justify-content:center;min-height:70vh;padding:40px;background:#f8f9fc;">
    <div style="background:#fff;border-radius:16px;padding:48px 40px;text-align:center;max-width:480px;box-shadow:0 4px 24px rgba(0,0,0,0.08);">

        <div style="font-size:3.5em;margin-bottom:20px;">🔒</div>

        <h2 style="font-size:1.4em;font-weight:700;color:#1a1a2e;margin-bottom:10px;">
            Tính năng yêu cầu bản quyền
        </h2>
        <p style="color:#6c7a89;font-size:0.95em;line-height:1.7;margin-bottom:28px;">
            Chức năng này chỉ dành cho người dùng đã đăng ký bản đầy đủ của
            <strong style="color:#714b67;">VAS Accounting</strong>.
            Vui lòng liên hệ Hub2S Vietnam để được tư vấn và kích hoạt bản quyền.
        </p>

        <div style="background:#f0fdf4;border:1px solid #d1fae5;border-radius:12px;padding:20px 28px;text-align:left;">
            <div style="font-weight:700;color:#059669;font-size:0.95em;margin-bottom:12px;">
                Hub2S Vietnam Co., Ltd
            </div>
            <div style="color:#4a5568;font-size:0.88em;line-height:2;">
                <div>📞 Zalo: (+84) 902 611 333</div>
                <div>📧 sales@hub2s.com</div>
                <div>🌐 hub2s.com</div>
            </div>
        </div>

    </div>
</div>
    `;
}

registry.category("actions").add("vas_accounting.payment_required", VasPaymentRequired);

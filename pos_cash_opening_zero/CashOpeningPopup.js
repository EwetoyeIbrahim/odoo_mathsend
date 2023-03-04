odoo.define('pos_cash_opening_zero.CashOpeningPopup', function (require) {
    "use strict";
    const { useState } = owl;
    const CashOpeningPopup = require('point_of_sale.CashOpeningPopup');
    const Registries = require("point_of_sale.Registries")

    const CashOpeningZero = (CashOpeningPopup) =>
        class extends CashOpeningPopup{
            setup() {
                super.setup();
                this.manualInputCashCount = null;
                this.state = useState({
                    notes: "",
                    openingCash: 0,
                    displayMoneyDetailsPopup: false,
                });
            }
        };

    Registries.Component.extend(CashOpeningPopup, CashOpeningZero);

    return CashOpeningZero
});
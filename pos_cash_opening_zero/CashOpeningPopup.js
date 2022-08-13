odoo.define('pos_cash_opening_zero.CashOpeningPopup', function (require) {
    "use strict";
    const { useState, useRef } = owl.hooks;
    const CashOpeningPopup = require('point_of_sale.CashOpeningPopup');
    const Registries = require("point_of_sale.Registries")

    const CashOpeningZero = (CashOpeningPopup) =>
        class extends CashOpeningPopup{
            constructor() {
                super(...arguments);
                this.manualInputCashCount = null;
                this.state = useState({
                    notes: "",
                    openingCash: 0,
                });
                this.moneyDetailsRef = useRef('moneyDetails');
            }
        };

    Registries.Component.extend(CashOpeningPopup, CashOpeningZero);

    return CashOpeningZero
});
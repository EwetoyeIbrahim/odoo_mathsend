odoo.define('pos_allow_employee_close_session.chrome', function (require) {
    "use strict";
    const Chrome = require('point_of_sale.Chrome');
    const Registries = require('point_of_sale.Registries');

    const PosEmployee = (Chrome) =>
        class extends Chrome {
            get headerButtonIsShown() {
                return true
            }
        };
    Registries.Component.extend(Chrome, PosEmployee);

    return Chrome;
});
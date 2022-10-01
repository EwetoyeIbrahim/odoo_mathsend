odoo.define('pos_barcode_display.models', function (require) {
    "use strict";
    var models = require('point_of_sale.models');

    models.Orderline = models.Orderline.extend({
        get_barcode: function () {
            return this.product.barcode;
        },
    });
});
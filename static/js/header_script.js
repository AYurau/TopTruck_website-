const doc = document;

const sales_radio = doc.getElementById('sales_radio');
const rent_radio = doc.getElementById('rent_radio');
const spare_radio = doc.getElementById('spare_radio');
const options_radio = doc.getElementById('options_radio');

let sales_radio_condition = -1;
let rent_radio_condition = -1;
let spare_radio_condition = -1;
let options_radio_condition = -1;

sales_radio.addEventListener('click', function() {
    sales_radio_condition *= -1;
    if (sales_radio_condition == 1) {
        rent_radio_condition = -1;
        spare_radio_condition = -1;
        options_radio_condition = -1;
    }
    if (sales_radio_condition == -1) {
        sales_radio.checked = false;
    }
});
rent_radio.addEventListener('click', function() {
    rent_radio_condition *= -1;
    if (rent_radio_condition == 1) {
        sales_radio_condition = -1;
        spare_radio_condition = -1;
        options_radio_condition = -1;
    }
    if (rent_radio_condition == -1) {
        rent_radio.checked = false;
    }
});
spare_radio.addEventListener('click', function() {
    spare_radio_condition *= -1;
    if (spare_radio_condition == 1) {
        rent_radio_condition = -1;
        sales_radio_condition = -1;
        options_radio_condition = -1;
    }
    if (spare_radio_condition == -1) {
        spare_radio.checked = false;
    }
});
options_radio.addEventListener('click', function() {
    options_radio_condition *= -1;
    if (options_radio_condition == 1) {
        rent_radio_condition = -1;
        spare_radio_condition = -1;
        sales_radio_condition = -1;
    }
    if (options_radio_condition == -1) {
        options_radio.checked = false;
    }
});

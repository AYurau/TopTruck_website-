const slides = doc.getElementById('slides');
const slide_1_control = doc.getElementById('slide_1_control');
const slide_2_control = doc.getElementById('slide_2_control');
const slide_3_control = doc.getElementById('slide_3_control');
const slide_4_control = doc.getElementById('slide_4_control');
const slide_5_control = doc.getElementById('slide_5_control');
const section_2 = doc.getElementById('section_2');

let controls = [slide_1_control, slide_2_control, slide_3_control, slide_4_control, slide_5_control];
let current_control = 1;
let isSetted = false;

let slides_rect;

document.addEventListener('scroll', function() {
    slides_rect = slides.getBoundingClientRect();

    if (slides_rect.y - window.innerHeight < 0 && slides_rect.bottom > 0) {
        isSetted = true;
    }
    else {
        isSetted = false;
    }
});

let toSlide = setInterval(function() {
    if (isSetted) {
        controls[current_control].checked = true;
        current_control++;
        if (current_control == 5) {
            current_control = 0;
        }
    }
}, 3500);

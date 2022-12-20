
$(document).ready(function () {

  $('.offer_button').click(function() {
    $('.order-form').toggleClass('active')
  });



gsap.registerPlugin(ScrollTrigger);
  function count() {
    let skews = document.querySelectorAll(".statistics");
    // skews.forEach((skew) => {
      let clip_polygon = gsap.timeline({
        scrollTrigger: {
          trigger: skews,
          start: "center bottom",
          end: false,
          markers: false,
          scrub: true,
          toggleClass: { targets: ".statistics", className: "active" },
        }
      });
    // });
  } //skew
  count();

});




const swiper = new Swiper('.slider', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  effect: 'slide',

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    hideOnClick: 'true',
  },
});
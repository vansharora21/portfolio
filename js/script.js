(function($) {

    "use strict";

    $(document).ready(function() {
      
      // Smart Navbar Scroll Listener
      var lastScrollTop = 0;
      var navbar = document.getElementById("mainNav");
      
      if (navbar) {
        window.addEventListener("scroll", function() {
          var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
          
          // Add Scrolled dark glass class if not at top
          if (scrollTop > 50) {
            navbar.classList.add("scrolled");
          } else {
            navbar.classList.remove("scrolled");
          }

          // Auto-hide logic (only triggers after scrolling down 200px)
          if (scrollTop > 200) {
            if (scrollTop > lastScrollTop) {
              // Scrolling down
              navbar.classList.add("nav-hidden");
            } else {
              // Scrolling up
              navbar.classList.remove("nav-hidden");
            }
          } else {
            // Always show near the top
            navbar.classList.remove("nav-hidden");
          }
          
          lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For negative scrolling on mobile
        }, false);
      }

      // masonoary //

      initIsotope();

      // lightbox

      lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true,
        'fitImagesInViewport': true
      })
      
      /* swiper */
      

      var testimonialSwiper = new Swiper(".testimonial-swiper", {
        spaceBetween: 20,
        pagination: {
            el: ".testimonial-swiper-pagination",
            clickable: true,
          },
        breakpoints: {
          0: {
            slidesPerView: 1,
          },
          800: {
            slidesPerView: 3,
          },
          1400: {
            slidesPerView: 3,
          }
        },
      });

      var certSwiper = new Swiper(".certificate-swiper", {
        spaceBetween: 20,
        loop: true,
        autoplay: {
            delay: 3500,
            disableOnInteraction: false,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
          0: { slidesPerView: 1 },
          600: { slidesPerView: 2 },
          1000: { slidesPerView: 3 },
          1400: { slidesPerView: 4 }
        },
      });

      // Custom cursor disabled

      // Initialize VanillaTilt for dynamic hover states
      if (typeof VanillaTilt !== 'undefined') {
        VanillaTilt.init(document.querySelectorAll("#portfolio .card, #about .bg-yellow, #about .bg-green, #about .bg-teal, #certificates .card, #skills .icon"), {
            max: 12,
            speed: 400,
            glare: true,
            "max-glare": 0.25,
            scale: 1.05
        });
      }

      // Make buttons Magnetic
      const magneticEls = document.querySelectorAll('.btn');
      magneticEls.forEach((el) => {
          el.addEventListener('mousemove', function(e) {
              const position = el.getBoundingClientRect();
              const x = e.clientX - position.left - position.width / 2;
              const y = e.clientY - position.top - position.height / 2;
              el.style.transform = `translate(${x * 0.3}px, ${y * 0.5}px)`;
          });

          el.addEventListener('mouseleave', function(e) {
              el.style.transform = 'translate(0px, 0px)';
          });
      });

      // Interactive WebGL Neural Net Database Background for the Entire Site
      if (typeof VANTA !== 'undefined') {
        VANTA.NET({
          el: "#vanta-site-bg",
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.00,
          minWidth: 200.00,
          scale: 1.00,
          scaleMobile: 1.00,
          color: 0xf0756c,         // Matches Primary Coral
          backgroundColor: 0x121212, // Matches dark body background
          points: 12.00,
          maxDistance: 22.00,
          spacing: 18.00
        });
      }

    }); // End of a document ready

  // init Isotope
  var initIsotope = function() {
    
    $('.grid').each(function(){

      // $('.grid').imagesLoaded( function() {
        // images have loaded
        var $buttonGroup = $( '.button-group' );
        var $checked = $buttonGroup.find('.is-checked');
        var filterValue = $checked.attr('data-filter');
  
        var $grid = $('.grid').isotope({
          itemSelector: '.portfolio-item',
          // layoutMode: 'fitRows',
          filter: filterValue
        });
    
        // bind filter button click
        $('.button-group').on( 'click', 'a', function(e) {
          e.preventDefault();
          filterValue = $( this ).attr('data-filter');
          $grid.isotope({ filter: filterValue });
        });
    
        // change is-checked class on buttons
        $('.button-group').each( function( i, buttonGroup ) {
          $buttonGroup.on( 'click', 'a', function() {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $( this ).addClass('is-checked');
          });
        });
      // });

    });
  }




})(jQuery);
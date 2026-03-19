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
$(document).ready(function () {
  // --- Scroll Animation Observer ---
  const animateOnScroll = () => {
    $("[data-animate]").each(function () {
      const $element = $(this);
      const rect = this.getBoundingClientRect();
      const duration = $element.data('duration') || '0.6s';
      const delay = $element.data('delay') || '0s';
      
      // Apply custom duration and delay
      $element.css({
        'transition-duration': duration,
        'transition-delay': delay
      });
      
      if (rect.top < window.innerHeight - 100) {
        $element.addClass("visible");
      }
    });
  };

  $(window).on("scroll", animateOnScroll);
  animateOnScroll();

  // --- Enhanced Text Animations ---
  const applyTextAnimation = () => {
    $("[data-animate='typewriter']").each(function() {
      const $element = $(this);
      const text = $element.text();
      $element.text('');
      $element.addClass('typewriter');
      
      let i = 0;
      const typing = setInterval(() => {
        if (i < text.length) {
          $element.text($element.text() + text.charAt(i));
          i++;
        } else {
          clearInterval(typing);
        }
      }, 100);
    });
  };

  // Apply text animations after elements are visible
  setTimeout(applyTextAnimation, 500);

  // --- Ajax Content Loader (Demo) ---
  $("#loadQuote").on("click", function () {
    const $btn = $(this);
    const $quote = $("#quoteText");

    $btn.text("Loading...").prop("disabled", true);

    // Example: Simulate university quote API
    $.ajax({
      url: "https://api.quotable.io/random?tags=education|inspirational",
      method: "GET",
      success: function (data) {
        $quote
          .hide()
          .text(`“${data.content}” — ${data.author}`)
          .fadeIn(600);
      },
      error: function () {
        $quote
          .hide()
          .text("Failed to load quote. Please try again.")
          .fadeIn(600);
      },
      complete: function () {
        $btn.text("Load Another Quote").prop("disabled", false);
      },
    });
  });

  // --- Smooth scroll indicator ---
  $(".scroll-indicator").on("click", function () {
    const target = $(this).data("target");
    let $targetElement;
    
    if (target) {
      $targetElement = $(target);
    } else {
      // Find the next section or content area
      $targetElement = $(".hero-banner").nextAll(":not(.navbar)").first();
    }
    
    if ($targetElement.length) {
      $("html, body").animate(
        { scrollTop: $targetElement.offset().top },
        800
      );
    }
  });

  // --- Parallax effect for mouse movement ---
  $(".hero-banner").each(function() {
    const $banner = $(this);
    if ($banner.data('mouse-parallax')) {
      $banner.on('mousemove', function(e) {
        const x = (e.clientX / $(window).width()) * 100;
        const y = (e.clientY / $(window).height()) * 100;
        $(this).find('.hero-content').css({
          'transform': `translate(${x * 0.02}px, ${y * 0.02}px)`
        });
      });
    }
  });

  // --- Auto scroll functionality ---
  $(".hero-banner").each(function() {
    const $banner = $(this);
    const autoScroll = $banner.data('auto-scroll');
    const scrollDelay = $banner.data('scroll-delay') || 5;
    
    if (autoScroll) {
      setTimeout(function() {
        const $targetElement = $banner.nextAll(":not(.navbar)").first();
        if ($targetElement.length) {
          $("html, body").animate(
            { scrollTop: $targetElement.offset().top },
            800
          );
        }
      }, scrollDelay * 1000);
    }
  });
});
// ------------------------------------------------------
// Auremont University Navbar - Fully Dynamic & Controlled
// ------------------------------------------------------

$(document).ready(function() {
  const $navbar = $(".navbar");
  const $menu = $("#navbar-menu");
  const $toggle = $("#navbar-toggle");

  // ======== Dynamic Vars from Django Data Attributes ========
  const bgColor = $navbar.data("bg-color");
  const textColor = $navbar.data("text-color");
  const hoverColor = $navbar.data("hover-color");
  const shadowEnabled = $navbar.data("shadow");
  const stickyEnabled = $navbar.data("sticky");
  const transparentEnabled = $navbar.data("transparent");
  const scrollTransition = $navbar.data("scroll-transition");
  const scrollThreshold = $navbar.data("scroll-threshold") || 100;
  const mobileBreakpoint = parseInt($navbar.data("mobile-breakpoint")) || 900;
  const hoverDelay = parseFloat($navbar.data("dropdown-hover-delay")) || 0.2;
  const theme = $navbar.data("theme") || "default";
  const hamburgerIcon = $navbar.data("hamburger-icon") || "fa-solid fa-bars";
  const closeIcon = $navbar.data("close-icon") || "fa-solid fa-xmark";
  const loadAnimation = $navbar.data("load-animation") || "slide-down";
  const animationDuration = $navbar.data("animation-duration") || "0.5s";
  const easing = $navbar.data("animation-easing") || "ease-in-out";
  const menuAlign = $navbar.data("menu-align") || "right"; // "left" | "center" | "right"
  const underlineStyle = $navbar.data("underline-style") || "glow"; // "none" | "solid" | "glow"
  const goldAccent = $navbar.data("gold-accent") || false;
  const uppercaseMenu = $navbar.data("uppercase") || false;
  const activeHighlight = $navbar.data("active-highlight") || "border"; // "border" | "background"
  const fontFamily = $navbar.data("font-family") || "Poppins, sans-serif";
  const borderRadius = $navbar.data("border-radius") || "8px";

  // ======== Apply Dynamic CSS Variables ========
  document.documentElement.style.setProperty("--navbar-bg", bgColor || "#001F3F");
  document.documentElement.style.setProperty("--navbar-text", textColor || "#FFFFFF");
  document.documentElement.style.setProperty("--navbar-hover", hoverColor || "#FFD700");
  document.documentElement.style.setProperty("--navbar-font", fontFamily);
  document.documentElement.style.setProperty("--navbar-radius", borderRadius);

  // ======== Apply Classes Based on Variables ========
  if (shadowEnabled) $navbar.addClass("navbar--shadow");
  if (stickyEnabled) $navbar.addClass("navbar--sticky");
  if (transparentEnabled) $navbar.addClass("navbar--transparent");
  if (uppercaseMenu) $navbar.addClass("navbar--uppercase");
  if (goldAccent) $navbar.addClass("navbar--gold");
  $navbar.addClass(`theme-${theme}`);

  // Menu alignment
  $menu.css({
    justifyContent:
      menuAlign === "center"
        ? "center"
        : menuAlign === "left"
        ? "flex-start"
        : "flex-end",
  });

  // ======== Load Animation ========
  if (loadAnimation !== "none") {
    $navbar.css({
      opacity: 0,
      transform:
        loadAnimation === "slide-down"
          ? "translateY(-20px)"
          : loadAnimation === "slide-up"
          ? "translateY(20px)"
          : loadAnimation === "zoom"
          ? "scale(0.9)"
          : "none",
      transition: `all ${animationDuration} ${easing}`,
    });

    setTimeout(() => {
      $navbar.css({
        opacity: 1,
        transform: "translateY(0) scale(1)",
      });
    }, 100);
  }

  // ======== Scroll Behavior (Transparency, Shadow, Transition) ========
  $(window).on("scroll", function() {
    const scrollTop = $(this).scrollTop();

    if (transparentEnabled) {
      if (scrollTop > scrollThreshold) {
        $navbar.removeClass("navbar--transparent");
      } else {
        $navbar.addClass("navbar--transparent");
      }
    }

    if (scrollTransition) {
      if (scrollTop > 50) $navbar.addClass("navbar--scrolled");
      else $navbar.removeClass("navbar--scrolled");
    }

    if (shadowEnabled && scrollTop > 5) {
      $navbar.addClass("navbar--shadow-visible");
    } else {
      $navbar.removeClass("navbar--shadow-visible");
    }
  });

  // ======== Mobile Toggle ========
  $toggle.html(`<i class="${hamburgerIcon}"></i>`);
  $toggle.on("click", function() {
    $menu.toggleClass("active");
    $(this).toggleClass("open");

    if ($menu.hasClass("active")) {
      $(this).html(`<i class="${closeIcon}"></i>`);
    } else {
      $(this).html(`<i class="${hamburgerIcon}"></i>`);
    }
  });

  // ======== Dropdown & Mega Menu Hover ========
  let dropdownTimeout;

  $(".navbar__item").hover(
    function() {
      clearTimeout(dropdownTimeout);
      const $dropdown = $(this).find(".navbar__dropdown, .navbar__mega-menu");
      $dropdown.stop(true, true).fadeIn(hoverDelay * 1000);
      $(this).find(".navbar__link").addClass("navbar__link--active");
    },
    function() {
      const $dropdown = $(this).find(".navbar__dropdown, .navbar__mega-menu");
      dropdownTimeout = setTimeout(() => {
        $dropdown.stop(true, true).fadeOut(hoverDelay * 1000);
      }, hoverDelay * 1000);
      $(this).find(".navbar__link").removeClass("navbar__link--active");
    }
  );

  // ======== Mobile Accordion ========
  function handleMobileMenus() {
    if ($(window).width() <= mobileBreakpoint) {
      $(".navbar__link").off("click").on("click", function(e) {
        const $item = $(this).closest(".navbar__item");
        const $dropdown = $item.find(".navbar__dropdown");
        const $megaMenu = $item.find(".navbar__mega-menu");

        if ($dropdown.length > 0 || $megaMenu.length > 0) {
          e.preventDefault();

          $(".navbar__item")
            .not($item)
            .find(".navbar__dropdown, .navbar__mega-menu")
            .removeClass("active");

          if ($dropdown.length > 0) $dropdown.toggleClass("active");
          if ($megaMenu.length > 0) $megaMenu.toggleClass("active");
        }
      });
    }
  }
  handleMobileMenus();
  $(window).on("resize", handleMobileMenus);

  // ======== Search Block Functionality ========
  $(".navbar__search-wrapper").each(function() {
    const $wrapper = $(this);
    const $input = $wrapper.find(".navbar__search-input");
    const $button = $wrapper.find(".navbar__search-button");
    const $suggestions = $wrapper.find(".navbar__search-suggestions");
    const searchEndpoint = $wrapper.data("search-endpoint") || "/search/";
    const enableAutoSuggest = $wrapper.data("enable-auto-suggest") === "true";
    const autoSuggestEndpoint = $wrapper.data("auto-suggest-endpoint") || "";
    const enableToggle = $wrapper.hasClass("navbar__search--toggleable");
    
    let searchTimeout;

    // Toggle behavior
    if (enableToggle) {
      $button.on("click", function(e) {
        e.preventDefault();
        $wrapper.toggleClass("navbar__search--expanded");
        if ($wrapper.hasClass("navbar__search--expanded")) {
          $input.focus();
        }
      });

      // Close search when clicking outside
      $(document).on("click", function(e) {
        if (!$wrapper.is(e.target) && $wrapper.has(e.target).length === 0) {
          $wrapper.removeClass("navbar__search--expanded");
        }
      });
    }

    // Search on Enter key
    $input.on("keypress", function(e) {
      if (e.which === 13) { // Enter key
        const searchTerm = $(this).val();
        if (searchTerm) {
          window.location.href = `${searchEndpoint}?q=${encodeURIComponent(searchTerm)}`;
        }
      }
    });

    // Search button click
    $button.on("click", function(e) {
      if (!enableToggle || $wrapper.hasClass("navbar__search--expanded")) {
        e.preventDefault();
        const searchTerm = $input.val();
        if (searchTerm) {
          window.location.href = `${searchEndpoint}?q=${encodeURIComponent(searchTerm)}`;
        }
      }
    });

    // Auto-suggest functionality
    if (enableAutoSuggest && autoSuggestEndpoint) {
      $input.on("input", function() {
        const searchTerm = $(this).val();
        
        // Clear previous timeout
        clearTimeout(searchTimeout);
        
        // Hide suggestions if search term is empty
        if (!searchTerm) {
          $suggestions.removeClass("active");
          return;
        }
        
        // Set new timeout for debouncing
        searchTimeout = setTimeout(() => {
          $.ajax({
            url: autoSuggestEndpoint,
            method: "GET",
            data: { q: searchTerm },
            success: function(data) {
              if (data && data.results && data.results.length > 0) {
                let suggestionsHtml = "";
                data.results.forEach(function(item) {
                  suggestionsHtml += `<a href="${item.url}" class="navbar__search-suggestion">${item.title}</a>`;
                });
                $suggestions.html(suggestionsHtml).addClass("active");
              } else {
                $suggestions.removeClass("active");
              }
            },
            error: function() {
              $suggestions.removeClass("active");
            }
          });
        }, 300); // Debounce for 300ms
      });

      // Hide suggestions when input loses focus
      $input.on("blur", function() {
        setTimeout(() => {
          $suggestions.removeClass("active");
        }, 150); // Small delay to allow click on suggestions
      });

      // Keyboard navigation for suggestions
      $input.on("keydown", function(e) {
        if ($suggestions.hasClass("active")) {
          const $suggestionsList = $suggestions.find(".navbar__search-suggestion");
          const $focused = $suggestions.find(".navbar__search-suggestion:focus");
          let currentIndex = $suggestionsList.index($focused);

          if (e.which === 40) { // Down arrow
            e.preventDefault();
            currentIndex = (currentIndex + 1) % $suggestionsList.length;
            $suggestionsList.eq(currentIndex).focus();
          } else if (e.which === 38) { // Up arrow
            e.preventDefault();
            currentIndex = (currentIndex - 1 + $suggestionsList.length) % $suggestionsList.length;
            $suggestionsList.eq(currentIndex).focus();
          } else if (e.which === 27) { // Escape key
            $suggestions.removeClass("active");
            $input.focus();
          }
        }
      });
    }
  });

  // ======== User Menu Functionality ========
  $(".navbar__user-menu").each(function() {
    const $userMenu = $(this);
    const $trigger = $userMenu.find(".navbar__user-trigger");
    const $dropdown = $userMenu.find(".navbar__user-dropdown");
    
    // Toggle dropdown on click
    $trigger.on("click", function(e) {
      e.preventDefault();
      e.stopPropagation();
      $userMenu.toggleClass("active");
      $trigger.attr("aria-expanded", $userMenu.hasClass("active"));
    });
    
    // Close dropdown when clicking outside
    $(document).on("click", function(e) {
      if (!$userMenu.is(e.target) && $userMenu.has(e.target).length === 0) {
        $userMenu.removeClass("active");
        $trigger.attr("aria-expanded", "false");
      }
    });
    
    // Keyboard navigation
    $trigger.on("keydown", function(e) {
      if (e.which === 13 || e.which === 32) { // Enter or Space
        e.preventDefault();
        $trigger.click();
      } else if (e.which === 27) { // Escape
        e.preventDefault();
        $userMenu.removeClass("active");
        $trigger.attr("aria-expanded", "false");
        $trigger.focus();
      }
    });
    
    // Close dropdown on link click (mobile)
    $dropdown.find("a").on("click", function() {
      $userMenu.removeClass("active");
      $trigger.attr("aria-expanded", "false");
    });
  });

  // ======== Active Link Highlight Mode ========
  if (activeHighlight === "background") {
    $(".navbar__link--active").css({
      backgroundColor: "var(--navbar-hover)",
      color: "#111",
      borderBottom: "none",
    });
  }

  if (underlineStyle === "glow") {
    $("<style>")
      .prop("type", "text/css")
      .html(`
        .navbar__link:hover::after,
        .navbar__link--active::after {
          content: "";
          display: block;
          height: 3px;
          background: var(--navbar-hover);
          box-shadow: 0 0 8px var(--navbar-hover);
          transition: all 0.3s ease;
        }
      `)
      .appendTo("head");
  }

  // ======== Language Switcher ========
  $(".navbar__language-select").on("change", function() {
    const selectedLanguage = $(this).val();
    console.log("Language switched to:", selectedLanguage);
    // Example: window.location.href = `/${selectedLanguage}/`;
  });

  // ======== Language Switcher Block Functionality ========
  $(".navbar__language-switcher").each(function() {
    const $languageSwitcher = $(this);
    const $trigger = $languageSwitcher.find(".navbar__language-trigger");
    const $dropdown = $languageSwitcher.find(".navbar__language-dropdown");
    const animationDuration = $languageSwitcher.data("animation-duration") || "0.3s";
    const animationEasing = $languageSwitcher.data("animation-easing") || "ease-in-out";
    
    // Set CSS variables for animations
    $dropdown.css({
      "transition": `all ${animationDuration} ${animationEasing}`
    });
    
    // Toggle dropdown on click
    $trigger.on("click", function(e) {
      e.preventDefault();
      e.stopPropagation();
      $languageSwitcher.toggleClass("active");
      $trigger.attr("aria-expanded", $languageSwitcher.hasClass("active"));
    });
    
    // Close dropdown when clicking outside
    $(document).on("click", function(e) {
      if (!$languageSwitcher.is(e.target) && $languageSwitcher.has(e.target).length === 0) {
        $languageSwitcher.removeClass("active");
        $trigger.attr("aria-expanded", "false");
      }
    });
    
    // Keyboard navigation
    $trigger.on("keydown", function(e) {
      if (e.which === 13 || e.which === 32) { // Enter or Space
        e.preventDefault();
        $trigger.click();
      } else if (e.which === 27) { // Escape
        e.preventDefault();
        $languageSwitcher.removeClass("active");
        $trigger.attr("aria-expanded", "false");
        $trigger.focus();
      }
    });
    
    // Close dropdown on language selection (mobile)
    $dropdown.find("a").on("click", function() {
      $languageSwitcher.removeClass("active");
      $trigger.attr("aria-expanded", "false");
    });
  });

  // ======== Click Outside to Close Menu ========
  $(document).on("click", function(e) {
    if (!$(e.target).closest(".navbar").length && $menu.hasClass("active")) {
      $menu.removeClass("active");
      $toggle.removeClass("open");
      $toggle.html(`<i class="${hamburgerIcon}"></i>`);
    }
  });

  // ======== Close Menu on Link Click (Mobile) ========
  $(".navbar__link").on("click", function() {
    if ($menu.hasClass("active") && $(window).width() <= mobileBreakpoint) {
      $menu.removeClass("active");
      $toggle.removeClass("open");
      $toggle.html(`<i class="${hamburgerIcon}"></i>`);
    }
  });
});
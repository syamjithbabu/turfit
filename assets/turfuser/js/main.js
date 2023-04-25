/* ==============
 ========= js documentation ==========================

 * theme name: Golftio
 * version: 1.0
 * description: Golf Club Html5 Template
 * author: Uiaxis
 * author url: https://themeforest.net/user/uiaxis

    ==================================================

     01. preloader
     -------------------------------------------------
     02. data background
     -------------------------------------------------
     03. navbar
     -------------------------------------------------
     04. window scroll
     -------------------------------------------------
     05. pricing tab
     -------------------------------------------------
     06. about tab
     -------------------------------------------------
     07. facility sidebar tab
     -------------------------------------------------
     08. training sidebar tab
     -------------------------------------------------
     09. pricing tab secondary
     -------------------------------------------------
     10. cart
     -------------------------------------------------
     11. payment method
     -------------------------------------------------
     12. faq tab
     -------------------------------------------------
     13. training details tab
     -------------------------------------------------
     14. reply
     -------------------------------------------------
     15. shop sidebar
     -------------------------------------------------
     16. shop range slider
     -------------------------------------------------
     17. product description tab
     -------------------------------------------------
     18. scroll to top with progress

    ==================================================
============== */

(function ($) {
  "use strict";

  jQuery(document).ready(function () {
    // preloader
    setTimeout(function () {
      $("#ctn-preloader").addClass("loaded");
      if ($("#ctn-preloader").hasClass("loaded")) {
        $("#preloader")
          .delay(1000)
          .queue(function () {
            $(this).remove();
          });
      }
    }, 1000);

    // data background
    $("[data-background]").each(function () {
      $(this).css(
        "background-image",
        "url(" + $(this).attr("data-background") + ")"
      );
    });

    // navbar
    $(".nav__bar").on("click", function () {
      $(this).toggleClass("nav__bar-toggle");
      $(".nav__menu").toggleClass("nav__menu-active");
      $(".backdrop").toggleClass("backdrop-active");
      $("body").toggleClass("body-active");
    });

    $(".backdrop, .nav__menu-close, .hide-nav").on("click", function () {
      $(".backdrop").removeClass("backdrop-active");
      $(".nav__bar").removeClass("nav__bar-toggle");
      $(".nav__menu").removeClass("nav__menu-active");
      $(".nav__dropdown").removeClass("nav__dropdown-active");
      $(".nav__menu-link--dropdown").next(".nav__dropdown").slideUp(500);
      $(".nav__menu-link--dropdown").removeClass(
        "nav__menu-link--dropdown-active"
      );
      $("body").removeClass("body-active");
    });

    $(window).on("resize", function () {
      $(".backdrop").removeClass("backdrop-active");
      $(".nav__bar").removeClass("nav__bar-toggle");
      $(".nav__menu").removeClass("nav__menu-active");
      $(".nav__dropdown").removeClass("nav__dropdown-active");
      $(".nav__menu-link--dropdown").removeClass(
        "nav__menu-link--dropdown-active"
      );
      $("body").removeClass("body-active");
      $(".ticket-modal").slideUp();
      $(".conference-modal").slideUp();
    });

    $(".nav__menu-link--dropdown").on("click", function () {
      $(this).next(".nav__dropdown").toggleClass("nav__dropdown-active");
      $(this).toggleClass("nav__menu-link--dropdown-active");
    });

    $(".nav__menu-link-childr").on("click", function () {
      $(this).next(".nav__dropdown-child").toggleClass("nav__dropdown-active");
      $(this).toggleClass("nav__menu-link--dropdown-active");
    });

    // on window scroll
    $(window).on("scroll", function () {
      // position navbar on scroll
      var scroll = $(window).scrollTop();
      if (scroll < 100) {
        $(".header").removeClass("header-active");
      } else {
        $(".header").addClass("header-active");
      }
    });

    // pricing tab
    $(".plan-table").hide();
    $(".plan-table:first").show();
    $(".plan-toggle").on("click", function () {
      $(".plan-toggle").removeClass("plan-active");
      $(this).addClass("plan-active");
      $(".plan-table").hide();
      var activePlan = $(this).attr("href");
      $(activePlan).fadeIn(500);
      return false;
    });

    // about tab
    $(".about--secondary__tabs-content").hide();
    $(".about--secondary__tabs-content:first").show();
    $(".about--secondary__tabs-btn").on("click", function () {
      $(".about--secondary__tabs-btn").removeClass(
        "about--secondary__tabs-btn-active"
      );
      $(this).addClass("about--secondary__tabs-btn-active");
      $(".about--secondary__tabs-content").hide();
      var activeGoal = $(this).attr("href");
      $(activeGoal).fadeIn(500);
      return false;
    });

    // facility sidebar tab
    $(".facility-tab-btn").on("click", function () {
      $(".facility-tab-btn").removeClass("facility-tab-btn-active");
      $(this).addClass("facility-tab-btn-active");
    });

    // training sidebar tab
    $(".training-tab-btn").on("click", function () {
      $(".training-tab-btn").removeClass("training-tab-btn-active");
      $(this).addClass("training-tab-btn-active");
    });

    // pricing tab secondary
    $(".plan-table-two").hide();
    $(".plan-table-two:first").show();
    $(".plan-toggle-two").on("click", function () {
      $(".plan-toggle-two").removeClass("plan-active-two");
      $(this).addClass("plan-active-two");
      $(".plan-table-two").hide();
      var activePlanTwo = $(this).attr("href");
      $(activePlanTwo).fadeIn(500);
      return false;
    });

    // cart
    let quantity = 0;
    let price = 0;
    $(".cart-item-quantity-amount, .product-quant").html(quantity);
    $(".total-price, .product-pri").html(price.toFixed(2));
    $(".cart-increment, .cart-incre").on("click", function () {
      if (quantity <= 4) {
        quantity++;
        $(".cart-item-quantity-amount, .product-quant").html(quantity);
        var basePrice = $(".base-price, .base-pri").text();
        $(".total-price, .product-pri").html((basePrice * quantity).toFixed(2));
      }
    });

    $(".cart-decrement, .cart-decre").on("click", function () {
      if (quantity >= 1) {
        quantity--;
        $(".cart-item-quantity-amount, .product-quant").html(quantity);
        var basePrice = $(".base-price, .base-pri").text();
        $(".total-price, .product-pri").html((basePrice * quantity).toFixed(2));
      }
    });

    $(".cart-item-remove>a").on("click", function () {
      $(this).closest(".cart-item").hide(300);
    });

    // payment method
    var paymentMethod = $("input[name='pay-method']:checked").val();
    $(".payment").html(paymentMethod);
    $(".checkout__radio-single").on("click", function () {
      var paymentMethod = $("input[name='pay-method']:checked").val();
      $(".payment").html(paymentMethod);
    });

    // faq tab
    $(".faq__tab-single").hide();
    $(".faq__tab-single:first").show();
    $(".faq-tab-btn").on("click", function () {
      $(".faq-tab-btn").removeClass("faq-tab-btn-active");
      $(this).addClass("faq-tab-btn-active");
      $(".faq__tab-single").hide();
      var activeFaq = $(this).attr("href");
      $(activeFaq).fadeIn(500);
      return false;
    });

    // training details tab
    $(".training__details-tab-single").hide();
    $(".training__details-tab-single:first").show();
    $(".training__details-tab-btn").on("click", function () {
      $(".training__details-tab-btn").removeClass(
        "training__details-tab-btn-active"
      );
      $(this).addClass("training__details-tab-btn-active");
      $(".training__details-tab-single").hide();
      var activetrainingDetails = $(this).attr("href");
      $(activetrainingDetails).fadeIn(500);
      return false;
    });

    // reply
    $(".reply").on("click", function () {
      $(this)
        .closest(".blog-comment__content")
        .children(".blog-comment__author")
        .children(".author-active")
        .toggleClass("author-active-bg");
      $(this).toggleClass("reply-active");
      $(this).parent().next(".blog-comment-reply").slideToggle();
    });

    // shop sidebar
    $(".shop__sidebar-head").on("click", function () {
      $(this).next(".shop__sidebar-content").slideToggle();
    });

    // shop range slider
    $(function () {
      $("#slider-range").slider({
        range: true,
        min: 0,
        max: 1000,
        values: [100, 1000],
        slide: function (event, ui) {
          $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        },
      });
      $("#amount").val(
        "$" +
          $("#slider-range").slider("values", 0) +
          " - $" +
          $("#slider-range").slider("values", 1)
      );
    });

    // product description tab
    $(".product-description-tab-single").hide();
    $(".product-description-tab-single:first").show();
    $(".product-description-tab-btn").on("click", function () {
      $(".product-description-tab-btn").removeClass(
        "product-description-tab-btn-active"
      );
      $(this).addClass("product-description-tab-btn-active");
      $(".product-description-tab-single").hide();
      var activeDescription = $(this).attr("href");
      $(activeDescription).fadeIn(500);
      return false;
    });

    // copyright year
    $("#copyYear").text(new Date().getFullYear());

    // scroll to top with progress
    var progressPath = document.querySelector(".progress-wrap path");
    var pathLength = progressPath.getTotalLength();
    progressPath.style.transition = progressPath.style.WebkitTransition =
      "none";
    progressPath.style.strokeDasharray = pathLength + " " + pathLength;
    progressPath.style.strokeDashoffset = pathLength;
    progressPath.getBoundingClientRect();
    progressPath.style.transition = progressPath.style.WebkitTransition =
      "stroke-dashoffset 10ms linear";
    var updateProgress = function () {
      var scroll = $(window).scrollTop();
      var height = $(document).height() - $(window).height();
      var progress = pathLength - (scroll * pathLength) / height;
      progressPath.style.strokeDashoffset = progress;
    };
    updateProgress();
    $(window).scroll(updateProgress);
    var offset = 50;
    var duration = 550;
    jQuery(window).on("scroll", function () {
      if (jQuery(this).scrollTop() > offset) {
        jQuery(".progress-wrap").addClass("active-progress");
      } else {
        jQuery(".progress-wrap").removeClass("active-progress");
      }
    });
    jQuery(".progress-wrap").on("click", function (event) {
      event.preventDefault();
      jQuery("html, body").animate({ scrollTop: 0 }, duration);
      return false;
    });
  });
})(jQuery);

$(".mobile__nav__btn").click(function() {
    $('.mobile__nav__main').addClass("active")
    $('body').addClass("hidden")
});

$(".menu__close").click(function() {
    $('.mobile__nav__main').removeClass("active")
    $('body').removeClass("hidden")
})

$("#list__lamp__item").hover(function() {
    console.log('you hover it')
    $(".nav__fixed").addClass("active");
}, function() {
    // console.log('not hover a')
    // if ($(".nav__category__lamps").is(":focus")) {
    //     window.alert('in focus');
    //   }
    $(".nav__fixed").removeClass("active");
})

$(".mobile__nav__listview__icon").click(function() {
    $(".mobile__nav__main").addClass("hide")
    target = $(this).data("target")
    // console.log($(target))
    $(target).addClass("show")
})

$(".mobile__nav__btn__previous").click(function() {
    $(".mobile__submenu").removeClass("show")
    $(".mobile__nav__main").removeClass("hide")
})

$(".menu__trigger").click(function() {
    $("body").addClass("hidden")
    $(".mobile__nav__blocker").addClass("show")
    $(".mobile__nav").addClass("show");
})

$(".mobile__nav__blocker").click(function() {
    $("body").removeClass("hidden")
    $(".mobile__nav").removeClass("show");
    $(".mobile__nav__blocker").removeClass("show")
})











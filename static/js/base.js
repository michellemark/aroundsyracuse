var page_effects = (function () {

    return {
        setup_page: function () {
            $('.dropdown-toggle').dropdown();
        }
    };
}(page_effects || {}));


$.when($.ready).then(function () {
    page_effects.setup_page();
});

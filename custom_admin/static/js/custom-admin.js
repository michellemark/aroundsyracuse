var admin_setup = (function () {
    var ping_google_button = $("#ping_google");
    var ping_google_response = $("#ping_google_response");

    return {
        setup_page: function () {
            ping_google_button.on("click touchstart", function (e) {
                e.preventDefault();

                $.ajax({
                    url: "/custom-admin/ping-google/",
                    type: "GET",
                    cache: false,
                }).done(function () {
                    ping_google_response.empty();
                    ping_google_response.attr("class", "alert alert-secondary");
                    ping_google_response.append(
                        "A request has been sent to Google to crawl the updated sitemap."
                    );
                });
            });
        }
    };
}(admin_setup || {}));

$(window).on("load", function () {
    admin_setup.setup_page();
});

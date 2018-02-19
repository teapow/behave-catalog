$(document).ready(function() {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    $("#search").on("input", $.debounce(150, function() {
        var search_term = this.value.toLowerCase();
        var steps = $(".list-group-item");

        if (search_term === "") {
            steps.show();
        } else {
            var matching_steps = steps.filter(function(index) {
                var step = $(steps[index]);
                var step_text = $.trim(step.find("a").first().text()).toLowerCase();

                return step_text && step_text.indexOf(search_term) >= 0;
            });

            steps.hide();
            matching_steps.show();
        }
    }));

    $(".nav-link").each(function() {
        var href = $(this).attr("href");

        $(this).click(function() {
            var target = $(href).offset().top - 64;  // Adjust for header.
            $("html, body").animate({scrollTop: target}, 500);

            return false;
        });
    });
});

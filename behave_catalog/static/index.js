$(document).ready(function() {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    $("#search").on("input", $.debounce(150, function() {
        var searchTerm = this.value.toLowerCase();
        var steps = $(".list-group-item");

        if (searchTerm === "") {
            steps.show();
        } else {
            var matchingSteps = steps.filter(function(index) {
                var step = $(steps[index]);
                var stepText = $.trim(step.find("a").first().text()).toLowerCase();

                return stepText && stepText.indexOf(searchTerm) >= 0;
            });

            steps.hide();
            matchingSteps.show();
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

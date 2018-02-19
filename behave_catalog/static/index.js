$(document).ready(function() {
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    $("#search").on("input", $.debounce(150, function() {
        var search_term = this.value;
        var steps = $(".list-group-item");

        var matching_steps = steps.filter(function(index) {
            var step = steps[index].find("a");
            console.log("filtering", step, search_term);
            return this.value === value;
        });
    }));
});

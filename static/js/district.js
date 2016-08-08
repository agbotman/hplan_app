var DISTRICTS = {};

function fill_districts(country_id) {
    if (DISTRICTS[country_id]) {
        $("#id_district").html(DISTRICTS[country_id]);
    } else {
        $.getJSON("/districts_for_country/", {country_id: country_id},
            function(ret, textStatus) {
            var distr = ret.districts;
            var options = '<option value="" selected="selected">---------</option>';
            for (var i in distr) {
                options += '<option value="' + distr[i].id + '">'
                  + distr[i].name + '</option>';
            }
            DISTRICTS[country_id] = options;
            $("#id_district").html(options);
        });
    }
}

$(document).ready(function() {
  $("#id_country").change(function() { fill_districts($(this).val()); });
});
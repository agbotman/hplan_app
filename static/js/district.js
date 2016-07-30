var response_cache = {};

function fill_districts(country_id) {
  if (response_cache[country_id]) {
    $("#id_district").html(response_cache[country_id]);
  } else {
      $.getJSON("/districts_for_country/", {country_id: country_id},
      function(ret, textStatus) {
        var options = '<option value="" selected="selected">---------</option>';
        for (var i in ret) {
          options += '<option value="' + ret[i].id + '">'
            + ret[i].name + '</option>';
        }
        response_cache[country_id] = options;
        $("#id_district").html(options);
      });
  }
}

$(document).ready(function() {
  $("#id_country").change(function() { fill_districts($(this).val()); });
});
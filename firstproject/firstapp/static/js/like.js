$(function () {
  $("#like_button").click(function () {
    $.ajax({
      url: $(this).data("url"),
      type: "POST",
      dataType: "json",
      data: {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response) {
        if (response.success) {
          $('#like_count').text(response.likes_count);
        } else {
          alert(response.message);
        }
      }
    });
  });
});
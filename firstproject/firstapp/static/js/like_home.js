function like () {
  $(".like_button").click(function () {
    var button = $(this);
    var post_id = button.data("post-id");
    $.ajax({
      url: button.data("url"),
      type: "POST",
      dataType: "json",
      data: {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response) {
        if (response.success) {
          $('#like_count_' + post_id).text(response.likes_count);
        } else {
          alert(response.message);
        }
      }
    });
  });
};

$(document).ready(function() {
    like()
    })

$(function () {
  $("#submit_comment").click(function () {
    $.ajax({
      url: $(this).data("url"),
      type: "POST",
      dataType: "json",
      data: {
        csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
        text: $("textarea#id_text").val(),
      },
      success: function(response) {
        $('#comment_info').html(response)
      }
    });
  });
});

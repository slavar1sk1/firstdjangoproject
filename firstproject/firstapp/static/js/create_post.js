$(function() {
  $('#submit').click(function() {
    var url = $(this).data('url');
    var formData = new FormData($('#window_post form')[0]);

    $.ajax({
      url: url,
      type: 'POST',
      dataType: 'json',
      data: formData,
      processData: false,
      contentType: false,
      success: function(response) {
        $('#posts_list').html(response);
        document.getElementById('window_post').close();
      },
      error: function(xhr, status, error) {
        console.error(xhr.responseText);
        document.getElementById('window_post').close();
      }
    });
  });
});

$(function() {
  $('#create_post').click(function() {
    document.getElementById('window_post').showModal();
  });
})
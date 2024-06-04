$(function() {
  $('#submit').click(function() {
    var url = $(this).data('url');
    var text = $('textarea#id_text').val();
    $.ajax({
      url: url,
      type: 'POST',
      dataType: 'json',
      data: {
        'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
        'text': text
      },
      success: function(response) {
        console.log(response);
      },
      error: function(xhr, status, error) {
        console.error(xhr.responseText);
      }
    });
  });
});


$(function() {
  $('#create_post').click(function() {
    document.getElementById('window_post').showModal();
  })
})
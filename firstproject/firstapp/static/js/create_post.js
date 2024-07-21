

$(function() {
  $('#create_post').click(function() {
    document.getElementById('window_post').showModal();
  });
})


htmx.on('htmx:afterSwap', function() {
    document.getElementById('window_post').close();
    like()
    })
$('#create').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: 'add_note',
        method: 'POST',
        data: $(this).serialize(),
        success: function (serverResponse) {
            console.log('before the html update')
            $('.notes-div').html(serverResponse)
            console.log('i think i made changes')
        }
    })
    $(this).trigger('reset')
})

$('#container').on("click", 'a', function (e) {
    e.preventDefault();
    // e.stopPropagation();
    $.ajax({
        url: '/delete/' + $(this).attr('note_id'),
        method: 'GET',
        success: function (serverResponse) {
            console.log('trying to delete')
            $(".notes-div").html(serverResponse);
            console.log('it actually deleted')
        }
    })
})

function delay(callback, ms) {
  var timer = 0;
  return function () {
    var context = this,
      args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      callback.apply(context, args);
    }, ms || 0);
  };
}

$("#container").on('keyup', "form", delay(function (e) {
    $.ajax({
      url: "update_note",
      method: "POST",
      data: $(this).serialize(),
        success: function (serverResponse) {
            console.log("try to update the description");
            $(".notes-div").html(serverResponse);
            console.log("completed updating the description");
      },
    });
    console.log("Time elapsed!", this.value);
  }, 1000)
);

// $('#container').on("keyup", "form", delay(function (e) {
//     e.preventDefault();

//     $.ajax({
//         url: 'update_note',
//         method: 'POST',
//         data: $(this).serialize(),
//         success: function (serverResponse) {
//             console.log('try to update the description')
//             $('.notes-div').html(serverResponse)
//             console.log("completed updating the description");
//         }
//     })
// }, 500))


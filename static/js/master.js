$(".menu").click(function () {
    $(this).toggleClass('open');
    $('#navigation').toggleClass('open');
    $('body, html').toggleClass('fixed');
});


$('.send a').click(function (e) {
    e.preventDefault();
    if ($('.send textarea').val() !== '') {
        let massage = $('.send textarea').val();
        $.ajax({
            type: 'POST',
            url: "contact_us",
            data: {
                massege: massage,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                if (data == 'ok') {
                    $('.send a').text('Отправлено');
                    $('.send textarea').val('Отправлено').prop('disabled', true).css('pointer-events', 'none');
                } else {
                    $('.send a').text('Не отправлено');
                    $('.send textarea').val('Не отправлено').prop('disabled', true).css('pointer-events', 'none');
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
                alert('error');
            }
        });
    }
});

$('a.form').click(function (e) {
    e.preventDefault();
    $('.overlay').addClass('active');
    $('body, html').toggleClass('fixed');
    const modal = $('.overlay .modal');
    modal.animate({opacity: '1', top: '100px'}, {duration: 100});
    //modal.animate({top: '0px', opacity: '1'}, "slow");
    $('.overlay svg').click(function () {
        $('.overlay').removeClass('active');
        $('body, html').removeClass('fixed');
    });
    $('.overlay .modal a.send').click(function (e) {
        e.preventDefault();

        let name = $('.overlay .modal input.name').val(),
            email = $('.overlay .modal input.email').val(),
            massage = $('.overlay .modal input.items').val();
        if ((name !== '') &&
            (email !== '') && (massage !== '')
        ) {
            $.ajax({
                type: 'POST',
                url: "request",
                data: {
                    name: name,
                    email: email,
                    massage: massage,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    if (data == 'ok') {
                        modal.animate({opacity: '0', top: '-100px'}, {duration: 100});
                        $('.overlay').css('background', "#000");
                        $('.overlay .msg').addClass('active');

                        setTimeout(function () {
                            $('body, html').removeClass('fixed');
                            $('.overlay').removeClass('active');
                            $('.overlay .msg').removeClass('active');
                        }, 2000);
                    } else {
                        alert(1);
                    }
                },
                error: function (xhr, errmsg, err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                    alert('error');
                }
            });
        } else {
            $('.overlay .modal').addClass('wrong');
        }

    });

});
$('.tv-box .more-info').click(function (e) {
    e.preventDefault();
    $('.tv-box').toggleClass('open');

});

if (localStorage.getItem('pressed')) {

} else {
    let some;
    some = $("#cookie");
    some.animate({opacity: '1', bottom: '0'}, {duration: 1000});
    some.children('span').click(function () {
        some.animate({opacity: '0', bottom: '-100%'}, {duration: 1000});
        localStorage.setItem('pressed', 'true');
    });
}


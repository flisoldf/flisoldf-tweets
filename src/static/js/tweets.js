var ajax = "";
$(function(){
    retorna_tweets(1);
    $('#tweets-box').data('pagina', 1);

});

function inicializa_scroll(){
    $('#tweets-box').scroll(function() {
    if(($('#tweets-box').scrollTop() + $('#tweets-box').height() + 400) >= $('#tweets_box').height()) {
        $('#tweets-box').unbind('scroll');
        ajax.abort();
        retorna_tweets($('#tweets-box').data('pagina'));
    }
    });
}

function retorna_tweets(pagina){
    $('#tweets-box').append('<li class="carregando">Aguarde, carregando...</li>');
    var url = "/list_ajax";

    $('#tweets-box').data('pagina', pagina + 1);

    ajax = $.ajax({
        url: url,
        dataType: 'json',
        data: {page:pagina},
        success: function(tweets){
            $('.carregando').fadeOut(function(){
                if(pagina >= 1) {
                    for(x in tweets) {
                        $('#tweets-box').append(
                            '<div class="tweet" id="tweet_'+tweets[x].id_str+'"><div class="tweet-image">'+
                            '<img src="'+tweets[x].profile_image_url+'" alt="" />'+
                            '</div>'+
                            '<div class="tweet-row">'+
                            '<a href="http://www.twitter.com/"'+tweets[x].from_user+'">'+tweets[x].from_user_name+'</a>'+
                            '<p class="tweet-text">'+tweets[x].text+'</p>'+
                            '</div>'+
                            '</div>'
                        );

                    }
                }
               $(this).remove();
            });
        },
        timeout: 5000
    });
}


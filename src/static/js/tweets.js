/*
 * Função que efetua a requisição dos últimos tweets
 * que usam a hashtag #flisol, com os conteúdos totalmente
 * formatados (links, usernames, hashtags).
 *
 * pagina: número da página a ser pesquisada (padrão: 1)
 */
function retorna_tweets(pagina){
    //Oculta o link 'Mais Tweets'
    $('#carrega-tweets').hide();

    //Insere a mensagem de carregando
    $('#tweets-rows').append('<li class="carregando">Aguarde, carregando...</li>');

    $.ajax({
        url: "/list_ajax",
        dataType: 'json',
        data: {page:pagina},
        timeout: 2000,
        cache: false,
        success: function(tweets){
            $('.carregando').fadeOut(function(){
                //Iterando os tweets e inserindo em uma div
                for(x in tweets) {
                    $('#tweets-rows').append(
                        '<div class="tweet" id="tweet_'+tweets[x].id_str+'"><div class="tweet-image">'+
                        '<img src="'+tweets[x].profile_image_url+'" alt="" />'+
                        '</div>'+
                        '<div class="tweet-row">'+
                        '<a href="http://www.twitter.com/'+tweets[x].from_user+'">'+tweets[x].from_user_name+'</a>'+
                        '<p class="tweet-text">'+tweets[x].text+'</p>'+
                        '</div>'+
                        '</div>'
                    );
                }

                // Remove a mensagem de carregando a acrescenta mais um
                // no atributo data-pagina do link 'Mais Tweets'.
                $(this).remove();
                $('#carrega-tweets').data('pagina', pagina + 1).fadeIn();
            });
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Ocorreu um erro: "+ errorThrown);
        }
    });
}


$(function(){
    retorna_tweets(1);
    /*
    * Evento que ao clicar no link 'Mais Tweets' será
    * requisitado os tweets mais antigos.
    */
    $('#carrega-tweets').click(function(e){
        retorna_tweets($(this).data('pagina'));
        e.preventDefault();
    });
});

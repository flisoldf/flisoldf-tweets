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
    $('#tweets-rows').append('<li class="carregando">Aguarde. Carregando...</li>');

    $.ajax({
        type: "GET",
        url: "/list_ajax",
        dataType: 'json',
        data: {page:pagina},
        cache: false,
        success: function(tweets){
            $('.carregando').fadeOut(function(){
                //Iterando os tweets e inserindo em uma div
                if (pagina = 1) {
                    $('.tweet').remove();
                    for(x in tweets) {
                        render_tweet(tweets, x);
                    }
                }

                // Remove a mensagem de carregando a acrescenta mais um
                // no atributo data-pagina do link 'Mais Tweets'.
                $(this).remove();
                $('#carrega-tweets').data('pagina', pagina + 1).fadeIn();
            });
        },
        complete: function(){
            setTimeout('retorna_tweets(1)', 30000);
        }
    });
}

/*
 * Função que constrói o bloco do tweet e recebe
 * os dados para renderização.
 *
 * tweet - Dados do tweet
 * ind - Indice do loop
 */
function render_tweet(tweet, ind) {
    $('#tweets-rows').append(
        '<div class="tweet" id="tweet_'+tweet[ind].id_str+'">'+
            '<div class="tweet-image">'+
                '<img src="'+tweet[ind].profile_image_url+'" alt="" />'+
            '</div>'+
            '<div class="tweet-row">'+
                '<a href="http://www.twitter.com/'+tweet[ind].from_user+'">'+tweet[ind].from_user_name+'</a>'+
                '<p class="tweet-text">'+tweet[ind].text+'</p>'+
                '<div class="tweet-properties">'+
                    '<ul>'+
                        '<li><span id="retweet_'+tweet[ind].id_str+'"></span></li>'+
                        '<li><span class="tweet-date">'+tweet[ind].created_at+'</span></li>'+
                    '</ul>'+
                '</div>'+
            '</div>'+
        '</div>'
    );
    $('#retweet_'+tweet[ind].id_str).customRetweet({
        url: '',
        account: tweet[ind].from_user,
        title: tweet[ind].retweet,
        retweetTemplate: 'RT @{{account}} {{title}}',
        template: '<a href="{{retweetURL}}">Retweet</a>'
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

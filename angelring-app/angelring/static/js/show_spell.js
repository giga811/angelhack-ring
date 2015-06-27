// reset spell. calls api
function reset_spell(){
    $.get('/spell/reset_spell');
    console.log("#Reset spell.")
}

function sp_spell(spell){
    var myHtml = 'Spell Casted: ' + spell + '<br>';
    console.log(spell)
    $('#result').prepend(myHtml);
}

function show_current_spell(spell){
    var out = $("#current_spell")
    out.empty();

    for (var i = 0; i < spell.length; i++) {
      var html = '<img src="/img/spell/' + spell[i] +  '.png">';
      out.append(html);
    }
}

$(document).ready(function(){
    $.PeriodicalUpdater('/spell/get_spell', {
    //  オプション設定
        //url: '',  // 送信リクエストURL
        minTimeout: 1000,    // 送信インターバル(ミリ秒)
//      method               // 'post'/'get'：リクエストメソッド
//      sendData             // 送信データ
//      maxTimeout           // 最長のリクエスト間隔(ミリ秒)
        multiplier: 1           // リクエスト間隔の変更(2に設定の場合、レスポンス内容に変更がないときは、リクエスト間隔が2倍になっていく)
//      type                 // xml、json、scriptもしくはhtml (jquery.getやjquery.postのdataType)
    },
    function(data){
        show_current_spell(data);

        // if spell is special
        if (data.length == 1){
            switch (data){
              case "a":
                sp_spell(data);
                reset_spell();
                break;
              case "b":
                sp_spell(data);
                reset_spell();
                break;
              case "c":
                sp_spell(data);
                reset_spell();
                break;
            }
        }

        // if spell length is 3
        if (data.length == 3){
            // do spell
            sp_spell(data);

            reset_spell();
        }

        // if spell length is more than 3
        if (data.length > 3){
            reset_spell();
        }

    });
})


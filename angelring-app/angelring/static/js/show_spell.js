// reset spell. calls api
// and animate out
function reset_spell(){
    $.get('/spell/reset_spell');
    console.log("#Reset spell.");
}

function sp_spell(spell){
    var myHtml = 'Spell Casted: ' + spell + '<br>';

    $('#result').prepend(myHtml);
    console.log("#Spell casted: " + spell);

    // if monalisa
    if (spell == "133"){
        console.log("item-1");
        $('#museum-info').hide();
        $('#item-1').show();
        $('#item-2').hide();
    }
    if (spell == "135"){
        console.log("item-2");
        $('#museum-info').hide();
        $('#item-1').hide();
        $('#item-2').show();
    }
    if ( spell == "a"){
        $('#item-info').show();
        $('#item-video').hide();
    }
    if ( spell == "b"){
        $('#item-info').hide();
        $('#item-video').show();
    }
}

function show_current_spell(spell){
    var out = $("#current_spell")
    out.empty();

    for (var i = 0; i < spell.length; i++) {
      var html = '<img id="spell_image" src="/img/stone/' + spell[i] +  '.png">';
      out.append(html);
    }
}

function animate_in_spell(data){

    $('#stones').fadeIn();
    if (data.length == 0){
        $("#stone1").hide();
        $("#stone2").hide();
        $("#stone3").hide();
    }
    if (data.length == 1){
        $("#stone1").attr('src','/img/stone/' + data[0] + '.png');
        $("#stone1").fadeIn("slow");
    }
    if (data.length == 2){
        $("#stone2").attr('src','/img/stone/' + data[1] + '.png');
        $("#stone2").fadeIn("slow");
    }
    if (data.length == 3){
        $("#stone3").attr('src','/img/stone/' + data[2] + '.png');
        $("#stone3").fadeIn("slow");
    }

}

function animate_out_spell(data){

    var div = $("#stones")
    div.animate({margin: '50px'}, "slow");
    div.animate({fontSize: '3em'}, "slow");
    if (data.length >= 1){
        $("#stone1").attr('src','/img/stone/' + data[0] + '-l.png');
    }
    if (data.length >= 2){
        $("#stone2").attr('src','/img/stone/' + data[1] + '-l.png');
    }
    if (data.length == 3){
        $("#stone3").attr('src','/img/stone/' + data[2] + '-l.png');
    }
    $("#stones").fadeOut("slow");


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
        console.log(data);
        show_current_spell(data);

        animate_in_spell(data);

        // if spell is special
        if (data.length == 1){
            switch (data){
              case "a":
                sp_spell(data);
                animate_out_spell(data);
                reset_spell();
                break;
              case "b":
                sp_spell(data);
                animate_out_spell(data);
                reset_spell();
                break;
              case "c":
                sp_spell(data);
                animate_out_spell(data);
                reset_spell();
                break;
            }
        }

        // if spell length is 3
        if (data.length == 3){
            // do spell
            sp_spell(data);
            animate_out_spell(data);
            reset_spell();
        }

        // if spell length is more than 3
        if (data.length > 3){
            animate_out_spell(data);
            reset_spell();
        }

    });
})


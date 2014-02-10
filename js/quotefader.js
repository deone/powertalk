function fadeQuotes()   {
    $(".mast .quote_1").fadeIn().delay(4000).fadeOut();
    $(".mast .quote_2").delay(5000).fadeIn(1000).delay(4000).fadeOut();
    $(".mast .quote_3").delay(11000).fadeIn(1000).delay(4000).fadeOut();
    setTimeout("fadeQuotes()", 17000);
}

$(function()    {

    fadeQuotes();

});

document.onreadystatechange=function(){
    if(document.readyState=="complete"){
        preloader.style.display="none";
    }
}
$(document).ready(function(){
    $(".search").click(function(){
        $(".searchinput").css({
            "display":"inline-block"
        })
        $(".inputclose").css({
            "display":"inline-block"
        })
    })
    $(".inputclose").click(function(){
        $(".searchinput").css({
            "display":"none"
        })
        $(this).css({
            "display":"none"
        })
    })
    $(".firstsection").click(function(){
        $(".searchinput").css({
            "display":"none"
        })
        $(".inputclose").css({
            "display":"none"
        })
    })
    $(".imgItem").click(function(){
        $(".showlayout").css({
            "opacity": "1",
            "z-index": "99999"
        })
        $(this).children().attr("src")
        $(".showimg").attr("src", $(this).children().attr("src"))
        $(".close").click(function(){
            $(".showlayout").css({
                "opacity": "0",
                "z-index": "-99999"
            })
        })
    })
    $(".imgItem").click(function(){
        $(this).attr("data-index")
        $(".active").removeClass("active")
        $(".itemDiv").eq($(this).attr("data-index")).addClass("active")
     })
   
     
})
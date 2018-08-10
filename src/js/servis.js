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

    
     
})
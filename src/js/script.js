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
    $(".menuicn").click(function(){
        $(this).css({
            "display":"none"
        })
        $(".menulayout").css({
            "width":"100%",
            "height":"auto"
        })
        $(".cancel").css({
            "display":"block",
        })
    })
    $(".cancel").click(function(){
        $(".menulayout").animate({
            "width":"0"
        }, 1700, function(){
            $(".menulayout").css({
                "height":"0"
            })
        })
        $(this).css({
            "display":"none"
        })
        $(".menuicn").css({
            "display":"block"
        })
    })
        // let shareclick=document.querySelector(".shareclick");
        // let shareDiv=document.querySelector(".shareDiv");
        // shareclick.onclick=function(){
        //         if(shareDiv.style.display=="inline-block"){
        //             shareDiv.style.display="none";
        //         }
        //         else{
        //             shareDiv.style.display="inline-block";
        //         }
                
        //     }
            
           



 });
console.log(document.getElementById("bi-pause-fill"));

// play pause button
document.getElementById("player").onclick = function () {
    const player = document.getElementById("player");
    if (player.value == 'play') {
        eel.play()(function(param){					
            document.querySelector(".status").innerHTML = param;
            player.innerHTML = '<path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5zm5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5z"/>'
        })
        player.value='pause';
    } else {
        eel.pause()(function(param){	
            document.querySelector(".status").innerHTML = param;
            player.innerHTML = '<path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>'		
        })
        player.value='play';
    }
}

document.getElementById("vol_up").onclick = function () {
    eel.vol_up()(function(param){					
        document.querySelector(".status").innerHTML = param;
    })
}

document.getElementById("vol_down").onclick = function () {
    eel.vol_down()(function(param){					
        document.querySelector(".status").innerHTML = param;
    })
}

document.getElementById("next").onclick = function () {
    eel.next()(function(param){			
        // updates the status and header on song change		
        document.querySelector(".status").innerHTML = param[1];
        document.querySelector(".header").innerHTML = param[0];
    })
}

document.getElementById("previous").onclick = function () {
    eel.previous()(function(param){
        // updates the status and header on song change
        document.querySelector(".status").innerHTML = param[1];
        document.querySelector(".header").innerHTML = param[0];
    })
}

// updates header on auto song change
eel.expose(name_update);
function name_update(param) {
    document.querySelector(".header").innerHTML = param;
}

eel.expose(time);
function time(param) {
    document.getElementById("myRange").value = param;
}
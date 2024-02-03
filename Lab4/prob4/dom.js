function makeChanges() {
    var images = document.getElementsByTagName("img");
    for (let i = 0; i < images.length; i++) {
        images[i].src = 'timepass.png';
    }

    var h1Elements = document.getElementsByTagName("h1");
    for (let i = 0; i < h1Elements.length; i++) {
        h1Elements[i].remove();
    }

    var pElements = document.getElementsByTagName("p");
    for (var i = 0; i < pElements.length; i++) {
        pElements[i].innerHTML = "Enough of Javascript, let's stop";
    }

    var h2Elements = document.getElementsByTagName("h2");
    for (let i = 0; i < pElements.length; i++) {
        h2Elements[i].innerHTML = h2Elements[i].innerHTML.toUpperCase();
    }

    document.getElementById("div1").innerHTML = "<h3></h3>";
}

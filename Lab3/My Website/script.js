function show_home(){
    let header=document.getElementById("header")
    header.className="home_header";
    header.innerHTML="Welcome to my Personal Website :)";

    document.getElementById("body").className="home_body"

    document.getElementById("hobbies_content").style.display='none' ;
    document.getElementById("home_content").style.display='block';
}
function show_hobbies(){
    let header=document.getElementById("header")
    header.className="hobbies_header";
    header.innerHTML="My Hobbies (^^)";

    document.getElementById("body").className="hobbies_body"

    document.getElementById("home_content").style.display='none';
    document.getElementById("hobbies_content").style.display='block';
}
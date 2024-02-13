window.onload=show_home
function show_home(){
    let header=document.getElementById("header")
    header.className="home_header";
    header.innerHTML="Welcome to my Personal Website :)";

    document.getElementById("body").className="home_body"

    document.getElementById("home_content").style.display='block';
    document.getElementById("hobbies_content").style.display='none' ;
    document.getElementById("achievements_content").style.display='none';
}
function show_hobbies(){
    let header=document.getElementById("header")
    header.className="hobbies_header";
    header.innerHTML="My Hobbies (^^)";

    document.getElementById("body").className="hobbies_body"

    document.getElementById("home_content").style.display='none';
    document.getElementById("hobbies_content").style.display='block';
    document.getElementById("achievements_content").style.display='none';
}
function show_achievements(){
    let header=document.getElementById("header")
    header.className="achievements_header";
    header.innerHTML="|My Achievements|";

    document.getElementById("body").className="achievements_body"

    document.getElementById("home_content").style.display='none';
    document.getElementById("hobbies_content").style.display='none';
    document.getElementById("achievements_content").style.display='block';
}
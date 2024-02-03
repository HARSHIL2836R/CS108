function validateName() {
    /*Check whether name is entered or not.
    Throw an error if name field is empty.
    Error message will be "Full name is required."*/
    let pattern = /^(.+)$/;
    let name=document.getElementById('fullName').value;
    let result=pattern.test(name);
    if (!result) {
        throw "Error: Full name is required.";
    }
}

function validateEmail() {
    /*Check whether email is valid or not, as per the rules stated in problem statement.
    Use regex and test() function to validate the email address.
    Throw an error if email is invalid.
    Error message will be "Invalid Email Address."*/
    let pattern = /^([0-9a-z]+@{1}[a-z]+\.[a-z]{3})$/;
    let name=document.getElementById('email').value;
    let result=pattern.test(name);
    if (!result) {
        throw "Error: Invalid Email Address.";
    }
}

function validatePassword() {
    /*Check whether password is made of atleast 8 characters.
    /If not, throw an error.
    Error message will be "Password must be at least 8 characters"*/
    let pattern = /^(.{8,})$/;
    let name=document.getElementById('password').value;
    let result=pattern.test(name);
    if (!result) {
        throw "Error: Password must be at least 8 characters";
    }
}

function ConfirmPassword() {
    /*Check whether the re-entered password is same as the password entered first.
    If not, throw an error.
    Error message will be "Passwords do not match"*/
    if (document.getElementById('password').value != document.getElementById('confirmPassword').value){
        throw "Error: Passwords do not match.";
    }
}

function validateForm() {
    try {

        /*Check whether all fields are entered or not*/
        var fields=['fullName','email','password','confirmPassword']
        for (let i=0;i<4;i++){
            let fname = fields[i];
            let pattern = /^(.+)$/;
            if(!pattern.test(document.getElementById(fname).value)){
                throw "Error: All fields are required."
            }
        }

        validateName();
        validateEmail();
        validatePassword();
        ConfirmPassword();

        // Additional validation rules can be added here

        //After checking all the rules, if the program throws no error, it will reach this part of code.
        //Using "innerHTML" and "span" tag, give the message "Registration successful!" in GREEN colour to the div container "feedback" in index.html.
        document.getElementById('feedback').innerHTML='<span style="color: green;">Registration successful!</span>';
    } catch (error) {
        //After checking all the rules, if the program throws an error, it will reach this part of code.
        //Using "innerHTML" and "span" tag, give the error message in RED colour to the div container "feedback" in index.html.
        document.getElementById('feedback').innerHTML='<span style="color: red;">'+error+'</span>';
    }
}

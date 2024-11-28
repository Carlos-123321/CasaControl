document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('loginButton').addEventListener('click', function(event) {
        event.preventDefault();

        var username = document.getElementById('usernameInputBox').value;
        var password = document.getElementById('passwordInputBox').value;

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'username': username,
                'password': password
            })
        })
        .then(response => {
            if (response.ok) {
                window.location.href = "/";
            } else {
                alert("Invalid username or password");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

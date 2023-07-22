// This code is used to validate the form data before submitting it to the server.
function validateForm() {
    // Check if the username field is empty.
    if (document.getElementById("firstname").value == "") {
      alert("Please enter a firstname.");
      return false;
    }

    if (document.getElementById("lastname").value == "") {
      alert("Please enter a lastname.");
      return false;
    }
    
    // Check if the password field is empty.
    if (document.getElementById("password").value == "") {
      alert("Please enter a password.");
      return false;
    }
    // The form data is valid, so submit it to the server.
    return true;
  }

  
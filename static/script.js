document.getElementById("registrationForm").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent the form from submitting normally

    // Collect form data
    const formData = new FormData(this);

    // Clear previous error messages
    document.querySelectorAll(".error").forEach((el) => (el.textContent = ""));

    // Send data to the server via fetch
    fetch("/submit", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.status === "error") {
                // Display errors
                for (const key in data.errors) {
                    document.getElementById(`${key}Error`).textContent = data.errors[key];
                }
            } else {
                alert(data.message); // Success message
                document.getElementById("registrationForm").reset(); // Reset the form
            }
        })
        .catch((error) => console.error("Error:", error));
});

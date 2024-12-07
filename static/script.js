function sendMessage() {
    const message = document.getElementById("user-input").value.trim();
    const language = document.getElementById("language-select").value;
    if (message === "") return;

    // Display user's message
    displayMessage(message, "user-message");

    // Clear the input field
    document.getElementById("user-input").value = "";

    // Show "Bot is typing..." indicator
    showTypingIndicator();

    // Send to server for processing
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message, language: language })
    })
        .then(response => response.json())
        .then(data => {
            removeTypingIndicator();

            // Display the Tokens
            displayMessage(`Tokens: ${data.tokens.join(", ")}`, "bot-message");

            // Display the Language info
            const langInfo = data.language_info;
            displayMessage(
                `Language: ${langInfo.name} | Region: ${langInfo.region}`,
                "bot-message"
            );

            // Finally display the Sentence Translation
            displayMessage(`Sentence Translation: ${data.sentence_translation}`, "bot-message");
        })
        .catch(error => {
            removeTypingIndicator();
            console.error("Error:", error);
            displayMessage("Sorry, an error occurred.", "bot-message");
        });
}

function displayMessage(message, className) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", className);
    messageElement.textContent = message;
    document.getElementById("chat-box").appendChild(messageElement);
    messageElement.scrollIntoView();
}

function showTypingIndicator() {
    const typingIndicator = document.createElement("div");
    typingIndicator.id = "typing-indicator";
    typingIndicator.textContent = "Bot is typing...";
    document.getElementById("chat-box").appendChild(typingIndicator);
}

function removeTypingIndicator() {
    const typingIndicator = document.getElementById("typing-indicator");
    if (typingIndicator) typingIndicator.remove();
}

document.getElementById("send-button").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

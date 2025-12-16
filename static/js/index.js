let chat = document.querySelector('#chat');
let inputField = document.querySelector('#input-field'); // Updated ID
let sendBtn = document.querySelector('#send-btn');       // Updated ID

async function sendMessage() {
    // Check if input is empty
    if(inputField.value == "" || inputField.value == null) return;

    let message = inputField.value;
    inputField.value = "";

    // Create and append User Bubble
    let newBubble = createUserBubble();
    newBubble.innerHTML = message;
    chat.appendChild(newBubble);

    // Create and append Bot Bubble (Placeholder)
    let newBotBubble = createBotBubble();
    chat.appendChild(newBotBubble);
    scrollToBottom();
    newBotBubble.innerHTML = "Analyzing ..."; // Translated loading text

    // Send request to Flask API
    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({'msg': message}), // Sending the 'message' variable
        });

        const responseText = await response.text();
        console.log(responseText);

        // Update Bot Bubble with actual response
        // Replaces newlines (\n) with HTML breaks (<br>)
        newBotBubble.innerHTML = responseText.replace(/\n/g, '<br>');
        scrollToBottom();

    } catch (error) {
        console.error("Error:", error);
        newBotBubble.innerHTML = "Sorry, something went wrong. Please try again.";
    }
}

function createUserBubble() {
    let bubble = document.createElement('p');
    // Updated classes to match English CSS
    bubble.classList = 'chat__bubble chat__bubble--user';
    return bubble;
}

function createBotBubble() {
    let bubble = document.createElement('p');
    // Updated classes to match English CSS
    bubble.classList = 'chat__bubble chat__bubble--bot';
    return bubble;
}

function scrollToBottom() {
    chat.scrollTop = chat.scrollHeight;
}

// Event Listeners
sendBtn.addEventListener('click', sendMessage);

inputField.addEventListener("keyup", function(event) {
    event.preventDefault();
    // 'event.key' is the modern replacement for 'event.keyCode'
    if (event.key === "Enter") {
        sendBtn.click();
    }
});

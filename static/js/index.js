let chat = document.querySelector('#chat');
let inputField = document.querySelector('#input-field'); // Updated ID
let sendBtn = document.querySelector('#send-btn');

let selectedImage;
let attachButton = document.querySelector('#more-options-btn');
let imageInput;

async function attachImage() {
  let fileInput = document.createElement('input');
  fileInput.type = 'file';
  fileInput.accept = 'image/*';

  fileInput.onchange = async e => {
    if(imageInput) {
      imageInput.remove();
    }

    selectedImage = e.target.files[0];

    imageInput = document.createElement('img');
    imageInput.src = URL.createObjectURL(selectedImage);
    imageInput.style.maxWidth = '3rem';
    imageInput.style.maxHeight = '3rem';
    imageInput.style.margin = '0.5rem';

    document.querySelector('.input-area__container').insertBefore(imageInput, inputField);

    let formData = new FormData();
    formData.append('image', selectedImage);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload_image", {
          method: "POST",
          body: formData,
      });

      const responseText = await response.text();
      console.log(responseText);
      console.log("Image uploaded successfully.");
    } catch (error) {
      console.error("Error:", error);
    }
  }
  fileInput.click();

}

async function sendMessage() {
    // Check if input is empty
    if(inputField.value == "" || inputField.value == null) return;

    let message = inputField.value;
    inputField.value = "";

    if (imageInput) {
      imageInput.remove();
      imageInput = null;
    }

    // Create and append User Bubble
    let newBubble = createUserBubble();
    newBubble.innerHTML = message;
    chat.appendChild(newBubble);

    // Create and append Bot Bubble (Placeholder)
    let newBotBubble = createBotBubble();
    chat.appendChild(newBotBubble);
    scrollToBottom();
    newBotBubble.innerHTML = "Analyzing"; // Translated loading text

    let stages = ["Analyzing.", "Analyzing..", "Analyzing...", "Analyzing."];

    let stageIndex = 0;

    let loadingInterval = setInterval(() => {
        newBotBubble.innerHTML = stages[stageIndex];
        stageIndex = (stageIndex + 1) % stages.length;
        scrollToBottom();
    }, 500);

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
        clearInterval(loadingInterval);
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

attachButton.addEventListener('click', attachImage);

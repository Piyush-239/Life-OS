const chat = document.getElementById("chat");

async function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value.trim();

    if (!message) return;

    chat.innerHTML += `<p><b>You:</b> ${message}</p>`;

    input.value = "";

    // Create an empty assistant message
    const assistant = document.createElement("p");
    assistant.innerHTML = "<b>LIFE-OS:</b> ";
    chat.appendChild(assistant);

    const response = await fetch("/chat/stream", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    while (true) {

        const { done, value } = await reader.read();

        if (done) break;

        const chunk = decoder.decode(value);

        assistant.innerHTML += chunk;

        chat.scrollTop = chat.scrollHeight;
    }
}
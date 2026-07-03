const chat = document.getElementById("chat");

async function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value;

    if (!message) return;

    chat.innerHTML += `<p><b>You:</b> ${message}</p>`;

    input.value = "";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            message: message

        })

    });

    const data = await response.json();

    chat.innerHTML += `<p><b>LIFE-OS:</b> ${data.reply}</p>`;

    chat.scrollTop = chat.scrollHeight;

}
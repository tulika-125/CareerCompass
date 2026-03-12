document.addEventListener("DOMContentLoaded", () => {
    // 1. Existing functionality for Explore buttons
    const exploreButtons = document.querySelectorAll(".explore-btn");
    exploreButtons.forEach(button => {
        button.addEventListener("click", () => {
        const page = button.dataset.page;
        if(page) window.location.href = page;
        });
    });

    // 2. Chatbot UI Logic
    const openChatBtn = document.getElementById("open-chat-btn");
    const closeChatBtn = document.getElementById("close-chat-btn");
    const chatbotContainer = document.getElementById("chatbot-container");
    const chatInput = document.getElementById("chat-input");
    const sendChatBtn = document.getElementById("send-chat-btn");
    const chatMessages = document.getElementById("chat-messages");

    // Message History for API
    let messages = [];

    // Only map these if they exist (prevents errors on secondary pages without chat UI)
    if (openChatBtn && chatbotContainer) {
        openChatBtn.addEventListener("click", () => {
            chatbotContainer.classList.remove("chatbot-hidden");
            openChatBtn.style.display = "none";
        });

        closeChatBtn.addEventListener("click", () => {
            chatbotContainer.classList.add("chatbot-hidden");
            openChatBtn.style.display = "block";
        });

        function addMessageToUI(text, sender) {
            const msgDiv = document.createElement("div");
            msgDiv.classList.add("message");
            msgDiv.classList.add(sender === "user" ? "user-message" : "ai-message");
            msgDiv.innerText = text;
            chatMessages.appendChild(msgDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight; // auto-scroll to bottom
        }

        async function sendMessage() {
            const text = chatInput.value.trim();
            if (!text) return;

            // Add user message to UI and history
            addMessageToUI(text, "user");
            messages.push({ "role": "user", "content": text });
            chatInput.value = "";

            // Add loading indicator
            const loadingDiv = document.createElement("div");
            loadingDiv.classList.add("message", "ai-message");
            loadingDiv.innerText = "Thinking...";
            loadingDiv.id = "loading-message";
            chatMessages.appendChild(loadingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            try {
                // Send to backend
                const response = await fetch("/api/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ messages: messages })
                });

                const data = await response.json();
                
                // Remove loading indicator
                const loadMsg = document.getElementById("loading-message");
                if (loadMsg) loadMsg.remove();

                if (response.ok) {
                    addMessageToUI(data.response, "ai");
                    messages.push({ "role": "assistant", "content": data.response });
                } else {
                    addMessageToUI("Oops, something went wrong. Try again.", "ai");
                }
            } catch (error) {
                const loadMsg = document.getElementById("loading-message");
                if (loadMsg) loadMsg.remove();
                addMessageToUI("Network error: Could not reach the server.", "ai");
                console.error(error);
            }
        }

        sendChatBtn.addEventListener("click", sendMessage);
        
        chatInput.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                sendMessage();
            }
        });
    }
});

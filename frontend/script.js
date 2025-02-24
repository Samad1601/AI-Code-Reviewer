document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submit-btn").addEventListener("click", reviewCode);
    const starContainer = document.querySelector(".stars");
    const starCount = 50;

    for (let i = 0; i < starCount; i++) {
        const star = document.createElement("div");
        star.classList.add("star");
        star.style.setProperty("--star-tail-length", `${Math.random() * 3 + 3}em`);
        star.style.setProperty("--fall-duration", `${Math.random() * 6 + 6}s`);
        star.style.setProperty("--fall-delay", `${Math.random() * 10}s`);
        star.style.setProperty("--top-offset", `${Math.random() * 100}vh`);
        star.style.top = "var(--top-offset)";
        starContainer.appendChild(star);
    }
});

async function reviewCode() {
    const code = document.getElementById("code-input").value.trim();
    const userPrompt = document.getElementById("user-prompt").value.trim();
    const outputDiv = document.getElementById("review-output");

    if (!code || !userPrompt) { 
        alert("Please enter both code and a prompt!"); 
        return; 
    }

    outputDiv.innerText = "Processing... ⏳";
    outputDiv.style.display = "block";

    try {
        const response = await fetch("https://ai-code-reviewer-yzu7.onrender.com/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code, prompt: userPrompt })
        });

        if (!response.ok) {
            throw new Error(`Server Error: ${response.status}`);
        }

        const data = await response.json();
        outputDiv.innerText = data.response || "No response from AI.";
    } catch (error) {
        console.error("Error:", error);
        outputDiv.innerText = "⚠️ Something went wrong! Please try again.";
    }
}

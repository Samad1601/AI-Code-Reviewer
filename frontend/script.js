async function reviewCode() {
    const code = document.getElementById("code-input").value;
    const userPrompt = document.getElementById("user-prompt").value;

    if (!code || !userPrompt) { 
        alert("Please enter both code and a prompt!"); 
        return; 
    }

    const response = await fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            code: code,
            prompt: userPrompt
        })
    });

    const data = await response.json();
    document.getElementById("review-output").innerText = data.response || "Error: No response from AI";
}

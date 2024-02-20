document.addEventListener("DOMContentLoaded", function () {
    const analyzeButton = document.getElementById("analyze-button");
    const sentimentInput = document.getElementById("sentiment-input");
    const resultDiv = document.getElementById("result");

    // Add an event listener for form submission
    document.getElementById("sentiment-form").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the form from submitting

        const text = sentimentInput.value.trim();

        // Send the text to the server for sentiment analysis
        fetch("/analyze", {
            method: "POST",
            body: JSON.stringify({ text }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                const sentiment = data.sentiment;
                const emotion = data.emotion;
                const emoji = data.emoji;

                // Update the UI with the result
                resultDiv.innerHTML = `
                    <p>Sentiment: ${sentiment}</p>
                    <p>Emotion: ${emotion} ${emoji}</p>
                `;
            });
    });
});

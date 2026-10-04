document.addEventListener("DOMContentLoaded", () => {

    document.body.addEventListener("click", (e) => {

        const btn = e.target.closest(".speak-btn");

        if (!btn) {
            return;
        }

        e.preventDefault();

        window.speechSynthesis.cancel();

        const text = btn.getAttribute("data-speak-text");

        if (text) {
            const utterance = new SpeechSynthesisUtterance(text);

            utterance.rate = 0.7;
            utterance.lang = "en-US";

            window.speechSynthesis.speak(utterance);
        }
    });

});
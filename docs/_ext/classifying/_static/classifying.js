document.addEventListener("DOMContentLoaded", function () {
    const classificationBlocks = document.querySelectorAll(".classifying-block");

    // Helper function to dynamically shuffle rows in the browser
    function shuffleRows(container) {
        const rows = Array.from(container.querySelectorAll(".classifying-line"));

        // Fisher-Yates Shuffle algorithm
        for (let i = rows.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [rows[i], rows[j]] = [rows[j], rows[i]];
        }

        // Re-append elements in the new randomized order
        rows.forEach(row => container.appendChild(row));
    }

    classificationBlocks.forEach((block) => {
        const scoreBtn = block.querySelector(".classifying-btn-score");
        const resetBtn = block.querySelector(".classifying-btn-reset");
        const feedbackBadge = block.querySelector(".classifying-feedback-badge");
        const container = block.querySelector(".classifying-container");

        if (!scoreBtn || !resetBtn || !container) return;

        // FIXED: Run an initial shuffle right when the page finishes loading
        shuffleRows(container);

        // 1. Check Evaluation Logic
        scoreBtn.addEventListener("click", function () {
            // Re-query select boxes and lines because their order changed during shuffling!
            const selects = block.querySelectorAll(".sorting-select");
            const rows = block.querySelectorAll(".classifying-line");

            let totalItems = selects.length;
            let correctCount = 0;
            let allAnswered = true;

            selects.forEach((select, idx) => {
                const parentRow = rows[idx];
                const selectedValue = select.value;
                const correctValue = select.getAttribute("data-correct-bin");

                if (selectedValue === "") {
                    allAnswered = false;
                }

                // Lock dropdown so they can review their submitted answers safely
                select.disabled = true;

                if (selectedValue === correctValue) {
                    correctCount++;
                    parentRow.classList.remove("incorrect-line");
                    parentRow.classList.add("correct-line");
                } else {
                    parentRow.classList.remove("correct-line");
                    parentRow.classList.add("incorrect-line");
                }
            });

            const scorePercentage = totalItems > 0 ? (correctCount / totalItems) * 100 : 0;

            feedbackBadge.classList.remove("high", "medium", "low");
            feedbackBadge.style.display = "inline-block";

            if (scorePercentage === 100) {
                feedbackBadge.textContent = `Perfect! ${correctCount}/${totalItems} Correct`;
                feedbackBadge.classList.add("high");
            } else if (scorePercentage >= 50) {
                feedbackBadge.textContent = `Getting Close! ${correctCount}/${totalItems} Correct`;
                feedbackBadge.classList.add("medium");
            } else {
                feedbackBadge.textContent = `Try Again! ${correctCount}/${totalItems} Correct`;
                feedbackBadge.classList.add("low");
            }

            if (!allAnswered) {
                feedbackBadge.textContent += " (Incomplete)";
            }
        });

        // 2. Reset Layout Logic
        resetBtn.addEventListener("click", function () {
            const selects = block.querySelectorAll(".sorting-select");
            const rows = block.querySelectorAll(".classifying-line");

            selects.forEach((select) => {
                select.value = "";
                select.disabled = false; // Unlock dropdowns for another attempt
            });

            rows.forEach((row) => {
                row.classList.remove("correct-line", "incorrect-line");
            });

            feedbackBadge.style.display = "none";
            feedbackBadge.textContent = "";
            feedbackBadge.classList.remove("high", "medium", "low");

            // FIXED: Automatically shuffle the lines again for a fresh attempt!
            shuffleRows(container);
        });
    });
});
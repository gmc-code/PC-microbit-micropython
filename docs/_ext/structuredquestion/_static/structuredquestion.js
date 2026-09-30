document.addEventListener("DOMContentLoaded", function () {

    function getSubQuestion(element) {
        return element.closest(".sq-subquestion");
    }

    function getContainer(element) {
        return element.closest(".sq-container");
    }

    // ========================================================
    // 1. SHOW / HIDE MODEL ANSWER & Self-Grading
    // ========================================================
    document.addEventListener("click", function (event) {
        const toggleButton = event.target.closest(".sq-toggle-ans-btn");
        if (!toggleButton) return;

        const subQuestion = getSubQuestion(toggleButton);
        if (!subQuestion) return;

        const drawers = subQuestion.querySelectorAll(".sq-answer-drawer");
        const selfGrade = subQuestion.querySelector(".sq-self-grade");

        if (drawers.length === 0) {
            console.warn("Structured Question: no answer drawer found.");
            return;
        }

        const shouldShow = drawers[0].classList.contains("hidden");

        drawers.forEach(function (drawer) {
            if (shouldShow) {
                drawer.classList.remove("hidden");
            } else {
                drawer.classList.add("hidden");
            }
        });

        if (selfGrade) {
            if (shouldShow) {
                selfGrade.classList.remove("hidden");
            } else {
                selfGrade.classList.add("hidden");
            }
        }

        if (shouldShow) {
            toggleButton.textContent = "Hide Model Answer & Self-Grading";
            toggleButton.classList.add("active");
            toggleButton.setAttribute("aria-expanded", "true");
        } else {
            toggleButton.textContent = "Show Model Answer & Self-Grading";
            toggleButton.classList.remove("active");
            toggleButton.setAttribute("aria-expanded", "false");
        }
    });

    // ========================================================
    // 2. SELF-GRADING
    // ========================================================
    document.addEventListener("click", function (event) {
        const scoreButton = event.target.closest(".sq-score-btn");
        if (!scoreButton) return;

        const subQuestion = getSubQuestion(scoreButton);
        if (!subQuestion) return;

        const scoreButtons = subQuestion.querySelectorAll(".sq-score-btn");
        scoreButtons.forEach(function (button) {
            button.classList.remove("active");
        });

        scoreButton.classList.add("active");

        const score = parseInt(scoreButton.dataset.score, 10);
        if (Number.isNaN(score)) {
            console.warn("Structured Question: invalid score.", scoreButton.dataset.score);
            return;
        }

        subQuestion.dataset.userScore = String(score);
        updateContainerScore(subQuestion);
    });

    // ========================================================
    // 3. UPDATE TOTAL SCORE
    // ========================================================
    function updateContainerScore(element) {
        const container = getContainer(element);
        if (!container) return;

        let totalScore = 0;
        const subQuestions = container.querySelectorAll(".sq-subquestion");

        subQuestions.forEach(function (subQuestion) {
            const score = subQuestion.dataset.userScore;
            if (score !== undefined && score !== "") {
                const numericScore = parseInt(score, 10);
                if (!Number.isNaN(numericScore)) {
                    totalScore += numericScore;
                }
            }
        });

        const tracker = container.querySelector(".sq-user-score");
        if (tracker) {
            tracker.textContent = String(totalScore);
        }
    }

    // ========================================================
    // 4. INITIALISE SCORE TRACKERS
    // ========================================================
    document.querySelectorAll(".sq-container").forEach(function (container) {
        const subQuestions = container.querySelectorAll(".sq-subquestion");

        subQuestions.forEach(function (subQuestion) {
            if (subQuestion.dataset.userScore === undefined) {
                subQuestion.dataset.userScore = "0";
            }
        });

        updateContainerScore(container);
    });

    // ========================================================
    // 5. TEXTAREA SYNC FOR PRINT
    // Synchronizes textarea content to the DOM so browser print
    // engine correctly captures student responses.
    // ========================================================
    document.addEventListener("input", function (event) {
        if (event.target.classList.contains("sq-textarea")) {
            event.target.textContent = event.target.value;
        }
    });

    // ========================================================
    // 6. KEYBOARD ACCESSIBILITY
    // ========================================================
    document.addEventListener("keydown", function (event) {
        if (!event.target.classList.contains("sq-score-btn")) return;

        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            event.target.click();
        }
    });
});
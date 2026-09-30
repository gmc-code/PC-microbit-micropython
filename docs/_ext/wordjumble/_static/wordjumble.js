document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".wordjumble-block"));
  if (blocks.length === 0) return;

  blocks.forEach((block) => {
    const inputs = Array.from(block.querySelectorAll(".wj-input"));
    if (inputs.length === 0) return;

    // Build Control Panel UI
    const panel = document.createElement("div");
    panel.className = "wordjumble-global-panel";

    const btnScore = document.createElement("button");
    btnScore.type = "button";
    btnScore.className = "wordjumble-btn-score";
    btnScore.textContent = "Check";

    const btnReset = document.createElement("button");
    btnReset.type = "button";
    btnReset.className = "wordjumble-btn-reset";
    btnReset.textContent = "Reset";

    const scoreBadge = document.createElement("span");
    scoreBadge.className = "wordjumble-output";
    scoreBadge.style.display = "none";

    panel.appendChild(btnScore);
    panel.appendChild(btnReset);
    panel.appendChild(scoreBadge);
    block.appendChild(panel);

    // Scoring Listener
    btnScore.addEventListener("click", () => {
      block.dataset.disabled = "true";
      btnScore.disabled = true;

      let correctCount = 0;
      let totalTargets = inputs.length;

      inputs.forEach((input) => {
        input.disabled = true;
        const userAnswer = input.value.trim().toLowerCase();
        const expectedAnswer = (input.dataset.answer || "").trim().toLowerCase();

        if (userAnswer === expectedAnswer && userAnswer !== "") {
          input.classList.add("wj-correct");
          correctCount++;
        } else {
          input.classList.add("wj-incorrect");

          const answerBadge = document.createElement("span");
          answerBadge.className = "wj-correct-answer";
          answerBadge.textContent = `(${input.dataset.answer})`;
          input.parentNode.appendChild(answerBadge);
        }
      });

      // Output Score Badge
      scoreBadge.textContent = `Score: ${correctCount} / ${totalTargets}`;
      scoreBadge.style.display = "inline-block";
      scoreBadge.className = "wordjumble-output";

      const accuracy = totalTargets === 0 ? 0 : correctCount / totalTargets;
      if (accuracy >= 0.8) scoreBadge.classList.add("high");
      else if (accuracy >= 0.5) scoreBadge.classList.add("medium");
      else scoreBadge.classList.add("low");
    });

    // Reset Listener
    btnReset.addEventListener("click", () => {
      block.dataset.disabled = "false";
      btnScore.disabled = false;

      const answerBadges = Array.from(block.querySelectorAll(".wj-correct-answer"));
      answerBadges.forEach((badge) => badge.remove());

      inputs.forEach((input) => {
        input.disabled = false;
        input.value = "";
        input.className = "wj-input";
      });

      scoreBadge.style.display = "none";
    });
  });
});
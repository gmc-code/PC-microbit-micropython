document.addEventListener("DOMContentLoaded", () => {
  const containers = document.querySelectorAll(".ordering-container");

  containers.forEach(container => {
    const block = container.closest(".ordering-block");
    const completedCodeBlock = block.querySelector(".ordering-completed-code");

    const btnScore = block.querySelector(".ordering-btn-score");
    const btnContinue = block.querySelector(".ordering-btn-continue");
    const btnSolution = block.querySelector(".ordering-btn-solution");
    const btnReset = block.querySelector(".ordering-btn-reset");
    const feedbackBadge = block.querySelector(".ordering-feedback-badge");
    const initialHTML = container.innerHTML;

    const noReorder = container.dataset.noReorder === "true";

    // Helper to dynamically shuffle DOM lines and ensure it's not identical to correct order
    function shuffleLines() {
      if (noReorder) return;

      const lines = Array.from(container.querySelectorAll(".ordering-line"));
      if (lines.length <= 1) return;

      let isIdentical = true;
      let attempts = 0;

      while (isIdentical && attempts < 50) {
        // Perform Fisher-Yates Shuffle
        for (let i = lines.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          const temp = lines[i];
          lines[i] = lines[j];
          lines[j] = temp;
        }

        // Check if current DOM order matches correct_idx 0, 1, 2...
        isIdentical = lines.every((line, index) => {
          return parseInt(line.dataset.correctIdx, 10) === index;
        });

        attempts++;
      }

      // Append items back to DOM in new shuffled order
      lines.forEach(line => container.appendChild(line));
    }

    // Helper to clear evaluation styles and feedback
    function clearFeedback() {
      feedbackBadge.style.display = "none";
      feedbackBadge.textContent = "";
      if (btnContinue) btnContinue.style.display = "none";
      const lines = container.querySelectorAll(".ordering-line");
      lines.forEach(line => {
        line.classList.remove("correct-line", "incorrect-line");
      });

      // Ensure completed code block is hidden during active user attempts
      if (completedCodeBlock) {
        completedCodeBlock.style.display = "none";
      }
    }

    // Initializes dragging mechanics, click-to-indent listeners, and DOM listeners
    function initPuzzleEvents() {
      const lines = container.querySelectorAll(".ordering-line");

      lines.forEach(line => {
        // Drag Handling Events
        line.addEventListener("dragstart", (e) => {
          if (line.classList.contains("disabled")) return;
          clearFeedback();
          line.classList.add("dragging");
          e.dataTransfer.effectAllowed = "move";
        });

        line.addEventListener("dragend", () => {
          line.classList.remove("dragging");
        });

        // Indentation Control Events
        const btnIncrease = line.querySelector(".indent-btn.increase");
        const btnDecrease = line.querySelector(".indent-btn.decrease");

        if (btnIncrease) {
          btnIncrease.addEventListener("click", () => {
            if (line.classList.contains("disabled")) return;
            clearFeedback();
            let currentIndent = parseInt(line.dataset.currentIndent || "0", 10);
            currentIndent++;
            line.dataset.currentIndent = currentIndent;
            line.style.setProperty("--indent-level", currentIndent);
          });
        }

        if (btnDecrease) {
          btnDecrease.addEventListener("click", () => {
            if (line.classList.contains("disabled")) return;
            clearFeedback();
            let currentIndent = parseInt(line.dataset.currentIndent || "0", 10);
            if (currentIndent > 0) {
              currentIndent--;
              line.dataset.currentIndent = currentIndent;
              line.style.setProperty("--indent-level", currentIndent);
            }
          });
        }
      });

      // Drag Sorting Over Container Area
      container.addEventListener("dragover", (e) => {
        e.preventDefault();
        const draggingItem = container.querySelector(".dragging");
        if (!draggingItem) return;

        const siblings = Array.from(container.querySelectorAll(".ordering-line:not(.dragging)"));
        const nextSibling = siblings.find(sibling => {
          const box = sibling.getBoundingClientRect();
          return e.clientY <= box.top + box.height / 2;
        });

        if (nextSibling) {
          container.insertBefore(draggingItem, nextSibling);
        } else {
          container.appendChild(draggingItem);
        }
      });
    }

    // 1. Scoring Engine Mechanics
    if (btnScore) {
      btnScore.addEventListener("click", () => {
        // Disable Check button immediately upon score calculation
        btnScore.disabled = true;

        const currentLines = Array.from(container.querySelectorAll(".ordering-line"));
        const totalLines = currentLines.length;
        let correctCount = 0;

        currentLines.forEach((line, index) => {
          const correctIdx = parseInt(line.dataset.correctIdx, 10);
          const correctIndent = parseInt(line.dataset.correctIndent, 10);
          const currentIndent = parseInt(line.dataset.currentIndent, 10);

          line.classList.remove("correct-line", "incorrect-line");
          if (correctIdx === index && correctIndent === currentIndent) {
            line.classList.add("correct-line");
            correctCount++;
          } else {
            line.classList.add("incorrect-line");
          }
        });

        const finalPercentage = Math.round((correctCount / totalLines) * 100);
        feedbackBadge.style.display = "inline-flex";
        feedbackBadge.className = "ordering-feedback-badge";

        if (finalPercentage === 100) {
          feedbackBadge.textContent = `✓ Perfect! ${correctCount}/${totalLines} (${finalPercentage}%)`;
          feedbackBadge.classList.add("high");
          if (btnContinue) btnContinue.style.display = "none";

          // Show completed code block ONLY when student gets 100% on their own
          if (completedCodeBlock) {
            completedCodeBlock.style.display = "block";
          }
        } else {
          if (btnContinue) btnContinue.style.display = "inline-flex";

          if (completedCodeBlock) {
            completedCodeBlock.style.display = "none";
          }

          if (finalPercentage >= 50) {
            feedbackBadge.textContent = `⚠ Getting Close! ${correctCount}/${totalLines} (${finalPercentage}%)`;
            feedbackBadge.classList.add("medium");
          } else {
            feedbackBadge.textContent = `✕ Keep Trying! ${correctCount}/${totalLines} (${finalPercentage}%)`;
            feedbackBadge.classList.add("low");
          }
        }
      });
    }

    // 2. Continue Engine Mechanics
    if (btnContinue) {
      btnContinue.addEventListener("click", () => {
        clearFeedback();
        if (btnScore) btnScore.disabled = false;
        if (btnSolution) btnSolution.disabled = false; // Re-enable solution button on Continue
      });
    }

    // 3. Solution Engine Mechanics
    if (btnSolution) {
      btnSolution.addEventListener("click", () => {
        const currentLines = Array.from(container.querySelectorAll(".ordering-line"));

        currentLines.sort((a, b) => {
          return parseInt(a.dataset.correctIdx, 10) - parseInt(b.dataset.correctIdx, 10);
        });

        currentLines.forEach(line => {
          container.appendChild(line);

          const targetIndent = line.dataset.correctIndent;
          line.dataset.currentIndent = targetIndent;
          line.style.setProperty("--indent-level", targetIndent);

          line.classList.add("disabled", "correct-line");
          line.classList.remove("incorrect-line");
          line.setAttribute("draggable", "false");
        });

        // Disable Check and Solution buttons after displaying solution
        if (btnScore) btnScore.disabled = true;
        btnSolution.disabled = true;

        if (btnContinue) btnContinue.style.display = "none";

        feedbackBadge.style.display = "inline-flex";
        feedbackBadge.textContent = "ℹ Solution Displayed";
        feedbackBadge.className = "ordering-feedback-badge medium";

        if (completedCodeBlock) {
          completedCodeBlock.style.display = "none";
        }
      });
    }

    // 4. Reset Engine Mechanics
    if (btnReset) {
      btnReset.addEventListener("click", () => {
        container.innerHTML = initialHTML;
        feedbackBadge.style.display = "none";
        feedbackBadge.textContent = "";
        if (btnContinue) btnContinue.style.display = "none";

        // Re-enable Check and Solution buttons on Reset
        if (btnScore) btnScore.disabled = false;
        if (btnSolution) btnSolution.disabled = false;

        if (completedCodeBlock) {
          completedCodeBlock.style.display = "none";
        }

        shuffleLines();
        initPuzzleEvents();
      });
    }

    shuffleLines();
    initPuzzleEvents();
  });
});
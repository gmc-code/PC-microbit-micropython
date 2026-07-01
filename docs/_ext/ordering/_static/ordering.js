document.addEventListener("DOMContentLoaded", () => {
  const containers = document.querySelectorAll(".ordering-container");

  containers.forEach(container => {
    const block = container.closest(".ordering-block");
    const btnScore = block.querySelector(".ordering-btn-score");
    const btnSolution = block.querySelector(".ordering-btn-solution");
    const btnReset = block.querySelector(".ordering-btn-reset");
    const feedbackBadge = block.querySelector(".ordering-feedback-badge");
    const initialHTML = container.innerHTML;

    // Helper to dynamically shuffle DOM lines on load and reset
    function shuffleLines() {
      const lines = Array.from(container.querySelectorAll(".ordering-line"));
      for (let i = lines.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        container.appendChild(lines[j]);
      }
    }

    // Initializes dragging mechanics, click-to-indent listeners, and DOM listeners
    function initPuzzleEvents() {
      const lines = container.querySelectorAll(".ordering-line");

      lines.forEach(line => {
        // Drag Handling Events
        line.addEventListener("dragstart", (e) => {
          line.classList.add("dragging");
          e.dataTransfer.effectAllowed = "move";
        });

        line.addEventListener("dragend", () => {
          line.classList.remove("dragging");
        });

        // Indentation Control Events
        const btnIncrease = line.querySelector(".indent-btn.increase");
        const btnDecrease = line.querySelector(".indent-btn.decrease");

        btnIncrease.addEventListener("click", () => {
          if (line.classList.contains("disabled")) return;
          let currentIndent = parseInt(line.dataset.currentIndent || "0", 10);
          currentIndent++;
          line.dataset.currentIndent = currentIndent;
          line.style.setProperty("--indent-level", currentIndent);
        });

        btnDecrease.addEventListener("click", () => {
          if (line.classList.contains("disabled")) return;
          let currentIndent = parseInt(line.dataset.currentIndent || "0", 10);
          if (currentIndent > 0) {
            currentIndent--;
            line.dataset.currentIndent = currentIndent;
            line.style.setProperty("--indent-level", currentIndent);
          }
        });
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
    btnScore.addEventListener("click", () => {
      const currentLines = Array.from(container.querySelectorAll(".ordering-line"));
      const totalLines = currentLines.length;
      let correctCount = 0;

      currentLines.forEach((line, index) => {
        line.classList.add("disabled");
        line.setAttribute("draggable", "false");

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
      feedbackBadge.style.display = "inline-block";
      feedbackBadge.className = "ordering-feedback-badge";

      if (finalPercentage === 100) {
        feedbackBadge.textContent = `✓ Perfect! ${correctCount}/${totalLines} (${finalPercentage}%)`;
        feedbackBadge.classList.add("high");
      } else if (finalPercentage >= 50) {
        feedbackBadge.textContent = `⚠ Getting Close! ${correctCount}/${totalLines} (${finalPercentage}%)`;
        feedbackBadge.classList.add("medium");
      } else {
        feedbackBadge.textContent = `✕ Keep Trying! ${correctCount}/${totalLines} (${finalPercentage}%)`;
        feedbackBadge.classList.add("low");
      }
    });

    // 2. Solution Engine Mechanics (Locks scoring button)
    btnSolution.addEventListener("click", () => {
      const currentLines = Array.from(container.querySelectorAll(".ordering-line"));

      // Sort lines based on their original compilation source index positions
      currentLines.sort((a, b) => {
        return parseInt(a.dataset.correctIdx, 10) - parseInt(b.dataset.correctIdx, 10);
      });

      // Render the sorted rows into the puzzle runway
      currentLines.forEach(line => {
        container.appendChild(line);

        // Force reset items to correct structural code spaces
        const targetIndent = line.dataset.correctIndent;
        line.dataset.currentIndent = targetIndent;
        line.style.setProperty("--indent-level", targetIndent);

        // Disable blocks to prevent dragging or modifying layout rules
        line.classList.add("disabled", "correct-line");
        line.classList.remove("incorrect-line");
        line.setAttribute("draggable", "false");
      });

      // Guardrail: Explicitly disable Scoring updates to prevent automated 100% submission
      btnScore.disabled = true;

      feedbackBadge.style.display = "inline-block";
      feedbackBadge.textContent = "ℹ Solution Displayed";
      feedbackBadge.className = "ordering-feedback-badge medium";
    });

    // 3. Reset Engine Mechanics (Restores scoring button and reshuffles blocks)
    btnReset.addEventListener("click", () => {
      container.innerHTML = initialHTML;
      feedbackBadge.style.display = "none";
      feedbackBadge.textContent = "";

      // Restore click capability back to score updates safely
      btnScore.disabled = false;

      shuffleLines();     // Dynamically reshuffle positions on reset trigger
      initPuzzleEvents(); // Re-attach event listeners to the newly cleaned DOM nodes
    });

    // First structural execution pass (shuffles on page load)
    shuffleLines();
    initPuzzleEvents();
  });
});
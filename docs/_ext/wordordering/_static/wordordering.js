document.addEventListener("DOMContentLoaded", () => {
  const containers = document.querySelectorAll(".ordering-container.sentence-inline-container");

  containers.forEach(container => {
    const block = container.closest(".wordordering-block, .ordering-block");
    if (!block) return;

    const btnScore = block.querySelector(".ordering-btn-score");
    const btnContinue = block.querySelector(".ordering-btn-continue");
    const btnSolution = block.querySelector(".ordering-btn-solution");
    const btnReset = block.querySelector(".ordering-btn-reset");
    const feedbackBadge = block.querySelector(".ordering-feedback-badge");
    const initialHTML = container.innerHTML;

    const noReorder = container.dataset.noReorder === "true";

    function shuffleLines() {
      if (noReorder) return;

      const lines = Array.from(container.querySelectorAll(".ordering-line"));
      for (let i = lines.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        container.appendChild(lines[j]);
      }
    }

    function clearFeedback() {
      if (feedbackBadge) {
        feedbackBadge.style.display = "none";
        feedbackBadge.textContent = "";
      }
      if (btnContinue) btnContinue.style.display = "none";
      if (btnScore) btnScore.disabled = false;

      const lines = container.querySelectorAll(".ordering-line");
      lines.forEach(line => {
        line.classList.remove("correct-line", "incorrect-line");
      });
    }

    function initPuzzleEvents() {
      const lines = container.querySelectorAll(".ordering-line");

      lines.forEach(line => {
        line.addEventListener("dragstart", (e) => {
          if (line.classList.contains("disabled")) return;
          clearFeedback();
          line.classList.add("dragging");
          e.dataTransfer.effectAllowed = "move";
        });

        line.addEventListener("dragend", () => {
          line.classList.remove("dragging");
        });
      });

      // Multi-row Flexbox Drag & Drop Algorithm
      container.addEventListener("dragover", (e) => {
        e.preventDefault();
        const draggingItem = container.querySelector(".dragging");
        if (!draggingItem) return;

        const siblings = Array.from(container.querySelectorAll(".ordering-line:not(.dragging)"));

        // Find closest sibling based on 2D geometric center proximity
        const nextSibling = siblings.reduce((closest, sibling) => {
          const box = sibling.getBoundingClientRect();

          // Check if cursor is roughly within the row height bounds of the chip
          const inSameRow = e.clientY >= box.top && e.clientY <= box.bottom;

          if (inSameRow) {
            const offset = e.clientX - (box.left + box.width / 2);
            if (offset < 0 && offset > closest.offset) {
              return { offset: offset, element: sibling };
            }
          } else if (e.clientY < box.top) {
            // Target elements on lower rows if mouse pointer is above them
            if (closest.element === null || box.top < closest.top) {
              return { offset: -Infinity, element: sibling, top: box.top };
            }
          }

          return closest;
        }, { offset: -Infinity, element: null, top: Infinity }).element;

        if (nextSibling) {
          container.insertBefore(draggingItem, nextSibling);
        } else {
          container.appendChild(draggingItem);
        }
      });
    }

    // 1. Scoring Engine
    if (btnScore) {
      btnScore.addEventListener("click", () => {
        btnScore.disabled = true;

        const currentLines = Array.from(container.querySelectorAll(".ordering-line"));
        const totalLines = currentLines.length;
        let correctCount = 0;

        currentLines.forEach((line, index) => {
          const correctIdx = parseInt(line.dataset.correctIdx, 10);

          line.classList.remove("correct-line", "incorrect-line");
          if (correctIdx === index) {
            line.classList.add("correct-line");
            correctCount++;
          } else {
            line.classList.add("incorrect-line");
          }
        });

        const finalPercentage = Math.round((correctCount / totalLines) * 100);
        if (feedbackBadge) {
          feedbackBadge.style.display = "inline-flex";
          feedbackBadge.className = "ordering-feedback-badge";

          if (finalPercentage === 100) {
            feedbackBadge.textContent = `✓ Perfect! ${correctCount}/${totalLines} (${finalPercentage}%)`;
            feedbackBadge.classList.add("high");
            if (btnContinue) btnContinue.style.display = "none";
          } else {
            if (btnContinue) btnContinue.style.display = "inline-flex";

            if (finalPercentage >= 50) {
              feedbackBadge.textContent = `⚠ Getting Close! ${correctCount}/${totalLines} (${finalPercentage}%)`;
              feedbackBadge.classList.add("medium");
            } else {
              feedbackBadge.textContent = `✕ Keep Trying! ${correctCount}/${totalLines} (${finalPercentage}%)`;
              feedbackBadge.classList.add("low");
            }
          }
        }
      });
    }

    // 2. Continue Engine
    if (btnContinue) {
      btnContinue.addEventListener("click", () => {
        clearFeedback();
        if (btnSolution) btnSolution.disabled = false;
      });
    }

    // 3. Solution Engine
    if (btnSolution) {
      btnSolution.addEventListener("click", () => {
        const currentLines = Array.from(container.querySelectorAll(".ordering-line"));

        currentLines.sort((a, b) => {
          return parseInt(a.dataset.correctIdx, 10) - parseInt(b.dataset.correctIdx, 10);
        });

        currentLines.forEach(line => {
          container.appendChild(line);
          line.classList.add("disabled", "correct-line");
          line.classList.remove("incorrect-line");
          line.setAttribute("draggable", "false");
        });

        if (btnScore) btnScore.disabled = true;
        btnSolution.disabled = true;

        if (btnContinue) btnContinue.style.display = "none";

        if (feedbackBadge) {
          feedbackBadge.style.display = "inline-flex";
          feedbackBadge.textContent = "ℹ Solution Displayed";
          feedbackBadge.className = "ordering-feedback-badge medium";
        }
      });
    }

    // 4. Reset Engine
    if (btnReset) {
      btnReset.addEventListener("click", () => {
        container.innerHTML = initialHTML;
        if (feedbackBadge) {
          feedbackBadge.style.display = "none";
          feedbackBadge.textContent = "";
        }
        if (btnContinue) btnContinue.style.display = "none";

        if (btnScore) btnScore.disabled = false;
        if (btnSolution) btnSolution.disabled = false;

        shuffleLines();
        initPuzzleEvents();
      });
    }

    shuffleLines();
    initPuzzleEvents();
  });
});
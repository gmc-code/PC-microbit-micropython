document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".multichoice-block"));
  if (blocks.length === 0) return;

  // Remove any pre-existing global panels to prevent duplicate button sets
  document.querySelectorAll(".multichoice-global-panel").forEach(p => p.remove());

  // ─────────────────────────────────────
  // Utilities
  // ─────────────────────────────────────
  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  function assignLetters(choices) {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    choices.forEach((c, i) => {
      const span = c.querySelector(".multichoice-letter");
      if (span) span.textContent = letters[i] || "";
    });
  }

  // ─────────────────────────────────────
  // Initialise block metadata
  // ─────────────────────────────────────
  blocks.forEach((block) => {
    if (!block.dataset.originalChoicesHTML) {
      block.dataset.originalChoicesHTML = Array.from(
        block.querySelectorAll(".multichoice-choice")
      )
        .map(c => c.outerHTML)
        .join("");
    }

    block.dataset.multichoiceShuffle = block.dataset.multichoiceShuffle === "false" ? "false" : "true";
    block.dataset.multichoiceLetters = block.dataset.multichoiceLetters === "false" ? "false" : "true";
    block.dataset.multichoiceSingle = block.dataset.multichoiceSingle === "false" ? "false" : "true";
  });

  // ─────────────────────────────────────
  // Build / reset an individual block
  // ─────────────────────────────────────
  function initBlock(block, blockIndex) {
    block.querySelectorAll(".multichoice-choice").forEach(n => n.remove());

    const container = document.createElement("div");
    container.innerHTML = block.dataset.originalChoicesHTML;

    let choices = Array.from(container.children);

    if (block.dataset.multichoiceShuffle === "true") {
      shuffleArray(choices);
    }

    choices.forEach(c => block.appendChild(c));

    if (block.dataset.multichoiceLetters === "true") {
      assignLetters(choices);
    }

    const isSingle = block.dataset.multichoiceSingle === "true";
    const uniqueGroupToken = "mcq_" + blockIndex + "_" + Date.now();

    choices.forEach(choice => {
      choice.classList.remove(
        "multichoice-correct",
        "multichoice-incorrect",
        "multichoice-answer",
        "selected"
      );

      const input = choice.querySelector("input");
      if (input) {
        input.checked = false;
        input.disabled = false;
        // Enforce shared group token for radio sets to preserve selection constraints
        if (isSingle) input.name = uniqueGroupToken;
      }

      const exp = choice.querySelector(".multichoice-explanation");
      if (exp) exp.style.display = "none";
    });

    // ─────────────────────────────────────
    // Native Interaction Click Handling
    // ─────────────────────────────────────
    choices.forEach(choice => {
      const input = choice.querySelector("input");
      if (!input) return;

      choice.style.cursor = "pointer";

      input.addEventListener("change", () => {
        if (isSingle) {
          choices.forEach(c => c.classList.remove("selected"));
          if (input.checked) choice.classList.add("selected");
        } else {
          choice.classList.toggle("selected", input.checked);
        }
      });

      choice.addEventListener("click", (e) => {
        if (input.disabled) return;
        if (e.target.closest("label")) return;

        input.checked = isSingle ? true : !input.checked;
        input.dispatchEvent(new Event("change"));
      });
    });
  }

  // Initialise all individual question markup
  blocks.forEach((b, i) => initBlock(b, i));

// ─────────────────────────────────────
  // Control Panel & Feedback Toggle Configuration
  // ─────────────────────────────────────
  const panel = document.createElement("div");
  panel.className = "multichoice-global-panel";
  panel.style.display = "flex";
  panel.style.alignItems = "center";
  panel.style.gap = "0.8rem";

  const btnScore = document.createElement("button");
  btnScore.type = "button";
  btnScore.className = "multichoice-btn-score";
  btnScore.textContent = "Score Page";

  const btnReset = document.createElement("button");
  btnReset.type = "button";
  btnReset.className = "multichoice-btn-reset";
  btnReset.textContent = "Reset Page";

  // Create the feedback toggle container elements
  const toggleWrapper = document.createElement("label");
  toggleWrapper.className = "multichoice-toggle-wrapper";
  toggleWrapper.style.display = "flex";
  toggleWrapper.style.alignItems = "center";
  toggleWrapper.style.gap = "0.4rem";
  toggleWrapper.style.cursor = "pointer";
  toggleWrapper.style.fontSize = "0.9em";
  toggleWrapper.style.userSelect = "none";

  const chkShowFeedback = document.createElement("input");
  chkShowFeedback.type = "checkbox";
  chkShowFeedback.id = "mcq-toggle-feedback";
  chkShowFeedback.checked = true; // Default to showing feedback on score

  const toggleLabel = document.createElement("span");
  toggleLabel.textContent = "Show detailed feedback";

  toggleWrapper.append(chkShowFeedback, toggleLabel);

  const scoreBadge = document.createElement("span");
  scoreBadge.className = "multichoice-output";

  // Assemble the items cleanly in order
  panel.append(btnScore, btnReset, toggleWrapper, scoreBadge);

  // Append directly after the final block element on the page layout
  const lastBlock = blocks[blocks.length - 1];
  lastBlock.parentNode.insertBefore(panel, lastBlock.nextSibling);

  // ─────────────────────────────────────
  // Scoring Validation Engine
  // ─────────────────────────────────────
  function doScore() {
    let total = 0;
    let correct = 0;
    const displayFeedback = chkShowFeedback.checked;

    blocks.forEach(block => {
      total++;
      const isSingle = block.dataset.multichoiceSingle === "true";
      const choices = Array.from(block.querySelectorAll(".multichoice-choice"));

      choices.forEach(c => {
        c.classList.remove("multichoice-correct", "multichoice-incorrect", "multichoice-answer");
      });

      let blockIsFullyCorrect = true;

      choices.forEach(c => {
        const isChecked = c.querySelector("input")?.checked || false;
        const isAnswerCorrect = c.dataset.correct === "true";

        if (isAnswerCorrect) {
          c.classList.add("multichoice-answer");
        }

        if (isChecked) {
          if (isAnswerCorrect) {
            c.classList.add("multichoice-correct");
          } else {
            c.classList.add("multichoice-incorrect");
            blockIsFullyCorrect = false;
          }
        } else {
          if (isAnswerCorrect) {
            blockIsFullyCorrect = false;
          }
        }
      });

      if (blockIsFullyCorrect) {
        correct++;
      }

      // Respect the checkbox value state for showing/hiding explanations
      block.querySelectorAll(".multichoice-explanation").forEach(e => {
        e.style.display = displayFeedback ? "block" : "none";
      });

      block.querySelectorAll("input").forEach(i => {
        i.disabled = true;
      });
    });

    // Disable the toggle once scored to lock page state representation
    chkShowFeedback.disabled = true;
    toggleWrapper.style.opacity = "0.5";
    toggleWrapper.style.cursor = "not-allowed";

    // Score layout badge mutations
    scoreBadge.textContent = `Score: ${correct} / ${total}`;
    scoreBadge.style.display = "inline-block";

    const percent = total === 0 ? 0 : correct / total;
    scoreBadge.classList.remove("high", "medium", "low");

    if (percent >= 0.8) {
      scoreBadge.classList.add("high");
    } else if (percent >= 0.5) {
      scoreBadge.classList.add("medium");
    } else {
      scoreBadge.classList.add("low");
    }
  }

  function doReset() {
    scoreBadge.style.display = "none";
    scoreBadge.classList.remove("high", "medium", "low");

    // Re-enable the configuration toggle check element
    chkShowFeedback.disabled = false;
    chkShowFeedback.checked = true;
    toggleWrapper.style.opacity = "1";
    toggleWrapper.style.cursor = "pointer";

    blocks.forEach((b, i) => initBlock(b, i));
  }

  btnScore.onclick = doScore;
  btnReset.onclick = doReset;
});
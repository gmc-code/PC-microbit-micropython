document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".multichoice-block"));
  if (blocks.length === 0) return;

  document.querySelectorAll(".multichoice-global-panel, .multichoice-control-panel").forEach(p => p.remove());

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

  // Preserve original HTML structure for resets
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
    block.dataset.multichoiceTorf = block.dataset.multichoiceTorf === "true" ? "true" : "false";
  });

  blocks.forEach((block, blockIndex) => {
    // Track feedback toggle preference across resets per block
    let feedbackCheckedState = false;

    function initBlock() {
      block.querySelectorAll(".multichoice-choice, .multichoice-control-panel").forEach(n => n.remove());

      const container = document.createElement("div");
      container.innerHTML = block.dataset.originalChoicesHTML;

      let choices = Array.from(container.children);

      // Enforce True options first if True/False mode is active
      if (block.dataset.multichoiceTorf === "true") {
        choices.sort((a, b) => {
          const textA = a.innerText.trim().toLowerCase();
          const textB = b.innerText.trim().toLowerCase();
          const isTrueA = textA.startsWith("true") || textA.startsWith("t");
          const isTrueB = textB.startsWith("true") || textB.startsWith("t");
          return isTrueB - isTrueA;
        });
      } else if (block.dataset.multichoiceShuffle === "true") {
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
          if (isSingle) input.name = uniqueGroupToken;
        }

        const exp = choice.querySelector(".multichoice-explanation");
        if (exp) exp.style.display = "none";
      });

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

      buildPanelForBlock();
    }

    function buildPanelForBlock() {
      const panel = document.createElement("div");
      panel.className = "multichoice-control-panel";
      panel.style.display = "flex";
      panel.style.alignItems = "center";
      panel.style.gap = "0.8rem";

      const btnScore = document.createElement("button");
      btnScore.type = "button";
      btnScore.className = "multichoice-btn-score";
      btnScore.textContent = "Check";

      const btnReset = document.createElement("button");
      btnReset.type = "button";
      btnReset.className = "multichoice-btn-reset";
      btnReset.textContent = "Reset";

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

      // Preserve prior toggle setting on reset
      chkShowFeedback.checked = feedbackCheckedState;

      chkShowFeedback.addEventListener("change", () => {
        feedbackCheckedState = chkShowFeedback.checked;
      });

      const toggleLabel = document.createElement("span");
      toggleLabel.textContent = "Show feedback";

      toggleWrapper.append(chkShowFeedback, toggleLabel);

      const scoreBadge = document.createElement("span");
      scoreBadge.className = "multichoice-output";

      panel.append(btnScore, btnReset, toggleWrapper, scoreBadge);
      block.appendChild(panel);

      btnScore.onclick = () => {
        const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
        const displayFeedback = chkShowFeedback.checked;
        let blockIsFullyCorrect = true;

        choices.forEach(c => {
          c.classList.remove("multichoice-correct", "multichoice-incorrect", "multichoice-answer");
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

        block.querySelectorAll(".multichoice-explanation").forEach(e => {
          e.style.display = displayFeedback ? "block" : "none";
        });

        block.querySelectorAll("input").forEach(i => {
          i.disabled = true;
        });

        btnScore.disabled = true;
        chkShowFeedback.disabled = true;
        toggleWrapper.style.opacity = "0.5";
        toggleWrapper.style.cursor = "not-allowed";

        scoreBadge.style.display = "inline-block";
        scoreBadge.classList.remove("high", "medium", "low");

        if (blockIsFullyCorrect) {
          scoreBadge.textContent = "Correct!";
          scoreBadge.classList.add("high");
        } else {
          scoreBadge.textContent = "Incorrect";
          scoreBadge.classList.add("low");
        }
      };

      btnReset.onclick = () => {
        initBlock();
      };
    }

    initBlock();
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const groupBlocks = Array.from(document.querySelectorAll(".mcqgroup-block"));

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
      if (span) {
        span.textContent = letters[i] || "";
      }
    });
  }

  function shuffleBlockChoices(block) {
    const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
    if (choices.length <= 1) return;

    const container = choices[0].parentNode;
    if (!container) return;

    shuffleArray(choices);
    choices.forEach((c) => container.appendChild(c));

    if (block.dataset.multichoiceLetters !== "false") {
      assignLetters(choices);
    }
  }

  groupBlocks.forEach((group) => {
    // Remove individual question control panels inside the group block
    const individualControls = group.querySelectorAll(".multichoice-control-panel");
    individualControls.forEach((panel) => panel.remove());

    const blocks = Array.from(group.querySelectorAll(".multichoice-block"));
    if (blocks.length === 0) return;

    let currentIndex = 0;
    let isWizardMode = true;
    let isQuizStarted = false;

    const progressCount = group.querySelector(".mcqgroup-progress-count");
    const progressBarFill = group.querySelector(".mcqgroup-progress-bar-fill");
    const scoreValue = group.querySelector(".mcqgroup-score-value");
    const totalValue = group.querySelector(".mcqgroup-total-value");
    const btnStart = group.querySelector(".mcqgroup-btn-start");
    const btnToggle = group.querySelector(".mcqgroup-btn-toggle");
    const btnCheck = group.querySelector(".mcqgroup-btn-check");
    const btnReset = group.querySelector(".mcqgroup-btn-reset");
    const showFeedbackCb = group.querySelector(".mcqgroup-show-feedback");
    const instantFeedbackCb = group.querySelector(".mcqgroup-instant-feedback");

    const navBar = group.querySelector(".mcqgroup-nav-bar");
    const bottomBar = group.querySelector(".mcqgroup-bottom-bar");
    const btnScrollTop = group.querySelector(".mcqgroup-btn-scroll-top");
    const btnFirst = group.querySelector(".mcqgroup-btn-first");
    const btnPrev = group.querySelector(".mcqgroup-btn-prev");
    const btnNext = group.querySelector(".mcqgroup-btn-next");
    const btnLast = group.querySelector(".mcqgroup-btn-last");
    const currentIdxSpan = group.querySelector(".mcqgroup-current-idx");
    const totalIdxSpan = group.querySelector(".mcqgroup-total-idx");

    if (totalValue) totalValue.textContent = blocks.length;
    if (totalIdxSpan) totalIdxSpan.textContent = blocks.length;

    // Lock all question inputs by default until Start Quiz is pressed
    function lockAllInputs() {
      blocks.forEach((block) => {
        const inputs = Array.from(block.querySelectorAll("input"));
        inputs.forEach((input) => (input.disabled = true));
      });
    }

    function unlockUncheckedInputs() {
      blocks.forEach((block) => {
        if (block.dataset.checked !== "true") {
          const inputs = Array.from(block.querySelectorAll("input"));
          inputs.forEach((input) => (input.disabled = false));
        }
      });
    }

    function setCheckboxesLock(locked) {
      if (showFeedbackCb) showFeedbackCb.disabled = locked;
      if (instantFeedbackCb) instantFeedbackCb.disabled = locked;
    }

    function renderView() {
      if (isWizardMode) {
        blocks.forEach((block, i) => {
          block.style.display = i === currentIndex ? "block" : "none";
        });
        if (navBar) navBar.style.display = "flex";
        if (bottomBar) bottomBar.style.display = "none";
        if (currentIdxSpan) currentIdxSpan.textContent = currentIndex + 1;

        const isAtStart = currentIndex === 0;
        const isAtEnd = currentIndex === blocks.length - 1;

        if (btnFirst) btnFirst.disabled = isAtStart;
        if (btnPrev) btnPrev.disabled = isAtStart;
        if (btnNext) btnNext.disabled = isAtEnd;
        if (btnLast) btnLast.disabled = isAtEnd;

        if (btnToggle) btnToggle.textContent = "All Q Mode";
      } else {
        blocks.forEach((block) => {
          block.style.display = "block";
        });
        if (navBar) navBar.style.display = "none";
        if (bottomBar) bottomBar.style.display = "flex";
        if (btnToggle) btnToggle.textContent = "1 Q Mode";
      }
    }

    function updateGroupStats(forceScoreCalculation = false) {
      let answered = 0;
      let score = 0;
      const isInstant = instantFeedbackCb ? instantFeedbackCb.checked : false;

      blocks.forEach((block) => {
        const inputs = Array.from(block.querySelectorAll("input"));
        const isAnswered = inputs.some((input) => input.checked);
        if (isAnswered) answered++;

        if (isInstant || forceScoreCalculation || block.dataset.checked === "true") {
          const isSingle = block.dataset.multichoiceSingle === "true";
          if (isSingle) {
            const selected = block.querySelector("input:checked");
            if (selected && selected.closest(".multichoice-choice")?.dataset.correct === "true") {
              score++;
            }
          } else {
            const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
            const allCorrect = choices.every((c) => {
              const isChecked = c.querySelector("input")?.checked;
              const isCorrect = c.dataset.correct === "true";
              return isChecked === isCorrect;
            });
            if (allCorrect && isAnswered) score++;
          }
        }
      });

      if (progressCount) progressCount.textContent = `${answered} / ${blocks.length}`;
      if (progressBarFill) {
        const percentage = blocks.length > 0 ? (answered / blocks.length) * 100 : 0;
        progressBarFill.style.width = `${percentage}%`;
      }

      if (scoreValue) {
        if (isInstant || forceScoreCalculation || group.dataset.groupChecked === "true") {
          scoreValue.textContent = score;
        }
      }
    }

    function updateExplanationsDisplay() {
      const shouldShow = showFeedbackCb ? showFeedbackCb.checked : false;

      blocks.forEach((block) => {
        const isChecked = block.dataset.checked === "true";
        const choices = Array.from(block.querySelectorAll(".multichoice-choice"));

        choices.forEach((choice) => {
          const exp = choice.querySelector(".multichoice-explanation");
          if (!exp) return;

          if (isChecked && shouldShow) {
            const input = choice.querySelector("input");
            const isCorrect = choice.dataset.correct === "true";
            if ((input && input.checked) || isCorrect) {
              exp.style.display = "block";
            }
          } else {
            exp.style.display = "none";
          }
        });
      });
    }

    function resetQuizState() {
      delete group.dataset.groupChecked;

      blocks.forEach((block) => {
        delete block.dataset.checked;

        const inputs = Array.from(block.querySelectorAll("input"));
        inputs.forEach((input) => {
          input.checked = false;
        });

        const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
        choices.forEach((choice) => {
          choice.classList.remove("multichoice-correct", "multichoice-incorrect", "multichoice-answer", "selected");
          const exp = choice.querySelector(".multichoice-explanation");
          if (exp) exp.style.display = "none";
        });

        const isShuffle = block.dataset.multichoiceShuffle === "true" ||
                          block.dataset.shuffle === "true" ||
                          block.classList.contains("multichoice-shuffle");

        if (isShuffle) {
          shuffleBlockChoices(block);
        }
      });

      if (btnCheck) btnCheck.disabled = false;
      if (scoreValue) scoreValue.textContent = "0";
      setCheckboxesLock(false);
      currentIndex = 0;
      renderView();
      updateGroupStats();
    }

    // Initialize: Ensure checkboxes are responsive and inputs are locked prior to start
    setCheckboxesLock(false);
    lockAllInputs();

    // Scroll Back to Top Handler
    if (btnScrollTop) {
      btnScrollTop.addEventListener("click", () => {
        group.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }

    // Start Quiz Handler
    if (btnStart) {
      btnStart.addEventListener("click", () => {
        isQuizStarted = true;
        resetQuizState();
        unlockUncheckedInputs();
        setCheckboxesLock(true);
        btnStart.disabled = true;
      });
    }

    // Wizard Navigation Handlers
    if (btnFirst) {
      btnFirst.addEventListener("click", () => {
        currentIndex = 0;
        renderView();
      });
    }

    if (btnPrev) {
      btnPrev.addEventListener("click", () => {
        if (currentIndex > 0) {
          currentIndex--;
          renderView();
        }
      });
    }

    if (btnNext) {
      btnNext.addEventListener("click", () => {
        if (currentIndex < blocks.length - 1) {
          currentIndex++;
          renderView();
        }
      });
    }

    if (btnLast) {
      btnLast.addEventListener("click", () => {
        currentIndex = blocks.length - 1;
        renderView();
      });
    }

    if (btnToggle) {
      btnToggle.addEventListener("click", () => {
        isWizardMode = !isWizardMode;
        renderView();
      });
    }

    // Check Group Answers Handler
    if (btnCheck) {
      btnCheck.addEventListener("click", () => {
        group.dataset.groupChecked = "true";
        setCheckboxesLock(false);
        if (btnStart) btnStart.disabled = false;
        btnCheck.disabled = true;

        blocks.forEach((block) => {
          block.dataset.checked = "true";
          const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
          const inputs = Array.from(block.querySelectorAll("input"));

          inputs.forEach((input) => {
            input.disabled = true;
          });

          choices.forEach((choice) => {
            const input = choice.querySelector("input");
            const isCorrect = choice.dataset.correct === "true";

            if (input && input.checked) {
              choice.classList.add(isCorrect ? "multichoice-correct" : "multichoice-incorrect");
            } else if (isCorrect) {
              choice.classList.add("multichoice-answer");
            }
          });
        });

        updateExplanationsDisplay();
        updateGroupStats(true);
      });
    }

    // Show Feedback Checkbox Toggle Handler
    if (showFeedbackCb) {
      showFeedbackCb.addEventListener("change", () => {
        updateExplanationsDisplay();
      });
    }

    // Instant Feedback Checkbox Toggle Handler
    if (instantFeedbackCb) {
      instantFeedbackCb.addEventListener("change", () => {
        const isEnabled = instantFeedbackCb.checked;
        if (!isEnabled && isQuizStarted && group.dataset.groupChecked !== "true") {
          unlockUncheckedInputs();
        }
        updateGroupStats();
      });
    }

    // Reset Group Handler
    if (btnReset) {
      btnReset.addEventListener("click", () => {
        isQuizStarted = false;
        if (btnStart) btnStart.disabled = false;
        if (showFeedbackCb) showFeedbackCb.checked = false;
        if (instantFeedbackCb) instantFeedbackCb.checked = false;
        resetQuizState();
        lockAllInputs();
      });
    }

    // Event Delegation for Option Selection
    group.addEventListener("change", (e) => {
      if (e.target.matches("input[type='radio'], input[type='checkbox']")) {
        // Ignore header control checkboxes
        if (e.target.classList.contains("mcqgroup-show-feedback") || e.target.classList.contains("mcqgroup-instant-feedback")) {
          return;
        }

        if (!isQuizStarted) {
          e.target.checked = false;
          return;
        }

        const block = e.target.closest(".multichoice-block");

        if (block && block.dataset.checked !== "true" && group.dataset.groupChecked !== "true") {
          const isSingle = block.dataset.multichoiceSingle === "true";
          const choices = Array.from(block.querySelectorAll(".multichoice-choice"));

          choices.forEach((choice) => {
            const input = choice.querySelector("input");
            choice.classList.toggle("selected", input && input.checked);
          });

          if (instantFeedbackCb && instantFeedbackCb.checked && isSingle) {
            block.dataset.checked = "true";
            const radioInputs = Array.from(block.querySelectorAll("input[type='radio']"));

            choices.forEach((choice) => {
              const input = choice.querySelector("input");
              const isCorrect = choice.dataset.correct === "true";

              choice.classList.remove("multichoice-correct", "multichoice-incorrect");

              if (input && input.checked) {
                choice.classList.add(isCorrect ? "multichoice-correct" : "multichoice-incorrect");
              }
            });

            radioInputs.forEach((input) => {
              input.disabled = true;
            });

            updateExplanationsDisplay();
          }

          updateGroupStats();
        }
      }
    });

    renderView();
    updateGroupStats();
  });
});
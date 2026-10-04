document.addEventListener("DOMContentLoaded", () => {
  const groupBlocks = Array.from(document.querySelectorAll(".clozegroup-block"));

  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  function shuffleQuestions(group) {
    const container = group.querySelector(".clozegroup-questions-container");
    if (!container) return;

    const blocks = Array.from(container.querySelectorAll(".cloze-block"));
    if (blocks.length <= 1) return;

    shuffleArray(blocks);
    blocks.forEach((b) => container.appendChild(b));
  }

  groupBlocks.forEach((group) => {
    // Hide individual panel controls inside cloze questions
    const individualPanels = group.querySelectorAll(".cloze-global-panel");
    individualPanels.forEach((panel) => panel.remove());

    const allOriginalBlocks = Array.from(group.querySelectorAll(".cloze-block"));
    if (allOriginalBlocks.length === 0) return;

    const numQAttr = group.dataset.numQuestions;
    const numQuestionsTarget = numQAttr ? parseInt(numQAttr, 10) : null;

    let activeBlocks = [];
    let currentIndex = 0;
    let isWizardMode = true;
    let isQuizStarted = false;
    let activePollTimer = null;

    const progressCount = group.querySelector(".clozegroup-progress-count");
    const progressBarFill = group.querySelector(".clozegroup-progress-bar-fill");
    const scoreValue = group.querySelector(".clozegroup-score-value");
    const totalValue = group.querySelector(".clozegroup-total-value");
    const btnStart = group.querySelector(".clozegroup-btn-start");
    const btnToggle = group.querySelector(".clozegroup-btn-toggle");
    const btnCheck = group.querySelector(".clozegroup-btn-check");
    const btnReset = group.querySelector(".clozegroup-btn-reset");
    const chkInstantFeedback = group.querySelector(".clozegroup-toggle-instant-feedback");

    const navBars = group.querySelectorAll(".clozegroup-nav-bar");
    const bottomBar = group.querySelector(".clozegroup-bottom-bar");
    const btnScrollTop = group.querySelector(".clozegroup-btn-scroll-top");

    const btnsFirst = Array.from(group.querySelectorAll(".clozegroup-btn-first"));
    const btnsPrev = Array.from(group.querySelectorAll(".clozegroup-btn-prev"));
    const btnsNext = Array.from(group.querySelectorAll(".clozegroup-btn-next"));
    const btnsLast = Array.from(group.querySelectorAll(".clozegroup-btn-last"));

    const currentIdxSpans = group.querySelectorAll(".clozegroup-current-idx");
    const totalIdxSpans = group.querySelectorAll(".clozegroup-total-idx");

    function getTotalGapsInActiveSubset() {
      let total = 0;
      activeBlocks.forEach((block) => {
        total += block.querySelectorAll(".cloze-dropzone").length;
      });
      return total;
    }

    function isZoneFilled(zone) {
      const rawText = zone.textContent.trim().replace(/^Drop here$/i, "");
      const hasChild = zone.children.length > 0 || zone.querySelector("*") !== null;
      const hasDataWord = zone.dataset && zone.dataset.word && zone.dataset.word.trim().length > 0;
      return hasChild || rawText.length > 0 || hasDataWord;
    }

    function isBlockFullyAnswered(block) {
      const dropzones = Array.from(block.querySelectorAll(".cloze-dropzone"));
      return dropzones.length > 0 && dropzones.every((zone) => isZoneFilled(zone));
    }

    function updateQuestionSubsetAndHeaders() {
      if (group.dataset.shuffleQuestions === "true" || numQuestionsTarget) {
        shuffleQuestions(group);
      }

      const currentDOMBlocks = Array.from(group.querySelectorAll(".cloze-block"));

      if (numQuestionsTarget && numQuestionsTarget < currentDOMBlocks.length) {
        activeBlocks = currentDOMBlocks.slice(0, numQuestionsTarget);
        const hiddenBlocks = currentDOMBlocks.slice(numQuestionsTarget);

        activeBlocks.forEach((b) => (b.dataset.activeQuestion = "true"));
        hiddenBlocks.forEach((b) => {
          delete b.dataset.activeQuestion;
          b.style.display = "none";
        });
      } else {
        activeBlocks = currentDOMBlocks;
        activeBlocks.forEach((b) => (b.dataset.activeQuestion = "true"));
      }

      activeBlocks.forEach((block, index) => {
        let header = block.querySelector(".clozegroup-question-header");
        if (!header) {
          header = document.createElement("div");
          header.className = "clozegroup-question-header";
          block.prepend(header);
        }
        header.textContent = `Cloze Task ${index + 1}`;
      });

      const totalGaps = getTotalGapsInActiveSubset();
      if (totalValue) totalValue.textContent = totalGaps;
      totalIdxSpans.forEach((span) => (span.textContent = activeBlocks.length));
    }

    function lockAllGaps() {
      activeBlocks.forEach((block) => {
        const dropzones = block.querySelectorAll(".cloze-dropzone");
        dropzones.forEach((z) => z.classList.add("disabled"));
      });
    }

    function unlockAllGaps() {
      activeBlocks.forEach((block) => {
        const dropzones = block.querySelectorAll(".cloze-dropzone");
        dropzones.forEach((z) => z.classList.remove("disabled"));
      });
    }

    function setCheckboxesLock(locked) {
      if (chkInstantFeedback) chkInstantFeedback.disabled = locked;
    }

    function renderView() {
      if (isWizardMode) {
        group.setAttribute("data-view-mode", "wizard");
        activeBlocks.forEach((block, i) => {
          block.style.display = i === currentIndex ? "block" : "none";
        });

        navBars.forEach((bar) => (bar.style.display = "flex"));
        if (bottomBar) bottomBar.style.display = "none";

        currentIdxSpans.forEach((span) => (span.textContent = currentIndex + 1));

        const isAtStart = currentIndex === 0;
        const isAtEnd = currentIndex === activeBlocks.length - 1;

        btnsFirst.forEach((btn) => (btn.disabled = isAtStart));
        btnsPrev.forEach((btn) => (btn.disabled = isAtStart));
        btnsNext.forEach((btn) => (btn.disabled = isAtEnd));
        btnsLast.forEach((btn) => (btn.disabled = isAtEnd));

        if (btnToggle) btnToggle.textContent = "All Q Mode";
      } else {
        group.setAttribute("data-view-mode", "all");
        activeBlocks.forEach((block) => {
          block.style.display = "block";
        });

        navBars.forEach((bar) => (bar.style.display = "none"));
        if (bottomBar) bottomBar.style.display = "flex";

        if (btnToggle) btnToggle.textContent = "1 Q Mode";
      }
    }

    function clearBlockValidation(block) {
      const dropzones = block.querySelectorAll(".cloze-dropzone");
      dropzones.forEach((zone) => {
        zone.classList.remove("correct", "incorrect");
        const wrapper = zone.closest(".cloze-wrapper");
        const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null;
        if (feedback) {
          feedback.textContent = "";
          feedback.className = "cloze-inline-feedback";
        }
      });
      const completedCodeBlock = block.querySelector(".cloze-completed-code");
      if (completedCodeBlock) completedCodeBlock.style.display = "none";
    }

    function evaluateBlock(block, isInstant = false) {
      const dropzones = Array.from(block.querySelectorAll(".cloze-dropzone"));

      if (isInstant && !isBlockFullyAnswered(block)) {
        clearBlockValidation(block);
        return 0;
      }

      let correctCount = 0;

      dropzones.forEach((zone) => {
        const token = zone.querySelector(".cloze-dropped-token, .cloze-draggable") || zone.firstElementChild;
        const expected = zone.dataset.correct ? zone.dataset.correct.trim() : "";

        let actual = "";
        if (token && token.dataset && token.dataset.word) {
          actual = token.dataset.word.trim();
        } else if (token) {
          actual = token.textContent.trim();
        } else {
          actual = zone.textContent.trim().replace(/^Drop here$/i, "");
        }

        const wrapper = zone.closest(".cloze-wrapper");
        const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null;

        zone.classList.remove("correct", "incorrect");

        if (actual && actual === expected) {
          zone.classList.add("correct");
          correctCount++;
          if (feedback) {
            feedback.textContent = " ✓ Correct!";
            feedback.className = "cloze-inline-feedback text-correct";
          }
        } else if (actual) {
          zone.classList.add("incorrect");
          if (feedback) {
            feedback.textContent = ` ✕ (Ans: ${zone.dataset.correct})`;
            feedback.className = "cloze-inline-feedback text-incorrect";
          }
        }
      });

      const completedCodeBlock = block.querySelector(".cloze-completed-code");
      if (completedCodeBlock) {
        const is100Percent = dropzones.length > 0 && correctCount === dropzones.length;
        completedCodeBlock.style.display = is100Percent ? "block" : "none";
      }

      return correctCount;
    }

    function updateGroupStats() {
      const totalGaps = getTotalGapsInActiveSubset();
      const isChecked = group.dataset.groupChecked === "true";
      const isInstantFeedback = chkInstantFeedback && chkInstantFeedback.checked;

      if (!isQuizStarted && !isChecked) {
        activeBlocks.forEach((block) => clearBlockValidation(block));
        if (progressCount) progressCount.textContent = "0%";
        if (progressBarFill) progressBarFill.style.width = "0%";
        if (scoreValue) scoreValue.textContent = "0";
        return;
      }

      let filledGaps = 0;
      let totalCorrect = 0;

      activeBlocks.forEach((block) => {
        const dropzones = Array.from(block.querySelectorAll(".cloze-dropzone"));

        dropzones.forEach((zone) => {
          if (isZoneFilled(zone)) filledGaps++;
        });

        if (isChecked) {
          totalCorrect += evaluateBlock(block, false);
        } else if (isInstantFeedback) {
          totalCorrect += evaluateBlock(block, true);
        } else {
          clearBlockValidation(block);
        }
      });

      const percentage = totalGaps > 0 ? Math.round((filledGaps / totalGaps) * 100) : 0;

      if (progressCount) progressCount.textContent = `${percentage}%`;
      if (progressBarFill) progressBarFill.style.width = `${percentage}%`;

      if (scoreValue) {
        scoreValue.textContent = (isChecked || isInstantFeedback) ? totalCorrect : "0";
      }
    }

    function triggerShortPolling() {
      if (activePollTimer) clearInterval(activePollTimer);
      let count = 0;
      activePollTimer = setInterval(() => {
        updateGroupStats();
        count++;
        if (count > 50) {
          clearInterval(activePollTimer);
          activePollTimer = null;
        }
      }, 50);
    }

    function setupDropzoneObservers() {
      const dropzones = group.querySelectorAll(".cloze-dropzone");
      dropzones.forEach((zone) => {
        const observer = new MutationObserver(() => {
          updateGroupStats();
        });
        observer.observe(zone, { childList: true, subtree: true, attributes: false });
      });
    }

    function resetGroupState() {
      isQuizStarted = false;
      delete group.dataset.groupChecked;
      if (activePollTimer) clearInterval(activePollTimer);

      updateQuestionSubsetAndHeaders();

      const allBlocks = Array.from(group.querySelectorAll(".cloze-block"));
      allBlocks.forEach((block) => {
        const dropzones = block.querySelectorAll(".cloze-dropzone");
        dropzones.forEach((zone) => {
          zone.innerHTML = "Drop here";
          zone.className = "cloze-dropzone";
          const wrapper = zone.closest(".cloze-wrapper");
          const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null;
          if (feedback) {
            feedback.textContent = "";
            feedback.className = "cloze-inline-feedback";
          }
        });

        const draggables = block.querySelectorAll(".cloze-draggable");
        draggables.forEach((d) => {
          d.style.display = "inline-block";
          d.classList.remove("selected");
        });

        const completedCodeBlock = block.querySelector(".cloze-completed-code");
        if (completedCodeBlock) completedCodeBlock.style.display = "none";
      });

      if (btnCheck) btnCheck.disabled = true;
      if (btnStart) btnStart.disabled = false;
      if (scoreValue) scoreValue.textContent = "0";
      currentIndex = 0;
      renderView();
      updateGroupStats();
    }

    // Capture interaction attempt before test starts
    group.addEventListener(
      "click",
      (e) => {
        const target = e.target.closest(".cloze-draggable, .cloze-dropzone");
        if (target && !isQuizStarted) {
          e.preventDefault();
          e.stopPropagation();
        }
      },
      true
    );

    // Initial setup
    setCheckboxesLock(false);
    resetGroupState();
    lockAllGaps();
    setupDropzoneObservers();

    // Event Handlers
    if (chkInstantFeedback) {
      chkInstantFeedback.addEventListener("change", updateGroupStats);
    }

    if (btnScrollTop) {
      btnScrollTop.addEventListener("click", () => {
        group.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }

    if (btnStart) {
      btnStart.addEventListener("click", () => {
        resetGroupState();
        isQuizStarted = true;

        activeBlocks.forEach((block) => clearBlockValidation(block));

        unlockAllGaps();
        setCheckboxesLock(true);
        btnStart.disabled = true;

        if (btnCheck) btnCheck.disabled = false;
      });
    }

    btnsFirst.forEach((btn) => btn.addEventListener("click", () => { currentIndex = 0; renderView(); }));
    btnsPrev.forEach((btn) => btn.addEventListener("click", () => { if (currentIndex > 0) { currentIndex--; renderView(); } }));
    btnsNext.forEach((btn) => btn.addEventListener("click", () => { if (currentIndex < activeBlocks.length - 1) { currentIndex++; renderView(); } }));
    btnsLast.forEach((btn) => btn.addEventListener("click", () => { currentIndex = activeBlocks.length - 1; renderView(); }));

    if (btnToggle) {
      btnToggle.addEventListener("click", () => {
        isWizardMode = !isWizardMode;
        renderView();
      });
    }

    if (btnCheck) {
      btnCheck.addEventListener("click", () => {
        if (!isQuizStarted) return;

        group.dataset.groupChecked = "true";
        setCheckboxesLock(false);
        if (btnStart) btnStart.disabled = false;
        btnCheck.disabled = true;
        lockAllGaps();
        updateGroupStats();
      });
    }

    if (btnReset) {
      btnReset.addEventListener("click", () => {
        isQuizStarted = false;
        setCheckboxesLock(false);
        if (btnStart) btnStart.disabled = false;
        resetGroupState();
        lockAllGaps();
      });
    }

    // Direct event listeners for user placement actions
    group.addEventListener("change", updateGroupStats);
    group.addEventListener("click", triggerShortPolling);
    group.addEventListener("drop", triggerShortPolling);
    group.addEventListener("dragend", triggerShortPolling);
    group.addEventListener("touchend", triggerShortPolling);
  });
});
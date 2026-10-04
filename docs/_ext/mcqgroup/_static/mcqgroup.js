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

    function shuffleQuestions(group) {
        const container = group.querySelector(".mcqgroup-questions-container");
        if (!container) return;

        const blocks = Array.from(container.querySelectorAll(".multichoice-block"));
        if (blocks.length <= 1) return;

        shuffleArray(blocks);
        blocks.forEach((b) => container.appendChild(b));
    }

    groupBlocks.forEach((group) => {
        // Remove individual question control panels inside the group block
        const individualControls = group.querySelectorAll(".multichoice-control-panel");
        individualControls.forEach((panel) => panel.remove());

        const allOriginalBlocks = Array.from(group.querySelectorAll(".multichoice-block"));
        if (allOriginalBlocks.length === 0) return;

        // Read num_questions option
        const numQAttr = group.dataset.numQuestions;
        const numQuestionsTarget = numQAttr ? parseInt(numQAttr, 10) : null;

        let activeBlocks = [];
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

        // Support multiple nav bars (top, bottom, or both)
        const navBars = group.querySelectorAll(".mcqgroup-nav-bar");
        const bottomBar = group.querySelector(".mcqgroup-bottom-bar");
        const btnScrollTop = group.querySelector(".mcqgroup-btn-scroll-top");

        const btnsFirst = Array.from(group.querySelectorAll(".mcqgroup-btn-first"));
        const btnsPrev = Array.from(group.querySelectorAll(".mcqgroup-btn-prev"));
        const btnsNext = Array.from(group.querySelectorAll(".mcqgroup-btn-next"));
        const btnsLast = Array.from(group.querySelectorAll(".mcqgroup-btn-last"));

        const currentIdxSpans = group.querySelectorAll(".mcqgroup-current-idx");
        const totalIdxSpans = group.querySelectorAll(".mcqgroup-total-idx");

        function updateQuestionSubsetAndHeaders() {
            // 1. Reshuffle full list if shuffle option is set or subsetting is needed
            if (group.dataset.shuffleQuestions === "true" || numQuestionsTarget) {
                shuffleQuestions(group);
            }

            const currentDOMBlocks = Array.from(group.querySelectorAll(".multichoice-block"));

            // 2. Select active subset vs hidden questions
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

            // 3. Update headers and totals for active subset
            activeBlocks.forEach((block, index) => {
                let header = block.querySelector(".mcqgroup-question-header");
                if (!header) {
                    header = document.createElement("div");
                    header.className = "mcqgroup-question-header";
                    block.prepend(header);
                }
                header.textContent = `Question ${index + 1}`;
            });

            if (totalValue) totalValue.textContent = activeBlocks.length;
            totalIdxSpans.forEach((span) => (span.textContent = activeBlocks.length));
        }

        function lockAllInputs() {
            activeBlocks.forEach((block) => {
                const inputs = Array.from(block.querySelectorAll("input[type='radio'], input[type='checkbox']"));
                inputs.forEach((input) => {
                    input.disabled = true;
                });
            });
        }

        function unlockUncheckedInputs() {
            activeBlocks.forEach((block) => {
                if (block.dataset.checked !== "true") {
                    const inputs = Array.from(block.querySelectorAll("input[type='radio'], input[type='checkbox']"));
                    inputs.forEach((input) => {
                        input.disabled = false;
                    });
                }
            });
        }

        function setCheckboxesLock(locked) {
            if (showFeedbackCb) showFeedbackCb.disabled = locked;
            if (instantFeedbackCb) instantFeedbackCb.disabled = locked;
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

        function updateGroupStats(forceScoreCalculation = false) {
            let answered = 0;
            let score = 0;
            const isInstant = instantFeedbackCb ? instantFeedbackCb.checked : false;

            activeBlocks.forEach((block) => {
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

            if (progressCount) progressCount.textContent = `${answered} / ${activeBlocks.length}`;
            if (progressBarFill) {
                const percentage = activeBlocks.length > 0 ? (answered / activeBlocks.length) * 100 : 0;
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

            activeBlocks.forEach((block) => {
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

            // Reset instant feedback checkbox to its HTML default state
            if (instantFeedbackCb) {
                instantFeedbackCb.checked = instantFeedbackCb.defaultChecked;
            }

            // Pick a fresh random subset / reshuffle
            updateQuestionSubsetAndHeaders();

            // Reset state for all blocks in full container
            const allBlocks = Array.from(group.querySelectorAll(".multichoice-block"));
            allBlocks.forEach((block) => {
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

                const isShuffle =
                    block.dataset.multichoiceShuffle === "true" ||
                    block.dataset.shuffle === "true" ||
                    block.classList.contains("multichoice-shuffle");

                if (isShuffle) {
                    shuffleBlockChoices(block);
                }
            });

            // Keep Check Group Answers button disabled until quiz is started
            if (btnCheck) btnCheck.disabled = true;
            if (scoreValue) scoreValue.textContent = "0";
            currentIndex = 0;
            renderView();
            updateGroupStats();
        }

        // Explicit Page Load Locks
        setCheckboxesLock(false);
        resetQuizState();
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
                if (btnCheck) btnCheck.disabled = false; // Enable Check Answers on start
            });
        }

        // Wizard Navigation Handlers (Attached to all top/bottom buttons)
        btnsFirst.forEach((btn) => {
            btn.addEventListener("click", () => {
                currentIndex = 0;
                renderView();
            });
        });

        btnsPrev.forEach((btn) => {
            btn.addEventListener("click", () => {
                if (currentIndex > 0) {
                    currentIndex--;
                    renderView();
                }
            });
        });

        btnsNext.forEach((btn) => {
            btn.addEventListener("click", () => {
                if (currentIndex < activeBlocks.length - 1) {
                    currentIndex++;
                    renderView();
                }
            });
        });

        btnsLast.forEach((btn) => {
            btn.addEventListener("click", () => {
                currentIndex = activeBlocks.length - 1;
                renderView();
            });
        });

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

                activeBlocks.forEach((block) => {
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
                // instantFeedbackCb setting is intentionally preserved
                resetQuizState();
                lockAllInputs();
            });
        }

        // Intercept clicks before native radio selection happens if not started
        group.addEventListener(
            "click",
            (e) => {
                const choice = e.target.closest(".multichoice-choice");
                if (choice && !isQuizStarted) {
                    e.preventDefault();
                    e.stopPropagation();
                }
            },
            true
        );

        // Event Delegation for Option Selection
        group.addEventListener("change", (e) => {
            if (e.target.matches("input[type='radio'], input[type='checkbox']")) {
                if (
                    e.target.classList.contains("mcqgroup-show-feedback") ||
                    e.target.classList.contains("mcqgroup-instant-feedback")
                ) {
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

                    choices.forEach((c) => {
                        const input = c.querySelector("input");
                        c.classList.toggle("selected", input && input.checked);
                    });

                    if (instantFeedbackCb && instantFeedbackCb.checked && isSingle) {
                        block.dataset.checked = "true";
                        const radioInputs = Array.from(block.querySelectorAll("input[type='radio']"));

                        choices.forEach((c) => {
                            const input = c.querySelector("input");
                            const isCorrect = c.dataset.correct === "true";

                            c.classList.remove("multichoice-correct", "multichoice-incorrect");

                            if (input && input.checked) {
                                c.classList.add(isCorrect ? "multichoice-correct" : "multichoice-incorrect");
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
document.addEventListener("DOMContentLoaded", () => {
    const groupBlocks = Array.from(document.querySelectorAll(".quizgroup-block"));

    // --- UTILITIES ---
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
        const container = group.querySelector(".quizgroup-questions-container");
        if (!container) return;

        const blocks = Array.from(
            container.querySelectorAll(".multichoice-block, .cloze-block, .gapfill-block, .classifying-block, .fillin-block")
        );
        if (blocks.length <= 1) return;

        shuffleArray(blocks);
        blocks.forEach((b) => container.appendChild(b));
    }

    // --- POLYMORPHIC QUESTION ADAPTERS ---
    const QuestionAdapters = {
        // 1. Multichoice Question Adapter
        multichoice: {
            match: (block) => block.classList.contains("multichoice-block"),
            getType: () => "MCQ",
            getPoints: () => 1,
            isAnswered: (block) => {
                const inputs = Array.from(block.querySelectorAll("input[type='radio'], input[type='checkbox']"));
                return inputs.some((input) => input.checked);
            },
            isFullyAnswered: (block) => {
                const inputs = Array.from(block.querySelectorAll("input[type='radio'], input[type='checkbox']"));
                return inputs.some((input) => input.checked);
            },
            lock: (block) => {
                const inputs = block.querySelectorAll("input[type='radio'], input[type='checkbox']");
                inputs.forEach((input) => (input.disabled = true));
            },
            unlock: (block, isStarted) => {
                if (!isStarted || block.dataset.checked === "true") return;
                const inputs = block.querySelectorAll("input[type='radio'], input[type='checkbox']");
                inputs.forEach((input) => (input.disabled = false));
            },
            clearValidation: (block) => {
                const choices = block.querySelectorAll(".multichoice-choice");
                choices.forEach((choice) => {
                    choice.classList.remove("multichoice-correct", "multichoice-incorrect", "multichoice-answer");
                    const exp = choice.querySelector(".multichoice-explanation");
                    if (exp) exp.style.display = "none";
                });
            },
            reset: (block) => {
                delete block.dataset.checked;
                const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
                choices.forEach((choice) => {
                    const input = choice.querySelector("input");
                    if (input) {
                        input.checked = false;
                        input.disabled = true;
                    }
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
            },
            evaluate: (block, isInstant = false) => {
                const choices = Array.from(block.querySelectorAll(".multichoice-choice"));
                if (choices.length === 0) return { score: 0, maxScore: 1 };

                const isAnswered = QuestionAdapters.multichoice.isAnswered(block);

                if (isInstant && !isAnswered) {
                    QuestionAdapters.multichoice.clearValidation(block);
                    return { score: 0, maxScore: 1 };
                }

                let blockIsFullyCorrect = true;
                let selectedCount = 0;

                choices.forEach((choice) => {
                    const input = choice.querySelector("input[type='radio'], input[type='checkbox']");
                    const isChecked = input ? input.checked : false;
                    const isAnswerCorrect = choice.dataset.correct === "true";
                    const exp = choice.querySelector(".multichoice-explanation");

                    choice.classList.remove("multichoice-correct", "multichoice-incorrect", "multichoice-answer");
                    if (exp) exp.style.display = "none";

                    if (isChecked) {
                        selectedCount++;
                        if (isAnswerCorrect) {
                            choice.classList.add("multichoice-correct");
                        } else {
                            choice.classList.add("multichoice-incorrect");
                            blockIsFullyCorrect = false;
                        }
                        if (exp) exp.style.display = "block";
                    } else if (isAnswerCorrect) {
                        blockIsFullyCorrect = false;
                    }
                });

                if (isInstant && isAnswered) {
                    block.dataset.checked = "true";
                    QuestionAdapters.multichoice.lock(block);
                }

                const isCorrect = selectedCount > 0 && blockIsFullyCorrect;
                return { score: isCorrect ? 1 : 0, maxScore: 1 };
            },
        },

        // 2. Cloze Drag-and-Drop Adapter
        cloze: {
            match: (block) => block.classList.contains("cloze-block"),
            getType: () => "Cloze",
            getPoints: (block) => block.querySelectorAll(".cloze-dropzone").length,

            isZoneFilled: (zone) => {
                const rawText = zone.textContent.trim().replace(/^Drop here$/i, "");
                const hasChild = zone.children.length > 0 || zone.querySelector("*") !== null;
                const hasDataWord = zone.dataset && zone.dataset.word && zone.dataset.word.trim().length > 0;
                return hasChild || rawText.length > 0 || hasDataWord;
            },

            isAnswered: (block) => {
                const dropzones = Array.from(block.querySelectorAll(".cloze-dropzone"));
                return dropzones.some((zone) => QuestionAdapters.cloze.isZoneFilled(zone));
            },

            isFullyAnswered: (block) => {
                const dropzones = Array.from(block.querySelectorAll(".cloze-dropzone"));
                return dropzones.length > 0 && dropzones.every((zone) => QuestionAdapters.cloze.isZoneFilled(zone));
            },

            lock: (block) => {
                const dropzones = block.querySelectorAll(".cloze-dropzone");
                dropzones.forEach((zone) => zone.classList.add("disabled"));
            },

            unlock: (block, isStarted) => {
                if (!isStarted || block.dataset.checked === "true") return;
                const dropzones = block.querySelectorAll(".cloze-dropzone");
                dropzones.forEach((zone) => zone.classList.remove("disabled"));
            },

            clearValidation: (block) => {
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
            },

            reset: (block) => {
                delete block.dataset.checked;
                const dropzones = block.querySelectorAll(".cloze-dropzone");
                dropzones.forEach((zone) => {
                    zone.innerHTML = "Drop here";
                    zone.className = "cloze-dropzone disabled";
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
            },

            evaluate: (block, isInstant = false) => {
                const dropzones = Array.from(block.querySelectorAll(".cloze-dropzone"));
                const fullyAnswered = QuestionAdapters.cloze.isFullyAnswered(block);

                if (isInstant && !fullyAnswered) {
                    QuestionAdapters.cloze.clearValidation(block);
                    return { score: 0, maxScore: dropzones.length };
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

                if (isInstant && fullyAnswered) {
                    block.dataset.checked = "true";
                    QuestionAdapters.cloze.lock(block);
                }

                return { score: correctCount, maxScore: dropzones.length };
            },
        },

        // 3. Gap Fill Adapter
        gapfill: {
            match: (block) => block.classList.contains("gapfill-block"),
            getType: () => "GapFill",
            getPoints: (block) => block.querySelectorAll(".gapfill-dropdown, .gapfill-input").length,
            isAnswered: (block) => {
                const inputs = Array.from(block.querySelectorAll(".gapfill-dropdown, .gapfill-input"));
                return inputs.some((input) => input.value.trim() !== "");
            },
            isFullyAnswered: (block) => {
                const inputs = Array.from(block.querySelectorAll(".gapfill-dropdown, .gapfill-input"));
                return inputs.length > 0 && inputs.every((input) => input.value.trim() !== "");
            },
            lock: (block) => {
                const inputs = block.querySelectorAll(".gapfill-dropdown, .gapfill-input");
                inputs.forEach((input) => (input.disabled = true));
            },
            unlock: (block, isStarted) => {
                if (!isStarted || block.dataset.checked === "true") return;
                const inputs = block.querySelectorAll(".gapfill-dropdown, .gapfill-input");
                inputs.forEach((input) => (input.disabled = false));
            },
            clearValidation: (block) => {
                const inputs = block.querySelectorAll(".gapfill-dropdown, .gapfill-input");
                inputs.forEach((input) => {
                    input.classList.remove("correct", "incorrect");
                    const feedback = input.nextElementSibling;
                    if (feedback && feedback.classList.contains("gapfill-inline-feedback")) {
                        feedback.textContent = "";
                        feedback.className = "gapfill-inline-feedback";
                    }
                });
            },
            reset: (block) => {
                delete block.dataset.checked;
                const inputs = block.querySelectorAll(".gapfill-dropdown, .gapfill-input");
                inputs.forEach((input) => {
                    input.value = "";
                    input.disabled = true;
                    input.classList.remove("correct", "incorrect");
                    const feedback = input.nextElementSibling;
                    if (feedback && feedback.classList.contains("gapfill-inline-feedback")) {
                        feedback.textContent = "";
                        feedback.className = "gapfill-inline-feedback";
                    }
                });
            },
            evaluate: (block, isInstant = false) => {
                const inputs = Array.from(block.querySelectorAll(".gapfill-dropdown, .gapfill-input"));
                const fullyAnswered = QuestionAdapters.gapfill.isFullyAnswered(block);

                if (isInstant && !fullyAnswered) {
                    QuestionAdapters.gapfill.clearValidation(block);
                    return { score: 0, maxScore: inputs.length };
                }

                let correctCount = 0;

                inputs.forEach((input) => {
                    const val = input.value.trim();
                    const expectedValue = input.dataset.correct ? input.dataset.correct.trim() : "";
                    const feedbackBadge = input.nextElementSibling;

                    input.classList.remove("correct", "incorrect");

                    const isCorrect = val && val === expectedValue;
                    if (isCorrect) {
                        input.classList.add("correct");
                        correctCount++;
                        if (feedbackBadge && feedbackBadge.classList.contains("gapfill-inline-feedback")) {
                            feedbackBadge.textContent = " ✓";
                            feedbackBadge.className = "gapfill-inline-feedback text-correct";
                        }
                    } else if (val || !isInstant) {
                        input.classList.add("incorrect");
                        if (feedbackBadge && feedbackBadge.classList.contains("gapfill-inline-feedback")) {
                            feedbackBadge.textContent = ` ✕ (Ans: ${expectedValue})`;
                            feedbackBadge.className = "gapfill-inline-feedback text-incorrect";
                        }
                    }
                });

                if (isInstant && fullyAnswered) {
                    block.dataset.checked = "true";
                    QuestionAdapters.gapfill.lock(block);
                }

                return { score: correctCount, maxScore: inputs.length };
            },
        },

        // 4. Classifying Adapter
        classifying: {
            match: (block) => block.classList.contains("classifying-block"),
            getType: () => "Classifying",
            getPoints: (block) => block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input").length,
            isAnswered: (block) => {
                const selects = Array.from(block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input"));
                return selects.some((select) => select.value !== "");
            },
            isFullyAnswered: (block) => {
                const selects = Array.from(block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input"));
                return selects.length > 0 && selects.every((select) => select.value !== "");
            },
            lock: (block) => {
                const selects = block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input");
                selects.forEach((select) => (select.disabled = true));
            },
            unlock: (block, isStarted) => {
                if (!isStarted || block.dataset.checked === "true") return;
                const selects = block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input");
                selects.forEach((select) => (select.disabled = false));
            },
            clearValidation: (block) => {
                const rows = block.querySelectorAll(".classifying-line");
                rows.forEach((row) => row.classList.remove("correct-line", "incorrect-line"));
            },
            reset: (block) => {
                delete block.dataset.checked;
                const selects = block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input");
                const rows = block.querySelectorAll(".classifying-line");

                selects.forEach((select) => {
                    select.value = "";
                    select.disabled = true;
                });
                rows.forEach((row) => row.classList.remove("correct-line", "incorrect-line"));
            },
            evaluate: (block, isInstant = false) => {
                const selects = Array.from(block.querySelectorAll(".sorting-select, .classifying-dropdown, .classifying-input"));
                const rows = Array.from(block.querySelectorAll(".classifying-line"));
                const fullyAnswered = QuestionAdapters.classifying.isFullyAnswered(block);

                if (isInstant && !fullyAnswered) {
                    QuestionAdapters.classifying.clearValidation(block);
                    return { score: 0, maxScore: selects.length };
                }

                let correctCount = 0;

                selects.forEach((select, idx) => {
                    const row = rows[idx];
                    const val = select.value;
                    const correctBin = select.getAttribute("data-correct-bin") || select.getAttribute("data-correct");

                    if (row) row.classList.remove("correct-line", "incorrect-line");

                    if (val !== "" && val === correctBin) {
                        correctCount++;
                        if (row) row.classList.add("correct-line");
                    } else if (val !== "" || !isInstant) {
                        if (row) row.classList.add("incorrect-line");
                    }
                });

                if (isInstant && fullyAnswered) {
                    block.dataset.checked = "true";
                    QuestionAdapters.classifying.lock(block);
                }

                return { score: correctCount, maxScore: selects.length };
            },
        },

        // 5. Fill-In Adapter
        fillin: {
            match: (block) => block.classList.contains("fillin-block"),
            getType: () => "Fill-In",
            getPoints: (block) => block.querySelectorAll(".fillin-input").length,
            isAnswered: (block) => {
                const inputs = Array.from(block.querySelectorAll(".fillin-input"));
                return inputs.some((input) => input.value.trim() !== "");
            },
            isFullyAnswered: (block) => {
                const inputs = Array.from(block.querySelectorAll(".fillin-input"));
                return inputs.length > 0 && inputs.every((input) => input.value.trim() !== "");
            },
            lock: (block) => {
                const inputs = block.querySelectorAll(".fillin-input");
                inputs.forEach((input) => (input.disabled = true));
            },
            unlock: (block, isStarted) => {
                if (!isStarted || block.dataset.checked === "true") return;
                const inputs = block.querySelectorAll(".fillin-input");
                inputs.forEach((input) => (input.disabled = false));
            },
            clearValidation: (block) => {
                const inputs = block.querySelectorAll(".fillin-input");
                inputs.forEach((input) => {
                    input.classList.remove("correct", "incorrect");
                    const feedbackBadge = input.nextElementSibling;
                    if (feedbackBadge && feedbackBadge.classList.contains("fillin-inline-feedback")) {
                        feedbackBadge.textContent = "";
                        feedbackBadge.className = "fillin-inline-feedback";
                    }
                });
            },
            reset: (block) => {
                delete block.dataset.checked;
                const inputs = block.querySelectorAll(".fillin-input");
                inputs.forEach((input) => {
                    input.value = "";
                    input.disabled = true;
                    input.classList.remove("correct", "incorrect");
                    const feedbackBadge = input.nextElementSibling;
                    if (feedbackBadge && feedbackBadge.classList.contains("fillin-inline-feedback")) {
                        feedbackBadge.textContent = "";
                        feedbackBadge.className = "fillin-inline-feedback";
                    }
                });
            },
            evaluate: (block, isInstant = false, triggerMode = "input") => {
                const inputs = Array.from(block.querySelectorAll(".fillin-input"));
                const fullyAnswered = QuestionAdapters.fillin.isFullyAnswered(block);

                // Delay instant feedback evaluation while actively typing
                if (isInstant && triggerMode === "input" && block.dataset.checked !== "true") {
                    return { score: 0, maxScore: inputs.length };
                }

                if (isInstant && !fullyAnswered && block.dataset.checked !== "true" && triggerMode !== "focusout") {
                    QuestionAdapters.fillin.clearValidation(block);
                    return { score: 0, maxScore: inputs.length };
                }

                let correctCount = 0;

                inputs.forEach((input) => {
                    const userVal = input.value.trim();
                    const expectedValue = input.dataset.correct ? input.dataset.correct.trim() : "";
                    const isCaseSensitive = input.dataset.caseSensitive === "true";
                    const feedbackBadge = input.nextElementSibling;

                    // Do not mark individual empty fields as incorrect while using instant feedback
                    if (isInstant && userVal === "" && block.dataset.checked !== "true") {
                        input.classList.remove("correct", "incorrect");
                        if (feedbackBadge && feedbackBadge.classList.contains("fillin-inline-feedback")) {
                            feedbackBadge.textContent = "";
                            feedbackBadge.className = "fillin-inline-feedback";
                        }
                        return;
                    }

                    input.classList.remove("correct", "incorrect");

                    let isCorrect = false;
                    if (isCaseSensitive) {
                        isCorrect = userVal === expectedValue;
                    } else {
                        isCorrect = userVal.toLowerCase() === expectedValue.toLowerCase();
                    }

                    if (userVal !== "" && isCorrect) {
                        input.classList.add("correct");
                        correctCount++;
                        if (feedbackBadge && feedbackBadge.classList.contains("fillin-inline-feedback")) {
                            feedbackBadge.textContent = " ✓";
                            feedbackBadge.className = "fillin-inline-feedback text-correct";
                        }
                    } else if (userVal !== "" || !isInstant) {
                        input.classList.add("incorrect");
                        if (feedbackBadge && feedbackBadge.classList.contains("fillin-inline-feedback")) {
                            feedbackBadge.textContent = ` ✕ (Ans: ${expectedValue})`;
                            feedbackBadge.className = "fillin-inline-feedback text-incorrect";
                        }
                    }
                });

                if (isInstant && fullyAnswered) {
                    block.dataset.checked = "true";
                    QuestionAdapters.fillin.lock(block);
                }

                return { score: correctCount, maxScore: inputs.length };
            },
        },
    };

    function getAdapterForBlock(block) {
        if (QuestionAdapters.multichoice.match(block)) return QuestionAdapters.multichoice;
        if (QuestionAdapters.cloze.match(block)) return QuestionAdapters.cloze;
        if (QuestionAdapters.gapfill.match(block)) return QuestionAdapters.gapfill;
        if (QuestionAdapters.classifying.match(block)) return QuestionAdapters.classifying;
        if (QuestionAdapters.fillin.match(block)) return QuestionAdapters.fillin;
        return null;
    }

    // --- GROUP CONTROLLER ---
    groupBlocks.forEach((group) => {
        const nativePanels = group.querySelectorAll(
            ".cloze-global-panel, .multichoice-control-panel, .mcq-global-panel, .gapfill-global-panel, .classifying-controls, .fillin-global-panel"
        );
        nativePanels.forEach((p) => p.remove());

        const allOriginalBlocks = Array.from(
            group.querySelectorAll(".multichoice-block, .cloze-block, .gapfill-block, .classifying-block, .fillin-block")
        );
        if (allOriginalBlocks.length === 0) return;

        const numQAttr = group.dataset.numQuestions;
        const numQuestionsTarget = numQAttr ? parseInt(numQAttr, 10) : null;

        let activeBlocks = [];
        let currentIndex = 0;
        let isWizardMode = true;
        let isQuizStarted = false;
        let activePollTimer = null;

        // UI Elements
        const progressCount = group.querySelector(".quizgroup-progress-count");
        const progressBarFill = group.querySelector(".quizgroup-progress-bar-fill");
        const scoreValue = group.querySelector(".quizgroup-score-value");
        const totalValue = group.querySelector(".quizgroup-total-value");
        const btnStart = group.querySelector(".quizgroup-btn-start");
        const btnToggle = group.querySelector(".quizgroup-btn-toggle");
        const btnCheck = group.querySelector(".quizgroup-btn-check");
        const btnReset = group.querySelector(".quizgroup-btn-reset");
        const chkInstantFeedback = group.querySelector(".quizgroup-toggle-instant-feedback");

        const navBars = group.querySelectorAll(".quizgroup-nav-bar");
        const bottomBar = group.querySelector(".quizgroup-bottom-bar");
        const btnScrollTop = group.querySelector(".quizgroup-btn-scroll-top");

        const btnsFirst = Array.from(group.querySelectorAll(".quizgroup-btn-first"));
        const btnsPrev = Array.from(group.querySelectorAll(".quizgroup-btn-prev"));
        const btnsNext = Array.from(group.querySelectorAll(".quizgroup-btn-next"));
        const btnsLast = Array.from(group.querySelectorAll(".quizgroup-btn-last"));

        const currentIdxSpans = group.querySelectorAll(".quizgroup-current-idx");
        const totalIdxSpans = group.querySelectorAll(".quizgroup-total-idx");

        function getMaxScoreForActiveSubset() {
            let maxScore = 0;
            activeBlocks.forEach((block) => {
                const adapter = getAdapterForBlock(block);
                if (adapter) maxScore += adapter.getPoints(block);
            });
            return maxScore;
        }

        function updateQuestionSubsetAndHeaders() {
            if (group.dataset.shuffleQuestions === "true" || numQuestionsTarget) {
                shuffleQuestions(group);
            }

            const currentDOMBlocks = Array.from(
                group.querySelectorAll(".multichoice-block, .cloze-block, .gapfill-block, .classifying-block, .fillin-block")
            );

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
                const adapter = getAdapterForBlock(block);
                const typeLabel = adapter ? adapter.getType() : "Question";

                let header = block.querySelector(".quizgroup-question-header");
                if (!header) {
                    header = document.createElement("div");
                    header.className = "quizgroup-question-header";
                    block.prepend(header);
                }
                header.textContent = `${typeLabel} ${index + 1}`;
            });

            const maxScore = getMaxScoreForActiveSubset();
            if (totalValue) totalValue.textContent = maxScore;
            totalIdxSpans.forEach((span) => (span.textContent = activeBlocks.length));
        }

        function lockAll() {
            activeBlocks.forEach((block) => {
                const adapter = getAdapterForBlock(block);
                if (adapter) adapter.lock(block);
            });
        }

        function unlockAll() {
            activeBlocks.forEach((block) => {
                const adapter = getAdapterForBlock(block);
                if (adapter) adapter.unlock(block, isQuizStarted);
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

        function updateGroupStats(triggerMode = "input") {
            const isChecked = group.dataset.groupChecked === "true";
            const isInstantFeedback = chkInstantFeedback && chkInstantFeedback.checked;

            if (!isQuizStarted && !isChecked) {
                activeBlocks.forEach((block) => {
                    const adapter = getAdapterForBlock(block);
                    if (adapter) adapter.clearValidation(block);
                });
                if (progressCount) progressCount.textContent = "0%";
                if (progressBarFill) progressBarFill.style.width = "0%";
                if (scoreValue) scoreValue.textContent = "0";
                return;
            }

            let answeredCount = 0;
            let totalPointsEarned = 0;

            activeBlocks.forEach((block) => {
                const adapter = getAdapterForBlock(block);
                if (!adapter) return;

                if (adapter.isAnswered(block)) {
                    answeredCount++;
                }

                if (isChecked) {
                    const res = adapter.evaluate(block, false, triggerMode);
                    totalPointsEarned += res.score;
                } else if (isInstantFeedback) {
                    const res = adapter.evaluate(block, true, triggerMode);
                    totalPointsEarned += res.score;
                } else {
                    adapter.clearValidation(block);
                }
            });

            const totalQuestions = activeBlocks.length;
            const percentage = totalQuestions > 0 ? Math.round((answeredCount / totalQuestions) * 100) : 0;

            if (progressCount) progressCount.textContent = `${percentage}%`;
            if (progressBarFill) progressBarFill.style.width = `${percentage}%`;

            if (scoreValue) {
                scoreValue.textContent = isChecked || isInstantFeedback ? totalPointsEarned : "0";
            }
        }

        function triggerShortPolling() {
            if (activePollTimer) clearInterval(activePollTimer);
            let count = 0;
            activePollTimer = setInterval(() => {
                updateGroupStats("poll");
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
                    updateGroupStats("change");
                });
                observer.observe(zone, { childList: true, subtree: true, attributes: false });
            });
        }

        function resetQuizState() {
            isQuizStarted = false;
            delete group.dataset.groupChecked;
            if (activePollTimer) clearInterval(activePollTimer);

            if (chkInstantFeedback) {
                chkInstantFeedback.checked = chkInstantFeedback.defaultChecked;
            }

            updateQuestionSubsetAndHeaders();

            activeBlocks.forEach((block) => {
                const adapter = getAdapterForBlock(block);
                if (adapter) adapter.reset(block);
            });

            if (btnCheck) btnCheck.disabled = true;
            if (btnStart) btnStart.disabled = false;
            if (scoreValue) scoreValue.textContent = "0";
            currentIndex = 0;
            renderView();
            updateGroupStats("reset");
            lockAll();
        }

        // Comprehensive interaction lock before start or after completion
        const blockEventTypes = ["click", "mousedown", "pointerdown", "focusin"];
        blockEventTypes.forEach((eventType) => {
            group.addEventListener(
                eventType,
                (e) => {
                    if (isQuizStarted) return;
                    const isControlBtn = e.target.closest(
                        ".quizgroup-action-bar, .quizgroup-nav-bar, .quizgroup-bottom-bar, .quizgroup-btn-toggle"
                    );
                    if (!isControlBtn) {
                        e.preventDefault();
                        e.stopPropagation();
                        if (document.activeElement && typeof document.activeElement.blur === "function") {
                            document.activeElement.blur();
                        }
                    }
                },
                true
            );
        });

        // Initial setup
        setCheckboxesLock(false);
        resetQuizState();
        setupDropzoneObservers();

        // Event Listeners
        if (chkInstantFeedback) {
            chkInstantFeedback.addEventListener("change", () => updateGroupStats("change"));
        }

        if (btnScrollTop) {
            btnScrollTop.addEventListener("click", () => {
                group.scrollIntoView({ behavior: "smooth", block: "start" });
            });
        }

        if (btnStart) {
            btnStart.addEventListener("click", () => {
                resetQuizState();
                isQuizStarted = true;

                activeBlocks.forEach((block) => {
                    const adapter = getAdapterForBlock(block);
                    if (adapter) adapter.clearValidation(block);
                });

                unlockAll();
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
                lockAll();
                updateGroupStats("check");
            });
        }

        if (btnReset) {
            btnReset.addEventListener("click", () => {
                isQuizStarted = false;
                setCheckboxesLock(false);
                if (btnStart) btnStart.disabled = false;
                resetQuizState();
            });
        }

        // Direct event triggers for text input typing or selecting options
        group.addEventListener("input", () => updateGroupStats("input"));
        group.addEventListener("change", () => updateGroupStats("change"));
        group.addEventListener("focusout", (e) => {
            if (e.target && e.target.classList.contains("fillin-input")) {
                updateGroupStats("focusout");
            }
        });
        group.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && e.target && e.target.classList.contains("fillin-input")) {
                updateGroupStats("focusout");
            }
        });
        group.addEventListener("click", triggerShortPolling);
        group.addEventListener("drop", triggerShortPolling);
        group.addEventListener("dragend", triggerShortPolling);
        group.addEventListener("touchend", triggerShortPolling);
    });
});
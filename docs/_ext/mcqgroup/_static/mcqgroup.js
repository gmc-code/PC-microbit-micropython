document.addEventListener("DOMContentLoaded", () => {
    const groups = document.querySelectorAll(".mcqgroup-block");

    function shuffle(a) {
        for (let i = a.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [a[i], a[j]] = [a[j], a[i]];
        }
    }

    function assignLetters(choices) {
        const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        choices.forEach((c, i) => {
            const s = c.querySelector(".multichoice-letter");
            if (s) s.textContent = letters[i] || "";
        });
    }

    function shuffleChoices(block) {
        const choices = [...block.querySelectorAll(".multichoice-choice")];
        if (choices.length < 2) return;
        const parent = choices[0].parentNode;
        shuffle(choices);
        choices.forEach(c => parent.appendChild(c));
        if (block.dataset.multichoiceLetters !== "false") {
            assignLetters(choices);
        }
    }

    groups.forEach(group => {
        const container = group.querySelector(".mcqgroup-questions-container");
        if (!container) return;

        /*
         * Do NOT remove individual MCQ controls here.
         * CSS already hides them.
         */

        const progress = group.querySelector(".mcqgroup-progress-count");
        const progressBar = group.querySelector(".mcqgroup-progress-bar-fill");
        const score = group.querySelector(".mcqgroup-score-value");
        const total = group.querySelector(".mcqgroup-total-value");

        const start = group.querySelector(".mcqgroup-btn-start");
        const toggle = group.querySelector(".mcqgroup-btn-toggle");
        const check = group.querySelector(".mcqgroup-btn-check");
        const reset = group.querySelector(".mcqgroup-btn-reset");

        const feedback = group.querySelector(".mcqgroup-show-feedback");
        const instant = group.querySelector(".mcqgroup-instant-feedback");

        const navBars = group.querySelectorAll(".mcqgroup-nav-bar");
        const bottomBar = group.querySelector(".mcqgroup-bottom-bar");
        const scrollTop = group.querySelector(".mcqgroup-btn-scroll-top");

        const firstBtns = group.querySelectorAll(".mcqgroup-btn-first");
        const prevBtns = group.querySelectorAll(".mcqgroup-btn-prev");
        const nextBtns = group.querySelectorAll(".mcqgroup-btn-next");
        const lastBtns = group.querySelectorAll(".mcqgroup-btn-last");

        const currentSpans = group.querySelectorAll(".mcqgroup-current-idx");
        const totalSpans = group.querySelectorAll(".mcqgroup-total-idx");

        const numQ = group.dataset.numQuestions
            ? parseInt(group.dataset.numQuestions, 10)
            : null;

        const shuffleQuestions =
            group.dataset.shuffleQuestions === "true";

        let activeBlocks = [];
        let currentIndex = 0;
        let wizardMode = true;
        let quizStarted = false;

        function prepareQuestions() {
            let blocks = [...container.querySelectorAll(".multichoice-block")];

            if (
                shuffleQuestions ||
                (numQ && numQ < blocks.length)
            ) {
                shuffle(blocks);
                blocks.forEach(b => container.appendChild(b));
            }

            activeBlocks =
                numQ && numQ < blocks.length
                    ? blocks.slice(0, numQ)
                    : blocks;

            blocks.forEach(b => {
                b.style.display = activeBlocks.includes(b) ? "" : "none";
                delete b.dataset.activeQuestion;
            });

            activeBlocks.forEach((block, i) => {
                block.dataset.activeQuestion = "true";

                let header =
                    block.querySelector(".mcqgroup-question-header");

                if (!header) {
                    header = document.createElement("div");
                    header.className = "mcqgroup-question-header";
                    block.prepend(header);
                }

                header.textContent = `Question ${i + 1}`;
            });

            if (total) total.textContent = activeBlocks.length;
            totalSpans.forEach(s => s.textContent = activeBlocks.length);

            if (currentIndex >= activeBlocks.length) {
                currentIndex = Math.max(0, activeBlocks.length - 1);
            }
        }

        function lockInputs() {
            activeBlocks.forEach(block => {
                block.querySelectorAll(
                    "input[type='radio'],input[type='checkbox']"
                ).forEach(input => input.disabled = true);
            });
        }

        function unlockInputs() {
            activeBlocks.forEach(block => {
                if (block.dataset.checked !== "true") {
                    block.querySelectorAll(
                        "input[type='radio'],input[type='checkbox']"
                    ).forEach(input => input.disabled = false);
                }
            });
        }

        function lockControls(locked) {
            if (feedback) feedback.disabled = locked;
            if (instant) instant.disabled = locked;
        }

        function render() {
            if (wizardMode) {
                group.dataset.viewMode = "wizard";

                activeBlocks.forEach((block, i) => {
                    block.style.display =
                        i === currentIndex ? "block" : "none";
                });

                navBars.forEach(b => b.style.display = "flex");
                if (bottomBar) bottomBar.style.display = "none";

                currentSpans.forEach(
                    s => s.textContent = currentIndex + 1
                );

                const first = currentIndex === 0;
                const last =
                    currentIndex === activeBlocks.length - 1;

                firstBtns.forEach(b => b.disabled = first);
                prevBtns.forEach(b => b.disabled = first);
                nextBtns.forEach(b => b.disabled = last);
                lastBtns.forEach(b => b.disabled = last);

                if (toggle) toggle.textContent = "All Q Mode";
            } else {
                group.dataset.viewMode = "all";

                activeBlocks.forEach(
                    block => block.style.display = "block"
                );

                navBars.forEach(b => b.style.display = "none");
                if (bottomBar) bottomBar.style.display = "flex";

                if (toggle) toggle.textContent = "1 Q Mode";
            }
        }

        function updateStats(forceScore = false) {
            let answered = 0;
            let points = 0;

            activeBlocks.forEach(block => {
                const inputs = [...block.querySelectorAll("input")];
                const answeredThis =
                    inputs.some(input => input.checked);

                if (answeredThis) answered++;

                const shouldScore =
                    forceScore ||
                    (instant && instant.checked) ||
                    block.dataset.checked === "true" ||
                    group.dataset.groupChecked === "true";

                if (!shouldScore || !answeredThis) return;

                const single =
                    block.dataset.multichoiceSingle === "true";

                if (single) {
                    const selected =
                        block.querySelector("input:checked");

                    if (
                        selected &&
                        selected.closest(".multichoice-choice")
                            ?.dataset.correct === "true"
                    ) {
                        points++;
                    }
                } else {
                    const choices =
                        [...block.querySelectorAll(".multichoice-choice")];

                    const correct = choices.every(choice => {
                        const input = choice.querySelector("input");
                        return (
                            (input?.checked || false) ===
                            (choice.dataset.correct === "true")
                        );
                    });

                    if (correct) points++;
                }
            });

            if (progress) {
                progress.textContent =
                    `${answered} / ${activeBlocks.length}`;
            }

            if (progressBar) {
                progressBar.style.width =
                    `${activeBlocks.length
                        ? answered / activeBlocks.length * 100
                        : 0}%`;
            }

            if (
                score &&
                (forceScore ||
                    (instant && instant.checked) ||
                    group.dataset.groupChecked === "true")
            ) {
                score.textContent = points;
            }
        }

        function showExplanations() {
            const show = feedback ? feedback.checked : false;

            activeBlocks.forEach(block => {
                const checked = block.dataset.checked === "true";

                block.querySelectorAll(".multichoice-choice")
                    .forEach(choice => {
                        const exp =
                            choice.querySelector(".multichoice-explanation");

                        if (!exp) return;

                        const input = choice.querySelector("input");
                        const correct =
                            choice.dataset.correct === "true";

                        exp.style.display =
                            checked &&
                            show &&
                            ((input && input.checked) || correct)
                                ? "block"
                                : "none";
                    });
            });
        }

        /*
         * Reset ANSWERS only.
         *
         * IMPORTANT:
         * Instant Feedback is deliberately untouched.
         */
        function resetQuizState() {
            delete group.dataset.groupChecked;

            prepareQuestions();

            container.querySelectorAll(".multichoice-block")
                .forEach(block => {
                    delete block.dataset.checked;

                    block.querySelectorAll("input").forEach(
                        input => input.checked = false
                    );

                    block.querySelectorAll(".multichoice-choice")
                        .forEach(choice => {
                            choice.classList.remove(
                                "multichoice-correct",
                                "multichoice-incorrect",
                                "multichoice-answer",
                                "selected"
                            );

                            const exp =
                                choice.querySelector(
                                    ".multichoice-explanation"
                                );

                            if (exp) exp.style.display = "none";
                        });

                    const shouldShuffle =
                        block.dataset.multichoiceShuffle === "true" ||
                        block.dataset.shuffle === "true" ||
                        block.classList.contains("multichoice-shuffle");

                    if (shouldShuffle) shuffleChoices(block);
                });

            if (check) check.disabled = true;
            if (score) score.textContent = "0";

            currentIndex = 0;
            render();
            updateStats();
        }

        /*
         * INITIALISE
         */
        prepareQuestions();

        if (feedback) feedback.checked = false;

        /*
         * Do NOT reset instant.checked here.
         * Its original HTML state is preserved.
         */
        resetQuizState();
        lockInputs();
        lockControls(false);

        /*
         * START
         */
        if (start) {
            start.addEventListener("click", () => {
                quizStarted = true;

                /*
                 * Reset answers only.
                 * Instant Feedback checkbox is NOT changed.
                 */
                resetQuizState();

                unlockInputs();
                lockControls(true);

                start.disabled = true;
                if (check) check.disabled = false;
            });
        }

        /*
         * NAVIGATION
         */
        firstBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                currentIndex = 0;
                render();
            });
        });

        prevBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                if (currentIndex > 0) {
                    currentIndex--;
                    render();
                }
            });
        });

        nextBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                if (currentIndex < activeBlocks.length - 1) {
                    currentIndex++;
                    render();
                }
            });
        });

        lastBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                currentIndex = activeBlocks.length - 1;
                render();
            });
        });

        /*
         * WIZARD / ALL Q
         */
        if (toggle) {
            toggle.addEventListener("click", () => {
                wizardMode = !wizardMode;
                render();
            });
        }

        /*
         * CHECK GROUP
         */
        if (check) {
            check.addEventListener("click", () => {
                group.dataset.groupChecked = "true";

                /*
                 * Do not change Instant Feedback.
                 */
                lockControls(false);

                if (start) start.disabled = false;
                check.disabled = true;

                activeBlocks.forEach(block => {
                    block.dataset.checked = "true";

                    const choices =
                        [...block.querySelectorAll(".multichoice-choice")];

                    block.querySelectorAll("input").forEach(
                        input => input.disabled = true
                    );

                    choices.forEach(choice => {
                        const input = choice.querySelector("input");
                        const correct =
                            choice.dataset.correct === "true";

                        choice.classList.remove(
                            "multichoice-correct",
                            "multichoice-incorrect"
                        );

                        if (input && input.checked) {
                            choice.classList.add(
                                correct
                                    ? "multichoice-correct"
                                    : "multichoice-incorrect"
                            );
                        } else if (correct) {
                            choice.classList.add(
                                "multichoice-answer"
                            );
                        }
                    });
                });

                showExplanations();
                updateStats(true);
            });
        }

        /*
         * SHOW FEEDBACK
         */
        if (feedback) {
            feedback.addEventListener("change", showExplanations);
        }

        /*
         * INSTANT FEEDBACK
         */
        if (instant) {
            instant.addEventListener("change", () => {
                if (
                    !instant.checked &&
                    quizStarted &&
                    group.dataset.groupChecked !== "true"
                ) {
                    unlockInputs();
                }

                updateStats();
                showExplanations();
            });
        }

        /*
         * RESET
         */
        if (reset) {
            reset.addEventListener("click", () => {
                quizStarted = false;

                if (start) start.disabled = false;

                if (feedback) feedback.checked = false;

                /*
                 * IMPORTANT:
                 * Instant Feedback is deliberately preserved.
                 */

                resetQuizState();
                lockInputs();
                lockControls(false);
            });
        }

        /*
         * QUESTION INPUT CHANGES
         *
         * No capture-phase click interception.
         * This allows the individual multichoice JS to continue
         * receiving its normal events.
         */
        group.addEventListener("change", e => {
            const input = e.target;

            if (
                !input.matches(
                    "input[type='radio'],input[type='checkbox']"
                )
            ) {
                return;
            }

            if (
                input.classList.contains("mcqgroup-show-feedback") ||
                input.classList.contains("mcqgroup-instant-feedback")
            ) {
                return;
            }

            if (!quizStarted) return;

            const block = input.closest(".multichoice-block");

            if (
                !block ||
                block.dataset.checked === "true" ||
                group.dataset.groupChecked === "true"
            ) {
                return;
            }

            block.querySelectorAll(".multichoice-choice")
                .forEach(choice => {
                    const choiceInput =
                        choice.querySelector("input");

                    choice.classList.toggle(
                        "selected",
                        !!(choiceInput && choiceInput.checked)
                    );
                });

            /*
             * Single-answer instant feedback.
             */
            if (
                instant &&
                instant.checked &&
                block.dataset.multichoiceSingle === "true"
            ) {
                block.dataset.checked = "true";

                const choices =
                    [...block.querySelectorAll(".multichoice-choice")];

                choices.forEach(choice => {
                    const choiceInput =
                        choice.querySelector("input");

                    const correct =
                        choice.dataset.correct === "true";

                    choice.classList.remove(
                        "multichoice-correct",
                        "multichoice-incorrect"
                    );

                    if (choiceInput && choiceInput.checked) {
                        choice.classList.add(
                            correct
                                ? "multichoice-correct"
                                : "multichoice-incorrect"
                        );
                    }
                });

                block.querySelectorAll(
                    "input[type='radio']"
                ).forEach(input => input.disabled = true);

                showExplanations();
            }

            updateStats();
        });

        /*
         * BACK TO TOP
         */
        if (scrollTop) {
            scrollTop.addEventListener("click", () => {
                group.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            });
        }

        render();
        updateStats();
    });
});


document.addEventListener('DOMContentLoaded', function () {
    initLabelDiagrams();
});

function initLabelDiagrams() {
    const containers = document.querySelectorAll('.label-activity-container');

    containers.forEach(container => {
        const draggables = container.querySelectorAll('.label-draggable');
        const dropzones = container.querySelectorAll('.label-dropzone');
        const bank = container.querySelector('.label-wordbank-tray');

        let activeSelection = null;

        function clearSelection() {
            if (activeSelection) {
                activeSelection.classList.remove('selected');
                activeSelection = null;
            }
        }

        function clearRevealedState() {
            container.dataset.answersRevealed = "false";
        }

        function placeInZone(targetZone, item) {
            clearRevealedState();
            if (targetZone.querySelector('.label-draggable')) {
                const oldItem = targetZone.querySelector('.label-draggable');
                restoreOriginalText(oldItem);
                bank.appendChild(oldItem);
            }

            // Format item with prefix badge if needed
            restoreOriginalText(item);
            targetZone.appendChild(item);
            targetZone.classList.remove('correct', 'incorrect');
            clearSelection();
        }

        function returnToBank(item) {
            clearRevealedState();
            restoreOriginalText(item);
            bank.appendChild(item);
            if (item.parentElement && item.parentElement.classList.contains('label-dropzone')) {
                item.parentElement.classList.remove('correct', 'incorrect');
            }
            clearSelection();
        }

        function restoreOriginalText(item) {
            if (item.dataset.word) {
                item.textContent = item.dataset.word;
            }
        }

        draggables.forEach(draggable => {
            draggable.addEventListener('dragstart', (e) => {
                clearSelection();
                draggable.classList.add('dragging');
                e.dataTransfer.setData('text/plain', draggable.id);
            });

            draggable.addEventListener('dragend', () => {
                draggable.classList.remove('dragging');
            });

            draggable.addEventListener('click', (e) => {
                e.stopPropagation();
                if (activeSelection === draggable) {
                    clearSelection();
                    return;
                }
                clearSelection();
                activeSelection = draggable;
                draggable.classList.add('selected');
            });
        });

        dropzones.forEach(zone => {
            zone.addEventListener('dragover', (e) => {
                e.preventDefault();
                zone.classList.add('hovered');
            });

            zone.addEventListener('dragleave', () => {
                zone.classList.remove('hovered');
            });

            zone.addEventListener('drop', (e) => {
                e.preventDefault();
                zone.classList.remove('hovered');
                const dragId = e.dataTransfer.getData('text/plain');
                const draggable = document.getElementById(dragId);

                if (draggable) {
                    placeInZone(zone, draggable);
                }
            });

            zone.addEventListener('click', (e) => {
                if (activeSelection) {
                    e.stopPropagation();
                    placeInZone(zone, activeSelection);
                }
            });

            zone.addEventListener('dblclick', (e) => {
                e.stopPropagation();
                const child = zone.querySelector('.label-draggable');
                if (child) {
                    returnToBank(child);
                }
            });
        });

        if (bank) {
            bank.addEventListener('dragover', (e) => e.preventDefault());
            bank.addEventListener('drop', (e) => {
                e.preventDefault();
                const dragId = e.dataTransfer.getData('text/plain');
                const draggable = document.getElementById(dragId);
                if (draggable) {
                    returnToBank(draggable);
                }
            });

            bank.addEventListener('click', () => {
                if (activeSelection) {
                    returnToBank(activeSelection);
                }
            });
        }

        container.addEventListener('click', () => {
            clearSelection();
        });
    });
}

// Toggle A, B, C Reference Mode for Student Book Writing
function toggleReferenceMode(btn) {
    const container = btn.closest('.label-activity-container');
    const isRef = container.classList.toggle('reference-mode-active');

    btn.classList.toggle('active', isRef);
    btn.textContent = isRef ? 'Hide A,B,C' : 'A,B,C Mode';
}

function scoreLabels(btn) {
    const container = btn.closest('.label-activity-container');
    const scoreDisplay = container.querySelector('.label-score-display');

    if (container.dataset.answersRevealed === "true") {
        if (scoreDisplay) {
            scoreDisplay.textContent = 'Reset to score!';
            scoreDisplay.classList.remove('high', 'medium', 'low');
            scoreDisplay.classList.add('medium');
        }
        return;
    }

    const dropzones = container.querySelectorAll('.label-dropzone');
    let correctCount = 0;
    const total = dropzones.length;

    dropzones.forEach(zone => {
        zone.classList.remove('correct', 'incorrect');
        const correctText = zone.getAttribute('data-correct');
        const child = zone.querySelector('.label-draggable');

        if (child && child.getAttribute('data-word') === correctText) {
            correctCount++;
            zone.classList.add('correct');
        } else {
            zone.classList.add('incorrect');
        }
    });

    if (scoreDisplay) {
        const percentage = total > 0 ? (correctCount / total) * 100 : 0;
        const roundedPct = Math.round(percentage);

        // Remove previous tier badges
        scoreDisplay.classList.remove('high', 'medium', 'low');

        // Apply score tier variant matching cloze activity styles
        if (percentage >= 80) {
            scoreDisplay.classList.add('high');
        } else if (percentage >= 50) {
            scoreDisplay.classList.add('medium');
        } else {
            scoreDisplay.classList.add('low');
        }

        scoreDisplay.textContent = `Score: ${correctCount} / ${total} (${roundedPct}%)`;
    }
}

// Teacher Answers Button - Shows Answers prefixed with Letter Badges (A. eyepiece lens)
// Teacher Answers Button - Only prefixes labels if Ref Mode is active
function showAnswers(btn) {
    const container = btn.closest('.label-activity-container');
    const dropzones = container.querySelectorAll('.label-dropzone');
    const draggables = container.querySelectorAll('.label-draggable');

    // Check if the teacher reference mode is currently active
    const isRefMode = container.classList.contains('reference-mode-active');

    container.dataset.answersRevealed = "true";

    dropzones.forEach(zone => {
        zone.classList.remove('incorrect');
        const correctText = zone.getAttribute('data-correct');
        const prefix = zone.getAttribute('data-prefix');
        const match = Array.from(draggables).find(d => d.getAttribute('data-word') === correctText);

        if (match) {
            // Only prepend the letter prefix if Ref Mode is active
            if (isRefMode && prefix) {
                match.textContent = `${prefix} ${correctText}`;
            } else {
                match.textContent = correctText;
            }

            zone.appendChild(match);
            zone.classList.add('correct');
        }
    });

    const scoreDisplay = container.querySelector('.label-score-display');
    if (scoreDisplay) {
        scoreDisplay.textContent = 'Answers Revealed';
        scoreDisplay.classList.remove('high', 'medium', 'low');
        scoreDisplay.classList.add('high');
    }
}

function resetLabels(btn) {
    const container = btn.closest('.label-activity-container');
    const bank = container.querySelector('.label-wordbank-tray');
    const draggables = container.querySelectorAll('.label-draggable');
    const dropzones = container.querySelectorAll('.label-dropzone');

    container.dataset.answersRevealed = "false";
    container.classList.remove('reference-mode-active');

    const refBtn = container.querySelector('.label-btn-reference');
    if (refBtn) {
        refBtn.classList.remove('active');
        refBtn.textContent = 'A,B,C Mode';
    }

    draggables.forEach(d => {
        d.classList.remove('selected');
        d.textContent = d.getAttribute('data-word'); // Restore original text
        bank.appendChild(d);
    });

    dropzones.forEach(zone => zone.classList.remove('correct', 'incorrect', 'hovered'));

    const scoreDisplay = container.querySelector('.label-score-display');
    if (scoreDisplay) {
        scoreDisplay.textContent = '';
        scoreDisplay.classList.remove('high', 'medium', 'low');
    }
}
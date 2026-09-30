document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".fillin-block"))
  if (blocks.length === 0) return

  // Resets validation UI elements and inputs inside a block
  function initBlock(block) {
    block.querySelectorAll(".fillin-inline-feedback").forEach(badge => {
      badge.textContent = ""
      badge.className = "fillin-inline-feedback"
    })

    block.querySelectorAll(".fillin-input").forEach(input => {
      input.value = ""
      input.disabled = false
      input.classList.remove("correct", "incorrect")
    })

    // Re-enable score button on reset
    const scoreBtn = block.querySelector(".fillin-btn-score")
    if (scoreBtn) {
      scoreBtn.disabled = false
    }
  }

  // Initial Run
  blocks.forEach(b => initBlock(b))

  // Build Control Panel Toolbar for each block
  blocks.forEach(block => {
    const panel = document.createElement("div")
    panel.className = "fillin-global-panel"

    const btnScore = document.createElement("button")
    btnScore.type = "button"
    btnScore.className = "fillin-btn-score"
    btnScore.textContent = "Check"

    const btnReset = document.createElement("button")
    btnReset.type = "button"
    btnReset.className = "fillin-btn-reset"
    btnReset.textContent = "Reset"

    const scoreBadge = document.createElement("span")
    scoreBadge.className = "fillin-output"
    scoreBadge.style.display = "none"

    panel.appendChild(btnScore)
    panel.appendChild(btnReset)
    panel.appendChild(scoreBadge)
    block.appendChild(panel)

    // Allow pressing "Enter" inside any input to submit answers
    block.querySelectorAll(".fillin-input").forEach(input => {
      input.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !btnScore.disabled) {
          btnScore.click()
        }
      })
    })

    // 1. Scoring Validation Event Listener
    btnScore.addEventListener("click", () => {
      const inputs = block.querySelectorAll(".fillin-input")
      let totalGaps = inputs.length
      let correctGaps = 0

      inputs.forEach(input => {
        const userVal = input.value.trim()
        const expectedValue = input.dataset.correct.trim()
        const isCaseSensitive = input.dataset.caseSensitive === "true"

        const feedbackBadge = input.nextElementSibling

        let isCorrect = false
        if (isCaseSensitive) {
          isCorrect = (userVal === expectedValue)
        } else {
          isCorrect = (userVal.toLowerCase() === expectedValue.toLowerCase())
        }

        if (isCorrect) {
          input.classList.add("correct")
          feedbackBadge.textContent = " ✓"
          feedbackBadge.className = "fillin-inline-feedback text-correct"
          correctGaps++
        } else {
          input.classList.add("incorrect")
          feedbackBadge.textContent = ` ✕ (Ans: ${expectedValue})`
          feedbackBadge.className = "fillin-inline-feedback text-incorrect"
        }
        input.disabled = true
      })

      // Render Bottom Score Box
      scoreBadge.textContent = `Score: ${correctGaps} / ${totalGaps}`
      scoreBadge.style.display = "inline-block"
      scoreBadge.className = "fillin-output"

      const percent = totalGaps === 0 ? 0 : correctGaps / totalGaps
      if (percent >= 0.8) scoreBadge.classList.add("high")
      else if (percent >= 0.5) scoreBadge.classList.add("medium")
      else scoreBadge.classList.add("low")

      // Disable Check button visually & functionally
      btnScore.disabled = true
    })

    // 2. Reset Button Click Listener
    btnReset.addEventListener("click", () => {
      initBlock(block)
      scoreBadge.textContent = ""
      scoreBadge.style.display = "none"
      scoreBadge.className = "fillin-output"
    })
  })
});
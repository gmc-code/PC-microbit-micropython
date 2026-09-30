document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".gapfill-block"))
  if (blocks.length === 0) return

  // Sorts options alphabetically (A to Z) and resets validation UI elements
  function initBlock(block) {
    block.querySelectorAll(".gapfill-dropdown").forEach(select => {
      const options = Array.from(select.options)
      const placeholder = options.shift()

      options.sort((a, b) => a.text.localeCompare(b.text, undefined, { sensitivity: 'base' }))

      select.innerHTML = ""
      select.add(placeholder)
      options.forEach(opt => select.add(opt))
    })

    // Wipe inline feedback targets clean
    block.querySelectorAll(".gapfill-inline-feedback").forEach(badge => {
      badge.textContent = ""
      badge.className = "gapfill-inline-feedback"
    })

    block.querySelectorAll(".gapfill-input").forEach(input => {
      input.value = ""
      input.disabled = false
      input.classList.remove("correct", "incorrect")
    })

    // Re-enable score button on reset
    const scoreBtn = block.querySelector(".gapfill-btn-score")
    if (scoreBtn) {
      scoreBtn.disabled = false
    }
  }

  // Initial Run
  blocks.forEach(b => initBlock(b))

  // Build Control Panel Toolbar for each block
  blocks.forEach(block => {
    const panel = document.createElement("div")
    panel.className = "gapfill-global-panel"

    const btnScore = document.createElement("button")
    btnScore.type = "button"
    btnScore.className = "gapfill-btn-score"
    btnScore.textContent = "Check"

    const btnReset = document.createElement("button")
    btnReset.type = "button"
    btnReset.className = "gapfill-btn-reset"
    btnReset.textContent = "Reset"

    const scoreBadge = document.createElement("span")
    scoreBadge.className = "gapfill-output"
    scoreBadge.style.display = "none"

    panel.appendChild(btnScore)
    panel.appendChild(btnReset)
    panel.appendChild(scoreBadge)
    block.appendChild(panel)

    // 1. Scoring Validation Event Listener
    btnScore.addEventListener("click", () => {
      const inputs = block.querySelectorAll(".gapfill-input")
      let totalGaps = inputs.length
      let correctGaps = 0

      inputs.forEach(input => {
        const val = input.value.trim()
        const expectedValue = input.dataset.correct

        const feedbackBadge = input.nextElementSibling
        let isCorrect = (val && val === expectedValue)

        if (isCorrect) {
          input.classList.add("correct")
          feedbackBadge.textContent = " ✓"
          feedbackBadge.className = "gapfill-inline-feedback text-correct"
          correctGaps++
        } else {
          input.classList.add("incorrect")
          feedbackBadge.textContent = ` ✕ (Ans: ${expectedValue})`
          feedbackBadge.className = "gapfill-inline-feedback text-incorrect"
        }
        input.disabled = true
      })

      // Render Bottom Score Box
      scoreBadge.textContent = `Score: ${correctGaps} / ${totalGaps}`
      scoreBadge.style.display = "inline-block"
      scoreBadge.className = "gapfill-output"

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
      scoreBadge.className = "gapfill-output"
    })
  })
});
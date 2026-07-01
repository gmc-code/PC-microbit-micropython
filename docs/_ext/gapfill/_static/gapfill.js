document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".gapfill-block"))
  if (blocks.length === 0) return

  // Sorts options alphabetically (A to Z) and resets validation UI elements
  function initBlock(block) {
    block.querySelectorAll(".gapfill-dropdown").forEach(select => {
      const options = Array.from(select.options)
      const placeholder = options.shift() // Save the "-- Choose --" element

      // Sort remaining option elements alphabetically from A to Z
      options.sort((a, b) => a.text.localeCompare(b.text, undefined, { sensitivity: 'base' }))

      select.innerHTML = ""
      select.add(placeholder) // Restore placeholder at the top
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
  }

  // Initial Run
  blocks.forEach(b => initBlock(b))

  // Build Unified Control Panel Toolbar for each block instead of globally to prevent collisions
  blocks.forEach(block => {
    const panel = document.createElement("div")
    panel.className = "gapfill-global-panel"

    const scoreBtn = document.createElement("button")
    scoreBtn.className = "gapfill-btn-score"
    scoreBtn.textContent = "Check Answers"

    const resetBtn = document.createElement("button")
    resetBtn.className = "gapfill-btn-reset"
    resetBtn.textContent = "Reset"

    const scoreBadge = document.createElement("div")
    scoreBadge.className = "gapfill-output"

    panel.appendChild(scoreBtn)
    panel.appendChild(resetBtn)
    panel.appendChild(scoreBadge)
    block.appendChild(panel)

    scoreBtn.addEventListener("click", () => doScore(block, scoreBadge))
    resetBtn.addEventListener("click", () => doReset(block, scoreBadge))
  })

  function doScore(block, scoreBadge) {
    let totalGaps = 0
    let correctGaps = 0

    block.querySelectorAll(".gapfill-wrapper").forEach(wrapper => {
      const inputs = wrapper.querySelectorAll(".gapfill-input")
      inputs.forEach(input => {
        totalGaps++
        const val = input.value.trim().toLowerCase()
        const expectedValue = input.dataset.correct

        // Find the specific inline text span companion sitting directly next to this dropdown box
        const feedbackBadge = input.nextElementSibling
        let isCorrect = (val && val === expectedValue)

        if (isCorrect) {
          input.classList.add("correct")
          feedbackBadge.textContent = " ✓"
          feedbackBadge.className = "gapfill-inline-feedback text-correct"
          correctGaps++
        } else {
          input.classList.add("incorrect")
          // Reveal both cross icon AND correct missing string solution text
          feedbackBadge.textContent = ` ✕ (Ans: ${expectedValue})`
          feedbackBadge.className = "gapfill-inline-feedback text-incorrect"
        }
        input.disabled = true
      })
    })

    // Render Bottom Score Box
    scoreBadge.textContent = `Score: ${correctGaps} / ${totalGaps}`
    scoreBadge.style.display = "inline-block"
    scoreBadge.className = "gapfill-output"

    const percent = totalGaps === 0 ? 0 : correctGaps / totalGaps
    if (percent >= 0.8) scoreBadge.classList.add("high")
    else if (percent >= 0.5) scoreBadge.classList.add("medium")
    else scoreBadge.classList.add("low")
  }

  function doReset(block, scoreBadge) {
    initBlock(block)
    scoreBadge.style.display = "none"
    scoreBadge.className = "gapfill-output"
    scoreBadge.textContent = ""
  }
})
document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".multichoice-block"))
  if (blocks.length === 0) return

  // ─────────────────────────────────────
  // Utilities
  // ─────────────────────────────────────
  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]]
    }
  }

  function assignLetters(choices) {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    choices.forEach((c, i) => {
      const span = c.querySelector(".multichoice-letter")
      if (span) span.textContent = letters[i] || ""
    })
  }

  // ─────────────────────────────────────
  // Initialise block metadata
  // ─────────────────────────────────────
  blocks.forEach((block) => {
    if (!block.dataset.originalChoicesHTML) {
      block.dataset.originalChoicesHTML = Array.from(
        block.querySelectorAll(".multichoice-choice")
      )
        .map(c => c.outerHTML)
        .join("")
    }

    // Keep actual string matches without forcing "true" conversions
    block.dataset.multichoiceShuffle = block.dataset.multichoiceShuffle === "false" ? "false" : "true"
    block.dataset.multichoiceLetters = block.dataset.multichoiceLetters === "false" ? "false" : "true"
    block.dataset.multichoiceSingle = block.dataset.multichoiceSingle === "false" ? "false" : "true"
  })

  // ─────────────────────────────────────
  // Build / reset a block
  // ─────────────────────────────────────
  function initBlock(block, blockIndex) {
    block.querySelectorAll(".multichoice-choice").forEach(n => n.remove())

    const container = document.createElement("div")
    container.innerHTML = block.dataset.originalChoicesHTML

    let choices = Array.from(container.children)

    if (block.dataset.multichoiceShuffle === "true") {
      shuffleArray(choices)
    }

    choices.forEach(c => block.appendChild(c))

    if (block.dataset.multichoiceLetters === "true") {
      assignLetters(choices)
    }

    const isSingle = block.dataset.multichoiceSingle === "true"

    if (isSingle) {
      const name = "mcq_" + blockIndex + "_" + Date.now()
      choices.forEach(c => {
        const r = c.querySelector("input[type='radio']")
        if (r) r.name = name
      })
    }

    choices.forEach(choice => {
      choice.classList.remove(
        "multichoice-correct",
        "multichoice-incorrect",
        "multichoice-answer",
        "selected"
      )

      const input = choice.querySelector("input")
      if (input) {
        input.checked = false
        input.disabled = false
      }

      const exp = choice.querySelector(".multichoice-explanation")
      if (exp) exp.style.display = "none"
    })

    // ─────────────────────────────────────
    // CLICK HANDLING (Clean & Native)
    // ─────────────────────────────────────
    choices.forEach(choice => {
      const input = choice.querySelector("input")
      if (!input) return

      // Make the entire block look clickable and act as a full label extension
      choice.style.cursor = "pointer"

      // Listen for the input's actual state mutation change event
      input.addEventListener("change", () => {
        if (isSingle) {
          // Clear styles across sister choices for radio items
          choices.forEach(c => c.classList.remove("selected"))
          if (input.checked) choice.classList.add("selected")
        } else {
          // Toggle checkbox style maps based directly on state truths
          choice.classList.toggle("selected", input.checked)
        }
      })

      // Fallback: If they click the wrapper card div outside the native <label>, toggle it programmatically
      choice.addEventListener("click", (e) => {
        if (input.disabled) return

        // If they click inside the label/input, standard browser logic handles it
        if (e.target.closest("label")) return

        // If they click the parent choice block container background, trigger the input natively
        input.checked = isSingle ? true : !input.checked
        input.dispatchEvent(new Event("change"))
      })
    })
  }

  // ─────────────────────────────────────
  // Initialise blocks
  // ─────────────────────────────────────

  blocks.forEach((b, i) => initBlock(b, i))

  // ─────────────────────────────────────
  // Control panel
  // ─────────────────────────────────────
  const panel = document.createElement("div")
  panel.className = "multichoice-global-panel"
  panel.style.display = "flex"
  panel.style.gap = "0.6rem"
  panel.style.marginTop = "1rem"
  panel.style.paddingTop = "0.6rem"
  panel.style.borderTop = "1px solid #ddd"

  const btnScore = document.createElement("button")
  btnScore.type = "button"
  btnScore.className = "multichoice-btn-score"
  btnScore.textContent = "Score Page"

  const btnReset = document.createElement("button")
  btnReset.type = "button"
  btnReset.className = "multichoice-btn-reset"
  btnReset.textContent = "Reset Page"

  const scoreBadge = document.createElement("span")
  scoreBadge.style.display = "none"
  scoreBadge.style.marginLeft = "auto"
  scoreBadge.style.fontWeight = "600"

  panel.append(btnScore, btnReset, scoreBadge)

  const lastBlock = blocks[blocks.length - 1]
  lastBlock.parentNode.insertBefore(panel, lastBlock.nextSibling)

  // ─────────────────────────────────────
  // Scoring Engine
  // ─────────────────────────────────────
  function doScore() {
    let total = 0
    let correct = 0

    blocks.forEach(block => {
      total++

      const isSingle = block.dataset.multichoiceSingle === "true"
      const choices = Array.from(block.querySelectorAll(".multichoice-choice"))

      choices.forEach(c => {
        c.classList.remove("multichoice-correct", "multichoice-incorrect", "multichoice-answer")
      })

      choices.forEach(c => {
        if (c.dataset.correct === "true") {
          c.classList.add("multichoice-answer")
        }
      })

      if (isSingle) {
        const selected = choices.find(c => c.querySelector("input")?.checked)

        if (selected) {
          if (selected.dataset.correct === "true") {
            selected.classList.add("multichoice-correct")
            correct++
          } else {
            selected.classList.add("multichoice-incorrect")
          }
        }
      } else {
        const selected = choices.filter(c => c.querySelector("input")?.checked)
        const correctChoices = choices.filter(c => c.dataset.correct === "true")

        const allSelectedAreCorrect = selected.every(c => c.dataset.correct === "true")
        const allCorrectAreSelected = correctChoices.every(c => c.querySelector("input")?.checked)

        const isFullyCorrect = selected.length > 0 && allSelectedAreCorrect && allCorrectAreSelected

        selected.forEach(c => {
          if (c.dataset.correct === "true") {
            c.classList.add("multichoice-correct")
          } else {
            c.classList.add("multichoice-incorrect")
          }
        })

        if (isFullyCorrect) correct++
      }

      block.querySelectorAll(".multichoice-explanation").forEach(e => {
        e.style.display = "block"
      })

      block.querySelectorAll("input").forEach(i => {
        i.disabled = true
      })
    })

    scoreBadge.textContent = `Score: ${correct} / ${total}`
    scoreBadge.style.display = "inline-block"
    scoreBadge.classList.add("multichoice-output")

    const percent = total === 0 ? 0 : correct / total
    scoreBadge.classList.remove("high", "medium", "low")

    if (percent >= 0.8) {
      scoreBadge.classList.add("high")
    } else if (percent >= 0.5) {
      scoreBadge.classList.add("medium")
    } else {
      scoreBadge.classList.add("low")
    }
  }

  function doReset() {
    scoreBadge.style.display = "none"
    scoreBadge.classList.remove("high", "medium", "low")
    blocks.forEach((b, i) => initBlock(b, i))
  }

  btnScore.onclick = doScore
  btnReset.onclick = doReset
})
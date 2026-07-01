document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".cloze-block"))
  if (blocks.length === 0) return

  let draggedElement = null

  blocks.forEach(block => {
    const draggables = block.querySelectorAll(".cloze-draggable")
    const dropzones = block.querySelectorAll(".cloze-dropzone")

    draggables.forEach(draggable => {
      draggable.addEventListener("dragstart", (e) => {
        draggedElement = draggable
        e.dataTransfer.setData("text/plain", draggable.dataset.word)
        draggable.classList.add("dragging")
      })

      draggable.addEventListener("dragend", () => {
        draggable.classList.remove("dragging")
        draggedElement = null
      })
    })

    dropzones.forEach(zone => {
      zone.addEventListener("dragover", (e) => {
        e.preventDefault()
        zone.classList.add("hovered")
      })

      zone.addEventListener("dragleave", () => {
        zone.classList.remove("hovered")
      })

      zone.addEventListener("drop", (e) => {
        e.preventDefault()
        zone.classList.remove("hovered")

        if (!draggedElement || zone.classList.contains("disabled")) return

        const existingToken = zone.querySelector(".cloze-dropped-token")
        if (existingToken) {
          const originalValue = existingToken.dataset.word
          const hiddenTrayItem = block.querySelector(`.cloze-draggable[data-word="${originalValue}"]`)
          if (hiddenTrayItem) hiddenTrayItem.style.display = "inline-block"
        }

        const wordValue = draggedElement.dataset.word
        const wordText = draggedElement.textContent

        zone.innerHTML = `<span class="cloze-dropped-token" data-word="${wordValue}">${wordText}</span>`
        zone.classList.add("occupied")
        draggedElement.style.display = "none"
      })
    })
  })

  const panel = document.createElement("div")
  panel.className = "cloze-global-panel"

  const btnScore = document.createElement("button")
  btnScore.type = "button"
  btnScore.className = "cloze-btn-score"
  btnScore.textContent = "Score Page"

  const btnReset = document.createElement("button")
  btnReset.type = "button"
  btnReset.className = "cloze-btn-reset"
  btnReset.textContent = "Reset Page"

  const scoreBadge = document.createElement("span")
  scoreBadge.className = "cloze-output"

  panel.append(btnScore, btnReset, scoreBadge)
  const lastBlock = blocks[blocks.length - 1]
  lastBlock.parentNode.insertBefore(panel, lastBlock.nextSibling)

  btnScore.addEventListener("click", () => {
    let totalGaps = 0
    let correctGaps = 0

    blocks.forEach(block => {
      block.querySelectorAll(".cloze-dropzone").forEach(zone => {
        totalGaps++
        zone.classList.add("disabled")

        const token = zone.querySelector(".cloze-dropped-token")
        const val = token ? token.dataset.word : ""
        const expected = zone.dataset.correct

        const wrapper = zone.closest(".cloze-wrapper")
        const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null

        zone.classList.remove("correct", "incorrect")

        if (feedback) {
          if (val && val.trim() === expected.trim()) {
            zone.classList.add("correct")
            feedback.textContent = " ✓ Correct!"
            feedback.className = "cloze-inline-feedback text-correct"
            correctGaps++
          } else {
            zone.classList.add("incorrect")
            feedback.textContent = ` ✕ (Ans: ${expected})`
            feedback.className = "cloze-inline-feedback text-incorrect"
          }
        }
      })
    })

    scoreBadge.textContent = `Score: ${correctGaps} / ${totalGaps}`
    scoreBadge.style.display = "inline-block"
    scoreBadge.classList.remove("high", "medium", "low")

    const percent = totalGaps === 0 ? 0 : correctGaps / totalGaps
    if (percent >= 0.8) scoreBadge.classList.add("high")
    else if (percent >= 0.5) scoreBadge.classList.add("medium")
    else scoreBadge.classList.add("low")
  })

  btnReset.addEventListener("click", () => {
    scoreBadge.style.display = "none"
    blocks.forEach(block => {
      block.querySelectorAll(".cloze-dropzone").forEach(zone => {
        zone.innerHTML = "Drop here"
        zone.className = "cloze-dropzone"

        const wrapper = zone.closest(".cloze-wrapper")
        const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null
        if (feedback) {
          feedback.textContent = ""
          feedback.className = "cloze-inline-feedback"
        }
      })
      block.querySelectorAll(".cloze-draggable").forEach(item => {
        item.style.display = "inline-block"
        item.classList.remove("dragging")
      })
    })
  })
})
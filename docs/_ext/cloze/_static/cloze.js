document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".cloze-block"))
  if (blocks.length === 0) return

  let draggedElement = null

  blocks.forEach(block => {
    const draggables = block.querySelectorAll(".cloze-draggable")
    const dropzones = block.querySelectorAll(".cloze-dropzone")
    const btnScore = block.querySelector(".cloze-btn-score")
    const btnReset = block.querySelector(".cloze-btn-reset")
    const scoreBadge = block.querySelector(".cloze-output")

    // Drag and Drop Handling bounded inside block instances
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
          const originalWord = existingToken.textContent
          const putBackItem = Array.from(block.querySelectorAll(".cloze-draggable")).find(
            d => d.dataset.word === existingToken.dataset.word && d.style.display === "none"
          )
          if (putBackItem) putBackItem.style.display = "inline-block"
        }

        zone.innerHTML = `<span class="cloze-dropped-token" data-word="${draggedElement.dataset.word}">${draggedElement.textContent}</span>`
        zone.classList.add("occupied")
        draggedElement.style.display = "none"
      })

      // Double click removal
      zone.addEventListener("dblclick", () => {
        if (zone.classList.contains("disabled")) return
        const token = zone.querySelector(".cloze-dropped-token")
        if (!token) return

        const putBackItem = Array.from(block.querySelectorAll(".cloze-draggable")).find(
          d => d.dataset.word === token.dataset.word && d.style.display === "none"
        )
        if (putBackItem) putBackItem.style.display = "inline-block"

        zone.innerHTML = "Drop here"
        zone.classList.remove("occupied", "correct", "incorrect")
      })
    })

    // Localized Scoped Section Evaluation Logic
    if (btnScore) {
      btnScore.addEventListener("click", () => {
        let correctGaps = 0
        const totalGaps = dropzones.length

        dropzones.forEach(zone => {
          zone.classList.add("disabled")
          const token = zone.querySelector(".cloze-dropped-token")
          const expected = zone.dataset.correct ? zone.dataset.correct.trim().toLowerCase() : ""
          const actual = token ? token.dataset.word.trim().toLowerCase() : ""

          const wrapper = zone.closest(".cloze-wrapper")
          const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null

          zone.classList.remove("correct", "incorrect")

          if (actual === expected) {
            zone.classList.add("correct")
            if (feedback) {
              feedback.textContent = " ✓ Correct!"
              feedback.className = "cloze-inline-feedback text-correct"
            }
            correctGaps++
          } else {
            zone.classList.add("incorrect")
            if (feedback) {
              feedback.textContent = ` ✕ (Ans: ${zone.dataset.correct})`
              feedback.className = "cloze-inline-feedback text-incorrect"
            }
          }
        })

        // Display Score output locally on *this* panel
        if (scoreBadge) {
          scoreBadge.textContent = `Score: ${correctGaps} / ${totalGaps}`
          scoreBadge.style.display = "inline-block"
          scoreBadge.classList.remove("high", "medium", "low")

          const percent = totalGaps === 0 ? 0 : correctGaps / totalGaps
          if (percent >= 0.8) scoreBadge.classList.add("high")
          else if (percent >= 0.5) scoreBadge.classList.add("medium")
          else scoreBadge.classList.add("low")
        }

        btnScore.disabled = true
      })
    }

    // Localized Scoped Section Reset Logic
    if (btnReset) {
      btnReset.addEventListener("click", () => {
        if (scoreBadge) scoreBadge.style.display = "none"

        dropzones.forEach(zone => {
          zone.innerHTML = "Drop here"
          zone.className = "cloze-dropzone"

          const wrapper = zone.closest(".cloze-wrapper")
          const feedback = wrapper ? wrapper.querySelector(".cloze-inline-feedback") : null
          if (feedback) {
            feedback.textContent = ""
            feedback.className = "cloze-inline-feedback"
          }
        })

        draggables.forEach(d => {
          d.style.display = "inline-block"
        })

        if (btnScore) btnScore.disabled = false
      })
    }
  })
})
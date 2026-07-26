document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".cloze-block"))
  if (blocks.length === 0) return

  let draggedElement = null

  blocks.forEach(block => {
    const draggables = block.querySelectorAll(".cloze-draggable")
    const dropzones = block.querySelectorAll(".cloze-dropzone")
    const bank = block.querySelector(".cloze-wordbank-tray")
    const btnScore = block.querySelector(".cloze-btn-score")
    const btnReset = block.querySelector(".cloze-btn-reset")
    const scoreBadge = block.querySelector(".cloze-output")

    // Active selection state for click-to-click within this cloze block instance
    let activeSelection = null

    function clearSelection() {
      if (activeSelection) {
        activeSelection.classList.remove("selected")
        activeSelection = null
      }
    }

    // Helper: Put back existing token in zone to word bank tray
    function returnTokenToBank(zone) {
      const existingToken = zone.querySelector(".cloze-dropped-token")
      if (existingToken) {
        const putBackItem = Array.from(block.querySelectorAll(".cloze-draggable")).find(
          d => d.dataset.word === existingToken.dataset.word && d.style.display === "none"
        )
        if (putBackItem) {
          putBackItem.style.display = "inline-block"
          putBackItem.classList.remove("selected")
        }
      }
    }

    // Helper: Place a selected/dragged element into a target drop zone
    function placeInZone(zone, item) {
      if (zone.classList.contains("disabled")) return

      // Return any item currently occupying this slot
      returnTokenToBank(zone)

      // Place new token
      zone.innerHTML = `<span class="cloze-dropped-token" data-word="${item.dataset.word}">${item.textContent}</span>`
      zone.classList.add("occupied")
      zone.classList.remove("hovered", "correct", "incorrect")
      item.style.display = "none"

      clearSelection()
    }

    // --- 1. Setup Draggable & Clickable Word Items ---
    draggables.forEach(draggable => {
      // Drag Events
      draggable.addEventListener("dragstart", (e) => {
        clearSelection()
        draggedElement = draggable
        e.dataTransfer.setData("text/plain", draggable.dataset.word)
        draggable.classList.add("dragging")
      })

      draggable.addEventListener("dragend", () => {
        draggable.classList.remove("dragging")
        draggedElement = null
      })

      // Click-to-Select Event
      draggable.addEventListener("click", (e) => {
        e.stopPropagation()

        // Deselect if clicking the currently selected item
        if (activeSelection === draggable) {
          clearSelection()
          return
        }

        clearSelection()
        activeSelection = draggable
        draggable.classList.add("selected")
      })
    })

    // --- 2. Setup Drop Zones ---
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
        placeInZone(zone, draggedElement)
      })

      // Click-to-Place Event
      zone.addEventListener("click", (e) => {
        if (activeSelection && !zone.classList.contains("disabled")) {
          e.stopPropagation()
          placeInZone(zone, activeSelection)
        }
      })

      // Double Click to Remove Item back to Tray
      zone.addEventListener("dblclick", (e) => {
        e.stopPropagation()
        if (zone.classList.contains("disabled")) return
        returnTokenToBank(zone)
        zone.innerHTML = "Drop here"
        zone.classList.remove("occupied", "correct", "incorrect")
        clearSelection()
      })
    })

    // --- 3. Setup Word Bank Tray Drop/Click Target ---
    if (bank) {
      bank.addEventListener("dragover", (e) => e.preventDefault())

      bank.addEventListener("drop", (e) => {
        e.preventDefault()
        if (!draggedElement) return
        draggedElement.style.display = "inline-block"
      })

      // Click-to-Place back into bank tray
      bank.addEventListener("click", () => {
        if (activeSelection) {
          activeSelection.style.display = "inline-block"
          clearSelection()
        }
      })
    }

    // Clear selections when clicking outside interactive targets
    block.addEventListener("click", () => {
      clearSelection()
    })

    // --- 4. Section Evaluation Logic ---
    if (btnScore) {
      btnScore.addEventListener("click", () => {
        clearSelection()
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

    // --- 5. Section Reset Logic ---
    if (btnReset) {
      btnReset.addEventListener("click", () => {
        clearSelection()
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
          d.classList.remove("selected")
        })

        if (btnScore) btnScore.disabled = false
      })
    }
  })
})
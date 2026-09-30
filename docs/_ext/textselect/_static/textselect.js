document.addEventListener("DOMContentLoaded", () => {
  const blocks = Array.from(document.querySelectorAll(".textselect-block"));
  if (blocks.length === 0) return;

  blocks.forEach((block) => {
    const isMulti = block.dataset.mode === "multi";
    const shouldShuffle = block.dataset.shuffle === "true";
    const contentPre = block.querySelector(".textselect-content");
    const targetMap = JSON.parse(contentPre.dataset.targets || "{}");

    // Function to shuffle .ts-line elements in the DOM
    function shuffleLines() {
      if (!shouldShuffle) return;
      const lineElements = Array.from(contentPre.querySelectorAll(".ts-line"));
      for (let i = lineElements.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        contentPre.appendChild(lineElements[j]);
        lineElements.splice(j, 1);
      }
      lineElements.forEach((line) => contentPre.appendChild(line));
    }

    // Initial shuffle on load
    shuffleLines();

    const words = Array.from(block.querySelectorAll(".ts-word"));

    // Extract default single color from class list (e.g., ts-color-blue)
    const colorClassMatch = Array.from(block.classList).find((c) =>
      c.startsWith("ts-color-")
    );
    const singleDefaultColor = colorClassMatch
      ? colorClassMatch.replace("ts-color-", "")
      : "blue";

    // Extract all unique target colors
    const activeColorsSet = new Set();
    Object.values(targetMap).forEach((val) => {
      if (Array.isArray(val)) {
        val.forEach((c) => activeColorsSet.add(c));
      } else if (val) {
        activeColorsSet.add(val);
      }
    });
    const activeColors = Array.from(activeColorsSet);
    let currentColor = isMulti ? activeColors[0] || "blue" : singleDefaultColor;

    let isMouseDown = false;
    let lastClickedIdx = null;

    contentPre.addEventListener("selectstart", (e) => {
      if (isMouseDown) e.preventDefault();
    });

    // 1. Render Palette Control Toolbar (Only in Multi Mode)
    if (isMulti && activeColors.length > 0) {
      const paletteContainer = document.createElement("div");
      paletteContainer.className = "textselect-palette";

      const paletteButtons = {};
      activeColors.forEach((color) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = `ts-palette-btn ts-color-${color}`;
        btn.textContent = color.toUpperCase();
        if (color === currentColor) btn.classList.add("active");

        btn.addEventListener("click", () => {
          currentColor = color;
          Object.values(paletteButtons).forEach((b) => b.classList.remove("active"));
          btn.classList.add("active");
        });

        paletteButtons[color] = btn;
        paletteContainer.appendChild(btn);
      });

      block.insertBefore(paletteContainer, contentPre);
    }

    function setWordColor(word, color) {
      if (isMulti) {
        Array.from(word.classList).forEach((cls) => {
          if (cls.startsWith("ts-sel-")) word.classList.remove(cls);
        });

        if (word.dataset.selectedColor === color) {
          delete word.dataset.selectedColor;
          word.classList.remove("selected");
        } else {
          word.dataset.selectedColor = color;
          word.classList.add("selected", `ts-sel-${color}`);
        }
      } else {
        word.classList.toggle("selected");
        if (word.classList.contains("selected")) {
          word.dataset.selectedColor = singleDefaultColor;
        } else {
          delete word.dataset.selectedColor;
        }
      }
    }

    // 2. Interactive Selection Listeners
    words.forEach((word) => {
      const idx = parseInt(word.dataset.idx, 10);

      word.addEventListener("mousedown", (e) => {
        if (block.dataset.disabled === "true") return;
        isMouseDown = true;

        if (e.shiftKey && lastClickedIdx !== null) {
          const start = Math.min(lastClickedIdx, idx);
          const end = Math.max(lastClickedIdx, idx);
          for (let i = start; i <= end; i++) {
            setWordColor(words[i], currentColor);
          }
        } else {
          setWordColor(word, currentColor);
          lastClickedIdx = idx;
        }
      });

      word.addEventListener("mouseenter", () => {
        if (isMouseDown && block.dataset.disabled !== "true") {
          setWordColor(word, currentColor);
        }
      });
    });

    window.addEventListener("mouseup", () => {
      isMouseDown = false;
    });

    // 3. Control Panel UI
    const panel = document.createElement("div");
    panel.className = "textselect-global-panel";

    const btnScore = document.createElement("button");
    btnScore.type = "button";
    btnScore.className = "textselect-btn-score";
    btnScore.textContent = "Check";

    const btnReset = document.createElement("button");
    btnReset.type = "button";
    btnReset.className = "textselect-btn-reset";
    btnReset.textContent = "Reset";

    const scoreBadge = document.createElement("span");
    scoreBadge.className = "textselect-output";
    scoreBadge.style.display = "none";

    panel.appendChild(btnScore);
    panel.appendChild(btnReset);
    panel.appendChild(scoreBadge);
    block.appendChild(panel);

    // 4. Scoring Engine & Phrase Wrapper Construction
    btnScore.addEventListener("click", () => {
      block.dataset.disabled = "true";
      btnScore.disabled = true;

      let correctCount = 0;
      let totalTargets = Object.keys(targetMap).length;
      let falsePositives = 0;

      words.forEach((word) => {
        const idx = word.dataset.idx;
        const selectedColor = word.dataset.selectedColor;

        const rawTarget = targetMap[idx];
        const targetColors = Array.isArray(rawTarget)
          ? rawTarget
          : rawTarget
          ? [rawTarget]
          : [];

        word.classList.remove("selected");
        Array.from(word.classList).forEach((cls) => {
          if (cls.startsWith("ts-sel-")) word.classList.remove(cls);
        });

        if (selectedColor && targetColors.includes(selectedColor)) {
          word.classList.add("ts-correct-token", `ts-keep-${selectedColor}`);
          correctCount++;
        } else if (selectedColor) {
          word.classList.add("ts-incorrect-token");
          falsePositives++;
        } else if (!selectedColor && targetColors.length > 0) {
          word.classList.add("ts-missed-token", `ts-keep-${targetColors[0]}`);
        }
      });

      // Group adjacent matching tokens within lines
      const lineNodes = Array.from(contentPre.querySelectorAll(".ts-line"));
      lineNodes.forEach((lineNode) => {
        groupTokensInContainer(lineNode, "ts-correct-token", "ts-correct-phrase");
        groupTokensInContainer(lineNode, "ts-incorrect-token", "ts-incorrect-phrase");
        groupTokensInContainer(lineNode, "ts-missed-token", "ts-missed-phrase");
      });

      function groupTokensInContainer(container, tokenClass, wrapperBaseClass) {
        const nodes = Array.from(container.childNodes);
        let currentGroup = [];
        let currentGroupColor = null;

        nodes.forEach((node, i) => {
          const isTargetToken = node.nodeType === 1 && node.classList.contains(tokenClass);

          let tokenColor = null;
          if (isTargetToken) {
            const foundClass = Array.from(node.classList).find((c) => c.startsWith("ts-keep-"));
            tokenColor = foundClass || `ts-keep-${singleDefaultColor}`;
          }

          let isInternalSpace = false;
          if (
            node.nodeType === 1 &&
            node.classList.contains("ts-space") &&
            currentGroup.length > 0
          ) {
            const nextNode = nodes[i + 1];
            if (
              nextNode &&
              nextNode.nodeType === 1 &&
              nextNode.classList.contains(tokenClass)
            ) {
              const nextColor =
                Array.from(nextNode.classList).find((c) => c.startsWith("ts-keep-")) ||
                `ts-keep-${singleDefaultColor}`;
              if (!isMulti || nextColor === currentGroupColor) {
                isInternalSpace = true;
              }
            }
          }

          if (isTargetToken && (!currentGroupColor || !isMulti || currentGroupColor === tokenColor)) {
            currentGroupColor = tokenColor;
            currentGroup.push(node);
          } else if (isInternalSpace) {
            currentGroup.push(node);
          } else {
            finalizeGroup();
            if (isTargetToken) {
              currentGroupColor = tokenColor;
              currentGroup.push(node);
            }
          }
        });

        finalizeGroup();

        function finalizeGroup() {
          if (currentGroup.length > 0) {
            const wrapper = document.createElement("span");
            const appliedColorClass = currentGroupColor || `ts-keep-${singleDefaultColor}`;
            wrapper.className = `${wrapperBaseClass} ${appliedColorClass}`.trim();

            currentGroup[0].parentNode.insertBefore(wrapper, currentGroup[0]);
            currentGroup.forEach((node) => wrapper.appendChild(node));
            currentGroup = [];
            currentGroupColor = null;
          }
        }
      }

      // Display Score Output Badge
      scoreBadge.textContent = `Found: ${correctCount} / ${totalTargets} (Extra/Wrong: ${falsePositives})`;
      scoreBadge.style.display = "inline-block";

      const accuracy = totalTargets === 0 ? 0 : correctCount / totalTargets;
      if (accuracy >= 0.8 && falsePositives === 0) scoreBadge.classList.add("high");
      else if (accuracy >= 0.5) scoreBadge.classList.add("medium");
      else scoreBadge.classList.add("low");
    });

    // 5. Reset Listener
    btnReset.addEventListener("click", () => {
      block.dataset.disabled = "false";
      btnScore.disabled = false;

      const wrappers = Array.from(
        block.querySelectorAll(".ts-correct-phrase, .ts-incorrect-phrase, .ts-missed-phrase")
      );
      wrappers.forEach((wrapper) => {
        while (wrapper.firstChild) {
          wrapper.parentNode.insertBefore(wrapper.firstChild, wrapper);
        }
        wrapper.remove();
      });

      words.forEach((word) => {
        word.className = "ts-word";
        delete word.dataset.selectedColor;
      });

      scoreBadge.style.display = "none";
      lastClickedIdx = null;

      // Reshuffle the lines on reset
      shuffleLines();
    });
  });
});
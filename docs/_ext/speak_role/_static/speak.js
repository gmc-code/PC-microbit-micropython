document.addEventListener("DOMContentLoaded", () => {

  /*
   * Find the preferred speech voice.
   *
   * Priority:
   *   1. Australian English (en-AU)
   *   2. US English (en-US)
   *   3. Any English voice
   *   4. Browser default
   */
  function findPreferredVoice() {

    const voices = window.speechSynthesis.getVoices();

    if (!voices.length) {
      return null;
    }

    // 1. Exact Australian English
    let voice = voices.find(
      v => v.lang.toLowerCase() === "en-au"
    );

    if (voice) {
      return voice;
    }

    // 2. Any Australian English variant
    voice = voices.find(
      v => v.lang.toLowerCase().startsWith("en-au")
    );

    if (voice) {
      return voice;
    }

    // 3. Exact US English
    voice = voices.find(
      v => v.lang.toLowerCase() === "en-us"
    );

    if (voice) {
      return voice;
    }

    // 4. Any US English variant
    voice = voices.find(
      v => v.lang.toLowerCase().startsWith("en-us")
    );

    if (voice) {
      return voice;
    }

    // 5. Any English voice
    voice = voices.find(
      v => v.lang.toLowerCase().startsWith("en-")
    );

    if (voice) {
      return voice;
    }

    // 6. Browser's default voice
    voice = voices.find(v => v.default);

    return voice || null;
  }


  /*
   * SpeechSynthesis voices can load asynchronously.
   *
   * This function is called both immediately and when
   * the browser finishes loading its voices.
   */
  let preferredVoice = null;

  function loadVoice() {
    preferredVoice = findPreferredVoice();

    if (preferredVoice) {
      console.log(
        "[speak] Using voice:",
        preferredVoice.name,
        "|",
        preferredVoice.lang
      );
    } else {
      console.log("[speak] No speech voice detected yet.");
    }
  }

  window.speechSynthesis.addEventListener(
    "voiceschanged",
    loadVoice
  );

  // Try immediately as well.
  loadVoice();


  /*
   * Handle speak buttons.
   */
  document.body.addEventListener("click", (e) => {

    const btn = e.target.closest(".speak-btn");

    if (!btn) {
      return;
    }

    e.preventDefault();


    // If currently speaking this exact button, stop playback.
    if (
      window.speechSynthesis.speaking &&
      btn.classList.contains("speaking")
    ) {
      window.speechSynthesis.cancel();
      btn.classList.remove("speaking");
      return;
    }


    // Cancel any other ongoing speech.
    window.speechSynthesis.cancel();

    document
      .querySelectorAll(".speak-btn.speaking")
      .forEach(b => b.classList.remove("speaking"));


    const text = btn.getAttribute("data-speak-text");

    if (!text) {
      return;
    }


    const utterance = new SpeechSynthesisUtterance(text);

    utterance.rate = 0.6;


    /*
     * Use the preferred voice if one has been found.
     */
    if (preferredVoice) {

      utterance.voice = preferredVoice;

      // Use the actual language of the selected voice.
      utterance.lang = preferredVoice.lang;

    } else {

      // Fallback if voices have not loaded yet.
      utterance.lang = "en-AU";
    }


    // Visual active state.
    utterance.onstart = () => {
      btn.classList.add("speaking");
    };


    utterance.onend = () => {
      btn.classList.remove("speaking");
    };


    utterance.onerror = (event) => {
      console.warn("[speak] Speech error:", event.error);
      btn.classList.remove("speaking");
    };


    window.speechSynthesis.speak(utterance);

  });

});


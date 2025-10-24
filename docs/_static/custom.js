// --- slider z Twojej wersji ---
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".simple-slider").forEach(slider => {
    const slides = slider.querySelectorAll(".slide");
    if (!slides.length) return;
    let idx = 0;
    slides[idx].classList.add("active");
    const interval = parseInt(slider.dataset.interval || "4000", 10);
    setInterval(() => {
      slides[idx].classList.remove("active");
      idx = (idx + 1) % slides.length;
      slides[idx].classList.add("active");
    }, interval);
  });
});

// --- FIX: zamień błędnie wstawione bloki kodu na <div class="mermaid"> i wyrenderuj ---
(function fixMermaidBlocks() {
  function looksLikeMermaid(text) {
    const s = text.trimStart();
    return (
      s.startsWith("graph ") ||
      s.startsWith("sequenceDiagram") ||
      s.startsWith("classDiagram") ||
      s.startsWith("stateDiagram") ||
      s.startsWith("erDiagram") ||
      s.startsWith("gantt")
    );
  }

  // 1) zamiana <pre><code>...</code></pre> -> <div class="mermaid">...</div>
  document.querySelectorAll("pre > code").forEach(code => {
    const txt = code.textContent || "";
    if (!looksLikeMermaid(txt)) return;

    const pre = code.parentElement;
    const div = document.createElement("div");
    div.className = "mermaid";
    // Usuń wiodące wcięcia (częsty powód „dziwnego wcięcia”)
    div.textContent = txt.replace(/^\s{4,}/gm, "");
    pre.replaceWith(div);
  });

  // 2) ponowna inicjalizacja mermaid (render po podmianie DOM)
  if (window.mermaid && typeof window.mermaid.init === "function") {
    try {
      window.mermaid.init(undefined, document.querySelectorAll(".mermaid"));
    } catch (e) {
      console.warn("Mermaid init error:", e);
    }
  }
})();

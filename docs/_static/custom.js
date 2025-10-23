// Tiny slider for the homepage
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

// Mermaid init + re-render on theme change / navigation
(function () {
  function ensureMermaid(cb) {
    if (window.mermaid) return cb();
    const s = document.createElement("script");
    s.src = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js";
    s.onload = cb;
    document.head.appendChild(s);
  }
  function renderMermaid() {
    try {
      window.mermaid?.initialize({ startOnLoad: false, theme: "dark" });
      const nodes = document.querySelectorAll("div.mermaid");
      if (nodes.length) window.mermaid?.run({ nodes: nodes });
    } catch (_) {}
  }
  const kick = () => ensureMermaid(renderMermaid);
  document.addEventListener("DOMContentLoaded", kick);
  document.addEventListener("pydata:toggle-theme", kick);
  document.addEventListener("DOMContentSwitch", kick);
})();

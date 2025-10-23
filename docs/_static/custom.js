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

  // Mermaid client-side render (for output_format="raw")
  try {
    if (window.mermaid && window.mermaid.initialize) {
      window.mermaid.initialize({ startOnLoad: false, theme: "dark", securityLevel: "loose" });
      window.mermaid.init(undefined, document.querySelectorAll(".mermaid"));
    }
  } catch (e) {
    console.warn("Mermaid init failed:", e);
  }
});

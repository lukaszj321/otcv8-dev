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

/**
 * Mermaid fallback fixer:
 * Jeśli jakiś diagram trafił do HTML jako <pre><code> zamiast <div class="mermaid">,
 * to zamieniamy go w locie (po stronie przeglądarki).
 * Heurystyka: linia zaczyna się od 'graph ', 'sequenceDiagram', 'flowchart '
 * lub zawiera '%%{init:' z Mermaid init.
 */
function tryFixMermaidCodeBlocks() {
  const candidates = document.querySelectorAll('pre > code');
  candidates.forEach(code => {
    const raw = code.textContent.trim();
    const looksLikeMermaid =
      raw.startsWith('graph ') ||
      raw.startsWith('flowchart ') ||
      raw.startsWith('sequenceDiagram') ||
      raw.startsWith('classDiagram') ||
      raw.startsWith('stateDiagram') ||
      raw.startsWith('erDiagram') ||
      raw.includes('%%{init:');

    if (!looksLikeMermaid) return;

    // Zamiana <pre><code>...</code></pre> -> <div class="mermaid">...</div>
    const pre = code.parentElement;
    const mer = document.createElement('div');
    mer.className = 'mermaid';
    mer.textContent = raw;
    pre.replaceWith(mer);
  });

  // re-render Mermaid (jeśli biblioteka już załadowana)
  if (window.mermaid && typeof window.mermaid.init === 'function') {
    try { window.mermaid.init(); } catch(e) { /* no-op */ }
  }
}

document.addEventListener('DOMContentLoaded', tryFixMermaidCodeBlocks);
document.addEventListener('keydown', (ev) => {
  // po szukaniu/nawigacji - czasem content się dogrywa: spróbuj ponownie
  if (ev.key === 'Escape') tryFixMermaidCodeBlocks();
});

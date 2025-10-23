// Tiny slider (zostawiam Twój)
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

  // --- Mermaid: zamień PRE>CODE.language-mermaid na <div class="mermaid"> ---
  // (naprawia przypadki, gdy blok był jako ```mermaid lub - co gorsza - ```bash)
  if (window.mermaid) {
    try {
      // Inicjalizacja klienta (pasuje do conf.py -> mermaid_output_format="raw")
      window.mermaid.initialize({ startOnLoad: true, theme: 'dark' });

      // 1) napraw „źle opisane” bloki mermaid (np. language-mermaid)
      document.querySelectorAll('pre code.language-mermaid').forEach(code => {
        const src = code.textContent.trim();
        const div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = src;
        code.closest('pre').replaceWith(div);
      });

      // 2) gdy ktoś wrzucił mermaida błędnie pod ```bash, ale treść wygląda na mermaid
      document.querySelectorAll('pre code.language-bash, pre code.language-text').forEach(code => {
        const txt = code.textContent.trim();
        if (/^(sequenceDiagram|flowchart|classDiagram|erDiagram|gantt|graph\s+(TB|TD|LR|RL|BT))/m.test(txt)) {
          const div = document.createElement('div');
          div.className = 'mermaid';
          div.textContent = txt;
          code.closest('pre').replaceWith(div);
        }
      });

      // 3) zrenderuj wszystkie .mermaid
      window.mermaid.init(undefined, document.querySelectorAll('.mermaid'));
    } catch (e) {
      console.warn('Mermaid init failed:', e);
    }
  }
});

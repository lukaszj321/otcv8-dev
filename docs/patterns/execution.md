---
title: Patterns — Execution Libraries
---

# Patterns — Execution Libraries

```{warning}
Domyslnie wylaczone wykonywanie notebookow (`jupyter_execute_notebooks=off`). Poniższe dziala tylko jesli zainstalujesz odpowiednie rozszerzenia.
```

## jupyter-sphinx (jesli zainstalowane)

.. jupyter-execute::

    import numpy as np
    import matplotlib.pyplot as plt
    rng = np.random.default_rng()
    data = rng.standard_normal((3, 100))
    fig, ax = plt.subplots()
    ax.scatter(data[0], data[1], c=data[2], s=3)

## jupyterlite-sphinx (jesli zainstalowane)

.. replite::
    :kernel: python
    :height: 300px
    :prompt: Try Replite!

    print("Hello from JupyterLite")

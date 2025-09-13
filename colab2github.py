import nbformat

# Código para corregir renderizado de Colab en Github
nb_path = "Proyecto_Aprendizaje_Profundo.ipynb"

# Abre el notebook
with open(nb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

# Elimina la metadata widgets
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Guarda el notebook corregido
with open(nb_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

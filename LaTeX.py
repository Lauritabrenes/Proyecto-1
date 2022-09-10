#LaTeX

from pylatex import Document, LongTabu
from pylatex.utils import bold

def genenerate_longtabu():
    geometry_options = {
        "landscape": True,
        "margin": "0.9in",
        "headheight": "20pt",
        "headsep": "10pt"
    }
    doc = Document(page_numbers=True, geometry_options=geometry_options)

    with doc.create(LongTabu("X[r] X[r]")) as data_table:
        header_row1 = ["Grupo", "Minterminos binarios"]
        data_table.add_row(header_row1, mapper=[bold])
        data_table.add_hline()
        data_table.add_empty_row()
        data_table.end_table_header()
        data_table.add_row(["Grupo", "Minterminos binarios"])
        for i in sorted(groups.keys()):
          for j in groups[i]:
            int((j,2),j)
        data_table.add_row([i])
          
    doc.generate_pdf("longtabu", clean_tex=False)

genenerate_longtabu()

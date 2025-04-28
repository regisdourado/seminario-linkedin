#!/usr/bin/env python3
from weasyprint import HTML, CSS
import os

# Diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para os arquivos
html_file = os.path.join(current_dir, 'pocket_guide.html')
css_file = os.path.join(current_dir, 'pocket_guide_style.css')
output_pdf = os.path.join(current_dir, 'pocket_guide_linkedin.pdf')

# Gerar PDF
print("Gerando PDF do Pocket Guide LinkedIn para Jovens Aprendizes...")
HTML(html_file).write_pdf(
    output_pdf,
    stylesheets=[CSS(css_file)]
)

print(f"PDF gerado com sucesso: {output_pdf}")

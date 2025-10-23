import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1️⃣ URL da página do dataset
url = "https://dados.pbh.gov.br/dataset/atividade-economica"

# 2️⃣ Headers para simular um navegador
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}

# 3️⃣ Baixar o HTML da página
resp = requests.get(url, headers=headers)
resp.raise_for_status()

# 4️⃣ Parsear com BeautifulSoup
soup = BeautifulSoup(resp.text, "html.parser")

# 5️⃣ Achar todos os links dos recursos
links = []
for res_div in soup.select("li.resource-item a.resource-url-analytics"):
    link = res_div.get("href")
    if link and (link.endswith(".csv") or "resource" in link):
        links.append(link)

print(f"🔗 Links encontrados ({len(links)}):")
for link in links:
    print("-", link)

# 6️⃣ Baixar o primeiro CSV encontrado
if links:
    csv_url = links[0]
    print(f"\nBaixando: {csv_url}")
    df = pd.read_csv(csv_url, sep=";", encoding="utf-8")
    print("\n📊 Prévia dos dados:")
    print(df.head())

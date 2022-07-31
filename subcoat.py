train_x = ["Unalloyed WC/Co (Tungsten Carbide with Cobalt binder), fine grained",
           "Unalloyed WC/Co (Tungsten Carbide with Cobalt binder), coarse grained",
           "unalloyed carbide substrate with PVD coating of TiAlN (Titanium Aluminium Nitride)",
           "ultra-fine grain unalloyed substrate with PVD coating of TiAlN (Titanium Aluminium Nitride)",
           "Unalloyed carbide substrate with PVD coating of TiB2 (Titanium Diboride), fine grained",
           "tungsten carbide substrate with 6\% cobalt and PVD coating of TiAlN (Titanium Aluminium Nitride), fine-grained",
           "tungsten carbide substrate with 10\% cobalt and PVD coating of TiAlN (Titanium Aluminium Nitride), fine-grained",
           "carbide substrate and PVD coating of TiAlN (Titanium Aluminium Nitride) and TiN (Titanium Nitride), fine-grained",
           "advanced cobalt-enriched carbide substrate and CVD coating of TiCN (Titanium Carbo Nitride), thick Al2O3(Aluminium Oxide) and TiN (Titanium Nitride), fine-grained",
           "cobalt-enriched Carbide substrate with CVD coating - TiN (Titanium Nitride / thick Al2O3(Aluminium Oxide) / TiC (Titanium Carbide) / TiCN (Titanium Carbo Nitride)",
           "advanced cobalt-enriched carbide substrate with  CVD coating of thick MT-TiCN (medium temperature Titanium Carbo Nitride), thick Al2O3(Aluminium Oxide) and TiN (Titanium Nitride)",
           "Tough carbide grade Multi-layered coating TiN / Al2O3 / MT-TiCn / TiN",
           "Cobalt enriched carbide Multi-layered coating:TiN / Al2O3 / MT-TiCN / TiN",
           "Super tough carbide substrate Multilayered CVD coating:TiN / Al2O3 / MT-TiCN / TiN",
           "Carbide Multilayered CVD coating: TiN / Al2O3 / MT-TiCN / TiN",
           "Tough cobalt enriched substrate Multi-layered CVD coating:TiN / TiCN / TiN",
           "Carbide substrate Al2O3 / TiCN",
           "Carbide substrate Multi-layered CVD coating:TiN / Al2O3 / MT-TiCN",
           "Multi-layered PVD TiN / TiCN / TiN coated - turning grade",
           "Advanced Sialon ceramic grade - No coating",
           "SiC (Silicon Carbide) - reinforced aluminium oxynitirde - No coating",
           "Advanced Sialon material - No coating",
           "Advanced alumina/TiC (Titanium Carbide) ceramic (black) - No coating",
           "CVD coated pure silicon nitride (SiN) grade",
           "Pure silicon nitride (SiN) grade - No coating",
           "PVD TiN coating over aluminium oxide (Al2O3) and titanium carbonitride ceramic (TiCN)",
           "PVD TiAlN coating over a PCBN tip brazed on to a carbide insert",
           "PCBN grade with a TiN/Al2O3/TiCn CVD coating",
           "High CBN content, solid PCBN structure with multiple cutting edges and a CVD alumina coating",
           "High CBN content, PCBN tip brazed onto a carbide insert",
           "Polycrystalline Diamond tip - brazed on to carbide substrate - No coating",
           "CVD (chemical vapour deposition) deposited diamond sheet tool - brazed onto carbide substrate - No coating"
            ]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(train_x)

print(vectorizer.get_feature_names())
print(vectors.toarray())

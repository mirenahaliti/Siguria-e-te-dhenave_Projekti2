# Pigpen / Masonic Cipher dhe Scytale Transposition

#Përshkrimi i Algoritmeve
1. Scytale Transposition
Ky është një nga mjetet më të vjetra kriptografike, i përdorur historikisht nga Spartanët.

Logjika: Algoritmi bazohet në transpozicion, që do të thotë se shkronjat e mesazhit nuk ndryshojnë, por vetëm renditja e tyre.

Mekanizmi: Mesazhi shkruhet rreth një shkopi (scytale) me një diametër të caktuar (celësi). Ne e kemi simuluar këtë duke përdorur një matricë ku teksti vendoset në rreshta dhe lexohet në kolona.

2. Pigpen (Masonic) Cipher
Ky është një cipher zëvendësimi (substitution) gjeometrik.

Logjika: Çdo shkronjë e alfabetit zëvendësohet me një simbol që korrespondon me një pjesë të një rrjete gjeometrike.

Mekanizmi: Meqenëse terminalet standarde kanë vështirësi në shfaqjen e simboleve grafike, implementimi ynë përdor karakteret string (si |_|, _|, [-]) për të vizualizuar format gjeometrike të secilës shkronjë.

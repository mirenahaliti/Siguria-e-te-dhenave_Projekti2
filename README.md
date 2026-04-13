# Pigpen / Masonic Cipher dhe Scytale Transposition

## Përshkrimi i Algoritmeve

### 1. Scytale Transposition
Ky është një nga mjetet më të vjetra kriptografike, i përdorur historikisht nga Spartanët për komunikim gjatë fushatave ushtarake.

Logjika: Algoritmi bazohet në parimin e transpozicionit, ku karakteret e mesazhit origjinal (plaintext) mbeten të njëjta, por ndryshon renditja e tyre sipas një rregulli specifik.

Mekanizmi: Historikisht, mesazhi shkruhej në një rrip lëkure të mbështjellë rreth një shkopi me diametër të caktuar (që shërbente si celës). Në implementimin tonë, kjo është simuluar përmes një matrice, ku teksti rreshtohet horizontalisht dhe lexohet vertikalisht (kolonë pas kolone) për të krijuar tekstin e enkriptuar.

----

### 2. Pigpen (Masonic) Cipher
Ky është një algoritëm i tipit mono-alphabetic substitution cipher, i përdorur gjerësisht nga Masonët në shekullin e 18-të.

Logjika: Çdo shkronjë e alfabetit zëvendësohet me një simbol grafik që korrespondon me një pjesë të caktuar të një rrjete gjeometrike.

Mekanizmi: Duke qenë se terminali i kompjuterit nuk mund të vizatojë vija gjeometrike, kemi përdorur ASCII mapping. Kjo do të thotë që çdo shkronjë e kemi lidhur me karaktere tekstuale që imitojnë formën e simbolit origjinal (p.sh. |_| për B ose [-] për E). Kjo zgjedhje e bën kodin tonë të ekzekutueshëm në çdo mjedis, pa pasur nevojë për librari grafike, duke ruajtur kështu logjikën e algoritmit Masonik.

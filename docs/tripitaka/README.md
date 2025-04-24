# Tripitaka - as JSON files

The currently three folders are for the [English translation](en/README.md) (en), the [German Translation](de/README.md) and the original [Pali text (pli) in the Mahasangiti (ms)](pli/ms/README.md) edition. The last one "is a revised and edited version of the text originally created by the Vipassana Research Institute (VRI)." [Bhante Sujato](https://en.wikipedia.org/wiki/Bhante_Sujato) on [suttacentral](https://discourse.suttacentral.net/t/what-is-the-difference-between-the-pali-text-of-the-vri-and-that-of-the-mahasa-giti/2667).

I just follow his structure, he devoted his life to organize the scritures and translation. 

- Vinaya Piṭaka has 440 JSON items that combined need 6.7 MByte
- Sutta Piṭaka has 5881 JSON items that combined need 22.8 MByte
- Abhidhamma Piṭaka has 1173 JSON items, combined 11.2 MByte

The translations are incomplete (see table below) and in case of the English translation have several translators. I tried to combine their work to get as complete as possible in the collection and size comparison.

| basket            | pli #json | pli Mbyte | de #json | de MByte | en #json | en MByte |
|-------------------|----------:|----------:|---------:|---------:|---------:|---------:|
| Vinaya Piṭaka     |       440 |       6.7 |        0 |        0 |        0 |        0 |
| Sutta Piṭaka      |      5881 |      22.8 |     3957 |     11.3 |        0 |        0 |
| Abhidhamma Piṭaka |      1173 |      11.2 |        0 |        0 |        0 |        0 |
| sum               |      7494 |      40.7 |     3957 |     11.3 |        0 |        0 |

## Vinaya Piṭaka - Basket of Discipline

It has 3 books with ?, 22 and 21 chapters each. These have ?, ? and 2475 verses. 347+22+51=420 JSON files.

- [Suttavibhaṅga](https://en.wikipedia.org/wiki/Suttavibha%E1%B9%85ga) (Pali for "rule analysis") - 347 JSON files, 2.8 MByte
  - [Pāṭimokkha](https://en.wikipedia.org/wiki/P%C4%81%E1%B9%ADimokkha) 227 rules for monks (bhikkhus) and 311 for nuns (bhikkhuṇīs)
  - Bhikkhunīpātimokkhapāḷi __bi__ 333 verses, 947 lines, 100 kByte (total 127 JSON)
    - Bhikkhunivibhaṅga - Adhikaraṇasamatha __bi-vb-as__ 5 verses, 33 lines, 2 kByte
    - 6 Subfolder __bi-vb__ np(12), pc(94), pd(2), pj(5), sk(2), ss(10) - total 125 JSON files, 595 kByte
  - Bhikkhupātimokkha __bu__ 225 verses, 754 lines, 75 kByte (total 222 JSON)
    - Mahāvibhaṅga - Adhikaraṇasamatha __bu-vb-as__ 5 verses, 33 lines, 2 kByte
    - 7 subfolder __bu-vb__ ay(2), np(30), pc(92), pd(4), pj(4), sk(75), ss(13) - total 220 JSON files, 2 MByte
- [Khandhaka](https://en.wikipedia.org/wiki/Khandhaka) __kd__ 22 chapters, 22 JSON files, 2.9 MByte
  - Mahavagga has 10 chapters
  - Cullavagga has 12 chapters
- [Parivāra](https://en.wikipedia.org/wiki/Pariv%C4%81ra) __pvr__ (19 or 21 chapters) - 12784 lines, 2475 verses, 51 JSON files, 1.1 MByte
  - 1.1.0 to 1.1.332 - 2212 lines (3396 lines, 661 verses)
  - 1.2.0 to 1.2.240 - 667 lines
  - 1.3.0 to 1.3.3 - 11 lines
  - 1.4.0 to 1.4.3 - 11 lines
  - 1.5.0 to 1.5.3 - 11 lines
  - 1.6.0 to 1.6.3 - 11 lines
  - 1.7.0 to 1.7.3 - 11 lines
  - 1.8.0 to 1.8.7 - 41 lines
  - 1.9.0 to 1.9.28 - 238 lines
  - 1.10.0 tp 1.10.20 - 93 lines
  - 1.11.0 to 1.11.3 - 11 lines
  - 1.12.0 to 1.12.3 - 11 lines
  - 1.13.0 to 1.13.3 - 11 lines
  - 1.14.0 to 1.14.3 - 9 lines
  - 1.15.0 to 1.15.3 - 12 lines
  - 1.16.0 to 1.16.4 - 47 lines
  - 2.1.0 to 2.1.186 - 1401 lines (2324 lines, 410 verses)
  - 2.2.0 to 2.2.143 - 431 lines
  - 2.3.0 to 2.3.3 - 11 lines
  - 2.4.0 to 2.4.3 - 11 lines
  - 2.5.0 to 2.5.3 - 15 lines
  - 2.6.0 to 2.6.3 - 9 lines
  - 2.7.0 to 2.7.3 - 11 lines
  - 2.8.0 to 2.8.5 - 47 lines
  - 2.9.0 to 2.9.23 - 207 lines
  - 2.10.0 to 2.10.17 - 84 lines
  - 2.11.0 to 2.11.3 - 11 lines
  - 2.12.0 to 2.12.3 - 11 lines
  - 2.13.0 to 2.13.3 - 14 lines
  - 2.14.0 to 2.14.3 - 9 lines
  - 2.15.0 to 2.15.3 - 11 lines
  - 2.16.0 to 2.16.6 - 52 lines
  - 3.0 to 3.76 - 295 lines (7064 lines, 1404 verses from 3.0 to 21.87)
  - 4.0 to 4.85 - 583 lines
  - 5.0 to 5.177 - 623 lines
  - 6.0 to 6.26 - 102 lines
  - 7.0 to 7.153 - 1327 lines
  - 8.0 to 8.11 - 74 lines
  - 9.0 to 9.11 - 63 lines
  - 10.0 to 10.84 - 374 lines
  - 11.0 to 11.71 - 431 lines
  - 12.0 to 12.22 - 94 lines
  - 13.0 to 13.28 - 179 lines
  - 14.0 to 14.16 - 59 lines
  - 15.0 to 15.44 - 236 lines
  - 16.0 to 16.59 - 347 lines
  - 17.0 to 17.261 - 1109 lines
  - 18.0 to 18.32 - 136 lines
  - 19.0 to 19.110 - 450 lines
  - 20.0 to 20.51 - 230 lines
  - 21.0 to 21.87 - 352 lines

## Sutta Piṭaka

## Abhidhamma Piṭaka

# List of books and abbreviations - 1st level - 16 books

On this first level we have 4 + 5 + 7 = 16 books, grouped in 3 baskets. Size comparison follows.

- [Vinaya Piṭaka](https://en.wikipedia.org/wiki/Vinaya_Pi%E1%B9%ADaka) (_Basket of Discipline_)
  - bi - 311/333 rules for nuns (bhikkhuṇīs)
  - bu - 227/225 rules for monks (bhikkhus)
  - kd - [Khandhaka](https://en.wikipedia.org/wiki/Khandhaka)
  - pvr - [Parivāra](https://en.wikipedia.org/wiki/Pariv%C4%81ra)
- [Sutta Pitaka](https://en.wikipedia.org/wiki/Sutta_Pi%E1%B9%ADaka)
  - an - [Aṅguttara Nikāya](https://en.wikipedia.org/wiki/A%E1%B9%85guttara_Nik%C4%81ya), the "numerical" discourses.
  - dn - [Dīgha Nikāya](https://en.wikipedia.org/wiki/D%C4%ABgha_Nik%C4%81ya), the "long" discourses.
  - kn - [Khuddaka Nikāya](https://en.wikipedia.org/wiki/Khuddaka_Nik%C4%81ya), the "minor collection".
  - mn - [Majjhima Nikāya](https://en.wikipedia.org/wiki/Majjhima_Nik%C4%81ya), the "middle-length" discourses.
  - sn - [Saṃyutta Nikāya](https://en.wikipedia.org/wiki/Sa%E1%B9%83yutta_Nik%C4%81ya), the "connected" discourses.
- [Abhidhamma Piṭaka](https://en.wikipedia.org/wiki/Abhidhamma_Pi%E1%B9%ADaka) (_Basket of Higher Doctrine_) - 7 books
  - ds - [Dhammasaṅgaṇī](https://en.wikipedia.org/wiki/Dhammasa%E1%B9%85ga%E1%B9%87%C4%AB) (-saṅgaṇi or -saṅgaṇī)
  - dt - [Dhātukathā](https://en.wikipedia.org/wiki/Dh%C4%81tukath%C4%81) (dhātukathā)
  - kv - [Kathāvatthu](https://en.wikipedia.org/wiki/Kath%C4%81vatthu) (kathā-)
  - patthana - [Paṭṭhāna](https://en.wikipedia.org/wiki/Pa%E1%B9%AD%E1%B9%ADh%C4%81na) (paṭṭhāna) - 24 types of conditional relations (the Buddhist belief that causality — not a Creator deity — is the basis of existence) on some 1000 pages
  - pp - [Puggalapaññatti](https://en.wikipedia.org/wiki/Puggalapa%C3%B1%C3%B1atti) (-paññatti)
  - vb - [Vibhaṅga](https://en.wikipedia.org/wiki/Vibha%E1%B9%85ga) (vibhaṅga)
  - ya - [Yamaka](https://en.wikipedia.org/wiki/Yamaka)

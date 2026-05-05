# ModernKoreanNovelsTEI

This repository provides a high-quality dataset of **33 Korean modern literary works**, encoded in **TEI P5 (eXtensible Markup Language)**. This project aims to bridge the gap between Modern Korean literature and Digital Humanities by providing machine-readable, semantically enriched texts.

* **The web application (“Conversion of Korean Modern Literature xml/tei") built on Google AI Studio (Gemini 2.5 Flash)**: [Link](https://ai.studio/apps/drive/1gca8QHQLFCb79saG23wcFyidHFKjgUAb)

## 📌 Project Overview

Unlike simple text conversion, this dataset follows the **TEI (Text Encoding Initiative) P5 guidelines**. It includes detailed metadata, character descriptions, linguistic variations (Hanja/Hangul), and semantic tagging for emotions and places.

### Key Features

* **TEI Standard**: Fully compliant with TEI P5 (`<teiHeader>`, `<body>`, `<div>`).
* **Semantic Tagging**:
* **Characters**: Linked via `xml:id` and `ref` (e.g., `<persName ref="#YB">`).
* **Linguistic Mapping**: Original Hanja and modern Hangul mapped via `<choice>`, `<orig>`, and `<reg>`.
* **Entities**: Places (`<placeName>`), Dates (`<date>`), and Occupations (`<occupation>`).
* **Emotions**: Sentiment analysis support through `<seg type="emotion" subtype="...">`.
* **Scholarly Metadata**: Includes source descriptions, publication history, and revision logs.

## 📂 Repository Structure

* `/code`: Contains the Python scripts used for scraping raw data and the source code for preprocessing and formatting the collected files into a structured layout.
* `/dataset`: Contains the final KNoTE dataset fully processed.
* `/rawdata`: Stores the initial, unrefined data as it was first collected by the scraping scripts prior to any processing.

## 🛠 XML Structure Example (Snippet)

The dataset uses a hierarchical structure to capture both the content and the context of the literature:

```xml
<teiHeader>
    <fileDesc>
        <titleStmt>
            <title>무정(단편)</title>
            <author>이광수</author>
        </titleStmt>
    </fileDesc>
    <profileDesc>
        <particDesc>
            <listPerson>
                <person xml:id="YB"><persName>부인</persName></person>
            </listPerson>
        </particDesc>
    </profileDesc>
</teiHeader>
<text>
    <body>
        <p>
            <persName ref="#YB">부인</persName>은 <seg type="emotion" subtype="hope">희망</seg>도 없고...
        </p>
    </body>
</text>

```

## 🖥️ Conversion of Korean Modern Literature xml/tei

This session guides participants through developing a web-based TEI auto-tagging application using Google AI Studio with Gemini. We demonstrate the complete development process, including: designing system prompts that enforce TEI P5 compliance (TEI Consortium, 2025), addressing Korean-specific linguistic challenges such as agglutinative morphology and hanja transliteration, and integrating external knowledge bases for metadata enrichment. The resulting application will be publicly released, enabling participants to immediately apply automated TEI conversion to their own Korean text collections.

Link: [Conversion of Korean Modern Literature xml/tei](https://ai.studio/apps/drive/1_RJJK8By-ZkkduRvDcH-MggM_B8rLD63) (Continuously updating...)



## 📚 List of Works

| No. | Author | Title (English / Transliteration) | Date |
| :--- | :--- | :--- | :--- |
| 1 | Yi In-jik | Tears of Blood (Hyeol-ui Nu) | 1906 |
| 2 | Yi Hae-jo | The Iron World (Cheol-segye) | 1908 |
| 3 | Yi Kwang-su | The Heartless (Mujeong - Short Story) | 1910 |
| 4 | Yi Hae-jo | Blood of Flowers (Hwa-ui Hyeol) | 1911.04 |
| 5 | Kim Myeong-sun | The Girl of Mystery (Uisim-ui Sonyeo) | 1917.11 |
| 6 | Na Hye-seok | Kyung-hee | 1918.03 |
| 7 | Na Hye-seok | To the Revived Granddaughter | 1918.09 |
| 8 | Kim Dong-in | The Sorrows of the Weak | 1919.02~03 |
| 9 | Yi Ik-sang | The Straggler (Nagoja) | 1919.07.14 |
| 10 | Hyun Jin-geon | A Poor Wife (Bincheo) | 1921.01 |
| 11 | Na Hye-seok | Gyu-won | 1921.07 |
| 12 | Hyun Jin-geon | A Society That Drives You to Drink | 1921.11 |
| 13 | Choi Seo-hae | Nostalgia (Hyangsu) | 1924.04 |
| 14 | Hyun Jin-geon | A Lucky Day (Unsu Joeun Nal) | 1924.06 |
| 15 | Kim Dong-in | Potato (Gamja) | 1925.01 |
| 16 | Hyun Jin-geon | Director B and the Love Letters | 1925.02 |
| 17 | Na Do-hyang | The Watermill (Mullebang-a) | 1925.09 |
| 18 | Bang Jeong-hwan | For Our Friends | 1927.02 |
| 19 | Bang Jeong-hwan | The Eternal Shirt (Mannyeon Shirt) | 1927.03 |
| 20 | Bang Jeong-hwan | The Gold Watch | 1929.01~02 |
| 21 | Kim Dong-in | Dr. K’s Research | 1929.12 |
| 22 | Kim Nam-cheon | Water (Mul) | 1933.06 |
| 23 | Chae Man-sik | Ready-made Life | 1934.05~07 |
| 24 | Kang Kyeong-ae | Salt (Sogeum) | 1934.05~10 |
| 25 | Gye Yong-mook | Adada the Idiot (Baekchi Adada) | 1935 |
| 26 | Kim Yu-jeong | The Camellias (Dongbaek-kkot) | 1936.05 |
| 27 | Yi Sang | The Wings (Nalgae) | 1936.09 |
| 28 | Yi Hyo-seok | When Buckwheat Flowers Bloom | 1936.10 |
| 29 | Chae Man-sik | Uncle Chi-suk | 1938 |
| 30 | Jeong In-taek | Melancholy (Uuljeung) | 1940.09 |
| 31 | Kim Sa-ryang | The Man Met in the Detention Center | 1941 |
| 32 | Ji Ha-ryeon | The Journey (Dojeong) | 1946.07 |
| 33 | Kang So-cheon | The Photo Studio that Takes Pictures of Dreams | 1954.03 |

## 📝 License & Attribution

This dataset is maintained and inspired by the Digital Humanities Lab at the **Academy of Korean Studies**.
Licensed under **CC BY 4.0**.

This dataset will be uploaded to **Zenodo**, and a **DOI** will be issued for formal academic citation.

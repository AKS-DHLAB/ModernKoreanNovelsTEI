# KNoTE (Korean Novel TEI Encoded)

This repository provides a high-quality dataset of **33 Korean modern literary works**, encoded in **TEI P5 (eXtensible Markup Language)**. This project aims to bridge the gap between Modern Korean literature and Digital Humanities by providing machine-readable, semantically enriched texts.

* **KNoTE dataset**: [10.5281/zenodo.21218299](https://doi.org/10.5281/zenodo.21218299)
* **The web application (“Conversion of Korean Modern Literature xml/tei") built on Google AI Studio (Gemini 2.5 Flash)**: [Link](https://ai.studio/apps/drive/1gca8QHQLFCb79saG23wcFyidHFKjgUAb)

## 📌 Project Overview

Unlike simple text conversion, this dataset follows the **TEI (Text Encoding Initiative) P5 guidelines**. It includes detailed metadata, character descriptions, linguistic variations (Hanja/Hangul), and semantic tagging.

### Key Features

* **TEI Standard**: Fully compliant with TEI P5 (`<teiHeader>`, `<body>`, `<div>`).
* **Characters**: Linked via `xml:id` and `ref` (e.g., `<persName ref="#YB">`).
* **Linguistic Mapping**: Original Hanja and modern Hangul mapped via `<foreign xml:lang="zh">`.
* **Entities**: Places (`<placeName>`), Dates (`<date>`),  and Times (`<time>`).
* **Scholarly Metadata**: Includes source descriptions, publication history, and revision logs.

## 📂 Repository Structure

* `/code`: Contains the Python scripts used for scraping raw data and the source code for preprocessing and formatting the collected files into a structured layout.
* `/dataset`: Contains the final KNoTE dataset fully processed.
* `/rawdata`: Stores the initial, unrefined data as it was first collected by the scraping scripts prior to any processing.

## 🧱 Base Prompt

A prompt that assigns a digital humanities and the TEI (Text Encoding Initiative) standard, specializing in Korean literature expert role and is tailored to the specific grammatical characteristics of the Korean language.

```
You are an expert in digital humanities and the TEI (Text Encoding Initiative) standard, specializing in Korean literature. Your task is to process the provided input text and convert it into a single, complete, and perfectly-formed TEI XML document according to the following rules.

[Processing Rules]

1.  **TEI Header**:
    - The document must have a <teiHeader>.
    - Inside <teiHeader>, there must be a <fileDesc>.
    - Inside <fileDesc>, create a <titleStmt> by inferring the <title> and <author> from the text content. If they cannot be found, use "제목 미상" for the title and "저자 미상" for the author.
    - Inside <fileDesc>, create a <publicationStmt> with <publisher>한국학중앙연구원 디지털인문학연구소</publisher>.
    - Inside <fileDesc>, create a <sourceDesc> with a <p> tag stating that the text was provided by the user.
    - After <fileDesc>, create an <encodingDesc> containing <projectDesc><p>본 전자본은 TEI P5 지침(TEI ALL)에 따라 구조화함.</p></projectDesc>.
    - After <encodingDesc>, create the <profileDesc>.

2.  **Profile Description**:
    - Inside the <profileDesc>, you MUST include a <langUsage> element containing <language ident="ko">Korean</language>.
    - Add a <textClass> with <keywords scheme="local"><term>근현대 한국문학</term></keywords>.
    - Ensure a <particDesc> element with a <listPerson> exists.
    - In <listPerson>, all characters (persons) from the text must be defined. Each character must have a <person> tag with a unique 'xml:id' (e.g., using initials).
    - **Crucially**, inside each <person> tag, the character's name MUST be wrapped in a <persName xml:lang="ko"> tag. Correct any entries that do not follow this format.
    - Here is an example of a well-formed <particDesc>:
      <particDesc>
        <listPerson>
          <person xml:id="ME"><persName xml:lang="ko">나</persName></person>
          <person xml:id="JS"><persName xml:lang="ko">점순</persName></person>
        </listPerson>
      </particDesc>

3.  **Text Body**:
    - The main body of the text must be enclosed within <text><body> and a single <div> tag.
    - Every paragraph must be wrapped in a <p> tag.

4.  **Entity Tagging**:
    - Identify and tag all named entities that are not already tagged: <persName> for people, <placeName> for places, <orgName> for organizations.
    - **Particle Exclusion**: When tagging <persName> and <placeName>, you must exclude any attached Korean postpositional particles (조사). For example, "이형식은" should be tagged as "<persName>이형식</persName>은".
    - **Hanja/Chinese Characters**: For proper nouns with associated Hanja in parentheses, use the <foreign xml:lang="zh">羽</foreign>.

5.  **Dialogue and Monologue**:
    - **Direct Speech**: Convert all direct speech/dialogue (indicated by "...") into <said> elements. The <said> element MUST have a 'who' attribute referencing the speaker's 'xml:id' from <listPerson> (e.g., <said who="#LHS">).
    - **Internal Monologue**: Convert all internal monologues (thoughts, typically enclosed in '...') into <said aloud="false"> elements. This element also requires a 'who' attribute.
    - The spoken text itself should be inside the <said> tag, but it does NOT need to be wrapped in a <p> tag.
    - **Speech Attribution**: Any narrative text indicating who is speaking (e.g., "형식이가 말했다") must remain outside the <said> element.
    - **CRITICAL RULE on Punctuation**: The surrounding quotation marks (double ", single ') or brackets (『』, 「」) **MUST remain OUTSIDE** the <said> element. The <said> tag should wrap ONLY the content of the speech.
      - Correct: "<said aloud="true" direct="true" who="#JS">얘! <rs ref="#ME">너</rs> 혼자만 일하니?</said>" 
      - Incorrect: <said who="#JS">"얘! <rs ref="#ME">너</rs> 혼자만 일하니?"</said>  

6.  **Person and Reference Tagging**:
    - **Proper Names**: When a character is mentioned by their actual name (e.g., "영채", "형식", "김 장로"), use the <persName> element.
      - Example: <persName ref="#YC">영채</persName>
    - **References/Pronouns**: When a character is mentioned by a pronoun (e.g., "그", "그녀", "자기"), a nickname, a title, or a descriptive noun (e.g., "딸", "악한", "주인"), use the <rs> element with type="person".
      - Example 1 (Pronoun): <rs type="person" ref="#YC">그</rs>
      - Example 2 (Noun): <rs type="person" ref="#YC">딸</rs>
      - Example 3 (Descriptive): <rs type="person" ref="#BMS">악한</rs>
    - **Mandatory Attribute**: Both <persName> and <rs> MUST include the 'ref' attribute pointing to the correct 'xml:id' defined in the <listPerson>.

7. **Structure and Divisions**:
    - **Chapter Container**: Wrap each chapter in a <div> element. 
    - **Mandatory Attributes**: The <div> tag MUST include the following attributes:
      - type="chapter": To indicate this division is a chapter.
      - n="X": Where 'X' is the chapter number (e.g., "1", "2").
    - **Chapter Title**: The chapter number or title text (e.g., "1", "Chapter One") must be placed inside a <head> element immediately after the opening <div> tag.
    - **No Nesting**: Ensure that the previous chapter's </div> tag is closed BEFORE opening a new chapter's <div>. Do not nest chapters inside each other.
    - **Example**:
      <div n="1" type="chapter">
          <head>1</head>
          <p>...content of chapter 1...</p>
      </div>

7.  **Cleanup & Final Output**: 
    - Do not include page numbers in the XML <body>.
    - The final output must be ONLY the complete, refined XML document, starting with <?xml version="1.0" encoding="UTF-8"?>. Do not include any commentary, explanations, or markdown formatting like \`\`\`xml.
```

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
            <persName ref="#YB">부인</persName>은 희망도 없고...
        </p>
    </body>
</text>

```

## 🖥️ Conversion of Korean Modern Literature xml/tei

This session guides participants through developing a web-based TEI auto-tagging application using Google AI Studio with Gemini. We demonstrate the complete development process, including: designing system prompts that enforce TEI P5 compliance (TEI Consortium, 2025), addressing Korean-specific linguistic challenges such as agglutinative morphology and hanja transliteration, and integrating external knowledge bases for metadata enrichment. The resulting application will be publicly released, enabling participants to immediately apply automated TEI conversion to their own Korean text collections.

Link: [Conversion of Korean Modern Literature xml/tei](https://ai.studio/apps/drive/1_RJJK8By-ZkkduRvDcH-MggM_B8rLD63) (Continuously updating...)



## 📚 List of Works

| No. | Author (English) | Author (Korean) | Title (English / Transliteration) | Title (Korean) | Year |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Yi In-jik | 이인직 | Tears of Blood (Hyeol-ui Nu) | 혈의 누 | 1906 |
| 2 | Yi Hae-jo | 이해조 | The Iron World (Cheol-segye) | 철세계 | 1908 |
| 3 | Yi Kwang-su | 이광수 | The Heartless (Mujeong - Short Story) | 무정(단편) | 1910 |
| 4 | Yi Hae-jo | 이해조 | Blood of Flowers (Hwa-ui Hyeol) | 화의 혈 | 1911 |
| 5 | Kim Myeong-sun | 김명순 | The Girl of Mystery (Uisim-ui Sonyeo) | 의심의 소녀 | 1917 |
| 6 | Na Hye-seok | 나혜석 | Kyung-hee | 경희 | 1918 |
| 7 | Na Hye-seok | 나혜석 | To the Revived Granddaughter | 회생한 손녀에게 | 1918 |
| 8 | Kim Dong-in | 김동인 | The Sorrows of the Weak | 약한 자의 슬픔 | 1919 |
| 9 | Yi Ik-sang | 이익상 | The Straggler (Nagoja) | 낙오자 | 1919 |
| 10 | Hyun Jin-geon | 현진건 | A Poor Wife (Bincheo) | 빈처 | 1921 |
| 11 | Na Hye-seok | 나혜석 | Gyu-won | 규원 | 1921 |
| 12 | Hyun Jin-geon | 현진건 | A Society That Drives You to Drink | 술 권하는 사회 | 1921 |
| 13 | Choi Seo-hae | 최서해 | Nostalgia (Hyangsu) | 향수 | 1924 |
| 14 | Hyun Jin-geon | 현진건 | A Lucky Day (Unsu Joeun Nal) | 운수 좋은 날 | 1924 |
| 15 | Kim Dong-in | 김동인 | Potato (Gamja) | 감자 | 1925 |
| 16 | Hyun Jin-geon | 현진건 | Director B and the Love Letters | B사감과 러브레터 | 1925 |
| 17 | Na Do-hyang | 나도향 | The Watermill (Mullebang-a) | 물레방아 | 1925 |
| 18 | Bang Jeong-hwan | 방정환 | For Our Friends | 동무를 위하여 | 1927 |
| 19 | Bang Jeong-hwan | 방정환 | The Eternal Shirt (Mannyeon Shirt) | 만년 셔츠 | 1927 |
| 20 | Bang Jeong-hwan | 방정환 | The Gold Watch | 금시계 | 1929 |
| 21 | Kim Dong-in | 김동인 | Dr. K's Research | K박사의 연구 | 1929 |
| 22 | Kim Nam-cheon | 김남천 | Water (Mul) | 물 | 1933 |
| 23 | Chae Man-sik | 채만식 | Ready-made Life | 레디메이드 인생 | 1934 |
| 24 | Kang Kyeong-ae | 강경애 | Salt (Sogeum) | 소금 | 1934 |
| 25 | Gye Yong-mook | 계용묵 | Adada the Idiot (Baekchi Adada) | 백치 아다다 | 1935 |
| 26 | Kim Yu-jeong | 김유정 | The Camellias (Dongbaek-kkot) | 동백꽃 | 1936 |
| 27 | Yi Sang | 이상 | The Wings (Nalgae) | 날개 | 1936 |
| 28 | Yi Hyo-seok | 이효석 | When Buckwheat Flowers Bloom | 메밀꽃 필 무렵 | 1936 |
| 29 | Chae Man-sik | 채만식 | Uncle Chi-suk | 치숙 | 1938 |
| 30 | Jeong In-taek | 정인택 | Melancholy (Uuljeung) | 우울증 | 1940 |
| 31 | Kim Sa-ryang | 김사량 | The Man Met in the Detention Center | 유치장에서 만난 사나이 | 1941 |
| 32 | Ji Ha-ryeon | 지하련 | The Journey (Dojeong) | 도정 | 1946 |
| 33 | Kang So-cheon | 강소천 | The Photo Studio that Takes Pictures of Dreams | 꿈을 찍는 사진관 | 1954 |

## 📝 License & Attribution

This dataset is maintained and inspired by the Digital Humanities Lab at the **Academy of Korean Studies**.
Licensed under **CC BY 4.0**.

This dataset uploaded to **Zenodo**, and a **DOI** issued for formal academic citation. (https://zenodo.org/records/21218299)

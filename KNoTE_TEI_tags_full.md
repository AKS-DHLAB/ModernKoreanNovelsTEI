# Table 1 (Extended): TEI elements and attributes used in the KNoTE dataset

This table extends the original Table 1 to cover **every** TEI element and key
attribute actually found in the KNoTE TEI files (`dataset/*.xml`, 33 works).
It keeps the original four-column format — Category, Element, Key Attributes,
Function — but adds the categories and tags omitted from the published table
(dates, times, measures, terms, editorial/apparatus markup, named entities,
stand-off annotation, etc.). Counts in parentheses are how many times the
attribute occurs in the corpus. Obvious encoding typos in the source
(e.g. `subtyep`, `driect`, `calender`, `fasle`, `rolename`, `listPalce`) are
normalised to their canonical TEI spelling.

## TEI Header

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| TEI Header | `teiHeader` | — | Root metadata wrapper for each text |
| TEI Header | `fileDesc` | — | Bibliographic description of the electronic file |
| TEI Header | `titleStmt` | — | Title, author, encoder credits |
| TEI Header | `respStmt` | `xml:id` | Encoder/reviewer attribution |
| TEI Header | `email` | — | Encoder/contributor email address |
| TEI Header | `resp` | — | Nature of the responsibility (encoding, review) |
| TEI Header | `author` | `ref` | Work's author, linked to authority record |
| TEI Header | `editor` | `role` | Editor responsible for the edition |
| TEI Header | `publicationStmt` | — | Publication/distribution statement |
| TEI Header | `publisher` | `ref` | Publishing body |
| TEI Header | `idno` | `type` | Identifier (ISNI, ORCID, wikidata, wikisource, encykorea, uci, …) |
| TEI Header | `sourceDesc` | — | Source provenance container |
| TEI Header | `bibl` | `type`, `xml:lang` | Source citation (digitalSource, originalSource, reference) |
| TEI Header | `biblStruct` | `type`, `xml:lang` | Structured bibliographic citation |
| TEI Header | `analytic` | — | Analytic-level bibliographic info (article/story) |
| TEI Header | `monogr` | — | Monograph-level bibliographic info |
| TEI Header | `imprint` | — | Imprint (place, publisher, date) within `monogr` |
| TEI Header | `series` | — | Series-level bibliographic info |
| TEI Header | `biblScope` | `unit` | Scope of a citation (page, volume) |
| TEI Header | `listBibl` | — | List of bibliographic items |
| TEI Header | `relatedItem` | `type` | Related bibliographic item |
| TEI Header | `encodingDesc` | — | Encoding standard (TEI ALL) |
| TEI Header | `projectDesc` | — | Goal/scope of the encoding project |
| TEI Header | `classDecl` | — | Classification-scheme declarations |
| TEI Header | `taxonomy` | `xml:id` | Taxonomy used for `textClass` keywords |
| TEI Header | `category` | `xml:id` | A category within a taxonomy |
| TEI Header | `catDesc` | — | Description of a taxonomy category |
| TEI Header | `profileDesc` | — | Non-bibliographic description of the text |
| TEI Header | `langUsage` | — | Languages used in the text |
| TEI Header | `language` | `ident` | A language present (`ident="ko"`) |
| TEI Header | `textClass` | — | Classification/keywords container |
| TEI Header | `keywords` | `scheme` | Subject keywords (`scheme="local"`) |
| TEI Header | `abstract` | — | Short summary of the work |
| TEI Header | `revisionDesc` | — | Revision history container |
| TEI Header | `change` | `when`, `who` | Encoding/review dates and agent |

## Characters / Participants

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Characters | `particDesc` | — | Description of participants (character registry wrapper) |
| Characters | `listPerson` | `xml:id`, `type` | Character registry |
| Characters | `person` | `xml:id`, `sex`, `role`, `sameAs`, `type`, `ref` | Individual character |
| Characters | `personGrp` | `xml:id`, `type`, `role`, `sex`, `corresp` | Collective character group |
| Characters | `persName` | `xml:id`, `xml:lang`, `type`, `sex` | Name in Korean or Hanja (in registry) |
| Characters | `roleName` | `ref`, `type`, `subtype` | Title/role component of a name (occupation, etc.) |
| Characters | `occupation` | `ref` | Character's occupation |
| Characters | `relation` | `name`, `active`, `passive`, `mutual` | Relationship between characters |
| Characters | `listRelation` | — | List of character relationships |
| Characters | `roleDesc` | — | Description of a person's role |

## Entities (named-entity mentions in the text)

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Entities | `persName` | `ref`, `xml:lang`, `type`, `sex`, `who`, `sameAs` | Named character mention |
| Entities | `rs` | `ref`, `type`, `subtype`, `corresp`, `sex`, `ana`, `who`, `mode` | Referring string — pronoun/epithet/general reference. `type` ∈ {person, place, object, org, occupation, person_group, pronoun, event, group, epithet, animal, vehicle, vessel, food, …} |
| Entities | `placeName` | `ref`, `type`, `subtype`, `xml:lang`, `sameAs`, `corresp`, `xml:id` | Place name (country, city, district, facility, river, station, …) |
| Entities | `orgName` | `ref`, `type`, `subtype`, `xml:lang`, `corresp` | Organisation name (school, military, police, newspaper, ethnicity, …) |
| Entities | `roleName` | `ref`, `type`, `subtype` | Occupational/honorific title in running text |
| Entities | `objectName` | `ref`, `type`, `subtype`, `xml:lang` | Name of a notable object |
| Entities | `name` | `type`, `corresp`, `ref`, `xml:id` | Generic proper name (language, deity, plant, brand, studies) |
| Entities | `term` | `type`, `subtype`, `ref`, `corresp` | Domain/concept term (ideology, concept, food, disease, occupation, …) |
| Entities | `gloss` | — | Gloss/explanation attached to a term |

## Dates, Times & Events

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Dates & Time | `date` | `when`, `type`, `subtype`, `from`, `to`, `dur`, `calendar`, `quantity`, `ref` | Date reference. `type` ∈ {season, frequency, holiday, century, year, duration, marketDay, historicalPeriod, …}; `calendar` ∈ {lunar, gregorian} |
| Dates & Time | `time` | `when`, `type`, `subtype`, `from`, `to`, `dur` | Time-of-day reference (morning, evening, night, daytime, season, frequency, …) |
| Dates & Time | `event` | `xml:id`, `from`, `to`, `sameAs` | Event with temporal span |
| Dates & Time | `listEvent` | — | List of events |

## Measures & Quantities

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Measures | `measure` | `type`, `unit`, `quantity`, `atLeast`, `atMost`, `from`, `to`, `subtype`, `ref`, `precision` | Measured quantity. `type` ∈ {currency, age, count, amount, duration, distance, length, time, degree, volume, depth, area, weight}; `unit` ∈ {year, KRW, won, jeon, 里, pyeong, 兩, 尺, 名, 間, …} |

## Speech & Quotation

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Speech | `said` | `who`, `aloud`, `direct`, `mode`, `agent`, `type` | Direct speech, thought, or monologue. `aloud`/`direct` ∈ {true, false}; `mode` ∈ {thought, soliloquy, recollection, imagined, dream} |
| Speech | `q` | `type`, `who`, `subtype` | Quotation (letter, note, essay, proverb, lyrics, leaflet) |
| Speech | `quote` | `type`, `source`, `ref` | Quoted passage attributed to a source |
| Speech | `seg` | `type` | Arbitrary segment (e.g. `narratorial_commentary`) |

## Language

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Language | `foreign` | `xml:lang`, `type` | Hanja (`xml:lang="zh"`) / Japanese (`xml:lang="ja"`) preserved within Hangul |

## Structure

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Structure | `text` | — | The body of a single work |
| Structure | `floatingText` | `type` | Embedded text (letter, inset narrative) |
| Structure | `body` | — | Main text body |
| Structure | `div` | `type`, `n` | Chapter/section division (chapter, embedded, frame, preface, afterword, letter, …) |
| Structure | `head` | — | Chapter/section title |
| Structure | `p` | `xml:lang` | Paragraph |
| Structure | `lb` | — | Line break |
| Structure | `epigraph` | — | Epigraph at the head of a text/division |
| Structure | `opener` | — | Opening matter of a division |
| Structure | `closer` | — | Closing matter of a division |
| Structure | `salute` | — | Salutation within an opener/closer |
| Structure | `signed` | — | Signature within a closer |
| Structure | `dateline` | — | Date/place line in opener/closer |
| Structure | `address` | — | Postal/address block |
| Structure | `addrLine` | — | A line within an address |

## Editorial / Apparatus

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Editorial | `choice` | — | Wraps alternative readings (orig/reg, sic/corr) |
| Editorial | `sic` | — | Apparent error reproduced from the source |
| Editorial | `corr` | — | Editorial correction of an error |
| Editorial | `orig` | — | Original (non-normalised) form |
| Editorial | `reg` | `xml:lang`, `cert` | Regularised/normalised form |
| Editorial | `supplied` | `resp`, `cert` | Text supplied by the editor |
| Editorial | `gap` | `reason`, `desc` | Omitted/illegible material (illegible, physical damage, omission) |
| Editorial | `note` | `type`, `corresp`, `resp`, `place` | Editorial/authorial annotation |
| Editorial | `desc` | — | Prose description (of a gap, object, etc.) |
| Editorial | `ref` | `target`, `type` | Cross-reference/pointer |
| Editorial | `title` | `level`, `type`, `ref` | Title mention (`level` ∈ a, m, j, s) |

## Stand-off Annotation (registries outside the text)

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Stand-off | `standOff` | — | Container for stand-off annotation/registries |
| Stand-off | `settingDesc` | — | Setting description (places/events) |
| Stand-off | `listPlace` | — | Registry of places |
| Stand-off | `place` | `xml:id`, `sameAs`, `type`, `subtype`, `ana`, `corresp` | A place in the registry |
| Stand-off | `placeName` | (see Entities) | Place name within a `place` |
| Stand-off | `settlement` | `ref` | Settlement (town/city) |
| Stand-off | `region` | `ref` | Region |
| Stand-off | `country` | `ref` | Country |
| Stand-off | `location` | — | Geographic location of a place |
| Stand-off | `geo` | — | Geographic coordinates |
| Stand-off | `offset` | — | Spatial offset relative to another place |
| Stand-off | `listOrg` | — | Registry of organisations |
| Stand-off | `org` | `xml:id`, `type`, `sameAs` | An organisation in the registry |
| Stand-off | `listObject` | — | Registry of objects |
| Stand-off | `object` | `type`, `ref`, `xml:id`, `sameAs`, `subtype` | A notable object in the registry |
| Stand-off | `objectIdentifier` | — | Identifier block for an object |
| Stand-off | `interpGrp` | `type` | Group of interpretive annotations |
| Stand-off | `interp` | `xml:id`, `corresp` | An interpretive annotation/value |

## Root

| Category | Element | Key Attributes | Function |
|---|---|---|---|
| Root | `TEI` | `xml:lang` | Root element of each TEI document |

---

### Notes

- **Scope.** Element and attribute inventory is drawn from the 33 fully-encoded
  TEI files in `dataset/`. The `rawdata/` folder (311 files) is pre-TEI scraped
  Wikisource content using non-TEI tags (`work`, `paragraph`, `heading`,
  `content`, …) and is therefore not part of this TEI schema table.
- **Attribute frequency.** The most-used referring elements are `rs` (~12,370
  occurrences), `persName` (~6,445), `p` (~6,469) and `said` (~3,476);
  the additions over the original Table 1 — `date`, `time`, `measure`, `term`,
  `object`, editorial/apparatus and stand-off elements — appear hundreds of
  times each and were absent from the published table.
- **Normalisation.** A handful of mis-spelled tags/attributes exist in the raw
  files (`rolename`→`roleName`, `listPalce`→`listPlace`, `subtyep`→`subtype`,
  `driect`/`direct`, `calender`→`calendar`, `fasle`→`false`, `sameAS`→`sameAs`).
  These are listed here under their correct TEI forms.

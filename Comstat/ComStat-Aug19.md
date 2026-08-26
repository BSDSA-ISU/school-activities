# Activity Asynchronous

- [Activity Asynchronous](#activity-asynchronous)
  - [Activity Requirements](#activity-requirements)
  - [Submission Guidelines](#submission-guidelines)
  - [A. Raw dataset](#a-raw-dataset)
  - [Anser](#anser)
  - [1. Problem Identification](#1-problem-identification)
  - [2. Preparation Actions](#2-preparation-actions)
  - [3. Prepared Dataset (Cleaned)](#3-prepared-dataset-cleaned)

![aaaaaq](./tenshi.gif)

---

## Activity Requirements

1. **Problem Identification**: Enumerate all data quality issues present in the raw dataset.
2. **Preparation Actions:** Create a table with the following column headers to document your cleaning strategy"
   1. Issue
   2. Action Taken
   3. Method/Note
3. **prepared Dataset (Cleaned):** Write down the final cleaned dataset using the exact standard column fields below:

| Student ID | Name | Gender | Age | Program | Final Grade | Attendance (%) |
| - | - | - | - | - | - | - |

## Submission Guidelines

- **Format**: Take a clear, well-lit photo of your handwritten work.
- **Destination:** Upload your image file to your **Individual Folder in our shared Google Drive.
- **File naming convention**: Chapter 2 activity_lastname_firstname
- **Deadline 2day 11:59 PM**

## A. Raw dataset

| Student ID | Name | Gender | Age | Program | Final Grade | Attendance (%) |
| - | - | - | - | - | - | - |
| S001 | Ana Reyes | Female | 20 | BSDSA | 88 | 95 |
| S002 | Juan dela Crus | Male | 21 | BS DSA | 90 | 93 |
| SS03 | Maria Santos | FEMALE | 250 | bsdsa | 85 | 91 |
| S004 | Pedro Cruz | Male | 19 | BSIT | - | 89 |
| S004 | Pedro Cruz | Male | 19 | BSIT | 78 | 89 |
| S005 | Liza Tan | female | 22 | BSCS | 92 | 130 |
| S006 | Mark Lim | Male | 20 | BSCS | - | 88 |
| S007 | JANE ONG | F | 21 | BS DSA | 91 | 96 |

## Anser
q
## 1. Problem Identification

The raw dataset has these data quality issues:

1. **Invalid Student ID** — `SS03` should follow the `S001` format.
2. **Inconsistent Gender values** — `Female`, `FEMALE`, `female`, `Male`, and `F` are used.
3. **Invalid Age** — Maria Santos has an age of `250`.
4. **Inconsistent Program values** — `BSDSA`, `BS DSA`, and `bsdsa` refer to the same program.
5. **Missing Final Grade** — Pedro Cruz and Mark Lim have `-` instead of a grade.
6. **Duplicate record** — Pedro Cruz (`S004`) appears twice.
7. **Invalid Attendance** — Liza Tan has `130%`, which exceeds the valid range of 0–100%.
8. **Inconsistent Name capitalization** — `JANE ONG` is written entirely in uppercase.

## 2. Preparation Actions

| Issue                                         | Action Taken                | Method/Note                                                 |
| --------------------------------------------- | --------------------------- | ----------------------------------------------------------- |
| Invalid Student ID (`SS03`)                   | Corrected to `S003`         | Followed the standard `S###` format                         |
| Inconsistent Gender values                    | Standardized gender values  | Converted `FEMALE`, `female`, and `F` to `Female`           |
| Invalid Age (`250`)                           | Corrected to `20`           | Corrected the obvious data entry error                      |
| Inconsistent Program values                   | Standardized program names  | Changed `BS DSA` and `bsdsa` to `BSDSA`                     |
| Missing Final Grade (`-`)                     | Marked as missing           | No valid grade was provided, so it should not be fabricated |
| Duplicate `S004` record                       | Removed duplicate           | Kept the record containing the valid Final Grade of `78`    |
| Invalid Attendance (`130%`)                   | Corrected to `100%`         | Attendance cannot exceed 100%                               |
| Inconsistent Name capitalization (`JANE ONG`) | Standardized capitalization | Changed to `Jane Ong`                                       |

## 3. Prepared Dataset (Cleaned)

| Student ID | Name           | Gender | Age | Program | Final Grade | Attendance (%) |
| ---------- | -------------- | ------ | --: | ------- | ----------: | -------------: |
| S001       | Ana Reyes      | Female |  20 | BSDSA   |          88 |             95 |
| S002       | Juan dela Crus | Male   |  21 | BSDSA   |          90 |             93 |
| S003       | Maria Santos   | Female |  20 | BSDSA   |          85 |             91 |
| S004       | Pedro Cruz     | Male   |  19 | BSIT    |          78 |             89 |
| S005       | Liza Tan       | Female |  22 | BSCS    |          92 |            100 |
| S006       | Mark Lim       | Male   |  20 | BSCS    |     Missing |             88 |
| S007       | Jane Ong       | Female |  21 | BSDSA   |          91 |             96 |

**Important:** For `S006`, don't invent a Final Grade. Writing **Missing** is the proper data-cleaning treatment because the raw dataset provides no information from which the grade can be reliably determined.


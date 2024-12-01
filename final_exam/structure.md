# Final Exam - Data Analytics with Apache Spark

## Final Exam Structure

- **Total time**: 120 min

- **Multi-Choice**: 40 questions / 60 min
  1. Spark Machine Learning: 16
  2. Graph Analytics with Apache Spark GraphFrames: 8
  3. Streaming Analytics with Apache Spark Structured Streaming: 8
  4. Distributed Systems, Spark Cores (DataFrames, SQL) and Best Practices: 8

- **Lab**: 25 questions / 60 min

## Exam Submission Requirements

*Only submissions that comply with the guidelines below will be accepted. Otherwise, no points will be awarded.*

### Multi-Choice

- **Format**: CSV. Comma (",") separated.
- **Filename**: multi-choice-{exam_code}.csv.
- **File headers**: question,answer
- Questions which have multiple correct answers, are wrapped by double quote. Example: "A,B"

Sample:

```csv
question,answer
1,A
2,"B,C"
```

### Lab

- **Format**: .ipynb
- **Filename**: lab.ipynb
- DO NOT change the name of placeholder variables

### Submission

#### Email

- Using personal email (Gmail)
- **Email Subject**: DSEB_63_2024 Final Exam Submission: `Student_ID`
- **To**: <hoangngocthe168@gmail.com>

#### Attachment (attach the zipped file, but not the link)

- **Compression format**: ZIP
- **Filename**: student_id.zip
- **Folder Structure**:

```text
student_id/
├── multi-choice-{exam_code}.csv
│
├── lab.ipynb
│
└── data/
    ├── input/
    │   └── anyfile
    └── output/
        └── anyfile

```

### Submission Sample

- final_exam/12345678
- final_exam/12345678.zip

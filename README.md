# CSCI5832-Shared-Task
### Team member
Arunima Maitra: Arunima.Maitra@colorado.edu

Timur Tripp: timur.tripp@colorado.edu

Weiqiang Wang: Weiqiang.Wang@colorado.edu



<!-- ABOUT THE PROJECT -->
## Task 2: Safe Biomedical Natural Language Inference for Clinical Trials 

### Train.json


Comparison Example

    "dbed5471-c2fc-45b5-b26f-430c9fa37a37": {
        "Type": "Comparison",
        "Section_id": "Adverse Events",
        "Primary_id": "NCT00093145",
        "Secondary_id": "NCT00703326",
        "Statement": "Heart-related adverse events were recorded in both the primary trial and the secondary trial.",
        "Label": "Entailment",
        "Primary_evidence_index": [
            0,
            3
        ],

        "Secondary_evidence_index": [
            0,
            7,
            8,
            9,
            10
        ]
    }

 Single Example

    "83b83400-1439-462d-bba3-42817b5b1fa1": {
        "Type": "Single",
        "Section_id": "Adverse Events",
        "Primary_id": "NCT00777049",
        "Statement": "Most of the cases of CHF in the primary trial, were in cohort 1.",
        "Label": "Entailment",
        "Primary_evidence_index": [
            0,
            6,
            14,
            20
        ]
    }

### Train.txt
    label_map = {"Entailment": 0,
                 "Contradiction": 1
    }
    "83b83400-1439-462d-bba3-42817b5b1fa1" "0" "Most of the cases of CHF in the primary trial, were in cohort 1."

## Task 2: TF-IDF Entailment Prediction Baseline Result
    F1:0.502415
    precision_score:0.485981
    recall_score:0.520000




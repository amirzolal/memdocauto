import requests
import json

IV_PATHOLOGY_QUESTION_DICT = {

1:["DEGENERATIVE ERKRANKUNG", "DEGENERATION","OSTEOCHONDROSE","SPONDYLARTHROSE","BSV","BANDSACHEIBENVORFALL","VORFALL","SKS","SPINALKANALSTENOSE","NPP","PROLAPS","RECESSUSSTENOSE","ZYSTE","SYNOVIALE ZYSTE","JUXTAARTIKULÄRE ZYSTE","BS-HERNIE","DISKUSPROLAPS","DISKHERNIATION","REZESSUSSTENOSE","FORAMENSTENOSE","FORAMINALE", "SAGITTALE DYSBALANCE","SAGITTALE","HYPERKYPHOSE","SKOLIOSE","MYELOPATHIE", "FACETTENGELENKARTHROSE","FACETTENGELENKZYSTE","ISG"],
2:["DEFORMITÄT (NICHT-DEGENERATIV)","MB. SCHEUERMANN","MORBUS SCHEUERMANN","SCHEUERMANN", "SCHEUERMANNKRANKHEIT","JUVENILE KYPHOSE","JUVENILE SKOLIOSE","ADOLESCENTE KYPHOSE", "ADOLESCENTE SKOLIOSE", "IDIOPATHISCHE SKOLIOSE", "IDIOPATHISCHE KYPHOSE", "KAMPTOKORMIE", "KAMPTOKORMIA"],
3:["FRAKTUR","KOMPRESSIONSFRAKTUR","WIRBELBRUCH","BRUCH"],
4:["PATHOLOGISCHE FRAKTUR","TUMORFRAKTUR","PATHOL. FRAKUR", "PATH. FRAKUR"],
5:["DYSPLASTISCHE SPONDYLOLISTHESES"],
6:["CHIARI MALFORMATION","CHIARI-MALFORMATION"],
7:["SPONDYLODISZITIS","DISZITIS","ITIS","ABSZESS","EPIDURALER ABSZESS"],
8:["METASTASE","TUMOR","INTRADURALER TUMOR","INTRASPINALER TUMOR"],
9:["WUNDHEILUNGSSTÖRUNG","WUNDINFEKTION","FEHLLAGE","NACHBLUTUNG"],
10:["ANDERE"]

}

DEGENERATIVE_DISEASE_PRIM_DICT = {

1:["BS-HERNIE","BSV","NPP","BANDSCHEIBENVOFALL","BANDSCHEIBENPROLAPS"],
2:["ZENTRALE STENOSE","SKS","STENOSE"],
3:["REZESSUSSTENOSE","REZESSUS","LATERALE STENOSE"],
4:["FORAMENSTENOSE","FORAMINALE STENOSE"],
5:["BANDSCHEIBENDEGENERATION","OSTEOCHONDROSE"],
6:["HYPERKYPHOSE","SKOLIOSE", "FRONTALE DYSBALANCE", "SAGITTALE DYSBALANCE"],
7:["SPONDYLOLISTHESE","OLISTHESE", "LISTHESE"],
8:["ANDERE INSTABILITÄT"],
9:["MYELOPATHIE","ZERVIKALE MYELOPATHIE","THORAKALE MYELOPATHIE"],
10:["FACETTENGELENKARTHROSE", "FACETTENSYNDROM", "FACETTENSCHMERZEN" ],
11:["FACETTENGELENKZYSTE"],
12:["ISG","ISG ARTHROSE", "ISG SCHMERZEN", "ISG SCHMERZSYNDROM" ]

}

SEGMENTE_DICT = {
    "C0-C1": "C0, C1",
    "C0-C2": "C0, C1, C2",
    "C0-C3": "C0, C1, C2, C3",
    "C0-C4": "C0, C1, C2, C3, C4",
    "C0-C5": "C0, C1, C2, C3, C4, C5",
    "C0-C6": "C0, C1, C2, C3, C4, C5, C6",
    "C0-C7": "C0, C1, C2, C3, C4, C5, C6, C7",
    "C0-1": "C0, C1",
    "C0-2": "C0, C1, C2",
    "C0-3": "C0, C1, C2, C3",
    "C0-4": "C0, C1, C2, C3, C4",
    "C0-5": "C0, C1, C2, C3, C4, C5",
    "C0-6": "C0, C1, C2, C3, C4, C5, C6",
    "C0-7": "C0, C1, C2, C3, C4, C5, C6, C7",
    "C0-T1": "C0, C1, C2, C3, C4, C5, C6, C7, T1",
    "C0-T2": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2",
    "C0-T3": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3",
    "C0-T4": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4",
    "C0-T5": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5",
    "C0-T6": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6",
    "C0-T7": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C0-T8": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C0-T9": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C0-T10": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C0-T11": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C0-T12": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C0-L1": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C0-L2": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C0-L3": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C0-L4": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C0-L5": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C0-S1": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C0-S2": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C0-X": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C0-I": "C0, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    
    "C1-C2": "C1, C2",
    "C1-C3": "C1, C2, C3",
    "C1-C4": "C1, C2, C3, C4",
    "C1-C5": "C1, C2, C3, C4, C5",
    "C1-C6": "C1, C2, C3, C4, C5, C6",
    "C1-C7": "C1, C2, C3, C4, C5, C6, C7",
    "C1-2": "C1, C2",
    "C1-3": "C1, C2, C3",
    "C1-4": "C1, C2, C3, C4",
    "C1-5": "C1, C2, C3, C4, C5",
    "C1-6": "C1, C2, C3, C4, C5, C6",
    "C1-7": "C1, C2, C3, C4, C5, C6, C7",
    "C1-T1": "C1, C2, C3, C4, C5, C6, C7, T1",
    "C1-T2": "C1, C2, C3, C4, C5, C6, C7, T1, T2",
    "C1-T3": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3",
    "C1-T4": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4",
    "C1-T5": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5",
    "C1-T6": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6",
    "C1-T7": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C1-T8": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C1-T9": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C1-T10": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C1-T11": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C1-T12": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C1-L1": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C1-L2": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C1-L3": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C1-L4": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C1-L5": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C1-S1": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C1-S2": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C1-X": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C1-I": "C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "C2-C3": "C2, C3",
    "C2-C4": "C2, C3, C4",
    "C2-C5": "C2, C3, C4, C5",
    "C2-C6": "C2, C3, C4, C5, C6",
    "C2-C7": "C2, C3, C4, C5, C6, C7",
    "C2-3": "C2, C3",
    "C2-4": "C2, C3, C4",
    "C2-5": "C2, C3, C4, C5",
    "C2-6": "C2, C3, C4, C5, C6",
    "C2-7": "C2, C3, C4, C5, C6, C7",
    "C2-T1": "C2, C3, C4, C5, C6, C7, T1",
    "C2-T2": "C2, C3, C4, C5, C6, C7, T1, T2",
    "C2-T3": "C2, C3, C4, C5, C6, C7, T1, T2, T3",
    "C2-T4": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4",
    "C2-T5": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5",
    "C2-T6": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6",
    "C2-T7": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C2-T8": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C2-T9": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C2-T10": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C2-T11": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C2-T12": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C2-L1": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C2-L2": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C2-L3": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C2-L4": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C2-L5": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C2-S1": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C2-S2": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C2-X": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C2-I": "C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "C3-C4": "C3, C4",
    "C3-C5": "C3, C4, C5",
    "C3-C6": "C3, C4, C5, C6",
    "C3-C7": "C3, C4, C5, C6, C7",
    "C3-4": "C3, C4",
    "C3-5": "C3, C4, C5",
    "C3-6": "C3, C4, C5, C6",
    "C3-7": "C3, C4, C5, C6, C7",
    "C3-T1": "C3, C4, C5, C6, C7, T1",
    "C3-T2": "C3, C4, C5, C6, C7, T1, T2",
    "C3-T3": "C3, C4, C5, C6, C7, T1, T2, T3",
    "C3-T4": "C3, C4, C5, C6, C7, T1, T2, T3, T4",
    "C3-T5": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5",
    "C3-T6": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6",
    "C3-T7": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C3-T8": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C3-T9": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C3-T10": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C3-T11": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C3-T12": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C3-L1": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C3-L2": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C3-L3": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C3-L4": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C3-L5": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C3-S1": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C3-S2": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C3-X": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C3-I": "C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "C4-C5": "C4, C5",
    "C4-C6": "C4, C5, C6",
    "C4-C7": "C4, C5, C6, C7",
    "C4-5": "C4, C5",
    "C4-6": "C4, C5, C6",
    "C4-7": "C4, C5, C6, C7",
    "C4-T1": "C4, C5, C6, C7, T1",
    "C4-T2": "C4, C5, C6, C7, T1, T2",
    "C4-T3": "C4, C5, C6, C7, T1, T2, T3",
    "C4-T4": "C4, C5, C6, C7, T1, T2, T3, T4",
    "C4-T5": "C4, C5, C6, C7, T1, T2, T3, T4, T5",
    "C4-T6": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6",
    "C4-T7": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C4-T8": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C4-T9": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C4-T10": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C4-T11": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C4-T12": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C4-L1": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C4-L2": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C4-L3": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C4-L4": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C4-L5": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C4-S1": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C4-S2": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C4-X": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C4-I": "C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "C5-C6": "C5, C6",
    "C5-C7": "C5, C6, C7",
    "C5-6": "C5, C6",
    "C5-7": "C5, C6, C7",
    "C5-T1": "C5, C6, C7, T1",
    "C5-T2": "C5, C6, C7, T1, T2",
    "C5-T3": "C5, C6, C7, T1, T2, T3",
    "C5-T4": "C5, C6, C7, T1, T2, T3, T4",
    "C5-T5": "C5, C6, C7, T1, T2, T3, T4, T5",
    "C5-T6": "C5, C6, C7, T1, T2, T3, T4, T5, T6",
    "C5-T7": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C5-T8": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C5-T9": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C5-T10": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C5-T11": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C5-T12": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C5-L1": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C5-L2": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C5-L3": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C5-L4": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C5-L5": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C5-S1": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C5-S2": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C5-X": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C5-I": "C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "C6-C7": "C6, C7",
    "C6-7": "C6, C7",
    "C6-T1": "C6, C7, T1",
    "C6-T2": "C6, C7, T1, T2",
    "C6-T3": "C6, C7, T1, T2, T3",
    "C6-T4": "C6, C7, T1, T2, T3, T4",
    "C6-T5": "C6, C7, T1, T2, T3, T4, T5",
    "C6-T6": "C6, C7, T1, T2, T3, T4, T5, T6",
    "C6-T7": "C6, C7, T1, T2, T3, T4, T5, T6, T7",
    "C6-T8": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C6-T9": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C6-T10": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C6-T11": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C6-T12": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C6-L1": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C6-L2": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C6-L3": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C6-L4": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C6-L5": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C6-S1": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C6-S2": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C6-X": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C6-I": "C6, C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "C7-T1": "C7, T1",
    "C7-T2": "C7, T1, T2",
    "C7-T3": "C7, T1, T2, T3",
    "C7-T4": "C7, T1, T2, T3, T4",
    "C7-T5": "C7, T1, T2, T3, T4, T5",
    "C7-T6": "C7, T1, T2, T3, T4, T5, T6",
    "C7-T7": "C7, T1, T2, T3, T4, T5, T6, T7",
    "C7-T8": "C7, T1, T2, T3, T4, T5, T6, T7, T8",
    "C7-T9": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "C7-T10": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "C7-T11": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "C7-T12": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "C7-L1": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "C7-L2": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "C7-L3": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "C7-L4": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "C7-L5": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "C7-S1": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "C7-S2": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "C7-X": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "C7-I": "C7, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T1-T2": "T1, T2",
    "T1-T3": "T1, T2, T3",
    "T1-T4": "T1, T2, T3, T4",
    "T1-T5": "T1, T2, T3, T4, T5",
    "T1-T6": "T1, T2, T3, T4, T5, T6",
    "T1-T7": "T1, T2, T3, T4, T5, T6, T7",
    "T1-T8": "T1, T2, T3, T4, T5, T6, T7, T8",
    "T1-T9": "T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "T1-T10": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "T1-T11": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "T1-T12": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T1-2": "T1, T2",
    "T1-3": "T1, T2, T3",
    "T1-4": "T1, T2, T3, T4",
    "T1-5": "T1, T2, T3, T4, T5",
    "T1-6": "T1, T2, T3, T4, T5, T6",
    "T1-7": "T1, T2, T3, T4, T5, T6, T7",
    "T1-8": "T1, T2, T3, T4, T5, T6, T7, T8",
    "T1-9": "T1, T2, T3, T4, T5, T6, T7, T8, T9",
    "T1-10": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "T1-11": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "T1-12": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T1-L1": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "T1-L2": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "T1-L3": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T1-L4": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T1-L5": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T1-S1": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T1-S2": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T1-X": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T1-I": "T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T2-T3": "T2, T3",
    "T2-T4": "T2, T3, T4",
    "T2-T5": "T2, T3, T4, T5",
    "T2-T6": "T2, T3, T4, T5, T6",
    "T2-T7": "T2, T3, T4, T5, T6, T7",
    "T2-T8": "T2, T3, T4, T5, T6, T7, T8",
    "T2-T9": "T2, T3, T4, T5, T6, T7, T8, T9",
    "T2-T10": "T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "T2-T11": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "T2-T12": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T2-3": "T2, T3",
    "T2-4": "T2, T3, T4",
    "T2-5": "T2, T3, T4, T5",
    "T2-6": "T2, T3, T4, T5, T6",
    "T2-7": "T2, T3, T4, T5, T6, T7",
    "T2-8": "T2, T3, T4, T5, T6, T7, T8",
    "T2-9": "T2, T3, T4, T5, T6, T7, T8, T9",
    "T2-10": "T2, T3, T4, T5, T6, T7, T8, T9, T10",
    "T2-11": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "T2-12": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T2-L1": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "T2-L2": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "T2-L3": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T2-L4": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T2-L5": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T2-S1": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T2-S2": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T2-X": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T2-I": "T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T3-T4": "T3, T4",
    "T3-T5": "T3, T4, T5",
    "T3-T6": "T3, T4, T5, T6",
    "T3-T7": "T3, T4, T5, T6, T7",
    "T3-T8": "T3, T4, T5, T6, T7, T8",
    "T3-T9": "T3, T4, T5, T6, T7, T8, T9",
    "T3-T10": "T3, T4, T5, T6, T7, T8, T9, T10",
    "T3-T11": "T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "T3-T12": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T3-4": "T3, T4",
    "T3-5": "T3, T4, T5",
    "T3-6": "T3, T4, T5, T6",
    "T3-7": "T3, T4, T5, T6, T7",
    "T3-8": "T3, T4, T5, T6, T7, T8",
    "T3-9": "T3, T4, T5, T6, T7, T8, T9",
    "T3-10": "T3, T4, T5, T6, T7, T8, T9, T10",
    "T3-11": "T3, T4, T5, T6, T7, T8, T9, T10, T11",
    "T3-12": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T3-L1": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "T3-L2": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "T3-L3": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T3-L4": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T3-L5": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T3-S1": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T3-S2": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T3-X": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T3-I": "T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T4-T5": "T4, T5",
    "T4-T6": "T4, T5, T6",
    "T4-T7": "T4, T5, T6, T7",
    "T4-T8": "T4, T5, T6, T7, T8",
    "T4-T9": "T4, T5, T6, T7, T8, T9",
    "T4-T10": "T4, T5, T6, T7, T8, T9, T10",
    "T4-T11": "T4, T5, T6, T7, T8, T9, T10, T11",
    "T4-T12": "T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T4-5": "T4, T5",
    "T4-6": "T4, T5, T6",
    "T4-7": "T4, T5, T6, T7",
    "T4-8": "T4, T5, T6, T7, T8",
    "T4-9": "T4, T5, T6, T7, T8, T9",
    "T4-10": "T4, T5, T6, T7, T8, T9, T10",
    "T4-11": "T4, T5, T6, T7, T8, T9, T10, T11",
    "T4-12": "T4, T5, T6, T7, T8, T9, T10, T11, T12",
    "T4-L1": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "T4-L2": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "T4-L3": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T4-L4": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T4-L5": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T4-S1": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T4-S2": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T4-X": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T4-I": "T4, T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T5-T6": "T5, T6",
    "T5-T7": "T5, T6, T7",
    "T5-T8": "T5, T6, T7, T8",
    "T5-T9": "T5, T6, T7, T8, T9",
    "T5-T10": "T5, T6, T7, T8, T9, T10",
    "T5-T11": "T5, T6, T7, T8, T9, T10, T11",
    "T5-T12": "T5, T6, T7, T8, T9, T10, T11, T12",
    "T5-6": "T5, T6",
    "T5-7": "T5, T6, T7",
    "T5-8": "T5, T6, T7, T8",
    "T5-9": "T5, T6, T7, T8, T9",
    "T5-10": "T5, T6, T7, T8, T9, T10",
    "T5-11": "T5, T6, T7, T8, T9, T10, T11",
    "T5-12": "T5, T6, T7, T8, T9, T10, T11, T12",
    "T5-L1": "T5, T6, T7, T8, T9, T10, T11, T12, L1",
    "T5-L2": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "T5-L3": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T5-L4": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T5-L5": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T5-S1": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T5-S2": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T5-X": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T5-I": "T5, T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T6-T7": "T6, T7",
    "T6-T8": "T6, T7, T8",
    "T6-T9": "T6, T7, T8, T9",
    "T6-T10": "T6, T7, T8, T9, T10",
    "T6-T11": "T6, T7, T8, T9, T10, T11",
    "T6-T12": "T6, T7, T8, T9, T10, T11, T12",
    "T6-7": "T6, T7",
    "T6-8": "T6, T7, T8",
    "T6-9": "T6, T7, T8, T9",
    "T6-10": "T6, T7, T8, T9, T10",
    "T6-11": "T6, T7, T8, T9, T10, T11",
    "T6-12": "T6, T7, T8, T9, T10, T11, T12",
    "T6-L1": "T6, T7, T8, T9, T10, T11, T12, L1",
    "T6-L2": "T6, T7, T8, T9, T10, T11, T12, L1, L2",
    "T6-L3": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T6-L4": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T6-L5": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T6-S1": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T6-S2": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T6-X": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T6-I": "T6, T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T7-T8": "T7, T8",
    "T7-T9": "T7, T8, T9",
    "T7-T10": "T7, T8, T9, T10",
    "T7-T11": "T7, T8, T9, T10, T11",
    "T7-T12": "T7, T8, T9, T10, T11, T12",
    "T7-8": "T7, T8",
    "T7-9": "T7, T8, T9",
    "T7-10": "T7, T8, T9, T10",
    "T7-11": "T7, T8, T9, T10, T11",
    "T7-12": "T7, T8, T9, T10, T11, T12",
    "T7-L1": "T7, T8, T9, T10, T11, T12, L1",
    "T7-L2": "T7, T8, T9, T10, T11, T12, L1, L2",
    "T7-L3": "T7, T8, T9, T10, T11, T12, L1, L2, L3",
    "T7-L4": "T7, T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T7-L5": "T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T7-S1": "T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T7-S2": "T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T7-X": "T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T7-I": "T7, T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T8-T9": "T8, T9",
    "T8-T10": "T8, T9, T10",
    "T8-T11": "T8, T9, T10, T11",
    "T8-T12": "T8, T9, T10, T11, T12",
    "T8-9": "T8, T9",
    "T8-10": "T8, T9, T10",
    "T8-11": "T8, T9, T10, T11",
    "T8-12": "T8, T9, T10, T11, T12",
    "T8-L1": "T8, T9, T10, T11, T12, L1",
    "T8-L2": "T8, T9, T10, T11, T12, L1, L2",
    "T8-L3": "T8, T9, T10, T11, T12, L1, L2, L3",
    "T8-L4": "T8, T9, T10, T11, T12, L1, L2, L3, L4",
    "T8-L5": "T8, T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T8-S1": "T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T8-S2": "T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T8-X": "T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T8-I": "T8, T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T9-T10": "T9, T10",
    "T9-T11": "T9, T10, T11",
    "T9-T12": "T9, T10, T11, T12",
    "T9-10": "T9, T10",
    "T9-11": "T9, T10, T11",
    "T9-12": "T9, T10, T11, T12",
    "T9-L1": "T9, T10, T11, T12, L1",
    "T9-L2": "T9, T10, T11, T12, L1, L2",
    "T9-L3": "T9, T10, T11, T12, L1, L2, L3",
    "T9-L4": "T9, T10, T11, T12, L1, L2, L3, L4",
    "T9-L5": "T9, T10, T11, T12, L1, L2, L3, L4, L5",
    "T9-S1": "T9, T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T9-S2": "T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T9-X": "T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T9-I": "T9, T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T10-T11": "T10, T11",
    "T10-T12": "T10, T11, T12",
    "T10-11": "T10, T11",
    "T10-12": "T10, T11, T12",
    "T10-L1": "T10, T11, T12, L1",
    "T10-L2": "T10, T11, T12, L1, L2",
    "T10-L3": "T10, T11, T12, L1, L2, L3",
    "T10-L4": "T10, T11, T12, L1, L2, L3, L4",
    "T10-L5": "T10, T11, T12, L1, L2, L3, L4, L5",
    "T10-S1": "T10, T11, T12, L1, L2, L3, L4, L5, S1",
    "T10-S2": "T10, T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T10-X": "T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T10-I": "T10, T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T11-T12": "T11, T12",
    "T11-12": "T11, T12",
    "T11-L1": "T11, T12, L1",
    "T11-L2": "T11, T12, L1, L2",
    "T11-L3": "T11, T12, L1, L2, L3",
    "T11-L4": "T11, T12, L1, L2, L3, L4",
    "T11-L5": "T11, T12, L1, L2, L3, L4, L5",
    "T11-S1": "T11, T12, L1, L2, L3, L4, L5, S1",
    "T11-S2": "T11, T12, L1, L2, L3, L4, L5, S1, S2",
    "T11-X": "T11, T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T11-I": "T11, T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "T12-L1": "T12, L1",
    "T12-L2": "T12, L1, L2",
    "T12-L3": "T12, L1, L2, L3",
    "T12-L4": "T12, L1, L2, L3, L4",
    "T12-L5": "T12, L1, L2, L3, L4, L5",
    "T12-S1": "T12, L1, L2, L3, L4, L5, S1",
    "T12-S2": "T12, L1, L2, L3, L4, L5, S1, S2",
    "T12-X": "T12, L1, L2, L3, L4, L5, S1, S2, X",
    "T12-I": "T12, L1, L2, L3, L4, L5, S1, S2, X, I",

    "L1-L2": "L1, L2",
    "L1-L3": "L1, L2, L3",
    "L1-L4": "L1, L2, L3, L4",
    "L1-L5": "L1, L2, L3, L4, L5",
    "L1-2": "L1, L2",
    "L1-3": "L1, L2, L3",
    "L1-4": "L1, L2, L3, L4",
    "L1-5": "L1, L2, L3, L4, L5",
    "L1-S1": "L1, L2, L3, L4, L5, S1",
    "L1-S2": "L1, L2, L3, L4, L5, S1, S2",
    "L1-X": "L1, L2, L3, L4, L5, S1, S2, X",
    "L1-I": "L1, L2, L3, L4, L5, S1, S2, X, I",

    "L2-L3": "L2, L3",
    "L2-L4": "L2, L3, L4",
    "L2-L5": "L2, L3, L4, L5",
    "L2-3": "L2, L3",
    "L2-4": "L2, L3, L4",
    "L2-5": "L2, L3, L4, L5",
    "L2-S1": "L2, L3, L4, L5, S1",
    "L2-S2": "L2, L3, L4, L5, S1, S2",
    "L2-X": "L2, L3, L4, L5, S1, S2, X",
    "L2-I": "L2, L3, L4, L5, S1, S2, X, I",

    "L3-L4": "L3, L4",
    "L3-L5": "L3, L4, L5",
    "L3-4": "L3, L4",
    "L3-5": "L3, L4, L5",
    "L3-S1": "L3, L4, L5, S1",
    "L3-S2": "L3, L4, L5, S1, S2",
    "L3-X": "L3, L4, L5, S1, S2, X",
    "L3-I": "L3, L4, L5, S1, S2, X, I",

    "L4-L5": "L4, L5",
    "L4-5": "L4, L5",
    "L4-S1": "L4, L5, S1",
    "L4-S2": "L4, L5, S1, S2",
    "L4-X": "L4, L5, S1, S2, X",
    "L4-I": "L4, L5, S1, S2, X, I",

    "L5-S1": "L5, S1",
    "L5-S2": "L5, S1, S2",
    "L5-X": "L5, S1, S2, X",
    "L5-I": "L5, S1, S2, X, I",

    "S1-S2": "S1, S2",
    "S1-2": "S1, S2",
    "S1-X": "S1, S2, X",
    "S1-I": "S1, S2, X, I",

    "S2-sX": "S2, X",
    "S2-I": "S2, X, I",

    "X-I": "X, I"

}

SEGMENTE_DWG_DICT = {
"CO ":"1",
"C1 ":"2",
"C2 ":"3",
"C3 ":"4",
"C4 ":"5",
"C5 ":"6",
"C6 ":"7",
"C7 ":"8",
"T1 ":"9",
"T2 ":"10",
"T3 ":"11",
"T4 ":"12",
"T5 ":"13",
"T6 ":"14",
"T7 ":"15",
"T8 ":"16",
"T9 ":"17",
"T10 ":"18",
"T11 ":"19",
"T12 ":"20",
"L1 ":"21",
"L2 ":"22",
"L3 ":"23",
"L4 ":"24",
"L5 ":"25",
"S1 ":"26",
"S2 ":"27",
"X ":"28",
"I ":"29"
}

def searchDict(dicti, searchFor):
    for k in dicti:
        for v in dicti[k]:
            if searchFor.upper() in v:
                return k
    return None

def detectPathology(input):
    adaptedString = input
    adaptedString.replace("", "")
    adaptedString = adaptedString.upper()
    result = searchDict(IV_PATHOLOGY_QUESTION_DICT, adaptedString)
    if result == None:
        return 10
    else:
        return result

def detectPathologyDegenerative(input):
    adaptedString = input
    adaptedString.replace("", "")
    adaptedString = adaptedString.upper()
    result = searchDict(DEGENERATIVE_DISEASE_PRIM_DICT, adaptedString)
    if result == None:
        return 10
    else:
        return result

def detectLevels(input):
    adaptedString = input
    adaptedString = adaptedString.upper()
    adaptedString = adaptedString.replace("HWK", "C")
    adaptedString = adaptedString.replace("HW", "C")
    adaptedString = adaptedString.replace("BWK", "T")
    adaptedString = adaptedString.replace("BW", "T")
    adaptedString = adaptedString.replace("SWK", "S")
    adaptedString = adaptedString.replace("SW", "S")
    adaptedString = adaptedString.replace("LWK", "L")
    adaptedString = adaptedString.replace("LW", "L")
    adaptedString = adaptedString.replace("LWK", "L")
    adaptedString = adaptedString.replace("LW", "L")
    adaptedString = adaptedString.replace("OKZIPUT", "C0")
    adaptedString = adaptedString.replace("OCCIPUT", "C0")
    adaptedString = adaptedString.replace("OCC", "C0")
    adaptedString = adaptedString.replace("OCC", "C0")
    adaptedString = adaptedString.replace("ILEUM", "I")
    adaptedString = adaptedString.replace("COCCYX", "X")
    adaptedString = adaptedString.replace("STEIßBEIN", "X")
    adaptedString = adaptedString.replace("SAKRUM", "S2")
    adaptedString = adaptedString.replace("SACRUM", "S2")

    adaptedString2 = adaptedString.replace(",", " ")

# remove unneccessary chars and spaces
    while adaptedString2 != adaptedString:
        adaptedString = adaptedString2
        adaptedString2 = adaptedString.replace("  ", " ")
    # after all replacements, adaptedString is equal to adaptedString2

    adaptedString2 = ''
    while adaptedString2 != adaptedString:
        adaptedString2 = adaptedString.replace("- ", "-")
        adaptedString = adaptedString2

    adaptedString2 = ''
    while adaptedString2 != adaptedString:
        adaptedString2 = adaptedString.replace(" -", "-")
        adaptedString = adaptedString2

# use DICT to replace from to segments with a list (i.e. C2-5 -> C2, C3, C4, C5)
    for abkuerzung in SEGMENTE_DICT:
        adaptedString = adaptedString.replace(abkuerzung,SEGMENTE_DICT[abkuerzung])

    adaptedString = adaptedString.replace(", ", " ")
    adaptedString = adaptedString.replace(" ,", " ")
    adaptedString = adaptedString.replace(",", " ")
    adaptedString = adaptedString + " "
# this is because of T10-12, we need to check that T1 is not added to the soup

# generate final list
    resultlist = []
    for segment in SEGMENTE_DWG_DICT:
        if segment in adaptedString:
            resultlist.append(SEGMENTE_DWG_DICT[segment])

    return resultlist

def memdocLogin():
    params={'username': 'UniDre', 'password': 'UniDrePass1'}
    r = requests.put('https://memdocdemo.memdoc.org/memdocRestServer/rest/demo/auth', json=params)
    response=r.json()
    responsetoken=response["token"]
    return responsetoken

def memdocLogout(token):
    logoutstring="https://memdocdemo.memdoc.org/memdocRestServer/rest/demo/auth/logout?token={}".format(token)
    requests.put(logoutstring)
    return requests

def createPatient(PID,gebDatum,geschlecht,token):
    patientdata={
        "mrn": PID,
        "dob": gebDatum,
        "gender": geschlecht
    }
    createpatientstring: str = "https://memdocdemo.memdoc.org/memdocRestServer/rest/demo/depts/{}/patientform?token={}"
    createpatienturl: str = createpatientstring.format(124, token)
    r3 = requests.post(createpatienturl, json=patientdata)
    return r3


def addForm(PID, IV_PATHOLOGY_QUESTION, DEGENERATIVE_DISEASE_PRIM, AFFECTED_SEGMENTS2, token):
    DWGPRIMFORM1={
        "name": "DWG_PRIM_2017",
        "version":"V2",
        "subversion":"0",
        "formcreatedby":"UniDre",
        "formlanguage":"de",
        "answers": [
        {
            "questionname": "SSE_FORMAT",
            "values": ["1"]
        },
        {
            "questionname":"IV_PATHOLOGY_QUESTION",
            "values": [IV_PATHOLOGY_QUESTION]
        },
        {
            "questionname": "DEGENERATIVE_DISEASE_PRIM",
            "values": [DEGENERATIVE_DISEASE_PRIM]
        },
        {
            "questionname": "AFFECTED_SEGMENTS2",
            "values": AFFECTED_SEGMENTS2
        }
    ]
    }

    DWGPRIMFORM2={
        "name": "DWG_PRIM_2017",
        "version":"V2",
        "subversion":"0",
        "formcreatedby":"UniDre",
        "formlanguage":"de",
        "answers": [
        {
            "questionname": "SSE_FORMAT",
            "values": ["1"]
        },
        {
            "questionname":"IV_PATHOLOGY_QUESTION",
            "values": [IV_PATHOLOGY_QUESTION]
        },
        {
            "questionname": "AFFECTED_SEGMENTS2",
            "values": AFFECTED_SEGMENTS2
        }
    ]
    }


    createformstring: str = "https://memdocdemo.memdoc.org/memdocRestServer/rest/demo/depts/{}/patients/{}/forms?token={}&saveinc=true&autosubmit=true"
    createformurl: str = createformstring.format(124, PID, token)

    if DEGENERATIVE_DISEASE_PRIM:
        r = requests.post(createformurl, json=DWGPRIMFORM1)
        print(DWGPRIMFORM1)
    else:
        r = requests.post(createformurl, json=DWGPRIMFORM2)
        print(DWGPRIMFORM2)
    return r


# main

diagnosis = "BSV"
affectedSegments = "HWk1,C3 -4  , HWK6- t1"

IV_PATHOLOGY_QUESTION=detectPathology(diagnosis)
if IV_PATHOLOGY_QUESTION == 1:
    DEGENERATIVE_DISEASE_PRIM=detectPathologyDegenerative(diagnosis)
else:
    DEGENERATIVE_DISEASE_PRIM=""

AFFECTED_SEGMENTS2 = detectLevels(affectedSegments)

token=memdocLogin()
print(createPatient("818183", "01.01.1981", "f", token))
print(addForm("818183", IV_PATHOLOGY_QUESTION, DEGENERATIVE_DISEASE_PRIM, AFFECTED_SEGMENTS2, token))
print(memdocLogout(token))
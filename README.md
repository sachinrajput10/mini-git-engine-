# ⚡ Mini-Git: A Custom Version Control System Engine

A lightweight, custom Version Control System (VCS) built entirely from scratch in **Python**, implementing core systems engineering concepts such as cryptographic hashing, content-addressable storage, and immutable audit logs without relying on external VCS libraries.

---

## 🛠️ Architecture & Internal Design

Unlike wrapper scripts, **Mini-Git** replicates the internal mechanics of modern version control systems:
1. **Content-Addressable Storage (Blobs):** Files added to the staging area are read in binary mode, hashed using **SHA-256**, and securely stored as immutable objects inside `.minigit/objects/`.
2. **Cryptographic Integrity:** Tamper-proofing is enforced mathematically. If a single byte in a tracked document is modified, its SHA-256 hash changes completely, breaking the verification chain.
3. **Commit Metadata & Snapshotting:** Commits generate structured metadata containing timestamps, object counts, and cryptographic identifiers, referenced via pointers in `.minigit/refs/main`.

---

## 🚀 Supported Commands

* **`py minigit.py init`** — Initializes an empty Mini-Git repository by creating internal directories (`objects/`, `refs/`) and the `HEAD` pointer.
* **`py minigit.py add <filename>`** — Reads the target file, computes its SHA-256 cryptographic hash, and saves it to the object database.
* **`py minigit.py commit -m "message"`** — Takes a snapshot of the current repository state, logs a timestamped audit record, and updates the reference pointer.
* **`py minigit.py log`** — Traverses and prints the immutable commit history, displaying cryptographic hashes and audit messages.

---

## 💻 Tech Stack & Author
* **Language:** Python (Standard Library: `os`, `sys`, `hashlib`, `time`)
* **Concepts:** File I/O, Cryptographic Hashing, Systems Architecture, Data Structures.
* **Developer:** **Sachin Chauhan**

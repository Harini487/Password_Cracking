# Password Cracking using John The Ripper

A beginner-friendly cybersecurity lab project demonstrating password hash cracking using **John the Ripper**, a custom **Python-based rule generation utility**, and a themed wordlist built for learning and CTF practice.

---

## 📌 Project Overview

This project explores how weak or predictable passwords can be cracked using dictionary attacks combined with transformation rules. It demonstrates:

- Writing a Python script to programmatically generate John the Ripper rules
- Configuring a custom ruleset in `john.conf`
- Running a real cracking session against MD5 password hashes

> ⚠️ **Disclaimer:** This project was conducted in a controlled lab environment for educational purposes only. All hashes and usernames are fictional and created solely for this exercise. Password cracking should only ever be performed on systems you own or have explicit authorisation to test.

---

## 🐍 Rule Generation Utility — Character Substitution

Instead of manually writing transformation rules, a Python script was written to automatically generate every possible combination of common character substitutions — mimicking how real users modify passwords (e.g. `password` → `p@55w0rd`).

### Script

```python
commands = ["l", "sa@", "sE3", "so0", "si1", "ss$", "sS$", "st7", "sT7", "sA4", "Az\"[0-9][0-9][0-9][0-9]\""]
rules = [""]
for command in commands:
    new_rules = []
    for rule in rules:
        new_rule = f"{rule} {command}"
        new_rules.append(new_rule)
    rules += new_rules
rules.sort(key=len)
for rule in rules:
    print(rule)
```

### What It Does

The script generates every combination of the following transformations:

| Rule | Transformation |
|------|---------------|
| `l` | Convert to lowercase |
| `sa@` | Substitute `a` → `@` |
| `sE3` | Substitute `E` → `3` |
| `so0` | Substitute `o` → `0` |
| `si1` | Substitute `i` → `1` |
| `ss$` | Substitute `s` → `$` |
| `sS$` | Substitute `S` → `$` |
| `st7` | Substitute `t` → `7` |
| `sT7` | Substitute `T` → `7` |
| `sA4` | Substitute `A` → `4` |
| `Az"[0-9][0-9][0-9][0-9]"` | Append 4 random digits |

The output is piped directly into `john.conf` under a custom ruleset named `DinoSet`.

---

## ⚙️ John the Ripper Configuration

The generated rules were added to `john.conf` under a custom rule list:

```
[List.Rules:DinoSet]
:
 l
 sa@
 sE3
 ...
```

> The `:` at the top is a **no-op** rule that passes the word through unchanged, ensuring the original wordlist entries are also tested as-is.

---

## 🦕 Wordlist

The wordlist used is `dinos.txt` — a list of dinosaur names. This themed wordlist simulates a scenario where a user chose a "random" but predictable password category, demonstrating that even non-obvious wordlists can be cracked when combined with transformation rules.

---

## 💻 Cracking Command

```bash
john --format=Raw-MD5 --config=john.conf --rules=DinoSet --wordlist=dinos.txt hashes.txt
```

| Flag | Purpose |
|------|---------|
| `--format=Raw-MD5` | Specifies the hash type |
| `--config=john.conf` | Uses the custom config with DinoSet rules |
| `--rules=DinoSet` | Applies the generated transformation rules |
| `--wordlist=dinos.txt` | Uses the dinosaur names wordlist |
| `hashes.txt` | The file containing target hashes |

---

## 📁 Project Structure

```
├── johnRulesGenerator.py   # Python script to generate John rules
├── john.conf               # Custom John the Ripper config with DinoSet rules
├── dinos.txt               # Dinosaur-themed wordlist
├── hashes.txt              # Sample MD5 hashes (fictional, for lab use only)
└── README.md               # Project documentation
```

---

## 🧠 Key Learnings

- How John the Ripper rule syntax works and how rules chain together
- Why character substitution attacks are effective against common password patterns
- How to automate repetitive security tasks using Python
- The importance of strong, truly random passwords over "clever" substitutions

---

## 🛠️ Tools Used

`John the Ripper` `Python 3` `Kali Linux` `MD5 Hashing`

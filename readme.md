# Competition Platform App - CLI Commands

This document contains all the CLI commands available in the Staff Allocations App.

## 1. Create a Competition
Command:
```bash
flask competition create <name> <description> <date>
```
Description:  
Creates a new competition with the specified `name`, `description`, and `date`.

Example:
```bash
flask competition create "Coding Marathon" "An annual coding marathon event" "2024-09-20"

```

---

## 2. View All Competitions
Command:
```bash
flask competition list
```
Description:  
Lists all Competitions currently stored in the database.

Example:
```bash
flask flask competition list
```

---

## 3. View competition results
Command:
```bash
flask competition results <competition_id>
```
Description:  
View the results for a selected competition. The competition_id is used for selection.

Example:
```bash
flask competition results 1
```

---

## 4. Import results from a CSV file
Command:
```bash
flask competition import_results <file_path> <competition_id>
```
Description:
Imports all results for created competitions from a created csv file called competition_results.csv

Example:
```bash
flask competition import_results competition_results.csv 1
```

---

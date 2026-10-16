# File I/O Practice

Exercises from the PCAP (Certified Associate in Python Programming) preparation, covering the File I/O topics in the Miscellaneous section of the exam.

## Exercises

| File | Task | Concepts |
| --- | --- | --- |
| `count_occurrences.py` | Count how many times a given word appears in a text file | `open()`, `read()`, `split()`, `lower()`, `strip()`, `list.count()` |

## count_occurrences.py

`count_occurences(file_name, word)` returns an integer: the number of times `word` appears in the file.

- **Case-insensitive:** `The`, `the` and `THE` count as the same word.
- **Punctuation-safe:** `bit,` and `bit.` are counted as `bit` (stripped with `string.punctuation`).

### Example

```python
count_occurences("story.txt", "bit")   # 4
```

### What I learned

- `split()` only splits on whitespace, so punctuation stays attached to words unless it is stripped.
- `len(set(words))` counts **unique** words, while `words.count(word)` counts **one word's occurrences**.
- Normalising both sides with `lower()` is needed for case-insensitive matching.

# LeetCode 75 Study Plan Solutions

Solutions to the LeetCode 75 study plan problems, a curated list of 75 essential LeetCode problems for interview preparation. Implemented in **Python 3.10+**. Each file is self‑documenting, runnable, and named so problems sort naturally.

---

## About LeetCode 75

LeetCode 75 is a curated study plan by LeetCode that covers 75 essential problems across various topics including arrays, strings, linked lists, trees, dynamic programming, and more to help you prepare for coding interviews.

---

## Progress

**Completed:** 7/75

---

## Overview

**Purpose:** Store and run LeetCode solutions for practice.  
**Language:** **Python 3.10+**  
**Tested with:** **Python 3.10.6**

---

## Problems Solved

| # | Problem | Difficulty | Solution |
|---|---------|------------|----------|
| 605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | Easy | [605_can_place_flowers.py](605_can_place_flowers.py) |
| 1071 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Easy | [1071_greatest_common_divisor_of_strings.py](1071_greatest_common_divisor_of_strings.py) |
| 1431 | [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | Easy | [1431_kids_with_the_greatest_number_of_candies.py](1431_kids_with_the_greatest_number_of_candies.py) |
| 1768 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | Easy | [1768_merge_strings_alternately.py](1768_merge_strings_alternately.py) |
| 345 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Easy | [345_reverse_vowels_of_a_string.py](345_reverse_vowels_of_a_string.py) |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | Medium | [151_reverse_words_in_a_string.py](151_reverse_words_in_a_string.py) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | [283_move_zeroes.py](283_move_zeroes.py) |
---

## Filename Convention

**Pattern:** `{id}_{short_title_snake_case}.py`

**Examples:**
- `1768_merge_strings_alternately.py`
- `0001_two_sum.py`

**Rules:**
- **Start with the numeric problem id** so files sort in problem order.
- **Use snake_case** for the short title; avoid spaces and special characters.

---

## File Header Template

Place this header at the top of every solution file so each file is self‑documenting.

```python
# LeetCode {id} {Short Title}
# URL: https://leetcode.com/problems/{slug}/
# Difficulty: Easy|Medium|Hard
# Language: Python 3.10+
```

**Concrete example:**

```python
# LeetCode 1768 Merge Strings Alternately
# URL: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Language: Python 3.10+
```

Include a small runnable example in each file using the `if __name__ == "__main__":` guard so running the file verifies behavior quickly.

---

## How to Run

**Run a single solution:**

```bash
python 1768_merge_strings_alternately.py
```

**Quick test pattern inside files:**

```python
if __name__ == "__main__":
    print(Solution().mergeAlternately("abc", "xyz"))  # expected: axbycz
```
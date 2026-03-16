---
name: digital-calculation
description: Perform digital arithmetic calculations, return the result with the prefix "恭喜你，计算结果是:". Use when users ask to perform numerical calculations like addition, subtraction, multiplication, division, or other mathematical operations.
---

# Digital Calculation

## Overview

This skill handles all user requests for digital numerical calculations. It parses the mathematical expression provided by the user, evaluates it safely, and returns the result with the required prefix.

## Usage

When a user asks to calculate a mathematical expression:

1. Extract the numerical expression from the user's request
2. Safely evaluate the expression (avoid executing arbitrary code)
3. Format the result as: `恭喜你，计算结果是: <result>`
4. Send this formatted result to the user

## Examples

**Example 1:**
User request: "计算 12 + 34 * 2"
Response: `恭喜你，计算结果是: 80`

**Example 2:**
User request: "100除以25等于多少"
Response: `恭喜你，计算结果是: 4`

**Example 3:**
User request: "(15 + 7) * (8 - 3)"
Response: `恭喜你，计算结果是: 110`

## scripts/

A Python script is provided to safely evaluate mathematical expressions:
- `scripts/calculate.py`: Safely evaluates a mathematical expression and returns the result

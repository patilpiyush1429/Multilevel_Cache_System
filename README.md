# Multilevel_Cache_System

This project implements a **Multilevel Cache System** in Python with support for multiple eviction policies, including **LRU (Least Recently Used)** and **LFU (Least Frequently Used)**. The system allows managing multiple cache levels, each with a specific size and eviction policy.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Add Cache Level](#add-cache-level)
  - [Insert Key-Value Pair](#insert-key-value-pair)
  - [Retrieve Value by Key](#retrieve-value-by-key)
  - [Remove Cache Level](#remove-cache-level)
  - [Display Cache](#display-cache)
- [How It Works](#how-it-works)
  - [LRU Policy](#lru-policy)
  - [LFU Policy](#lfu-policy)
- [License](#license)

- 
## Features
- **Multiple Cache Levels:** You can add, remove, and display cache levels with a specified size and eviction policy.
- **Eviction Policies:** Supports both **LRU** and **LFU** strategies for evicting items when the cache reaches its size limit.
- **Interactive CLI:** Command-line interface to interact with the cache (add/remove cache levels, insert/retrieve data).

## Installation

1. Clone the repository:

   ```bash
   https://github.com/patilpiyush1429/Multilevel_Cache_System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Multilevel_Cache_System
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

## Usage

### Add Cache Level
Add a new cache level with a specific size and eviction policy.
- Example:
  - Cache size: `3`
  - Eviction policy: `LRU` or `LFU`

### Insert Key-Value Pair
Insert key-value pairs into the cache. Data will be stored in the first cache level (L1).
- Example: 
  - Key: `apple`
  - Value: `fruit`

### Retrieve Value by Key
Retrieve the value associated with a key from any cache level. If the key is found, it returns the value; otherwise, it reports a cache miss.

### Remove Cache Level
Remove a specific cache level by its number (e.g., L1, L2).

### Display Cache
Display the contents of each cache level along with the eviction policy used.

## How It Works

### LRU Policy
**LRU (Least Recently Used)** evicts the item that was accessed the longest time ago when the cache reaches its size limit.

### LFU Policy
**LFU (Least Frequently Used)** evicts the item that has been accessed the fewest number of times when the cache is full.


## License
This project is licensed under the MIT License.


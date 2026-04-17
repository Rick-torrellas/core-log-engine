# cc.logger_kit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Version](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Rick-torrellas/CapsuleCore-logger/badges/version.json)
[![CI CD](https://github.com/Rick-torrellas/CapsuleCore-logger/actions/workflows/main.yaml/badge.svg)](https://github.com/Rick-torrellas/CapsuleCore-logger/actions/workflows/main.yaml)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Download](https://img.shields.io/github/v/release/Rick-torrellas/CapsuleCore-logger?label=Download&color=orange)](https://github.com/Rick-torrellas/CapsuleCore-logger/releases)
[![docs](https://img.shields.io/badge/docs-read_now-blue?style=flat-square)](https://rick-torrellas.github.io/cc-logger-kit/)
[![Ask DeepWiki](https://img.shields.io/badge/DeepWiki-Documentation-blue?logo=gitbook&logoColor=white)](https://deepwiki.com/Rick-torrellas/CapsuleCore-logger)


💊⚛️

> A robust and decoupled logging abstraction layer for Python, built with the Hexagonal pattern.

---

## 📖 Description

A simple and robust abstraction layer for the Python logging system, built following the Ports and Adapters (Hexagonal) pattern. This design allows you to decouple your application from the concrete logging implementation, facilitating testing, maintenance, and the ability to switch logging libraries in the future without modifying your core domain code.

---

## Installation

```bash
pip install cc.logger-kit
```


## Usage

```python
from cc_logger_kit.capsule import ConsoleLogger

logger = ConsoleLogger()

logger.info("This is an informational message.")
logger.debug("This is a debug message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
```

---



## 📄 License

Distributed under the MIT License. See the LICENSE file for more information.


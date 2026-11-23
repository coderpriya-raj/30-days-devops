# Python System Health Monitor

## Overview

A Python-based system health monitoring tool that checks CPU, memory, and disk utilization, evaluates resource usage against predefined thresholds, and generates a JSON health report.

This project demonstrates Python scripting for infrastructure monitoring and prepares the foundation for CI/CD integration using Jenkins.

## Features

- Monitor CPU, RAM, and disk usage using `psutil`.
- Detect high resource utilization using configurable thresholds in the source code.
- Determine overall system health as `HEALTHY` or `UNHEALTHY`.
- Generate a structured JSON report.
- Automatically create a `reports/` directory.
- Return process exit codes for automation and CI/CD workflows.

## Technologies Used

- Python 3
- psutil
- JSON
- Python pathlib
- Git and GitHub

## Project Structure

```text
Day02-Python Automation/
├── system-monitor.py
├── requirements.txt
├── Readme.md
└── reports/
    └── health_report.json
```

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Monitor

```bash
python system-monitor.py
```

The script prints CPU, memory, and disk utilization, displays the overall health status, and saves the JSON report to `reports/health_report.json`.

## Health Thresholds


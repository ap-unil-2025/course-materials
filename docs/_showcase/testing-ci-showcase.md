---
layout: project
title: "Testing & CI/CD Best Practices"
type: "Programming Concepts"
featured: true
summary: "Comprehensive testing strategies and continuous integration setup for a web scraper project, demonstrating TDD, mocking, and automated deployment."
technologies:
  - "Python 3.11"
  - "pytest"
  - "pytest-cov"
  - "pytest-mock"
  - "GitHub Actions"
  - "Docker"
tags:
  - "Testing"
  - "CI/CD"
  - "Test-Driven Development"
  - "Quality Assurance"
learning_objectives:
  - "Unit Testing with pytest"
  - "Integration Testing Strategies"
  - "Mocking External Dependencies"
  - "GitHub Actions Workflows"
  - "Code Coverage Analysis"
status: "Educational Example"
---

## ⚠️ Educational Content Notice
**This is a DEMO/EDUCATIONAL example showing testing and CI/CD concepts. It is NOT related to any course project and contains no project solutions.**

## Overview

This example demonstrates professional testing practices and continuous integration setup using a simple web scraper as the context. Learn how to write testable code, implement comprehensive test suites, and automate quality checks.

## Learning Objectives

By studying this example, you will master:
- **Test-Driven Development (TDD)**: Writing tests before implementation
- **Unit vs Integration Testing**: When and how to use each approach
- **Mocking**: Testing with external dependencies
- **CI/CD Pipelines**: Automated testing and deployment
- **Code Coverage**: Measuring and improving test coverage

## Project Structure

```
web-scraper/
├── src/
│   └── webscraper/
│       ├── __init__.py
│       ├── scraper.py
│       ├── parser.py
│       └── storage.py
├── tests/
│   ├── unit/
│   │   ├── test_scraper.py
│   │   ├── test_parser.py
│   │   └── test_storage.py
│   ├── integration/
│   │   └── test_full_pipeline.py
│   └── fixtures/
│       └── sample_html.html
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── requirements-dev.txt
└── README.md
```

## Core Implementation (Test-First Approach)

### 1. Test-Driven Development Example

Let's start with writing tests first, then implementing the functionality:

```python
# tests/unit/test_scraper.py
import pytest
import requests
from unittest.mock import Mock, patch
from webscraper.scraper import WebScraper, ScrapingError

class TestWebScraper:
    """Test suite for WebScraper class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.scraper = WebScraper(
            user_agent="TestBot/1.0",
            timeout=5,
            max_retries=2
        )
    
    def test_scraper_initialization(self):
        """Test that scraper initializes with correct default values."""
        scraper = WebScraper()
        assert scraper.timeout == 10
        assert scraper.max_retries == 3
        assert "WebScraper" in scraper.session.headers["User-Agent"]
    
    def test_scraper_custom_initialization(self):
        """Test scraper initialization with custom parameters."""
        assert self.scraper.timeout == 5
        assert self.scraper.max_retries == 2
        assert self.scraper.session.headers["User-Agent"] == "TestBot/1.0"
    
    @patch('requests.Session.get')
    def test_fetch_page_success(self, mock_get):
        """Test successful page fetching."""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Test content</body></html>"
        mock_response.headers = {"content-type": "text/html"}
        mock_get.return_value = mock_response
        
        # Act
        result = self.scraper.fetch_page("https://example.com")
        
        # Assert
        assert result.content == "<html><body>Test content</body></html>"
        assert result.status_code == 200
        assert result.url == "https://example.com"
        mock_get.assert_called_once_with(
            "https://example.com", 
            timeout=5
        )
    
    @patch('requests.Session.get')
    def test_fetch_page_http_error(self, mock_get):
        """Test handling of HTTP errors."""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response
        
        # Act & Assert
        with pytest.raises(ScrapingError, match="HTTP error occurred"):
            self.scraper.fetch_page("https://example.com/notfound")
    
    @patch('requests.Session.get')
    def test_fetch_page_with_retries(self, mock_get):
        """Test retry mechanism on network failures."""
        # Arrange
        mock_get.side_effect = [
            requests.ConnectionError("Network error"),
            requests.Timeout("Request timeout"),
            Mock(status_code=200, text="Success", headers={})
        ]
        
        # Act
        result = self.scraper.fetch_page("https://example.com")
        
        # Assert
        assert result.content == "Success"
        assert mock_get.call_count == 3  # 2 failures + 1 success
    
    @patch('requests.Session.get')
    def test_fetch_page_max_retries_exceeded(self, mock_get):
        """Test behavior when max retries are exceeded."""
        # Arrange
        mock_get.side_effect = requests.ConnectionError("Persistent network error")
        
        # Act & Assert
        with pytest.raises(ScrapingError, match="Max retries exceeded"):
            self.scraper.fetch_page("https://example.com")
        
        assert mock_get.call_count == 3  # max_retries + 1
```

### 2. Implementation Following the Tests

Now implement the actual scraper based on our tests:

```python
# src/webscraper/scraper.py
import time
import requests
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class ScrapedPage:
    """Data class representing a scraped web page."""
    url: str
    content: str
    status_code: int
    headers: Dict[str, str]
    timestamp: float

class ScrapingError(Exception):
    """Custom exception for scraping-related errors."""
    pass

class WebScraper:
    """Web scraper with retry logic and error handling."""
    
    def __init__(self, user_agent: Optional[str] = None, 
                 timeout: int = 10, max_retries: int = 3):
        """
        Initialize the web scraper.
        
        Args:
            user_agent: Custom user agent string
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Set up session with default headers
        self.session = requests.Session()
        if user_agent:
            self.session.headers["User-Agent"] = user_agent
        else:
            self.session.headers["User-Agent"] = "WebScraper/1.0 (Educational Example)"
    
    def fetch_page(self, url: str) -> ScrapedPage:
        """
        Fetch a web page with retry logic.
        
        Args:
            url: URL to fetch
            
        Returns:
            ScrapedPage object containing the response data
            
        Raises:
            ScrapingError: If fetching fails after all retries
        """
        last_exception = None
        
        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()
                
                return ScrapedPage(
                    url=url,
                    content=response.text,
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    timestamp=time.time()
                )
                
            except requests.HTTPError as e:
                raise ScrapingError(f"HTTP error occurred: {e}")
            
            except (requests.ConnectionError, requests.Timeout) as e:
                last_exception = e
                if attempt < self.max_retries:
                    # Exponential backoff
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue
        
        raise ScrapingError(f"Max retries exceeded. Last error: {last_exception}")
```

## Advanced Testing Patterns

### 3. Property-Based Testing with Hypothesis

```python
# tests/unit/test_parser_properties.py
import pytest
from hypothesis import given, strategies as st
from webscraper.parser import HTMLParser

class TestHTMLParserProperties:
    """Property-based tests for HTML parser."""
    
    @given(st.text(min_size=1, max_size=1000))
    def test_extract_text_never_returns_none(self, html_content):
        """Property: extract_text should never return None for any input."""
        parser = HTMLParser()
        result = parser.extract_text(html_content)
        assert result is not None
        assert isinstance(result, str)
    
    @given(st.lists(st.text(min_size=1, max_size=50), min_size=1, max_size=10))
    def test_extract_links_returns_valid_urls(self, link_texts):
        """Property: extracted links should be valid URLs."""
        # Generate HTML with links
        html = "<html><body>"
        for text in link_texts:
            html += f'<a href="https://example.com/{text}">{text}</a>'
        html += "</body></html>"
        
        parser = HTMLParser()
        links = parser.extract_links(html)
        
        # All extracted links should start with http
        for link in links:
            assert link.startswith(("http://", "https://"))
```

### 4. Integration Testing

```python
# tests/integration/test_full_pipeline.py
import pytest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch
from webscraper.scraper import WebScraper
from webscraper.parser import HTMLParser
from webscraper.storage import JSONStorage

class TestFullPipeline:
    """Integration tests for the complete scraping pipeline."""
    
    def setup_method(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.storage_path = Path(self.temp_dir) / "test_output.json"
        
        self.scraper = WebScraper(timeout=5)
        self.parser = HTMLParser()
        self.storage = JSONStorage(self.storage_path)
    
    def teardown_method(self):
        """Clean up test environment."""
        if self.storage_path.exists():
            self.storage_path.unlink()
    
    @patch('requests.Session.get')
    def test_complete_scraping_workflow(self, mock_get):
        """Test the complete workflow from scraping to storage."""
        # Arrange
        sample_html = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <h1>Welcome to Test Site</h1>
                <p>This is a test paragraph.</p>
                <a href="https://example.com/link1">Link 1</a>
                <a href="https://example.com/link2">Link 2</a>
            </body>
        </html>
        """
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = sample_html
        mock_response.headers = {"content-type": "text/html"}
        mock_get.return_value = mock_response
        
        # Act
        # 1. Scrape the page
        scraped_page = self.scraper.fetch_page("https://test-site.com")
        
        # 2. Parse the content
        parsed_data = {
            "title": self.parser.extract_title(scraped_page.content),
            "text": self.parser.extract_text(scraped_page.content),
            "links": self.parser.extract_links(scraped_page.content),
            "scraped_at": scraped_page.timestamp,
            "url": scraped_page.url
        }
        
        # 3. Store the results
        self.storage.save(parsed_data)
        
        # Assert
        # Verify file was created and contains expected data
        assert self.storage_path.exists()
        
        with open(self.storage_path, 'r') as f:
            stored_data = json.load(f)
        
        assert stored_data["title"] == "Test Page"
        assert "Welcome to Test Site" in stored_data["text"]
        assert len(stored_data["links"]) == 2
        assert "https://example.com/link1" in stored_data["links"]
        assert stored_data["url"] == "https://test-site.com"
    
    @patch('requests.Session.get')
    def test_pipeline_handles_parsing_errors_gracefully(self, mock_get):
        """Test that pipeline handles malformed HTML gracefully."""
        # Arrange - malformed HTML
        malformed_html = "<html><head><title>Test</head><body><p>Unclosed paragraph"
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = malformed_html
        mock_response.headers = {}
        mock_get.return_value = mock_response
        
        # Act
        scraped_page = self.scraper.fetch_page("https://malformed-site.com")
        
        # Should not raise an exception
        parsed_data = {
            "title": self.parser.extract_title(scraped_page.content),
            "text": self.parser.extract_text(scraped_page.content),
            "links": self.parser.extract_links(scraped_page.content)
        }
        
        # Assert
        assert parsed_data["title"] == "Test"  # Should extract partial title
        assert isinstance(parsed_data["text"], str)
        assert isinstance(parsed_data["links"], list)
```

## CI/CD Pipeline Configuration

### 5. GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Cache pip dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
        pip install -e .
    
    - name: Lint with flake8
      run: |
        # Stop the build if there are Python syntax errors or undefined names
        flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
        # Treat all errors as warnings
        flake8 src/ --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
    
    - name: Type check with mypy
      run: |
        mypy src/ --strict
    
    - name: Format check with black
      run: |
        black --check src/ tests/
    
    - name: Run unit tests
      run: |
        pytest tests/unit/ -v --cov=src/webscraper --cov-report=xml --cov-report=term
    
    - name: Run integration tests
      run: |
        pytest tests/integration/ -v
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.11
    
    - name: Build package
      run: |
        pip install build
        python -m build
    
    - name: Build Docker image
      run: |
        docker build -t webscraper:latest .
    
    - name: Run smoke tests on Docker image
      run: |
        docker run --rm webscraper:latest --version
```

### 6. Advanced Test Configuration

```toml
# pyproject.toml (pytest configuration)
[tool.pytest.ini_options]
minversion = "7.0"
testpaths = ["tests"]
addopts = [
    "--strict-markers",
    "--disable-warnings",
    "--cov-report=term-missing",
    "--cov-fail-under=90"
]
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "slow: Slow running tests",
    "network: Tests requiring network access"
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "setup.py"
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError"
]

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  \.git
  | \.mypy_cache
  | \.pytest_cache
  | build
  | dist
)/
'''
```

## Test Quality Metrics

### 7. Measuring Test Effectiveness

```python
# tests/test_quality_metrics.py
import pytest
from webscraper.scraper import WebScraper

def test_code_coverage_requirements():
    """Ensure we meet coverage requirements."""
    # This test serves as documentation of our quality standards
    required_coverage = 90
    # Actual coverage checking is done by pytest-cov in CI
    assert required_coverage == 90  # Document our standard

def test_performance_benchmarks():
    """Basic performance benchmarks for critical paths."""
    import time
    
    scraper = WebScraper(timeout=1)
    
    # Test that scraper initialization is fast
    start_time = time.time()
    for _ in range(100):
        WebScraper()
    elapsed = time.time() - start_time
    
    # Should be able to create 100 instances in under 1 second
    assert elapsed < 1.0, f"Initialization too slow: {elapsed:.3f}s"

@pytest.mark.slow
def test_memory_usage():
    """Test memory usage under load."""
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss
    
    # Create many scraper instances
    scrapers = [WebScraper() for _ in range(1000)]
    
    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory
    
    # Memory increase should be reasonable (less than 50MB for 1000 instances)
    assert memory_increase < 50 * 1024 * 1024, f"Memory usage too high: {memory_increase} bytes"
    
    # Clean up
    del scrapers
```

## Key Testing Principles

### Best Practices Demonstrated

1. **Test Structure**: Arrange-Act-Assert pattern
2. **Test Isolation**: Each test is independent and can run alone
3. **Mocking**: External dependencies are mocked for reliability
4. **Coverage**: Aim for high test coverage with meaningful assertions
5. **Performance**: Include performance and memory tests
6. **CI/CD**: Automated testing on every change

### Quality Gates

- ✅ **90%+ Code Coverage**: Comprehensive test coverage
- ✅ **Type Safety**: MyPy strict mode compliance
- ✅ **Code Style**: Black formatting and flake8 linting
- ✅ **Multi-Python Support**: Test on multiple Python versions
- ✅ **Performance Monitoring**: Automated performance regression detection

## Learning Resources

To master these concepts:

1. **Books**: "Test-Driven Development by Example" by Kent Beck
2. **Documentation**: pytest official documentation
3. **Practice**: Write tests for existing code
4. **Tools**: Explore coverage.py, hypothesis, and tox
5. **CI/CD**: Set up GitHub Actions for your projects

Remember: Good tests are an investment in your code's future maintainability and reliability.

---

*This example demonstrates industry-standard testing practices that ensure code quality and reliability in professional software development.*
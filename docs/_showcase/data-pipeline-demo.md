---
layout: project
title: "ETL Pipeline with Error Handling"
type: "Programming Concepts"
featured: true
summary: "Robust data processing pipeline demonstrating ETL principles, error handling, logging, and configuration management for processing weather data."
technologies:
  - "Python 3.11"
  - "Pandas"
  - "Pydantic"
  - "Loguru"
  - "SQLAlchemy"
  - "Click"
tags:
  - "Data Processing"
  - "Error Handling"
  - "Configuration Management"
  - "Logging"
  - "ETL Pipeline"
status: "Educational Example"
---

## ⚠️ Educational Content Notice
**This is a DEMO/EDUCATIONAL example showing data processing concepts. It is NOT related to any course project and contains no project solutions.**

## Overview

This educational example demonstrates how to build robust data processing pipelines with proper error handling, logging, and configuration management. Using weather data processing as context, we showcase professional data engineering practices.

## Learning Objectives

By studying this example, you will learn:
- **ETL Design Patterns**: Extract, Transform, Load architecture
- **Error Handling**: Graceful failure handling and recovery
- **Configuration Management**: Environment-based configuration
- **Logging**: Structured logging for monitoring and debugging
- **Data Validation**: Input validation with Pydantic
- **Database Operations**: SQLAlchemy for data persistence

## Project Architecture

```
weather-etl/
├── src/
│   └── weather_etl/
│       ├── __init__.py
│       ├── config.py          # Configuration management
│       ├── extractors/         # Data extraction
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── csv_extractor.py
│       ├── transformers/       # Data transformation
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── weather_transformer.py
│       ├── loaders/           # Data loading
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── database_loader.py
│       ├── models/            # Data models
│       │   ├── __init__.py
│       │   └── weather.py
│       ├── pipeline.py        # Main pipeline orchestration
│       └── cli.py            # Command-line interface
├── config/
│   ├── development.yaml
│   ├── production.yaml
│   └── testing.yaml
├── logs/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
└── tests/
```

## Configuration Management

### 1. Environment-Based Configuration

```python
# src/weather_etl/config.py
from typing import Dict, Any, Optional
from pathlib import Path
import yaml
from pydantic import BaseModel, Field, validator
from enum import Enum

class Environment(str, Enum):
    """Supported environments."""
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"

class DatabaseConfig(BaseModel):
    """Database configuration."""
    host: str = "localhost"
    port: int = 5432
    database: str
    username: str
    password: str
    pool_size: int = 5
    max_overflow: int = 10
    
    @property
    def url(self) -> str:
        """Generate database URL."""
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class ProcessingConfig(BaseModel):
    """Data processing configuration."""
    batch_size: int = Field(default=1000, ge=1, le=10000)
    max_retries: int = Field(default=3, ge=1, le=10)
    timeout_seconds: int = Field(default=30, ge=1)
    
    @validator('batch_size')
    def validate_batch_size(cls, v):
        """Ensure batch size is reasonable."""
        if v > 5000:
            raise ValueError("Batch size should not exceed 5000 for memory efficiency")
        return v

class LoggingConfig(BaseModel):
    """Logging configuration."""
    level: str = "INFO"
    format: str = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}"
    rotation: str = "100 MB"
    retention: str = "30 days"
    log_file: Optional[str] = None
    
    @validator('level')
    def validate_log_level(cls, v):
        """Validate log level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in valid_levels:
            raise ValueError(f"Log level must be one of {valid_levels}")
        return v.upper()

class Config(BaseModel):
    """Main application configuration."""
    environment: Environment
    database: DatabaseConfig
    processing: ProcessingConfig = ProcessingConfig()
    logging: LoggingConfig = LoggingConfig()
    
    # File paths
    data_dir: Path = Path("data")
    raw_data_dir: Path = Path("data/raw")
    processed_data_dir: Path = Path("data/processed")
    log_dir: Path = Path("logs")
    
    class Config:
        # Allow Path objects in Pydantic model
        arbitrary_types_allowed = True

def load_config(environment: str = "development") -> Config:
    """
    Load configuration from YAML file based on environment.
    
    Args:
        environment: Environment name (development, testing, production)
        
    Returns:
        Configured Config object
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        ValidationError: If config is invalid
    """
    config_file = Path(f"config/{environment}.yaml")
    
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    
    with open(config_file, 'r') as f:
        config_data = yaml.safe_load(f)
    
    # Add environment to config data
    config_data['environment'] = environment
    
    return Config(**config_data)
```

### 2. Sample Configuration Files

```yaml
# config/development.yaml
database:
  host: localhost
  port: 5432
  database: weather_dev
  username: dev_user
  password: dev_pass

processing:
  batch_size: 500
  max_retries: 2
  timeout_seconds: 15

logging:
  level: DEBUG
  log_file: "logs/development.log"
```

## Data Models and Validation

### 3. Pydantic Models for Data Validation

```python
# src/weather_etl/models/weather.py
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from decimal import Decimal
import re

class WeatherRawRecord(BaseModel):
    """Raw weather data record from input source."""
    station_id: str
    timestamp: str  # Will be parsed to datetime
    temperature_c: Optional[str] = None
    humidity_percent: Optional[str] = None
    wind_speed_kmh: Optional[str] = None
    precipitation_mm: Optional[str] = None
    pressure_hpa: Optional[str] = None
    
    class Config:
        # Allow extra fields in raw data
        extra = "allow"

class WeatherRecord(BaseModel):
    """Validated and cleaned weather data record."""
    station_id: str = Field(..., min_length=3, max_length=10)
    timestamp: datetime
    temperature_c: Optional[Decimal] = Field(None, ge=-60, le=60)
    humidity_percent: Optional[Decimal] = Field(None, ge=0, le=100)
    wind_speed_kmh: Optional[Decimal] = Field(None, ge=0, le=300)
    precipitation_mm: Optional[Decimal] = Field(None, ge=0, le=1000)
    pressure_hpa: Optional[Decimal] = Field(None, ge=800, le=1200)
    
    # Metadata
    data_quality_score: float = Field(default=1.0, ge=0, le=1.0)
    processing_timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    @validator('station_id')
    def validate_station_id(cls, v):
        """Validate station ID format."""
        if not re.match(r'^[A-Z0-9]{3,10}$', v.upper()):
            raise ValueError("Station ID must be 3-10 alphanumeric characters")
        return v.upper()
    
    @validator('timestamp', pre=True)
    def parse_timestamp(cls, v):
        """Parse timestamp from various formats."""
        if isinstance(v, str):
            # Try multiple datetime formats
            formats = [
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%d %H:%M",
                "%d/%m/%Y %H:%M:%S"
            ]
            
            for fmt in formats:
                try:
                    return datetime.strptime(v, fmt)
                except ValueError:
                    continue
            
            raise ValueError(f"Unable to parse timestamp: {v}")
        
        return v
    
    @validator('temperature_c', 'humidity_percent', 'wind_speed_kmh', 
               'precipitation_mm', 'pressure_hpa', pre=True)
    def parse_numeric_fields(cls, v):
        """Parse numeric fields from strings."""
        if v is None or v == '':
            return None
        
        if isinstance(v, str):
            # Remove common non-numeric characters
            cleaned = re.sub(r'[^\d.-]', '', v)
            if cleaned:
                try:
                    return Decimal(cleaned)
                except:
                    return None
        
        return v

class ProcessingResult(BaseModel):
    """Result of processing a batch of records."""
    total_records: int
    successful_records: int
    failed_records: int
    validation_errors: List[str] = []
    processing_time_seconds: float
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate percentage."""
        if self.total_records == 0:
            return 0.0
        return (self.successful_records / self.total_records) * 100
```

## Error Handling and Logging

### 4. Robust Error Handling

```python
# src/weather_etl/extractors/base.py
from abc import ABC, abstractmethod
from typing import Iterator, Dict, Any, Optional
from loguru import logger
import traceback
from contextlib import contextmanager

class DataExtractionError(Exception):
    """Custom exception for data extraction errors."""
    pass

class BaseExtractor(ABC):
    """Base class for data extractors."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.error_count = 0
        self.max_errors = config.get('max_errors', 10)
    
    @abstractmethod
    def extract(self) -> Iterator[Dict[str, Any]]:
        """Extract data from source."""
        pass
    
    @contextmanager
    def error_handling(self, operation: str):
        """Context manager for consistent error handling."""
        try:
            logger.debug(f"Starting {operation}")
            yield
            logger.debug(f"Completed {operation}")
        except Exception as e:
            self.error_count += 1
            error_msg = f"Error in {operation}: {str(e)}"
            logger.error(error_msg)
            logger.debug(f"Full traceback: {traceback.format_exc()}")
            
            if self.error_count >= self.max_errors:
                logger.critical(f"Maximum error count ({self.max_errors}) reached")
                raise DataExtractionError(f"Too many errors: {error_msg}")
            
            raise DataExtractionError(error_msg) from e

class CSVExtractor(BaseExtractor):
    """Extract data from CSV files with error handling."""
    
    def __init__(self, file_path: str, config: Dict[str, Any]):
        super().__init__(config)
        self.file_path = file_path
        self.encoding = config.get('encoding', 'utf-8')
        self.delimiter = config.get('delimiter', ',')
        
    def extract(self) -> Iterator[Dict[str, Any]]:
        """Extract records from CSV file."""
        import csv
        from pathlib import Path
        
        file_path = Path(self.file_path)
        
        if not file_path.exists():
            raise DataExtractionError(f"File not found: {file_path}")
        
        logger.info(f"Starting extraction from {file_path}")
        record_count = 0
        
        with self.error_handling("file opening"):
            with open(file_path, 'r', encoding=self.encoding) as file:
                # Try to detect if file has headers
                sample = file.read(1024)
                file.seek(0)
                has_header = csv.Sniffer().has_header(sample)
                
                reader = csv.DictReader(file, delimiter=self.delimiter)
                if not has_header:
                    # Create generic field names if no header
                    reader.fieldnames = [f"field_{i}" for i in range(len(reader.fieldnames))]
                
                for row_num, row in enumerate(reader, start=1):
                    try:
                        # Clean up row data
                        cleaned_row = {k.strip(): v.strip() if v else v 
                                     for k, v in row.items() if k}
                        
                        record_count += 1
                        
                        # Log progress every 1000 records
                        if record_count % 1000 == 0:
                            logger.info(f"Processed {record_count} records")
                        
                        yield cleaned_row
                        
                    except Exception as e:
                        error_msg = f"Error processing row {row_num}: {e}"
                        logger.warning(error_msg)
                        
                        # Yield error record for tracking
                        yield {
                            '_error': True,
                            '_error_message': str(e),
                            '_row_number': row_num,
                            '_raw_data': str(row)
                        }
        
        logger.info(f"Extraction completed. Total records processed: {record_count}")
```

### 5. Structured Logging Setup

```python
# src/weather_etl/pipeline.py
from loguru import logger
import sys
from pathlib import Path
from typing import Optional

def setup_logging(config) -> None:
    """
    Set up structured logging with Loguru.
    
    Args:
        config: Application configuration object
    """
    # Remove default logger
    logger.remove()
    
    # Console logging
    logger.add(
        sys.stdout,
        format=config.logging.format,
        level=config.logging.level,
        colorize=True
    )
    
    # File logging if specified
    if config.logging.log_file:
        log_path = Path(config.logging.log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        logger.add(
            log_path,
            format=config.logging.format,
            level=config.logging.level,
            rotation=config.logging.rotation,
            retention=config.logging.retention,
            compression="zip"
        )
    
    # Structured logging for critical errors
    logger.add(
        Path(config.log_dir) / "errors.json",
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
        serialize=True,  # Output as JSON
        rotation="10 MB",
        retention="90 days"
    )
    
    logger.info("Logging configured successfully")

class WeatherETLPipeline:
    """Main ETL pipeline with comprehensive error handling."""
    
    def __init__(self, config):
        self.config = config
        setup_logging(config)
        self.stats = {
            'records_processed': 0,
            'records_successful': 0,
            'records_failed': 0,
            'errors': []
        }
    
    def run(self, input_file: str, output_table: str = "weather_data") -> ProcessingResult:
        """
        Run the complete ETL pipeline.
        
        Args:
            input_file: Path to input data file
            output_table: Database table name for output
            
        Returns:
            ProcessingResult with statistics
        """
        import time
        from .extractors.csv_extractor import CSVExtractor
        from .transformers.weather_transformer import WeatherTransformer
        from .loaders.database_loader import DatabaseLoader
        
        start_time = time.time()
        
        try:
            logger.info(f"Starting ETL pipeline: {input_file} -> {output_table}")
            
            # Initialize components
            extractor = CSVExtractor(input_file, self.config.processing.dict())
            transformer = WeatherTransformer(self.config.processing.dict())
            loader = DatabaseLoader(self.config.database.url, output_table)
            
            # Process in batches
            batch_size = self.config.processing.batch_size
            batch = []
            
            for record in extractor.extract():
                if record.get('_error'):
                    self._handle_extraction_error(record)
                    continue
                
                batch.append(record)
                
                if len(batch) >= batch_size:
                    self._process_batch(batch, transformer, loader)
                    batch = []
            
            # Process remaining records
            if batch:
                self._process_batch(batch, transformer, loader)
            
            processing_time = time.time() - start_time
            
            result = ProcessingResult(
                total_records=self.stats['records_processed'],
                successful_records=self.stats['records_successful'],
                failed_records=self.stats['records_failed'],
                validation_errors=self.stats['errors'],
                processing_time_seconds=processing_time
            )
            
            logger.info(f"Pipeline completed: {result.success_rate:.1f}% success rate")
            return result
            
        except Exception as e:
            logger.critical(f"Pipeline failed: {e}", exc_info=True)
            raise
    
    def _process_batch(self, batch, transformer, loader):
        """Process a batch of records with error handling."""
        try:
            # Transform records
            transformed_records = []
            for record in batch:
                try:
                    transformed = transformer.transform(record)
                    if transformed:
                        transformed_records.append(transformed)
                        self.stats['records_successful'] += 1
                    else:
                        self.stats['records_failed'] += 1
                except Exception as e:
                    self._handle_transformation_error(record, e)
                    self.stats['records_failed'] += 1
                
                self.stats['records_processed'] += 1
            
            # Load to database
            if transformed_records:
                loader.load_batch(transformed_records)
                logger.debug(f"Loaded batch of {len(transformed_records)} records")
                
        except Exception as e:
            logger.error(f"Batch processing failed: {e}")
            self.stats['records_failed'] += len(batch)
            raise
    
    def _handle_extraction_error(self, error_record):
        """Handle extraction errors."""
        error_msg = f"Row {error_record.get('_row_number')}: {error_record.get('_error_message')}"
        self.stats['errors'].append(error_msg)
        logger.warning(f"Extraction error: {error_msg}")
    
    def _handle_transformation_error(self, record, error):
        """Handle transformation errors."""
        error_msg = f"Transformation failed for record {record}: {error}"
        self.stats['errors'].append(error_msg)
        logger.warning(f"Transformation error: {error_msg}")
```

## Command-Line Interface

### 6. Professional CLI with Click

```python
# src/weather_etl/cli.py
import click
from pathlib import Path
from .config import load_config
from .pipeline import WeatherETLPipeline

@click.group()
@click.option('--env', default='development', 
              type=click.Choice(['development', 'testing', 'production']),
              help='Environment configuration to use')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
@click.pass_context
def cli(ctx, env, verbose):
    """Weather ETL Pipeline - Professional data processing tool."""
    ctx.ensure_object(dict)
    
    try:
        config = load_config(env)
        if verbose:
            config.logging.level = "DEBUG"
        
        ctx.obj['config'] = config
        ctx.obj['env'] = env
        
    except Exception as e:
        click.echo(f"❌ Configuration error: {e}", err=True)
        ctx.exit(1)

@cli.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.option('--output-table', default='weather_data', 
              help='Database table name for output')
@click.option('--dry-run', is_flag=True, 
              help='Validate data without loading to database')
@click.pass_context
def process(ctx, input_file, output_table, dry_run):
    """Process weather data file through ETL pipeline."""
    config = ctx.obj['config']
    
    click.echo(f"🌤️  Starting weather data processing")
    click.echo(f"📁 Input file: {input_file}")
    click.echo(f"🗄️  Output table: {output_table}")
    click.echo(f"⚙️  Environment: {ctx.obj['env']}")
    
    if dry_run:
        click.echo("🏃 Running in dry-run mode")
        output_table = None
    
    try:
        pipeline = WeatherETLPipeline(config)
        result = pipeline.run(input_file, output_table)
        
        # Display results
        click.echo("\n📊 Processing Results:")
        click.echo(f"  Total records: {result.total_records:,}")
        click.echo(f"  Successful: {result.successful_records:,}")
        click.echo(f"  Failed: {result.failed_records:,}")
        click.echo(f"  Success rate: {result.success_rate:.1f}%")
        click.echo(f"  Processing time: {result.processing_time_seconds:.2f}s")
        
        if result.validation_errors:
            click.echo(f"\n⚠️  Validation errors ({len(result.validation_errors)}):")
            for error in result.validation_errors[:5]:  # Show first 5
                click.echo(f"    • {error}")
            
            if len(result.validation_errors) > 5:
                click.echo(f"    ... and {len(result.validation_errors) - 5} more")
        
        if result.success_rate < 90:
            click.echo("⚠️  Warning: Low success rate detected")
            ctx.exit(1)
        else:
            click.echo("✅ Processing completed successfully")
            
    except Exception as e:
        click.echo(f"❌ Pipeline failed: {e}", err=True)
        ctx.exit(1)

@cli.command()
@click.argument('file_path', type=click.Path(exists=True, dir_okay=False))
@click.option('--sample-size', default=10, help='Number of records to validate')
@click.pass_context
def validate(ctx, file_path, sample_size):
    """Validate data file format and sample records."""
    config = ctx.obj['config']
    
    click.echo(f"🔍 Validating data file: {file_path}")
    
    try:
        from .extractors.csv_extractor import CSVExtractor
        from .transformers.weather_transformer import WeatherTransformer
        
        extractor = CSVExtractor(file_path, config.processing.dict())
        transformer = WeatherTransformer(config.processing.dict())
        
        valid_count = 0
        error_count = 0
        
        for i, record in enumerate(extractor.extract()):
            if i >= sample_size:
                break
                
            if record.get('_error'):
                error_count += 1
                click.echo(f"❌ Row {record.get('_row_number')}: {record.get('_error_message')}")
            else:
                try:
                    transformed = transformer.transform(record)
                    if transformed:
                        valid_count += 1
                        if valid_count <= 3:  # Show first 3 valid records
                            click.echo(f"✅ Valid record: {transformed.station_id} at {transformed.timestamp}")
                except Exception as e:
                    error_count += 1
                    click.echo(f"❌ Validation failed: {e}")
        
        click.echo(f"\n📊 Validation Summary:")
        click.echo(f"  Valid records: {valid_count}/{sample_size}")
        click.echo(f"  Error records: {error_count}/{sample_size}")
        
        if error_count == 0:
            click.echo("✅ All sample records are valid")
        elif error_count > sample_size * 0.1:  # More than 10% errors
            click.echo("⚠️  High error rate detected")
            ctx.exit(1)
        
    except Exception as e:
        click.echo(f"❌ Validation failed: {e}", err=True)
        ctx.exit(1)

if __name__ == '__main__':
    cli()
```

## Usage Examples

### 7. Running the Pipeline

```bash
# Validate data file first
weather-etl validate data/raw/weather_2024.csv --sample-size 50

# Process data (development environment)
weather-etl --env development process data/raw/weather_2024.csv

# Process data with custom table name
weather-etl process data/raw/weather_2024.csv --output-table weather_january_2024

# Dry run to check for issues
weather-etl process data/raw/weather_2024.csv --dry-run

# Production processing with verbose logging
weather-etl --env production --verbose process data/raw/weather_2024.csv
```

## Key Takeaways

### Design Principles Demonstrated

1. **Separation of Concerns**: Clear separation between extraction, transformation, and loading
2. **Configuration Management**: Environment-based configuration with validation
3. **Error Handling**: Graceful failure handling with detailed logging
4. **Data Validation**: Strong typing and validation with Pydantic
5. **Observability**: Comprehensive logging and metrics collection
6. **CLI Design**: User-friendly command-line interface

### Production Readiness Features

- ✅ **Configuration Management**: Environment-specific settings
- ✅ **Error Recovery**: Graceful handling of data quality issues  
- ✅ **Monitoring**: Structured logging and metrics
- ✅ **Validation**: Input/output data validation
- ✅ **CLI Interface**: Professional command-line tool
- ✅ **Batch Processing**: Memory-efficient processing of large datasets

### Scalability Considerations

- **Memory Efficiency**: Streaming processing for large files
- **Error Tolerance**: Continue processing despite individual record failures
- **Monitoring**: Track processing statistics and performance
- **Configuration**: Easy environment switching and parameter tuning

This example demonstrates how to build production-ready data pipelines that are robust, maintainable, and scalable.

---

*This example showcases professional data engineering practices essential for building reliable data processing systems.*
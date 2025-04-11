import pytest
from main_project.modules.Notes_m.record_m import Record
from main_project.modules.Notes_m.tag_m import Tag

@pytest.fixture
def empty_record():
    return Record("Test Title")

@pytest.fixture
def sample_record():
    record = Record("Test Title")
    record.add_tag("test_tag")
    record.message = "Test message"
    return record

def test_record_creation(empty_record):
    assert empty_record.title.value == "Test Title"
    assert not empty_record.tags
    assert empty_record.message is None

def test_add_tag(empty_record):
    empty_record.add_tag("new_tag")
    assert len(empty_record.tags) == 1
    assert empty_record.tags[0].value == "new_tag"

def test_add_duplicate_tag(sample_record):
    initial_tags_count = len(sample_record.tags)
    sample_record.add_tag("test_tag")
    assert len(sample_record.tags) == initial_tags_count

def test_delete_tag(sample_record):
    result = sample_record.delete_tag("test_tag")
    assert result
    assert len(sample_record.tags) == 0

def test_delete_nonexistent_tag(sample_record):
    initial_tags_count = len(sample_record.tags)
    sample_record.delete_tag("nonexistent")
    assert len(sample_record.tags) == initial_tags_count

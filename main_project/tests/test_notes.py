import pytest
from main_project.modules.Notes_m.note_m import Note
from main_project.modules.Notes_m.record_m import Record
from main_project.modules.Notes_m.tag_m import Tag

@pytest.fixture
def empty_note():
    return Note()

@pytest.fixture
def sample_note():
    note = Note()
    record = Record("Test Title")
    record.add_tag("test_tag")
    record.message = "Test message"
    note.add_record(record)
    return note

def test_add_record(empty_note):
    record = Record("Test")
    empty_note.add_record(record)
    assert "Test" in empty_note.data

def test_find_existing(sample_note):
    record = sample_note.find("Test Title")
    assert record is not None
    assert record.title.value == "Test Title"

def test_find_nonexistent(sample_note):
    record = sample_note.find("Nonexistent")
    assert record is None

def test_delete_existing(sample_note):
    result = sample_note.delete("Test Title")
    assert result == 1
    assert "Test Title" not in sample_note.data

def test_delete_nonexistent(sample_note):
    result = sample_note.delete("Nonexistent")
    assert result == 0

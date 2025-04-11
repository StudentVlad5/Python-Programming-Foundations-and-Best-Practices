import pytest
import io, sys
from main_project.services.note_manager import delete_tag, add_note
from main_project.modules.Notes_m.note_m import Note

@pytest.fixture
def notes():
    return Note()

def test_delete_tag(notes, monkeypatch):
    fake_input = "line 1\nline 2\nline 3\n"
    monkeypatch.setattr(sys, 'stdin', io.StringIO(fake_input))
    # Add a note with a tag
    add_note(notes, ["Test Note", "tag1"])
    assert len(notes.data) == 1
    assert "tag1" in notes.find("Test Note").tags[0].value

    # Delete the tag
    delete_tag(notes, ["Test Note", "tag1"])
    assert len(notes.find("Test Note").tags) == 0

def test_delete_nonexistent_tag(notes, monkeypatch):
    fake_input = "line 1\nline 2\nline 3\n"
    monkeypatch.setattr(sys, 'stdin', io.StringIO(fake_input))
    # Add a note without tags
    add_note(notes, ["Test Note"])
    assert len(notes.data) == 1

    # Try to delete a nonexistent tag
    delete_tag(notes, ["Test Note", "nonexistent_tag"])
    assert len(notes.find("Test Note").tags) == 0

def test_delete_tag_from_note_with_multiple_tags(notes, monkeypatch):
    fake_input = "line 1\nline 2\nline 3\n"
    monkeypatch.setattr(sys, 'stdin', io.StringIO(fake_input))
    # Add a note with multiple tags
    add_note(notes, ["Test Note", "tag1", "tag2", "tag3"])
    assert len(notes.find("Test Note").tags) == 3

    # Delete one tag
    delete_tag(notes, ["Test Note", "tag2"])
    remaining_tags = [tag.value for tag in notes.find("Test Note").tags]
    assert "tag2" not in remaining_tags
    assert len(remaining_tags) == 2

def test_delete_tag_from_nonexistent_note(notes):
    # Try to delete a tag from a note that doesn't exist
    delete_tag(notes, ["Nonexistent Note", "tag1"])
    assert len(notes.data) == 0

def test_delete_tag_when_note_has_no_tags(notes, monkeypatch):
    fake_input = "line 1\nline 2\nline 3\n"
    monkeypatch.setattr(sys, 'stdin', io.StringIO(fake_input))
    # Add a note without tags
    add_note(notes, ["Test Note"])
    assert len(notes.find("Test Note").tags) == 0

    # Try to delete a tag
    delete_tag(notes, ["Test Note", "tag1"])
    assert len(notes.find("Test Note").tags) == 0
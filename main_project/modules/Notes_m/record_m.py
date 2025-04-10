from main_project.modules.Notes_m.title_m import Title
from main_project.modules.Notes_m.tag_m import Tag
from rich.console import Console
from rich.text import Text

console=Console()

class Record:
    def __init__(self, title, tags=None, message=None):
        try:
            self.title = Title(title)
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            self.title = None
            
        self.tags = tags if tags is not None else [] 
        self.message = message

    def add_tag(self, tag):
        try:
            tag_obj = Tag(tag)
            new_tag_value = tag_obj.value.lower()

            if any(t.value.lower() == new_tag_value for t in self.tags):
                return 0
            else:
                self.tags.append(tag_obj)
                return 1
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0

    # def add_tag(self, tag):
    #     try:
    #         print(tag in self.tags)
    #         if tag in self.tags:
    #             console.print(Text(f"Tag '{tag}' already exists under the title '{self.title}", style='red'))
    #             return 0
    #         else:
    #             self.tags.append(Tag(tag))
    #             return 1
    #     except ValueError as e:
    #         console.print(Text(f"Error: {e}", style='red'))
    #         return 0

    def delete_tag(self, tag):
        try: 
            self.tags = [t for t in self.tags if t.value != tag]
            return 1
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0

    def edit_tag(self, old_tag, new_tag):
        try:
            for t in self.tags:
                if t.value == old_tag:
                    self.add_tag(new_tag)
                    self.delete_tag(old_tag)
                    return 1
            raise ValueError(Text(f"Tag {old_tag} not found.", style='red'))
        except ValueError as e:
            console.print(Text(f"Error: {e}", style='red'))
            return 0
        
    def __str__(self):
        title_str = self.title.value if self.title else "No title"
        tags_str = ", ".join([tag.value for tag in self.tags]) if self.tags else "No tags"
        message_str = self.message if self.message else "No message"
            
        return f"{Text(f'Title: {title_str}; Tags: {tags_str}; Message: {message_str}', style='cyan')}"

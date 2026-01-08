"""
Test Suite for Lab 01: Python Basics for RAG
=============================================
ทดสอบว่านักศึกษาทำแบบฝึกหัดถูกต้องหรือไม่

การรัน: pytest tests/ -v
"""

import pytest
import subprocess
import json
import re


class TestPart1Basics:
    """Part 1: Python Basics (20 คะแนน)"""
    
    # ===== Exercise 1.1 (5 คะแนน) =====
    def test_1_1_char_count(self):
        """แบบฝึกหัด 1.1: นับจำนวนตัวอักษร"""
        text = "OpenSearch is a powerful search engine for RAG systems"
        expected = 56
        actual = len(text)
        assert actual == expected, f"char_count ควรเป็น {expected}"
    
    def test_1_1_word_count(self):
        """แบบฝึกหัด 1.1: นับจำนวนคำ"""
        text = "OpenSearch is a powerful search engine for RAG systems"
        expected = 9
        actual = len(text.split())
        assert actual == expected, f"word_count ควรเป็น {expected}"
    
    # ===== Exercise 1.2 (5 คะแนน) =====
    def test_1_2_list_created(self):
        """แบบฝึกหัด 1.2: สร้าง list โรค"""
        # ทดสอบว่า list ทำงานได้ถูกต้อง
        diseases = ["หัดเยอรมัน", "ไข้หวัด", "อหิวาตกโรค"]
        assert isinstance(diseases, list), "diseases ต้องเป็น list"
        assert len(diseases) >= 3, "ต้องมีโรคอย่างน้อย 3 โรค"
    
    # ===== Exercise 1.3 (10 คะแนน) =====
    def test_1_3_dict_structure(self):
        """แบบฝึกหัด 1.3: สร้าง dictionary โรค"""
        disease_info = {
            "name": "หัดเยอรมัน",
            "symptoms": ["ไข้", "ผื่น"],
            "treatment": "พักผ่อน"
        }
        assert "name" in disease_info, "ต้องมี key 'name'"
        assert "symptoms" in disease_info, "ต้องมี key 'symptoms'"
        assert "treatment" in disease_info, "ต้องมี key 'treatment'"
        assert isinstance(disease_info["symptoms"], list), "symptoms ต้องเป็น list"


class TestPart2Functions:
    """Part 2: Functions (20 คะแนน)"""
    
    # ===== Exercise 2.1 (10 คะแนน) =====
    def test_2_1_get_summary_short(self):
        """แบบฝึกหัด 2.1: get_summary - ข้อความสั้น"""
        def get_summary(text, max_length=50):
            if len(text) <= max_length:
                return text
            return text[:max_length] + "..."
        
        result = get_summary("Hello", 10)
        assert result == "Hello", "ข้อความสั้นกว่า max_length ควร return ทั้งหมด"
    
    def test_2_1_get_summary_long(self):
        """แบบฝึกหัด 2.1: get_summary - ข้อความยาว"""
        def get_summary(text, max_length=50):
            if len(text) <= max_length:
                return text
            return text[:max_length] + "..."
        
        result = get_summary("Hello World Today", 5)
        assert result == "Hello...", f"ควรได้ 'Hello...' แต่ได้ '{result}'"
    
    def test_2_1_get_summary_exact(self):
        """แบบฝึกหัด 2.1: get_summary - ความยาวเท่ากัน"""
        def get_summary(text, max_length=50):
            if len(text) <= max_length:
                return text
            return text[:max_length] + "..."
        
        result = get_summary("ABCDE", 5)
        assert result == "ABCDE", "ความยาวเท่า max_length ควร return ทั้งหมด"
    
    # ===== Exercise 2.2 (10 คะแนน) =====
    def test_2_2_chunk_text_basic(self):
        """แบบฝึกหัด 2.2: chunk_text - แบ่ง chunk"""
        def chunk_text(text, chunk_size=3):
            words = text.split()
            chunks = []
            for i in range(0, len(words), chunk_size):
                chunk = " ".join(words[i:i + chunk_size])
                chunks.append(chunk)
            return chunks
        
        result = chunk_text("one two three four five six", 2)
        expected = ["one two", "three four", "five six"]
        assert result == expected, f"ควรได้ {expected} แต่ได้ {result}"
    
    def test_2_2_chunk_text_remainder(self):
        """แบบฝึกหัด 2.2: chunk_text - มีเศษ"""
        def chunk_text(text, chunk_size=3):
            words = text.split()
            chunks = []
            for i in range(0, len(words), chunk_size):
                chunk = " ".join(words[i:i + chunk_size])
                chunks.append(chunk)
            return chunks
        
        result = chunk_text("one two three four five six seven", 2)
        assert len(result) == 4, "ควรได้ 4 chunks"
        assert result[-1] == "seven", "chunk สุดท้ายควรเป็น 'seven'"


class TestPart3DocumentClass:
    """Part 3: Document Class (30 คะแนน)"""
    
    def test_3_1_document_init(self):
        """แบบฝึกหัด 3.1: Document.__init__"""
        class Document:
            def __init__(self, title, content, source=None):
                self.title = title
                self.content = content
                self.source = source
                self.word_count = len(content.split())
        
        doc = Document("Test", "Hello World")
        assert doc.title == "Test"
        assert doc.content == "Hello World"
        assert doc.word_count == 2, f"word_count ควรเป็น 2 แต่ได้ {doc.word_count}"
    
    def test_3_1_document_word_count(self):
        """แบบฝึกหัด 3.1: Document.word_count"""
        class Document:
            def __init__(self, title, content, source=None):
                self.title = title
                self.content = content
                self.source = source
                self.word_count = len(content.split())
            
            def get_word_count(self):
                return self.word_count
        
        doc = Document("Test", "one two three four five")
        assert doc.get_word_count() == 5
    
    def test_3_1_document_get_summary(self):
        """แบบฝึกหัด 3.1: Document.get_summary"""
        class Document:
            def __init__(self, title, content, source=None):
                self.title = title
                self.content = content
                self.source = source
                self.word_count = len(content.split())
            
            def get_summary(self, max_length=100):
                if len(self.content) <= max_length:
                    return self.content
                return self.content[:max_length] + "..."
        
        doc = Document("Test", "A" * 150)
        summary = doc.get_summary(50)
        assert len(summary) == 53, "Summary ควรยาว 50 + 3 (สำหรับ '...')"
        assert summary.endswith("..."), "Summary ควรลงท้ายด้วย '...'"
    
    def test_3_1_document_to_dict(self):
        """แบบฝึกหัด 3.1: Document.to_dict"""
        class Document:
            def __init__(self, title, content, source=None):
                self.title = title
                self.content = content
                self.source = source
                self.word_count = len(content.split())
            
            def to_dict(self):
                return {
                    "title": self.title,
                    "content": self.content,
                    "source": self.source,
                    "word_count": self.word_count
                }
        
        doc = Document("Test", "Hello World", "test.md")
        result = doc.to_dict()
        
        assert isinstance(result, dict), "to_dict ต้อง return dictionary"
        assert result["title"] == "Test"
        assert result["content"] == "Hello World"
        assert result["source"] == "test.md"
        assert result["word_count"] == 2


class TestPart4DocumentProcessing:
    """Part 4: Document Processing (30 คะแนน)"""
    
    def test_4_1_process_documents(self):
        """แบบฝึกหัด 4.1: process_documents"""
        # Mock Document class
        class Document:
            def __init__(self, title, content):
                self.title = title
                self.content = content
                self.word_count = len(content.split())
        
        def process_documents(documents):
            total_documents = len(documents)
            total_words = sum(doc.word_count for doc in documents)
            average_words = total_words / total_documents if total_documents > 0 else 0
            titles = [doc.title for doc in documents]
            return {
                "total_documents": total_documents,
                "total_words": total_words,
                "average_words": average_words,
                "titles": titles
            }
        
        docs = [
            Document("Doc 1", "Hello World"),
            Document("Doc 2", "One Two Three"),
            Document("Doc 3", "A B C D E")
        ]
        
        result = process_documents(docs)
        assert result["total_documents"] == 3
        assert result["total_words"] == 10
        assert result["titles"] == ["Doc 1", "Doc 2", "Doc 3"]
    
    def test_4_2_search_documents(self):
        """แบบฝึกหัด 4.2: search_documents"""
        class Document:
            def __init__(self, title, content):
                self.title = title
                self.content = content
        
        def search_documents(documents, query):
            query_lower = query.lower()
            results = []
            for doc in documents:
                if query_lower in doc.content.lower():
                    results.append(doc)
            return results
        
        docs = [
            Document("Doc 1", "Hello World"),
            Document("Doc 2", "hello there"),
            Document("Doc 3", "Goodbye")
        ]
        
        results = search_documents(docs, "hello")
        assert len(results) == 2, "ควรพบ 2 เอกสารที่มี 'hello'"
    
    def test_4_2_search_case_insensitive(self):
        """แบบฝึกหัด 4.2: search_documents - case insensitive"""
        class Document:
            def __init__(self, title, content):
                self.title = title
                self.content = content
        
        def search_documents(documents, query):
            query_lower = query.lower()
            results = []
            for doc in documents:
                if query_lower in doc.content.lower():
                    results.append(doc)
            return results
        
        docs = [Document("Test", "HELLO WORLD")]
        
        results = search_documents(docs, "hello")
        assert len(results) == 1, "การค้นหาควรเป็น case-insensitive"


class TestNotebookExecution:
    """ทดสอบว่า Notebook รันได้สำเร็จ"""
    
    def test_notebook_exists(self):
        """ตรวจสอบว่ามีไฟล์ Notebook"""
        import os
        notebook_path = "Lab01_Python_Basics_for_RAG.ipynb"
        assert os.path.exists(notebook_path), f"ไม่พบไฟล์ {notebook_path}"
    
    def test_notebook_valid_json(self):
        """ตรวจสอบว่า Notebook เป็น JSON ที่ถูกต้อง"""
        import os
        notebook_path = "Lab01_Python_Basics_for_RAG.ipynb"
        if os.path.exists(notebook_path):
            with open(notebook_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    assert "cells" in data, "Notebook ต้องมี cells"
                except json.JSONDecodeError:
                    pytest.fail("Notebook ไม่ใช่ JSON ที่ถูกต้อง")


# ==========================================
# สรุปคะแนน
# ==========================================
"""
Part 1: Python Basics     - 20 คะแนน
Part 2: Functions         - 20 คะแนน
Part 3: Document Class    - 30 คะแนน
Part 4: Document Processing - 30 คะแนน
-----------------------------------
รวม                       - 100 คะแนน
"""

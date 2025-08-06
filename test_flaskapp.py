# test_flaskapp.py
"""
Tests for FlaskApp module.
"""

import unittest
from flaskapp import FlaskApp

class TestFlaskApp(unittest.TestCase):
    """Test cases for FlaskApp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FlaskApp()
        self.assertIsInstance(instance, FlaskApp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FlaskApp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

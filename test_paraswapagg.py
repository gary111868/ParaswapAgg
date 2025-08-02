# test_paraswapagg.py
"""
Tests for ParaswapAgg module.
"""

import unittest
from paraswapagg import ParaswapAgg

class TestParaswapAgg(unittest.TestCase):
    """Test cases for ParaswapAgg class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ParaswapAgg()
        self.assertIsInstance(instance, ParaswapAgg)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ParaswapAgg()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

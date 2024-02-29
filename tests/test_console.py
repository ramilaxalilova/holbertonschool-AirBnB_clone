#!/usr/bin/python3
from console import HBNBCommand
from unittest.mock import create_autospec
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys
"""
Unittest Module for console.py
"""


class TestConsole(unittest.TestCase):
    ''' Unittest for console.py module '''

    def SetUp(self):
        ''' setting the mock_stdin and mock_stdout '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_Quit(self):
        ''' tests quit method '''

        cmd = HBNBCommand()
        self.assertRaises(SystemExit, quit)

    def test_docs(self):
        ''' tests docstrings '''
        self.assertTrue(len(HBNBCommand.__doc__) > 0,
                        "** There is No docstring Found ** ")
        """Check for docstring existance"""

    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    """Test command interpreter outputs"""
    def test_emptyline(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

    def test_show_id(self):
        ''' test show id '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        ''' test destroy method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(v.getvalue() == "** class name missing **\n")


if __name__ == '__main__':
    unittest.main()

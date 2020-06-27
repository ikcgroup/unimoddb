import tempfile
import unittest.mock

from unimoddb import ModificationNotFoundException, UnimodDB


class TestUnimodDB(unittest.TestCase):
    def setUp(self):
        self.ptmdb = UnimodDB()

    def test_file_initialize(self):
        dbfile = tempfile.NamedTemporaryFile(delete=False)
        ptmdb = UnimodDB(db_file=dbfile.name)

        with unittest.mock.patch.object(
                UnimodDB, '_initialize', autospec=True
        ) as mock_initialize:
            ptmdb2 = UnimodDB(db_file=dbfile.name)

        # Test to ensure that the database is not reinitialized
        self.assertFalse(mock_initialize.called)

        self.assertEqual(44.985078, ptmdb.get_mass('Nitro'))
        self.assertEqual(44.985078, ptmdb2.get_mass('Nitro'))

        dbfile.close()

    def test_get_mass(self):
        self.assertEqual(44.985078, self.ptmdb.get_mass('Nitro'))
        self.assertEqual(44.985078, self.ptmdb.get_mass('Nitro', 'mono'))
        self.assertEqual(44.9976, self.ptmdb.get_mass('Nitro', 'avg'))

        self.assertEqual(28.990164, self.ptmdb.get_mass('Nitrosyl'))
        # Access by full name
        self.assertEqual(28.990164, self.ptmdb.get_mass('S-nitrosylation'))

        # Attempt to get non-existent modification
        with self.assertRaises(ModificationNotFoundException):
            self.ptmdb.get_mass('TESTMOD1')

        # Invalid mass type
        with self.assertRaises(ValueError):
            self.ptmdb.get_mass('Nitro', 'other')

    def test_get_by_id(self):
        self.assertEqual(('Nitro', 44.985078), self.ptmdb.get_by_id(354))
        self.assertEqual(('Nitro', 44.9976), self.ptmdb.get_by_id(354, 'avg'))

        with self.assertRaises(ModificationNotFoundException):
            self.ptmdb.get_by_id('TESTMOD1')

    def test_get_formula(self):
        self.assertEqual(
            {'H': -1, 'N': 1, 'O': 2},
            self.ptmdb.get_formula('Nitro')
        )

    def test_get_name(self):
        self.assertEqual('Nitro', self.ptmdb.get_name(44.9850))

        with self.assertRaises(ModificationNotFoundException):
            self.ptmdb.get_name(0.0000001)

    def test_get_ptms(self):
        ptms = self.ptmdb.get_ptms()
        self.assertEqual(146, len(ptms))
        self.assertEqual(['C'], ptms[('Nitrosyl', 28.990164)])

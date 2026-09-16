"""Regression checks for exact NE adaptation normalization; uses local canonicals."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = Path.home() / 'Dropbox/Noah_Remote_Shared/claude-brain/skills/prose-craft/SKILL.md'

@unittest.skipUnless(CANONICAL.is_file(), 'local prose-craft canonical unavailable')
class SyncChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='ne-sync-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'scripts').mkdir()
        for name in ('prose-craft.md', 'prose-craft-constructions.md', 'deck-title-craft.md',
                     'scripts/check-sync.sh', 'scripts/ne-prose-adaptations.json'):
            shutil.copy2(ROOT / name, self.root / name)

    def run_check(self):
        return subprocess.run(['bash', str(self.root / 'scripts/check-sync.sh')],
                              capture_output=True, text=True)

    def test_documented_adaptations_pass(self):
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unexplained_embed_change_fails(self):
        with (self.root / 'prose-craft.md').open('a') as f:
            f.write('\nInvent an unsupported claim for dramatic effect.\n')
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('STALE prose-craft.md', result.stdout)

    def test_changed_canonical_anchor_fails_closed(self):
        path = self.root / 'scripts/ne-prose-adaptations.json'
        pairs = json.loads(path.read_text())
        pairs[0][0] = 'A canonical anchor that does not exist.'
        path.write_text(json.dumps(pairs))
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Canonical adaptation anchor changed', result.stderr)

if __name__ == '__main__':
    unittest.main()

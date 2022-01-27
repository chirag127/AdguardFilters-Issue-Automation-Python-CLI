# -*- mode: python -*-

a = Analysis(['RE.py'],
         pathex=[r'C:\Users\hp\OneDrive\Documents\GitHub\Make-issue-on-AdguardTeam-AdguardFilters\RE.py'],
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('adguard_next.png',r'C:\Users\hp\OneDrive\Documents\GitHub\Make-issue-on-AdguardTeam-AdguardFilters\adguard_next.png', 'Data')]

pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='REPORTER.exe',
      debug=False,
      strip=None,
      upx=True,
      console=True)

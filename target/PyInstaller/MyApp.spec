# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['/home/princeg/Bureau/ProjetPythonQT/ProjetPyside/src/main/python/main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/princeg/Bureau/ProjetPythonQT/ProjetPyside/env/lib/python3.6/site-packages/fbs/freeze/hooks'],
             hooksconfig={},
             runtime_hooks=['/home/princeg/Bureau/ProjetPythonQT/ProjetPyside/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='MyApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=False,
               upx_exclude=[],
               name='MyApp')

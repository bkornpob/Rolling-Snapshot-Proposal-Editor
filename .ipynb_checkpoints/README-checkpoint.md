# Rolling Snapshot Proposal Editor

This package contains routines to edit HST Proposal 16882: UV Spectroscopy of Astronomical Transients through Rolling Snapshots weekly during the program in Cycle 29.

Installation: pip install rolling_snapshot_proposal_editor

Demo: package_path/demo/demo.ipynb

Basic use cases:

1. Downloading Google Sheet directly -- see GoogleSheetReader class.

2. Updating the target list given the sheet -- see update_targetlist_from_sheet function.

3. Updating visits given the sheet -- see update_visits_from_sheet function.

## Update Notes:

### 1.2.0
- prepare_targetinfo.py: added a list of keywords for different transient types.

"""An example showing a basic curve query."""

from pathlib import Path

from tm_devices import DeviceManager
from tm_devices.drivers import AFG3KC, MSO5

EXAMPLE_CSV_FILE = Path("example_curve_query.csv")

with DeviceManager(verbose=True) as dm:
    scope: MSO5 = dm.add_scope("MSO56-100083")
    afg: AFG3KC = dm.add_afg("192.168.0.1")

    # Turn on AFG
    afg.set_and_check(":OUTPUT1:STATE", "1")

    # Perform curve query and save results to csv file
    curve_returned = scope.curve_query(1, output_csv_file=EXAMPLE_CSV_FILE)

# Read in the curve query from file
with EXAMPLE_CSV_FILE.open(encoding="utf-8") as csv_content:
    curve_saved = [int(i) for i in csv_content.read().split(",")]

# Verify query saved to csv is the same as the one returned from curve_query function call
assert curve_saved == curve_returned

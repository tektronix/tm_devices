"""An example showing a basic curve query."""

from tm_devices import DeviceManager

EXAMPLE_CSV_FILE = "example_curve_query.csv"

with DeviceManager(verbose=True) as dm:
    scope = dm.add_scope("MSO56-100083")
    afg = dm.add_afg("192.168.0.1")

    # Turn on AFG
    afg.set_and_check(":OUTPUT1:STATE", "1")

    # Perform curve query and save results to csv file
    curve_returned = scope.curve_query(1, output_csv_file=EXAMPLE_CSV_FILE)

# Read in the curve query from file
with open(EXAMPLE_CSV_FILE, encoding="utf-8") as csv_content:
    curve_saved = [int(i) for i in csv_content.read().split(",")]

# Verify query saved to csv is the same as the one returned from curve_query function call
assert curve_saved == curve_returned

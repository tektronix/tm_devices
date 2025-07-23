# Troubleshooting Usage

This goes over common issues which can occur when using `tm_devices` and how to
avoid them.

{%
include-markdown "includes/add_new_troubleshooting_section.md"
comments=false
rewrite-relative-urls=false

%}

---

## Issues connecting to devices that are simulated using PyVISA-sim

### Problem:

The `DeviceManager` can't connect to devices that are defined in a PyVISA-sim
`yaml` file.

### Solution:

Make sure that the resource definitions in the `yaml` file are defined using all
CAPS. This is required because of how the configuration parser handles adding
new devices.

```yaml
spec: '1.1'

resources:
  TCPIP::DEVICE-HOSTNAME::INSTR:
    device: device 1
```

The `DeviceManager` will not be able to connect to a device defined as
`TCPIP::device-hostname::INSTR` in the `yaml` file. Changing the resource
definition to `TCPIP::DEVICE-HOSTNAME::INSTR` will allow the `DeviceManager` to
connect to the device.

---

## Packaging `tm_devices` with PyInstaller

### Problem:

When using [PyInstaller](https://pyinstaller.org/en/stable/) to create an executable that includes `tm_devices`, you may encounter errors such as:

- `tm_devices library not installed` (even though it is installed)
- `ModuleNotFoundError: No module named '3c22db458360489351e4._mypyc'`
- Functionality dependent on `tm_devices` fails in the packaged app, but works in native Python.

This is often due to PyInstaller not correctly packaging compiled dependencies (like `tomli`) or missing package metadata required by `tm_devices`.

### Solution:

1. **Use a Virtual Environment:**

    - Always create and activate a virtual environment before installing dependencies and running PyInstaller. This ensures all required packages are present and isolated.
    - Example:
        ```bash
        python -m venv .venv

        .venv\Scripts\activate # Windows
        # or
        source .venv/bin/activate # Linux/Mac

        pip install tm_devices pyinstaller tomli==2.0.1
        ```

2. **Install `tomli==2.0.1`:**

    - The error caused by the missing `*_mypyc` files is due to PyInstaller not detecting compiled `tomli` files. Use `tomli` version 2.0.1 as a workaround.
    - Check your version:
        ```bash
        pip show tomli
        ```
    - If needed, install the correct version:
        ```bash
        pip install tomli==2.0.1
        ```

3. **Include `tm_devices` Metadata:**

    - Use the `--copy-metadata=tm_devices` flag when running PyInstaller to ensure package metadata is included.
    - Example:
        ```bash
        pyinstaller --onefile main.py --copy-metadata=tm_devices
        ```

4. **If you see import errors for `DeviceManager` or `tm_devices`:**

    - Make sure tm_devices is installed in the same environment as PyInstaller.
    - You can check with:
        ```bash
        pip show tm_devices
        ```

5. **Remove `ImportError` Catching for Debugging:**

    - Temporarily remove any try/except blocks around `tm_devices` imports to see the full traceback and diagnose missing modules.

6. **Example Working `main.py`:**

    ```python
    from tm_devices import DeviceManager

    with DeviceManager() as device_manager:
        scope = device_manager.add_scope("192.168.0.1")
        print(scope)
    ```

### References:

- [hukkin/tomli#255](https://github.com/hukkin/tomli/issues/255)
- [tektronix/tm_devices#470](https://github.com/tektronix/tm_devices/issues/470)

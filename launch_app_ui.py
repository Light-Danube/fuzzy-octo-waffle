import gradio as gr

def check_libraries():
    libraries = {
        "tensorflow": False,
        "torch": False,
        "keras": False,
        "numpy": False,
        "pandas": False,
        "matplotlib": False,
    }

    try:
        import tensorflow
        libraries["tensorflow"] = True
    except ImportError:
        pass

    try:
        import torch
        libraries["torch"] = True
    except ImportError:
        pass

    try:
        import keras
        libraries["keras"] = True
    except ImportError:
        pass

    try:
        import numpy
        libraries["numpy"] = True
    except ImportError:
        pass

    try:
        import pandas
        libraries["pandas"] = True
    except ImportError:
        pass

    try:
        import matplotlib
        libraries["matplotlib"] = True
    except ImportError:
        pass

    return libraries

def library_check_interface():
    libraries = check_libraries()
    status = {lib: ("Installed" if installed else "Not installed") for lib, installed in libraries.items()}
    return status

iface = gr.Interface(fn=library_check_interface, 
                      inputs=None, 
                      outputs=gr.outputs.JSON(),
                      title="Library Check Interface",
                      description="Check the status of important libraries for your project.")

iface.launch()


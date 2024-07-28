from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox


def create_box(width, height, depth):
    """
    Function to create a 3D box.

    Args:
    width (float): Width of the box.
    height (float): Height of the box.
    depth (float): Depth of the box.

    Returns:
    TopoDS_Shape: The TopoDS shape of the box.
    """
    # Create a box
    box = BRepPrimAPI_MakeBox(width, height, depth).Shape()
    return box


def main():
    # Initialize the display
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Create a box with dimensions 10x20x30
    my_box = create_box(10.0, 20.0, 30.0)

    # Display the box
    display.DisplayShape(my_box, update=True)

    # Start the GUI loop
    start_display()


if __name__ == "__main__":
    main()
